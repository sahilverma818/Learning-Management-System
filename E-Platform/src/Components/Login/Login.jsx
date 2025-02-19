import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { toast } from "react-toastify";
import './Login.css'

const Login = () => {

  const navigate = useNavigate();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("")

    if (!validateEmail(email)) {
      setError('Email is not valid')
      return;
    }

    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}auth/get_token`, {
        'email': email,
        'password': password
      });

      if (response.status === 200) {
        localStorage.setItem('access_token', response.data.access_token);
        localStorage.setItem('refresh_token', response.data.refresh_token);
        toast.success('Login successful', {
          onClose: () => {
            navigate('/')
          }
        })

      };
    } catch (error){
      toast.error(error.response.data.message)
    }
  }

  return (
    <div className="login-wrapper">
      <div className="login-container">
        <h2 className="login-title">Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="email">Email</label>
            <input
              type="text"
              id="email"
              name="email"
              value={email}
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
              value={password}
              placeholder="Enter your password"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          {error && <p className="error-text">{error} !! </p>}
          <button type="submit" className="login-btn">Login</button>
          <div className="footer-links">
            <a href="#">Forgot Password?</a>
            <a href="#">Sign Up</a>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login