// frontend/tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f4f8',
          100: '#d9e2ec',
          500: '#334e68',
          700: '#243b53',
          900: '#0f172a', // Deep Navy / Slate 900 for banking theme
        },
        alert: {
          low: '#10b981',    // Emerald
          medium: '#f59e0b', // Amber
          high: '#ef4444',   // Red
          critical: '#7f1d1d' // Dark Red
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}