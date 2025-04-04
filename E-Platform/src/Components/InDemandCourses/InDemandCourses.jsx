import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Course from "../Course/Course";
import { toast } from "react-toastify";
import axios from "axios";
import "./InDemandCourses.css";
import Loader from "../Loader/Loader";

const InDemandCourses = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.post(`${import.meta.env.VITE_API_URL}courses/get_courses`);

                if (response.status === 200) {
                    setCourses(response.data);
                }
            } catch (error) {
                toast(`Exception error: ${error}`)
                console.error("Exception error:", error);
            }
        };

        fetchCourses();
    }, []); 

    if (!courses) {
        return <Loader/>
    }

    return (
        <div className="course_wrapper">
            <h2>
                In-Demand <span>Courses</span>
            </h2>
            <div className="course_container">
                {courses.map((course) => (
                    <Link to={`/course/${course.id}`} key={course.id} className="link">
                        <Course course={course} />
                    </Link>
                ))}
            </div>
        </div>
    );
};

export default InDemandCourses;
