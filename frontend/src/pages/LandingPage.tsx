// frontend/src/pages/LandingPage.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import { Shield, Activity, ArrowRight, Database } from 'lucide-react';
import { Button } from '../components/common/Button';

export const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans">
      {/* Header */}
      <header className="bg-white border-b border-slate-200 sticky top-0 z-10 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center">
            <Shield className="w-8 h-8 text-brand-900 mr-2" />
            <span className="text-xl font-bold text-brand-900 tracking-tight">SentinelAI</span>
          </div>
          <nav className="flex items-center space-x-4">
            <Link to="/login">
              <Button variant="outline" size="sm">Sign In</Button>
            </Link>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-grow">
        <section className="bg-brand-900 text-white py-20 lg:py-32">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center text-center">
            <span className="px-3 py-1 rounded-full bg-brand-700 text-blue-100 text-xs font-semibold tracking-wide border border-brand-500 mb-6 uppercase">
              Enterprise Security Prototype
            </span>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6 max-w-4xl text-white">
              Adaptive Insider Risk Intelligence for Banking Operations
            </h1>
            <p className="text-lg md:text-xl text-slate-300 mb-10 max-w-2xl">
              Detect suspicious activities by authorized personnel. SentinelAI combines deterministic security rules with machine learning to identify anomalous behavior, privilege misuse, and data exfiltration indicators.
            </p>
            <div className="flex space-x-4">
              <Link to="/login">
                <Button variant="primary" size="lg" className="bg-blue-700 hover:bg-blue-600 text-white border border-blue-500 group shadow-lg">
                  Get Started
                  <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
                </Button>
              </Link>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-20 bg-slate-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-slate-900 mb-4">Core Platform Capabilities</h2>
              <p className="text-lg text-slate-600 max-w-2xl mx-auto">
                Designed to address the unique challenges of insider threat detection using hybrid analytical models.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {/* Feature 1 */}
              <div className="bg-white p-8 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 bg-brand-100 text-brand-900 rounded-lg flex items-center justify-center mb-6">
                  <Activity className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-semibold text-slate-900 mb-3">Behavioral Profiling</h3>
                <p className="text-slate-600 leading-relaxed">
                  Establish historical and role-based baselines for employees to identify unauthorized deviations in access times, transaction volumes, and device usage.
                </p>
              </div>

              {/* Feature 2 */}
              <div className="bg-white p-8 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 bg-brand-100 text-brand-900 rounded-lg flex items-center justify-center mb-6">
                  <Shield className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-semibold text-slate-900 mb-3">Hybrid Detection Engine</h3>
                <p className="text-slate-600 leading-relaxed">
                  Utilize a combination of deterministic security thresholds and unsupervised machine learning to detect unusual combinations of behavior.
                </p>
              </div>

              {/* Feature 3 */}
              <div className="bg-white p-8 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 bg-brand-100 text-brand-900 rounded-lg flex items-center justify-center mb-6">
                  <Database className="w-6 h-6" />
                </div>
                <h3 className="text-xl font-semibold text-slate-900 mb-3">Explainable Risk Scoring</h3>
                <p className="text-slate-600 leading-relaxed">
                  Translate complex model outputs into an interpretable 1–100 risk score, providing security analysts with clear textual evidence for every alert.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-brand-900 py-8 border-t border-brand-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between">
          <div className="flex items-center mb-4 md:mb-0 text-slate-400">
            <Shield className="w-5 h-5 mr-2" />
            <span className="font-semibold text-slate-300">SentinelAI Project</span>
          </div>
          <p className="text-slate-400 text-sm">
            Academic Prototype — AI-Powered Insider Threat Detection
          </p>
        </div>
      </footer>
    </div>
  );
};