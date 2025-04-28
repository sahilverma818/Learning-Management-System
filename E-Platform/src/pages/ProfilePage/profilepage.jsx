import React, { useState, useEffect } from "react"
import axios from "axios"
import "./profilepage.css"
import { Link } from "react-router-dom";
import CreateCourse from "../../Components/CreateCourse/CreateCourse";


const ProfilePage = () => {

    const [isOpen, setIsOpen] = useState(false)
    const [userData, setUserData] = useState({});

    const fetchUserData = async () => {
        try {
            const token = localStorage.getItem('access_token');
            const res = await axios.get(`${import.meta.env.VITE_API_URL}users/get`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'accept': 'application/json'
                }
            });
            if (res.status === 200) {
                setUserData(res.data.data);
            }
        } catch (error) {
            console.error('Error fetching user data:', error);
        }
    };

    useEffect(() => {
        fetchUserData();
    }, []);

    return (
        <div>
            {isOpen && <CreateCourse onClose={() => setIsOpen(false)} />}
            <div className="profile-wrapper">
                <div className="profile-header">
                    <div className="profile-info">
                        <h2>{ userData.role }'s Profile</h2>
                        <div className="user-details">
                            <div className="detail-group">
                                <label>First Name:</label>
                                <span>{userData.firstname}</span>
                            </div>
                            <div className="detail-group">
                                <label>Last Name:</label>
                                <span>{userData.lastname}</span>
                            </div>
                            <div className="detail-group">
                                <label>Email:</label>
                                <span>{userData.email}</span>
                            </div>
                            <div className="detail-group">
                                <label>Role:</label>
                                <span>{userData.role}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="dashboard-section">
                    <h3>Dashboard</h3>
                    <div className="dashboard-stats">
                        <div className="stat-card">
                            <h4>Enrolled Courses</h4>
                            <span className="stat-number">{userData.courses && userData.courses.length}</span>
                        </div>
                        <div className="stat-card">
                            <h4>Completed Courses</h4>
                            <span className="stat-number">3</span>
                        </div>
                        <div className="stat-card">
                            <h4>In Progress</h4>
                            <span className="stat-number">2</span>
                        </div>
                    </div>
                </div>
                { localStorage.getItem('user_role') != 'admin' && (
                    <div className="courses-section">

                        <div className="courses-header">
                            <h3>My Courses</h3>
                            <button className="add-course-btn" onClick={() => setIsOpen(true)}>Add Courses +</button>
                        </div>

                        <div className="courses-grid">
                            { userData.courses && userData.courses.map((course) => (
                                <div className="course-card" key={course.id}>
                                    <h4> { course.course_name } </h4>
                                    <p>Progress: 75%</p>
                                    <div className="progress-bar">
                                        <div className="progress" style={{width: '75%'}}></div>
                                    </div>
                                    <Link to={`/course/${course.id}`}>
                                        <button className="continue-btn">Continue</button>
                                    </Link>
                                </div>
                            )) }
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
}

export default ProfilePage