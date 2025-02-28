import React, { useState } from "react";
import axios from "axios";
import "./CreateCourse.css"
import { toast } from "react-toastify";
import userData from "../../pages/ProfilePage/profilepage";

const CreateCourse = ({ onClose }) => {

    const [formData, setFormData] = useState({
        "course_name": "",
        "course_description": "",
        "start_date": "",
        "duration": "",
        "fees": "",
        "last_enrollment_date": "",
    })
    const [imagePreview, setImagePreview] = useState("");

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                setImagePreview(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
      };

    const handleSubmit = async(e) => {
        e.preventDefault();
        console.log("Image: ", imagePreview)
        console.log("Form data: ", formData);
        const token = localStorage.getItem('access_token')

        let bodyData = {
            'course_name': formData.course_name,
            'course_description': formData.course_description,
            'start_date': formData.start_date,
            'duration': parseInt(formData.duration),
            'fees': parseInt(formData.fees),
            'image': imagePreview.split(",")[1]
        }

        if (formData.last_enrollment_date) {
            bodyData.last_enrollment_date = formData.last_enrollment_date
        }

        const response = await axios.post(`${import.meta.env.VITE_API_URL}courses/post`, bodyData, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'accept': 'application/json'
            } 
        })

        if (response.status === 200) {
            toast.success('Course Created Successfully')
            toast.success(userData)
            onClose();
        }
    }

    return (
        <div className="courseCreate-overlay">
            <div className="courseCreate-modal">
                <h2 className="courseCreate-title">Create a New Course</h2>
                <form onSubmit={handleSubmit} className="courseCreate-form">
                    <div>
                        <label className="courseCreate-label">Course Name:</label>
                        <input type="text" name="course_name" value={formData.course_name} onChange={handleChange} className="courseCreate-input" />
                    </div>
                    <div className="courseCreate-full">
                        <label className="courseCreate-label">Course Description:</label>
                        <textarea name="course_description" value={formData.course_description} onChange={handleChange} className="courseCreate-textarea"></textarea>
                    </div>
                    <div>
                        <label className="courseCreate-label">Start Date:</label>
                        <input type="date" name="start_date" value={formData.start_date} onChange={handleChange} className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Duration (months):</label>
                        <input type="number" name="duration" value={formData.duration} onChange={handleChange} className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Fees (Rs):</label>
                        <input type="number" name="fees" value={formData.fees} onChange={handleChange} className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Last Enrollment Date:</label>
                        <input type="date" name="last_enrollment_date" value={formData.last_enrollment_date} onChange={handleChange} className="courseCreate-input" />
                    </div>
                    <div className="courseCreate-imageUpload">
                        <label className="courseCreate-label">Upload Course Image:</label>
                        <input
                            type="file"
                            accept="image/*"
                            id="courseImage"
                            onChange={handleImageChange}
                        />
                        <p>Click or Drag to Upload</p>
                        {imagePreview && (
                            <img src={imagePreview} className="courseCreate-imagePreview" alt="Course Preview" />    
                        )}
                    </div>

                    <div className="courseCreate-buttonGroup courseCreate-full">
                        <button className="courseCreate-submitBtn">Create Course</button>
                        <button className="courseCreate-closeBtn" onClick={onClose}>Close</button>
                    </div>
                </form>
            </div>
        </div>
    )
};

export default CreateCourse;