import '../App.css';
import React, { useState } from 'react';
import apiClient from './apiClient';
import { AuthContext } from './AuthProvider';
const Login = ({ onLogin }) => {
    const [credentials, setCredentials] = useState({ email: '', password: '' });
    const [error, setError] = useState(null);

    const handleChange = (e) => {
      const { name, value } = e.target;
      setCredentials({ ...credentials, [name]: value });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log(JSON.stringify(credentials))
      try {
        const response = await fetch('http://127.0.0.1:5000/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(credentials),
          
        });
  
        if (!response.ok) {
          throw new Error('Login failed');
        }
        
        const data = await response.json();
        console.log(data)
        console.log('Login successful, token received:', data.refresh_token);
        onLogin({ username: data.username});
        localStorage.setItem('accessToken', data.access_token);
        localStorage.setItem('refreshToken', data.refresh_token);

      } catch (err) {
        console.error('Error during login:', err);
        setError('Invalid email or password');
      }
    };
  
    return (
      <div className="form-container">
        <h2 className="form-header">Login</h2>
        <form className="form" onSubmit={handleSubmit}>
          <label htmlFor="email" className="form-label">Email:</label>
          <input type="email" id="email" name="email" value={credentials.email} onChange={handleChange} className="form-input" />
  
          <label htmlFor="password" className="form-label">Password:</label>
          <input type="password" id="password" name="password" value={credentials.password} onChange={handleChange} className="form-input" />
  
          <button type="submit" className="form-button">Login</button>
          {error && <p className="error-message">{error}</p>}
        </form>
      </div>
    );
  };
  export default Login;