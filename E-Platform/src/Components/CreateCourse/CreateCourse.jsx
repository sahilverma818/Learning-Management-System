import React from "react";
import "./CreateCourse.css"

const CreateCourse = ({ onClose }) => {

    return (
        <div className="courseCreate-overlay">
            <div className="courseCreate-modal">
                <h2 className="courseCreate-title">Create a New Course</h2>
                <form className="courseCreate-form">
                    <div>
                        <label className="courseCreate-label">Course Name:</label>
                        <input type="text" className="courseCreate-input" />
                    </div>
                    <div className="courseCreate-full">
                        <label className="courseCreate-label">Course Description:</label>
                        <textarea className="courseCreate-textarea"></textarea>
                    </div>
                    <div>
                        <label className="courseCreate-label">Start Date:</label>
                        <input type="date" className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Duration (months):</label>
                        <input type="number" className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Fees (Rs):</label>
                        <input type="number" className="courseCreate-input" />
                    </div>
                    <div>
                        <label className="courseCreate-label">Last Enrollment Date:</label>
                        <input type="date" className="courseCreate-input" />
                    </div>
                    <div className="courseCreate-imageUpload">
                        <label className="courseCreate-label">Upload Course Image:</label>
                        <input
                            type="file"
                            accept="image/*"
                            id="courseImage"
                            onChange={(e) => {
                                const file = e.target.files[0];
                                if (file) {
                                    const reader = new FileReader();
                                    reader.onload = () => {
                                        document.getElementById("imagePreview").src = reader.result;
                                    };
                                    reader.readAsDataURL(file);
                                }
                            }}
                        />
                        <p>Click or Drag to Upload</p>
                        <img id="imagePreview" className="courseCreate-imagePreview" alt="" />
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