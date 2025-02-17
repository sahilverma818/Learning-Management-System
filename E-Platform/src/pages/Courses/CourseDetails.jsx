import React, { useEffect, useState } from "react";
import axios from "axios";
import './CourseDetails.css'
import { useParams } from "react-router-dom";
import Loader from "../../Components/Loader/Loader";


const CourseDetails = () => {
    const {id} = useParams();

    const [courseDetail, setCourseDetail] = useState()

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const course = await axios.post(`http://localhost:8000/courses/get/${id}`, {
                    'id': id
                })

                if (course.status === 200) {
                    setCourseDetail(course.data.data)
                }
            } catch (error) {
                
            };
        }
        fetchCourse();
    }, [id])

    if (!courseDetail) {
        return <Loader />;
    }

    return (
        <div>
            <div className="course_details">
                <div className="details_top">
                    <div className="details_left">
                        <h2 className="name"> {courseDetail.course_name} </h2>
                        <p className="desc"> {courseDetail.course_description} </p>
                        <p className="lang"> English / Hindi </p>
                        <p className="date"> {Date(courseDetail.start_date)} </p>
                        <div className="price_container">
                            <h3 className="price">Price: ${courseDetail.fees}</h3>
                            <button> Buy Now !! </button>
                        </div>
                    </div>
                    <div className="details_right">
                        <img src={`http://localhost:8000/${courseDetail.image}`} alt="course_img" className="course_img" />
                    </div>
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