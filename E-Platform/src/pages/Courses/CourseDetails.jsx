import React, { useEffect, useState } from "react";
import axios from "axios";
import './CourseDetails.css'
import { Link, useParams, useLocation } from "react-router-dom";
import Loader from "../../Components/Loader/Loader";
import LectureInformation from "../../Components/LectureInformation/LectureInformation";
import CreateOrder from "../../Components/CreateOrder/CreateOrder";
import PaymentSuccessModal from "../../Components/PaymentModel/paymentModel";
import { toast } from "react-toastify";


const CourseDetails = () => {
    const {id} = useParams();
    const location = useLocation();
    const [isOrderPopUp, setIsOrderPopUp] = useState(false);
    const [courseDetail, setCourseDetail] = useState()
    const [viewIndex, setViewIndex] = useState(false);
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [validatedPaymentData, setValidatedPaymentData] = useState(null);

    useEffect(() => {
        const queryParams = new URLSearchParams(location.search);
        const sessionId = queryParams.get('session_id');
    
        if (sessionId) {
            validatePayment(sessionId);
        }
    }, [location]);
    
    const validatePayment = async (sessionId) => {
        try {
            const response = await axios.get(
                `${import.meta.env.VITE_API_URL}payments/handle-payment?session_id=${sessionId}`,
                {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                }
            );
    
            if (response.status === 200) {
                toast.success(response.data.message || 'Payment validated successfully');
                setValidatedPaymentData(response.data);
                setShowSuccessModal(true);
            } else {
                toast.error(response.data.message || 'Payment verification failed');
            }
        } catch (error) {
            const message =
                error.response?.data?.message || 'Something went wrong during payment validation.';
            toast.error(message);
        }
    };

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
                courseDetail={courseDetail}
            />

            <PaymentSuccessModal
                isOpen={showSuccessModal}
                onClose={() => setShowSuccessModal(false)}
                paymentData={validatedPaymentData}
            />
        </div>
    )
}

export default CourseDetails;