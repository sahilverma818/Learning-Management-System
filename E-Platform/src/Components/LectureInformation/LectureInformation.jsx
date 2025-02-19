import React, { useEffect, useState } from "react";
import axios from "axios";
import Loader from "../Loader/Loader";
import "./LectureInformation.css"

const LectureInformation = (props) => {

    const [lectures, setLectures] = useState();
    
    useEffect(() => {
        const fetchLectures = async() => {
            try {
                const response = await axios.post(`${process.env.REACT_APP_API_URL}lectures/list`, {
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
                                <button className="view-btn">View Lecture</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default LectureInformation