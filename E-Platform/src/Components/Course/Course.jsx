import React from "react";
import { FaChartSimple } from "react-icons/fa6";
import './Course.css'

const Course = ({course}) => {
    const {course_name, course_description, start_date, image, fees, last_enrollment_date} = course;
    return (
        <div>
            <div className="course_card">
                <img src={`http://localhost:8000/${image}`} alt="course_img" className="course_img" />
                <h3 className="course_name">{course_name}</h3>
                <h4 className="course_price">${fees}</h4>
                <p className="course_standard"><FaChartSimple className="analytic"/> {course_description}</p>
                <button className="course_button"> Explore </button>
            </div>
        </div>
    )
}

export default Course