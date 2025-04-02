import React, { useEffect, useState } from "react";
import axios from "axios";
import './CourseDetails.css'
import { Link, useParams } from "react-router-dom";
import Loader from "../../Components/Loader/Loader";
import LectureInformation from "../../Components/LectureInformation/LectureInformation";
import CreateOrder from "../../Components/CreateOrder/CreateOrder";


const CourseDetails = () => {
    const {id} = useParams();
    const [isOrderPopUp, setIsOrderPopUp] = useState(false);
    const [courseDetail, setCourseDetail] = useState()
    const [viewIndex, setViewIndex] = useState(false);

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const course = await axios.get(`${import.meta.env.VITE_API_URL}courses/get_courses/${id}`)

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

    const handleToggle = (index) => {
        setViewIndex(prevState => ({
            ...prevState,
            [index]: !prevState[index]
        }));
    };
    

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
                            <h3 className="price">Price: Rs. {courseDetail.fees}</h3>
                            { (localStorage.getItem('user_role') === 'student')? <button onClick={() => setIsOrderPopUp(true)}> Buy Now !! </button>: <Link to={`/createlecture/${id}`}><button> Add Lectures </button></Link>}
                        </div>
                    </div>
                    <div className="details_right">
                        <img src={`http://localhost:8000/${courseDetail.image}`} alt="course_img" className="course_img" />
                    </div>
                </div>
                <div className="course_journey">
                    <h2> Modules </h2>
                    {courseDetail.modules && courseDetail.modules.map((module, index) => (
                        <fieldset className="field_container">
                            <legend className="phase"> Phase {index + 1} </legend>
                            <h3 className="p_name"> { module.module_title } </h3>
                            <p className="p_description"> { module.module_description } </p>
                            <button className="p_lectureview" onClick={() => handleToggle(index)}>
                                { viewIndex[index] ? "Hide Lectures" : "View Lectures" }
                            </button>

                            {viewIndex[index] && (
                                <LectureInformation moduleId = {module.id} courseId = {courseDetail.id}/>
                            )}
                        </fieldset>
                    ))}
                </div>
            </div>

            <CreateOrder 
                isOpen={isOrderPopUp} 
                onClose={() => setIsOrderPopUp(false)} 
            />
        </div>
    )
}

export default CourseDetails;