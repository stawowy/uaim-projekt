import React, { useState, useEffect, useContext } from 'react';
import { AuthContext } from './AuthProvider'; // lub './AuthContext' jeśli tam masz export

const UserProfile = ({ user }) => {
  const [profileData, setProfileData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  // Użyj 'accessToken' zgodnie z tym, co mamy w AuthProvider
  const { accessToken } = useContext(AuthContext);

  useEffect(() => {
    // Sprawdź, czy mamy wszystkie dane
    if (!user || !accessToken || !user.username) {
      setError('User not logged in or token missing');
      setLoading(false);
      return;
    }

    const fetchUserProfile = async () => {
      try {
        console.log('Używamy accessToken:', accessToken);
        console.log('Używamy user:', user.username);
        const response = await fetch(`http://localhost:5000/api/profile/${user.username}`, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user profile');
        }

        const data = await response.json();
        setProfileData(data);
        setError(null);
      } catch (err) {
        console.error('Error fetching user profile:', err);
        setError('Failed to load profile data');
      } finally {
        setLoading(false);
      }
    };

    fetchUserProfile();
  }, [user, accessToken]);

  // Dalej logika obsługi update'u
  // UWAGA: w handleUpdateProfile używasz: 'Bearer ${user.token}'
  // -> Zmień na 'Bearer ${accessToken}' lub dostosuj do swojej logiki

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfileData({ ...profileData, [name]: value });
  };

  const handleUpdateProfile = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://localhost:5000/api/profile/${user.username}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(profileData),
      });

      if (!response.ok) {
        throw new Error('Failed to update profile');
      }

      const updatedData = await response.json();
      setProfileData(updatedData);
      alert('Profile updated successfully');
    } catch (err) {
      console.error('Error updating profile:', err);
      setError('Failed to update profile');
    }
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p className="error-message">{error}</p>;

  return (
    <div className="form-container">
      <h2 className="form-header">Profil Użytownika</h2>
      <form className="form" onSubmit={handleUpdateProfile}>
        <label htmlFor="username" className="form-label">Nazwa Użytkownia:</label>
        <input
          type="text"
          id="username"
          name="username"
          value={profileData?.username || ''}
          onChange={handleInputChange}
          className="form-input"
          disabled
        />

        
        <label htmlFor="email" className="form-label">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={profileData?.email || ''}
          onChange={handleInputChange}
          className="form-input"
          disabled
        />

<label htmlFor="name" className="form-label">Imie:</label>
        <input
          name="imie"
          value={profileData?.first_name || ''}
          onChange={handleInputChange}
          className="form-input"
          disabled
        />

<label htmlFor="surname" className="form-label">Nazwisko:</label>
        <input
          name="nazwisko"
          value={profileData?.last_name || ''}
          onChange={handleInputChange}
          className="form-input"
          disabled
        />

<label htmlFor="surname" className="form-label">Numer Telefonu:</label>
        <input
          name="nazwisko"
          value={profileData?.phone || ''}
          onChange={handleInputChange}
          className="form-input"
          disabled
        />

       
      </form>
    </div>
  );
};

export default UserProfile;
