import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Course from "../Course/Course";
import axios from "axios";
import "./CourseList.css";

const CourseList = () => {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.post("http://localhost:8000/courses/list");

                if (response.status === 200) {
                    console.log(response.data);
                    setCourses(response.data);
                } else {
                    console.error("Error occurred:", response.data);
                    setError("Error fetching courses");
                }
            } catch (error) {
                console.error("Exception error:", error);
                setError("Failed to load courses");
            } finally {
                setLoading(false);
            }
        };

        fetchCourses();
    }, []); // ✅ Runs only once when component mounts

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

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

export default CourseList;
