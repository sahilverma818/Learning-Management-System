import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
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
      let response = await axios.post(`${import.meta.env.VITE_API_URL}auth/get_token`, {
        'email': email,
        'password': password
      });

      if (response.status === 200) {
        debugger
        localStorage.setItem('access_token', response.data.data.tokens.access_token);
        localStorage.setItem('refresh_token', response.data.data.tokens.refresh_token);
        localStorage.setItem('user_role', response.data.data.role)

        let intervalId = setInterval(async() => {
          const userLoggedIn = localStorage.getItem('refresh_token');
          if (userLoggedIn) {
            try{
              response = await axios.get(`${import.meta.env.VITE_API_URL}auth/refresh-token?refresh_token=${userLoggedIn}`)
  
              if (response.status === 200) {
                localStorage.setItem('access_token', response.data.data.tokens.access_token);
                localStorage.setItem('refresh_token', response.data.data.tokens.refresh_token);
                localStorage.setItem('user_role', response.data.data.role)
              }
            } catch (error) {
              toast.error(error.response?.data?.message || "An error occurred");
            }
          } else {
            clearInterval(intervalId)
          }
        }, 1000 * 60 * 4);

        toast.success('Login successful')
        navigate('/')

      };
    } catch (error){
      toast.error(error.response?.data?.message || "An error occurred");
    }
  }

  useEffect(() => {
    if (localStorage.getItem('access_token')) {
      navigate("/")
    }
  }, []);

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
            <Link to={'/register'}>
              <a href="#">Sign Up</a>
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login