/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'gradient': 'gradient 8s ease infinite',
        'fade-in': 'fadeIn 0.5s ease-out',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        gradient: {
          '0%, 100%': {
            'background-position': '0% 50%'
          },
          '50%': {
            'background-position': '100% 50%'
          },
        },
        fadeIn: {
          '0%': {
            opacity: '0',
            transform: 'translateY(10px)'
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)'
          },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
} 