import '../App.css';
import React, { useState } from 'react';
const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    first_name: '',
    last_name: '',
    phone: '',
    address: ''
  });

  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(formData);
    try {
      const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message || 'Registration successful!');
        setError('');
      } else {
        setError(data.error || 'Registration failed.');
        setMessage('');
      }
    } catch (err) {
      console.error('Error during registration:', err);
      setError('An unexpected error occurred. Please try again later.');
      setMessage('');
    }
  };

  return (
    <div className="form-container">
      <h2 className="form-header">Register</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label htmlFor="username" className="form-label">Username:</label>
        <input type="text" id="username" name="username" value={formData.username} onChange={handleChange} className="form-input" required />

        <label htmlFor="password" className="form-label">Password:</label>
        <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} className="form-input" required />

        <label htmlFor="email" className="form-label">Email:</label>
        <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} className="form-input" required />

        <label htmlFor="first_name" className="form-label">First Name:</label>
        <input type="text" id="first_name" name="first_name" value={formData.first_name} onChange={handleChange} className="form-input" required />

        <label htmlFor="last_name" className="form-label">Last Name:</label>
        <input type="text" id="last_name" name="last_name" value={formData.last_name} onChange={handleChange} className="form-input" required />

        <label htmlFor="phone" className="form-label">Phone:</label>
        <input type="tel" id="phone" name="phone" value={formData.phone} onChange={handleChange} className="form-input" required />

        <button type="submit" className="form-button">Register</button>
      </form>
      {message && <p className="success-message">{message}</p>}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default Register;