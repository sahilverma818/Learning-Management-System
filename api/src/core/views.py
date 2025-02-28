import base64
from typing import Dict, Any
from datetime import datetime as dt

from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm.collections import InstrumentedList
from src.users.models import Users

from src.auth.dependencies import get_current_user
from src.core.database import get_db
from src.core.logger import *

class BaseManager:
    """
    Base Manager Class
    """
    def __init__(self, model):
        """
        Base Manager Initialization
        """
        self.model = model
        self._get_routes()

    def _get_routes(self):
        """
        Get Routes Method
        """
        self.routes.add_api_route('/get/{id}', self.fetch_record, methods=['GET'], response_model=None)
        self.routes.add_api_route('/post', self.create_record, methods=['POST'], response_model=None)
        self.routes.add_api_route("/list", self.fetch_all_records, methods=["POST"], response_model=None)
        self.routes.add_api_route("/update", self.update_record, methods=["PATCH"], response_model=None)
        self.routes.add_api_route("/delete", self.delete_record, methods=["DELETE"], response_model=None)
        
    def _get_queryset(self, db: Session):
        """
        Get Queryset method
        """
        return db.query(self.model)
    
    def _serialize(self, objects):
        """
        To Serialize data
        """
        data = {}
        for object in objects:
            if hasattr(self.model, object):
                if isinstance(objects[object], InstrumentedList) and objects[object]:
                    class_object = type(objects[object][0])
                    data[object] = self._serialize_all(objects[object], class_object)
                elif isinstance(objects[object], dt):
                    data[object] = str(objects[object])
                else:
                    data[object] = objects[object]
        return data
    
    def _serialize_all(self, objects, related_field=None):
        generated_list = []
        for object in objects:
            obj_dict = {}
            for data in object.__dict__:
                if hasattr(related_field, data):
                    if isinstance(object.__dict__[data], dt):
                        obj_dict[data] = str(object.__dict__[data])
                    else:
                        obj_dict[data] = object.__dict__[data]
            generated_list.append(obj_dict)
        return generated_list
    
    def _commit(self, db: Session, db_object=None):
        """
        DB commit method
        """
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    
    def fetch_record(
        self,
        id: int,
        related_field=None,
        db: Session = Depends(get_db)
    ):
        """
        Get Method
        """
        try:
            objects = self._get_queryset(db)
            if related_field:
                objects = objects.options(joinedload(related_field))
            
            objects = objects.get(id)

            if objects:
                objects = self._serialize(objects.__dict__)
                return JSONResponse({
                    "success" : True,
                    "data": objects
                })
            else:
                return JSONResponse({
                    "success": False,
                    "message": "No records found"
                }, status_code=404)
            
        except Exception as e:
            return JSONResponse(
                content={"success": False, "message": f"failed to fetch records {str(e)}"},
                status_code=500
            )
        
    def fetch_all_records(
        self,
        db: Session = Depends(get_db),
        params: Dict[str, Any]=None,
        page_number: int=1,
        page_size: int = 10
    ):
        """
        Get all method
        """
        try:
            page_number = 1 if page_number < 0 else page_number
            page_size = 10 if page_size <= 0 else page_size
            
            skip = (page_number - 1)*page_size 
            query = self._get_queryset(db)

            if params:
                for attr, value in params.items():
                    if hasattr(self.model, attr) and value is not None:
                        column_attr = getattr(self.model, attr)
                        query = query.filter(column_attr.ilike(f"%{value}%") if isinstance(value, str) else column_attr == value)
            return query.offset(skip).limit(page_size).all()
        
        except Exception as e:
            logger.error(f'Exception occured: {str(e)}')
            return JSONResponse(
                content={"message": "Error occured while fetching the data", "success": False},
                status_code=400
            )
    
    def create_record(self, data,  db: Session = Depends(get_db)):
        """
        Create method
        """
        try:
            if not isinstance(data, dict):
                data = data.__dict__

            db_obj = self.model(**data)
            db_obj = self._commit(db, db_obj)
            return db_obj
        
        except Exception as e:
            return JSONResponse(
                content={"message": "Failed to create record", "success": False},
                status_code=400
            )
                
    def update_record(self, id: int, data, db: Session = Depends(get_db)):
        """
        Update method
        """
        try:
            object_data = self._get_queryset(db).get(id)
            for field in data.__dict__:
                if data.__dict__[field]:
                    setattr(object_data, field, data.__dict__[field])
            object_data = self._commit(db, object_data)
            return object_data
        
        except Exception as e:
            logger.error(f"Exception caught: {str(e)}")
            return JSONResponse(
                content={"message": "Unable to update record", "success": False},
                status_code=400
            )

    def delete_record(
        self,
        id: int,
        current_user = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
        """
        Delete Method
        """
        try:
            record = db.query(self.model).get(id)
            db.delete(record)
            db.commit()
            return JSONResponse(
                content={"message": "Record deleted successfully", "success": True},
                status_code=200
            )
        
        except Exception as e:
            logger.error(f"Exception caught: {str(e)}")
            return JSONResponse(
                content={"message": "Unable to update record", "success": False},
                status_code=400
            )
