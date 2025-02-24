import React, { useState, useRef } from "react";
import "./CreateLecture.css"; // Import global CSS
import ReactMarkdown from 'react-markdown';
import { FiUpload } from "react-icons/fi";
import { Link } from "react-router-dom";

const CreateLecture = () => {
    
    const inputRef = useRef(null);
    const [preview, setPreview] = useState('')
    const previewMarkdown = () => {
        setPreview(inputRef.current.value)
    }

    return (
        <div className="lecture-form-container">
            <h2>Add New Lecture</h2>
            <form>
                <label htmlFor="lectureTitle">Lecture Title</label>
                <input
                    type="text"
                    id="lectureTitle"
                    name="lectureTitle"
                    placeholder="Enter lecture title"
                    required
                />

                <label htmlFor="videoUpload">Upload Video</label>
                <input
                    type="file"
                    id="videoUpload"
                    name="videoUpload"
                    accept="video/*"
                    required
                />
                <span> Video Uploaded <Link to={`${import.meta.env.VITE_API_URL}static/lectures/Salesforce-video-VEED.mp4`}>  Click here to view </Link></span>

                <label htmlFor="moduleId">Select Module</label>
                <select
                    id="moduleId"
                    name="moduleId"
                    required
                >
                    <option value="">-- Select a Module --</option>
                    <option value="1">Module 1</option>
                    <option value="2">Module 2</option>
                </select>

                <div className="new-module-link">
                    <a href="#">Create a new module</a>
                </div>
                <label>Lecture Description (Markdown)</label>
                    <div className="description-portion">
                        <textarea
                            id="markdown-input"
                            name="lectureDescription"
                            ref={inputRef}
                            placeholder="Type your Markdown here..."
                        />
                    <div id="preview" className="markdown-preview">
                        <ReactMarkdown>{preview}</ReactMarkdown>
                    </div>
                </div>
                <button type="button" className="preview-btn" onClick={previewMarkdown}>
                    Preview
                </button>


                <button type="submit" className="submit-btn">
                    Add Lecture
                </button>
            </form>
        </div>
    );
};

export default CreateLecture;
