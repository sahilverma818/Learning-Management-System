import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './VideoComponent.css';
import ReactMarkdown from 'react-markdown';
import { toast } from 'react-toastify';
import Loader from '../Loader/Loader';


const VideoComponent = () => {
  
  const { 'course-id': courseId, id } = useParams();
  const [lectureDetails, setLectureDetails] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    const fetchLectureDetails = async() => {
      try {
        const token = localStorage.getItem('access_token')
        const response = await axios.get(`${import.meta.env.VITE_API_URL}lectures/course/${courseId}/lecture/get/${id}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'accept': 'application/json'
          }
        })

        if (response.status === 200) {
          setLectureDetails(response.data)
        }

      } catch (error) {
        toast.error(error.response.data.message);
        navigate(-1)
      } 
    };
    fetchLectureDetails(); 
  }, [id, courseId])

  if (!lectureDetails) {
    return <Loader />
  }

  return (
    <div className="video-content">
      <h1>{lectureDetails.lecture_title}</h1>
      <div className="video-player">
        <iframe 
          src={`${import.meta.env.VITE_API_URL}${lectureDetails.video_path}`} 
          title={`${lectureDetails.lecture_title}`}
          allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
      </div>
      <div className="video-description">
        <ReactMarkdown>{lectureDetails.lecture_description}</ReactMarkdown>
      </div>
    </div>
  );
};

export default VideoComponent;
