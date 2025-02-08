import React, { useState } from "react";
import axios from 'axios';
import './Login.css'

const Login = () => {
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    console.log(emailRegex.test(email))
    return emailRegex.test(email);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("")
    console.log('Email:', email);
    console.log('Password:', password);

    if (!validateEmail(email)) {
      setError('Email is not valid')
      console.log('Error: ', error)
      return;
    }

    try {
      const response = await axios.post('http://localhost:8000/auth/get_token', {
        'email': email,
        'password': password
      });

      if (response.status === 200) {
        console.log(response.data);
      };
    } catch {
      console.log('Exception:', response.data)
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