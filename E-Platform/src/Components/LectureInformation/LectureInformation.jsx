import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";
import axios from "axios";
import Loader from "../Loader/Loader";
import "./LectureInformation.css"

const LectureInformation = (props) => {

    const {id} = useParams();
    const [lectures, setLectures] = useState();
    
    useEffect(() => {
        const fetchLectures = async() => {
            try {
                const response = await axios.post(`${import.meta.env.VITE_API_URL}lectures/get_lectures`, {
                    "module_id": props.moduleId
                })

                if (response.status === 200) {
                    setLectures(response.data)

                }
            } catch (error){
                console.log(error)
            }
        }
        fetchLectures();
    }, [props.moduleId])

    if (!lectures) {
        return <Loader />
    }

    return (
        <div className="lecture-container">
            <h2 className="lecture-header">Lectures for Module {props.moduleId}</h2>
            <table className="lecture-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th className="lecture-title">Lecture Title</th>
                        <th className="lecture-description">Description</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {lectures.map((lecture, index) => (
                        <tr key={lecture.id}>
                            <td>{index + 1}</td>
                            <td className="lecture-title">{lecture.lecture_title}</td>
                            <td className="lecture-description">{lecture.lecture_description}</td>
                            <td>
                                <Link to={`/course/${props.courseId}/lectures/${lecture.id}`}>
                                    <button className="view-btn">View Lecture</button>
                                </Link>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default LectureInformation