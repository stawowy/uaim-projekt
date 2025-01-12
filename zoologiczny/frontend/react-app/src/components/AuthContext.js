import React, { createContext, useState, useEffect, useCallback } from 'react';


export const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState(() => localStorage.getItem('accessToken') || null);
  const [refreshToken, setRefreshToken] = useState(() => localStorage.getItem('refreshToken') || null);

  // Funkcja do uzyskania nowego accessToken za pomocą refreshToken
  const refreshAccessToken = useCallback(async () => {
    if (!refreshToken) {
      console.warn('No refresh token available');
      return;
    }

    try {
      const response = await fetch('http:localhost:5000/api/refresh-token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refreshToken }),
      });

      if (response.ok) {
        const data = await response.json();
        setAccessToken(data.accessToken);
        localStorage.setItem('accessToken', data.accessToken); // Zapisz accessToken w localStorage
      } else {
        console.error('Failed to refresh access token');
      }
    } catch (error) {
      console.error('Error refreshing access token:', error);
    }
  }, [refreshToken]);

  // Logowanie użytkownika: zapisanie obu tokenów
  const login = (tokens) => {
    setAccessToken(tokens.accessToken);
    setRefreshToken(tokens.refreshToken);

    localStorage.setItem('accessToken', tokens.accessToken);
    localStorage.setItem('refreshToken', tokens.refreshToken);
  };

  // Wylogowanie użytkownika: usunięcie tokenów
  const logout = () => {
    setAccessToken(null);
    setRefreshToken(null);

    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  };

  // Automatyczne odświeżanie accessToken przed jego wygaśnięciem
  useEffect(() => {
    if (!accessToken) return;

    // Załóżmy, że accessToken wygasa po 15 minutach
    const tokenExpiryTime = 15 * 60 * 1000; // 15 minut w milisekundach
    const refreshBeforeExpiry = tokenExpiryTime - 60 * 1000; // Odśwież na minutę przed wygaśnięciem

    const interval = setInterval(() => {
      refreshAccessToken();
    }, refreshBeforeExpiry);

    return () => clearInterval(interval);
  }, [accessToken, refreshAccessToken]);

  return (
    <AuthContext.Provider
      value={{
        accessToken,
        refreshToken,
        login,
        logout,
        refreshAccessToken,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;

