import React, { useState } from "react"
import axios from "axios"
import "./profilepage.css"

const ProfilePage = () => {

    const [userData, setUserData] = useState({
        firstname: '',
        lastname: '',
        email: '',
        role: '',
        enrolledCourses: []
    });

    const fetchUserData = async () => {
        try {
            const token = localStorage.getItem('access_token');
            const res = await axios.post('http://localhost:8000/users/get', null, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'accept': 'application/json'
                }
            });
            if (res.status === 200) {
                console.log(res.data.data);
                setUserData(res.data.data);
                console.log("useState Data:", userData);
            }
        } catch (error) {
            console.error('Error fetching user data:', error);
        }
    };

    React.useEffect(() => {
        fetchUserData();
    }, []);
    return (
        <div>
            <div className="profile-wrapper">
                <div className="profile-header">
                    <div className="profile-info">
                        <h2>Student Profile</h2>
                        <div className="user-details">
                            <div className="detail-group">
                                <label>First Name:</label>
                                <span>John</span>
                            </div>
                            <div className="detail-group">
                                <label>Last Name:</label>
                                <span>Doe</span>
                            </div>
                            <div className="detail-group">
                                <label>Email:</label>
                                <span>john.doe@example.com</span>
                            </div>
                            <div className="detail-group">
                                <label>Role:</label>
                                <span>Student</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="dashboard-section">
                    <h3>Dashboard</h3>
                    <div className="dashboard-stats">
                        <div className="stat-card">
                            <h4>Enrolled Courses</h4>
                            <span className="stat-number">5</span>
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

                <div className="courses-section">
                    <h3>My Courses</h3>
                    <div className="courses-grid">
                        <div className="course-card">
                            <h4>Web Development</h4>
                            <p>Progress: 75%</p>
                            <div className="progress-bar">
                                <div className="progress" style={{width: '75%'}}></div>
                            </div>
                            <button className="continue-btn">Continue Learning</button>
                        </div>
                        <div className="course-card">
                            <h4>Data Structures</h4>
                            <p>Progress: 45%</p>
                            <div className="progress-bar">
                                <div className="progress" style={{width: '45%'}}></div>
                            </div>
                            <button className="continue-btn">Continue Learning</button>
                        </div>
                        <div className="course-card">
                            <h4>Machine Learning</h4>
                            <p>Progress: 90%</p>
                            <div className="progress-bar">
                                <div className="progress" style={{width: '90%'}}></div>
                            </div>
                            <button className="continue-btn">Continue Learning</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ProfilePage