import React, { useState, useRef, useEffect } from "react";
import { useParams } from "react-router-dom";
import { toast } from "react-toastify";
import ReactMarkdown from 'react-markdown';
import axios from "axios";
import CreateModule from "../../Components/CreateModule/CreateModule";
import "./CreateLecture.css";

const CreateLecture = () => {
    const {id} = useParams();
    const videoRef = useRef(null);
    const [preview, setPreview] = useState('');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [modules, setModules] = useState([]);
    const [lectureData, setLectureData] = useState({
        "lecture_title": "",
        "lecture_description": "",
        "video_path": "",
        "module_id": ""
    })


    const previewMarkdown = () => {
        setPreview(lectureData.lecture_description);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    useEffect(() => {
        const fetchModules = async () => {
            try {
                const moduleResponse = await axios.post(`${import.meta.env.VITE_API_URL}modules/get_modules`, {
                    "course_id": parseInt(id)
                })

                if (moduleResponse.status === 200) {
                    setModules(moduleResponse.data)
                }
            } catch (error) {
                toast.error(error.response?.data?.message || "An error occurred");
            }
        };
        fetchModules();
    },[id])

    const handleVideoUpload = async () => {
        try {
            const formData = new FormData();
            formData.append("file", videoRef.current.files[0])
            const videoResponse = await axios.post(`${import.meta.env.VITE_API_URL}lectures/lecture-video`, formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            })

            if (videoResponse.status === 201) {
                setLectureData({ ...lectureData, [video_path]: videoResponse.data.video_path})
                toast.success('Video Uploaded Successfully')
            }
        } catch (error) {
            toast.error(error.response?.data?.message || "An error occurred");
        }
    }

    const handleChange = (e) => {
        setLectureData({ ...lectureData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const token = localStorage.getItem('access_token')
            const lectureResponse = await axios.post(`${import.meta.env.VITE_API_URL}lectures/create_lectures`, lectureData, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'accept': 'application/json'
                }
            })

            if (lectureResponse.status === 200) {
                toast.success('Lecture Record Added Successfully')
            }
        } catch (error) {
            toast.error(error.response?.data?.message || "An error occurred");
        }
    }

    return (
        <div className="lecture-form-container">
            <h2 className="add-lecture-heading">Add New Lecture</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="lectureTitle">Lecture Title</label>
                <input type="text" id="lectureTitle" name="lecture_title" value={lectureData.lecture_title} onChange={handleChange} placeholder="Enter lecture title" required />

                <label htmlFor="videoUpload">Upload Video</label>
                <div className="video-upload-container">
                    <input type="file" id="videoUpload" name="videoUpload" accept="video/*" ref={videoRef} required />
                    <button className="upload-btn" type="button" onClick={handleVideoUpload}> Upload Video </button>
                </div>

                <label htmlFor="moduleId">Select Module</label>
                <select id="moduleId" name="module_id" onChange={handleChange} value={lectureData.module_id} required>
                    <option value="" disabled>-- Select a Module --</option>
                    { modules && (
                        modules.map((module) => (
                            <option key={module.id} value={module.id}> { module.module_title } </option>
                        ))
                    )}
                </select>

                <div className="new-module-link">
                    <a href="#" onClick={(e) => { e.preventDefault(); setIsPopupOpen(true); }}>Create a new module</a>
                </div>
                
                <label>Lecture Description (Markdown)</label>
                <textarea id="markdown-input" name="lecture_description" value={lectureData.lecture_description} onChange={handleChange} placeholder="Type your Markdown here..." />
                
                <button type="button" className="preview-btn" onClick={previewMarkdown}>Preview</button>
                <button type="submit" className="submit-btn">Add Lecture</button>
            </form>
            
            <CreateModule isOpen={isPopupOpen} onClose={() => setIsPopupOpen(false)} />
            {isModalOpen && (
                <div className="modal-overlay">
                    <div className="modal-content">
                        <div className="markdown-heading">
                            <h2>Markdown Preview</h2>
                            <span className="close-btn" onClick={closeModal}>&times;</span>
                        </div>
                        <div className="markdown-preview">
                            <ReactMarkdown>{preview}</ReactMarkdown>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default CreateLecture;
