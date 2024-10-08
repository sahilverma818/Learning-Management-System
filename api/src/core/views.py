from typing import Dict, Any, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.users.utils import RoleEnum

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
        self.routes.add_api_route('/get', self.get, methods=['GET'], response_model=None)
        self.routes.add_api_route('/post', self.create, methods=['POST'], response_model=None)
        self.routes.add_api_route("/list", self.get_all, methods=["GET"], response_model=None)
        self.routes.add_api_route("/update", self.update, methods=["PATCH"], response_model=None)
        self.routes.add_api_route("/delete", self.delete, methods=["DELETE"], response_model=None)
        
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
                data[object] = objects[object]
        return data
    
    def _commit(self, db: Session, db_object=None):
        """
        DB commit method
        """
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    
    def get(self, id: int, db: Session = Depends(get_db)):
        """
        Get Method
        """
        try:
            objects = self._get_queryset(db).get(id)
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
                })
        except Exception as e:
            print("Error in generating response: \n\n", e)
            pass
        
    def get_all(self, db: Session = Depends(get_db), params: Dict[str, Any]=None, page_number: int=1, page_size: int = 10):
        """
        Get all method
        """
        skip = (page_number - 1)*page_size 
        query = self._get_queryset(db)
        if params:
            for attr in [x for x in params if params[x] is not None]:
                query = query.filter(getattr(self.model, attr) == params[attr])

        return query.offset(skip).limit(page_size).all()
    
    def create(self, data,  db: Session = Depends(get_db)):
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
            print("Error in generating response:--->>>>\n\n",e)
                
    def update(self, id: int, data, db: Session = Depends(get_db)):
        """
        Update method
        """
        object_data = self._get_queryset(db).get(id)
        for field in data.__dict__:
            setattr(object_data, field, data.__dict__[field])
        object_data = self._commit(db, object_data)
        return object_data

    def delete(self, id: int, db: Session = Depends(get_db)):
        """
        Delete Method
        """
        object = self._get_queryset(db).get(id)
        db.delete(object)
        db.commit()
        return object
