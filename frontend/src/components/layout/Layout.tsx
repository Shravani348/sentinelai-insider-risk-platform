import React from 'react';
import { Outlet, Link, useLocation } from 'react-router-dom';
import { Shield, Activity, FileText, LogOut } from 'lucide-react';

export const Layout: React.FC = () => {
  const location = useLocation();
  
  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: Activity },
    { name: 'Security Alerts', path: '/alerts', icon: Shield },
    { name: 'Audit Logs', path: '/audit', icon: FileText },
  ];

  return (
    <div className="flex h-screen bg-slate-50">
      {/* Sidebar Navigation */}
      <aside className="w-64 bg-brand-900 text-white flex flex-col">
        <div className="h-16 flex items-center px-6 border-b border-brand-700">
          <Shield className="w-6 h-6 mr-2 text-blue-400" />
          <span className="text-lg font-bold tracking-wide">SentinelAI</span>
        </div>
        
        <nav className="flex-1 py-6 px-3 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname.startsWith(item.path);
            return (
              <Link
                key={item.name}
                to={item.path}
                className={`flex items-center px-3 py-2.5 text-sm font-medium rounded-md transition-colors ${
                  isActive ? 'bg-brand-700 text-white' : 'text-slate-300 hover:bg-brand-700 hover:text-white'
                }`}
              >
                <Icon className="w-5 h-5 mr-3 flex-shrink-0" />
                {item.name}
              </Link>
            );
          })}
        </nav>

        <div className="p-4 border-t border-brand-700">
          <div className="flex items-center px-3 py-2 text-sm font-medium text-slate-300 hover:text-white cursor-pointer rounded-md hover:bg-brand-700 transition-colors">
            <LogOut className="w-5 h-5 mr-3 flex-shrink-0" />
            Sign Out
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden">
        <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 shadow-sm">
          <h1 className="text-xl font-semibold text-slate-800 capitalize">
            {location.pathname.replace('/', '') || 'Dashboard'}
          </h1>
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-full bg-brand-100 flex items-center justify-center text-brand-900 font-bold border border-brand-500">
              SA
            </div>
            <span className="text-sm font-medium text-slate-700">Security Admin</span>
          </div>
        </header>
        <div className="flex-1 overflow-y-auto p-8">
          {/* This renders whatever nested route is currently active */}
          <Outlet /> 
        </div>
      </main>
    </div>
  );
};