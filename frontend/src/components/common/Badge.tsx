import React from 'react';
import { cn } from './Button';

interface BadgeProps {
  children: React.ReactNode;
  level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL' | 'INFO';
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({ children, level, className }) => {
  const levels = {
    LOW: "bg-green-100 text-green-800 border border-green-200",
    MEDIUM: "bg-amber-100 text-amber-800 border border-amber-200",
    HIGH: "bg-red-100 text-red-800 border border-red-200",
    CRITICAL: "bg-red-900 text-white shadow-sm",
    INFO: "bg-slate-100 text-slate-800 border border-slate-200"
  };

  return (
    <span className={cn("px-2.5 py-0.5 rounded-full text-xs font-semibold uppercase tracking-wide", levels[level], className)}>
      {children}
    </span>
  );
};