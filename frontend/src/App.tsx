// frontend/src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from './components/layout/Layout';

// Temporary placeholders for pages we will build in Steps 8, 9, and 27
const LandingPage = () => <div className="p-8 text-slate-900">Landing Page (Public) - Go to <a href="/login" className="text-blue-600 underline">Login</a></div>;
const LoginPage = () => <div className="p-8 text-slate-900">Login Page (Public) - Go to <a href="/dashboard" className="text-blue-600 underline">Dashboard</a></div>;
const DashboardPage = () => <div className="p-6 bg-white rounded-lg shadow-sm border border-slate-200">Dashboard Visualizations will go here.</div>;
const AlertsPage = () => <div className="p-6 bg-white rounded-lg shadow-sm border border-slate-200">Alert Table will go here.</div>;

function App() {
  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<LoginPage />} />

        {/* Protected Dashboard Routes (Wrapped inside the Layout) */}
        <Route element={<Layout />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/alerts" element={<AlertsPage />} />
          <Route path="/audit" element={<div className="p-6 bg-white rounded-lg shadow-sm border border-slate-200">Audit Logs will go here.</div>} />
        </Route>

        {/* Fallback for unknown URLs */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;