// frontend/src/context/AuthContext.tsx
import React, { createContext, useContext, useState, type ReactNode } from 'react';
import axios from 'axios';
import type { AuthState } from '../types/auth';

interface AuthContextType extends AuthState {
  login: (employee_id: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [authState, setAuthState] = useState<AuthState>({
    user: null,
    token: localStorage.getItem('token'),
    isAuthenticated: !!localStorage.getItem('token'),
    isLoading: false,
  });

  const login = async (employee_id: string, password: string) => {
    setAuthState(prev => ({ ...prev, isLoading: true }));
    try {
      // FastAPI OAuth2 strictly expects x-www-form-urlencoded format
      const formData = new URLSearchParams();
      formData.append('username', employee_id); // Maps to our employee_id
      formData.append('password', password);

      // UPDATED: Changed localhost to 127.0.0.1 to prevent Windows IPv6 resolution blocking
      const response = await axios.post('http://127.0.0.1:8001/api/v1/auth/access-token', formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });
      
      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      
      setAuthState({
        user: null, // We will fetch the full User profile in Step 12
        token: access_token,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error) {
      setAuthState(prev => ({ ...prev, isLoading: false }));
      throw error; // Pass the error to the UI
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setAuthState({
      user: null,
      token: null,
      isAuthenticated: false,
      isLoading: false,
    });
  };

  return (
    <AuthContext.Provider value={{ ...authState, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};