import React, { useState } from "react"
import './signUp.css'
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

const SignUp = () => {

    const navigate = useNavigate();

    const [firstname, setFirstName] = useState('');
    const [lastname, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('student')

    const handleSubmit = async(e) => {
        e.preventDefault();
        console.log(firstname, lastname, email, password, role);
        try {
            const response = await axios.post('http://localhost:8000/users/post/', {
                'email': email,
                'hashed_password': password,
                'role': role,
                'firstname': firstname,
                'lastname': lastname
            })
            if (response.status == 200) {
                toast.success('User registration successful', {
                    onClose: () => navigate('/login')
                });
            }
        } catch (error) {
            toast.error(error.response.data.message)
        }
        
    }

    return (
        <div className="register-wrapper">
            <div className="register-container">
                <h2 className="register-title">Register</h2>
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="firstname">First Name</label>
                        <input
                            type="text"
                            id="firstname"
                            name="firstname"
                            placeholder="Enter your first name"
                            onChange={(e) => setFirstName(e.target.value)}
                            required
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="lastname">Last Name</label>
                        <input
                            type="text"
                            id="lastname"
                            name="lastname"
                            placeholder="Enter your last name"
                            onChange={(e) => setLastName(e.target.value)}
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            placeholder="Enter your email"
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            placeholder="Enter your password"
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="role">User Role</label>
                        <select name="role" id="role" onChange={(e) => setRole(e.target.value)}>
                            <option value="student"> Student </option>
                            <option value="lecturer"> Lecturer </option>
                        </select>
                    </div>
                    
                    <button type="submit" className="register-btn">Register</button>
                    <div className="footer-links">
                        <a href="#">Already have an account? Login</a>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default SignUp