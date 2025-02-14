import React, { useEffect } from "react";
import axios from "axios";
import './CourseDetails.css'

import {coursesData} from '../../data';

// import params
import { useParams } from "react-router-dom";


const CourseDetails = () => {
    const {id} = useParams();

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const course = await axios.post(`http://localhost:8000/courses/get/${id}`, {
                    'id': id
                })

                if (course.status === 200) {
                    console.log(course.data)
                }
            } catch (error) {

            };
        }
        fetchCourse();
    }, [id])

    // const course = coursesData.find(course=> {
    //     return course.id === parseInt(id);
    // })


    return (
        <div>
            <div className="course_details">
                <div className="details_top">
                    <div className="details_left">
                        {/* <h2 className="name"> {course.name} </h2>
                        <p className="desc"> {course.courseDetail.description} </p>
                        <p className="lang"> {course.courseDetail.language} </p>
                        <p className="date"> {course.courseDetail.date} </p> */}
                        <div className="price_container">
                            {/* <h3 className="price">Price: ${course.price}</h3> */}
                            <button> Buy Now !! </button>
                        </div>
                    </div>
                    {/* <div className="details_right">
                        <img src={course.image} alt="course_img" className="course_img" />
                    </div> */}
                </div>
                {/* <div className="course_journey">
                    <h2> Curriculum </h2>
                    <fieldset className="field_container">
                        <legend className="phase"> Phase 01 </legend>
                        <h3 className="p_name">{course.phase1.phaseName}</h3>
                        <ul>
                            <li> {course.phase1.phaseList} </li>
                            <li> {course.phase1.phaseList1} </li>
                            <li> {course.phase1.phaseList2} </li>
                            <li> {course.phase1.phaseList3} </li>
                            <li> {course.phase1.phaseList4} </li>
                        </ul>
                    </fieldset>
                    <fieldset className="field_container">
                        <legend className="phase"> Phase 01 </legend>
                        <h3 className="p_name">{course.phase1.phaseName}</h3>
                        <ul>
                            <li> {course.phase1.phaseList} </li>
                            <li> {course.phase1.phaseList1} </li>
                            <li> {course.phase1.phaseList2} </li>
                            <li> {course.phase1.phaseList3} </li>
                            <li> {course.phase1.phaseList4} </li>
                        </ul>
                    </fieldset>
                    <fieldset className="field_container">
                        <legend className="phase"> Phase 01 </legend>
                        <h3 className="p_name">{course.phase1.phaseName}</h3>
                        <ul>
                            <li> {course.phase1.phaseList} </li>
                            <li> {course.phase1.phaseList1} </li>
                            <li> {course.phase1.phaseList2} </li>
                            <li> {course.phase1.phaseList3} </li>
                            <li> {course.phase1.phaseList4} </li>
                        </ul>
                    </fieldset>
                    <fieldset className="field_container">
                        <legend className="phase"> Phase 01 </legend>
                        <h3 className="p_name">{course.phase1.phaseName}</h3>
                        <ul>
                            <li> {course.phase1.phaseList} </li>
                            <li> {course.phase1.phaseList1} </li>
                            <li> {course.phase1.phaseList2} </li>
                            <li> {course.phase1.phaseList3} </li>
                            <li> {course.phase1.phaseList4} </li>
                        </ul>
                    </fieldset>
                </div> */}
            </div>
        </div>
    )
}

export default CourseDetails