import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import './VideoSidebar.css';
import axios from 'axios';
import { toast } from 'react-toastify';

const VideoSidebar = () => {

  const { 'course-id': courseId, id } = useParams();
  const [lectureList, setLectureList] = useState([]);

  useEffect(() => {
    const fetchLectureList = async() => {
      try{
        const response = await axios.get(`${import.meta.env.VITE_API_URL}lectures/get-course-lectures/${courseId}`)
        if (response.status === 200) {
          setLectureList(response.data)
        }
      } catch(error) {
        toast.error(`Error fetching lectures ${error.message}`)
      }
    }
    fetchLectureList();
  }, [id, courseId])

  return (
    <aside className="sidebar">
      <h2>Course Contents</h2>
      <ul>
        {lectureList.map((lecture, index) => (
          <li key={index}>
            <Link to={`/course/${courseId}/lectures/${lecture.lecture_id}`}>
              <div className="lecture-card">
                {index + 1} . { lecture.lecture_title }
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default VideoSidebar;
