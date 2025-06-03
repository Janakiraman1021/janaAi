// Cyberpunk Background Initialization
// Add this to your main component or App.js useEffect

import { useEffect } from 'react';

export const useCyberpunkBackground = () => {
  useEffect(() => {
    // Create particles container
    const createParticlesContainer = () => {
      // Remove existing container if it exists
      const existing = document.querySelector('.cyberpunk-particles');
      if (existing) {
        existing.remove();
      }

      const particlesContainer = document.createElement('div');
      particlesContainer.className = 'cyberpunk-particles';
      document.body.appendChild(particlesContainer);
      return particlesContainer;
    };

    // Create circuit lines container
    const createCircuitsContainer = () => {
      // Remove existing container if it exists
      const existing = document.querySelector('.cyberpunk-circuits');
      if (existing) {
        existing.remove();
      }

      const circuitsContainer = document.createElement('div');
      circuitsContainer.className = 'cyberpunk-circuits';
      document.body.appendChild(circuitsContainer);
      return circuitsContainer;
    };

    // Create floating particles
    const createParticles = () => {
      const particlesContainer = createParticlesContainer();
      const particleCount = window.innerWidth < 768 ? 8 : 15; // Reduced for performance
      
      for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'cyberpunk-particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (Math.random() * 8 + 15) + 's';
        particlesContainer.appendChild(particle);
      }
    };

    // Create circuit lines
    const createCircuits = () => {
      const circuitsContainer = createCircuitsContainer();
      
      for (let i = 0; i < 3; i++) {
        const circuit = document.createElement('div');
        circuit.className = 'cyberpunk-circuit';
        circuit.style.top = Math.random() * 80 + 10 + '%';
        circuit.style.left = Math.random() * 80 + 10 + '%';
        circuit.style.animationDelay = (i * 3) + 's';
        circuitsContainer.appendChild(circuit);
      }
    };

    // Initialize background effects
    const initializeCyberpunkBg = () => {
      // Only create effects if not in green screen mode
      if (!document.body.classList.contains('greenScreen')) {
        createParticles();
        createCircuits();
      }
    };

    // Initialize on mount
    initializeCyberpunkBg();

    // Handle window resize
    const handleResize = () => {
      // Debounce resize handler
      clearTimeout(window.cyberpunkResizeTimeout);
      window.cyberpunkResizeTimeout = setTimeout(() => {
        if (!document.body.classList.contains('greenScreen')) {
          createParticles(); // Recreate particles with new count
        }
      }, 250);
    };

    window.addEventListener('resize', handleResize);

    // Cleanup function
    return () => {
      window.removeEventListener('resize', handleResize);
      clearTimeout(window.cyberpunkResizeTimeout);
      
      // Clean up containers
      const particles = document.querySelector('.cyberpunk-particles');
      const circuits = document.querySelector('.cyberpunk-circuits');
      
      if (particles) particles.remove();
      if (circuits) circuits.remove();
    };
  }, []);
};

// Alternative: Direct initialization function if not using React hooks
export const initCyberpunkBackground = () => {
  const createParticles = () => {
    let particlesContainer = document.querySelector('.cyberpunk-particles');
    if (!particlesContainer) {
      particlesContainer = document.createElement('div');
      particlesContainer.className = 'cyberpunk-particles';
      document.body.appendChild(particlesContainer);
    }
    
    particlesContainer.innerHTML = ''; // Clear existing particles
    
    const particleCount = window.innerWidth < 768 ? 8 : 15;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.className = 'cyberpunk-particle';
      particle.style.left = Math.random() * 100 + '%';
      particle.style.animationDelay = Math.random() * 20 + 's';
      particle.style.animationDuration = (Math.random() * 8 + 15) + 's';
      particlesContainer.appendChild(particle);
    }
  };

  const createCircuits = () => {
    let circuitsContainer = document.querySelector('.cyberpunk-circuits');
    if (!circuitsContainer) {
      circuitsContainer = document.createElement('div');
      circuitsContainer.className = 'cyberpunk-circuits';
      document.body.appendChild(circuitsContainer);
    }
    
    circuitsContainer.innerHTML = ''; // Clear existing circuits
    
    for (let i = 0; i < 3; i++) {
      const circuit = document.createElement('div');
      circuit.className = 'cyberpunk-circuit';
      circuit.style.top = Math.random() * 80 + 10 + '%';
      circuit.style.left = Math.random() * 80 + 10 + '%';
      circuit.style.animationDelay = (i * 3) + 's';
      circuitsContainer.appendChild(circuit);
    }
  };

  // Initialize
  if (!document.body.classList.contains('greenScreen')) {
    createParticles();
    createCircuits();
  }

  // Handle resize
  window.addEventListener('resize', () => {
    clearTimeout(window.cyberpunkTimeout);
    window.cyberpunkTimeout = setTimeout(() => {
      if (!document.body.classList.contains('greenScreen')) {
        createParticles();
      }
    }, 250);
  });
};

// Usage in your React component:
// 
// Option 1: Using the hook
// import { useCyberpunkBackground } from './cyberpunk-bg';
// 
// function App() {
//   useCyberpunkBackground();
//   return <YourComponent />;
// }
//
// Option 2: Direct initialization
// import { initCyberpunkBackground } from './cyberpunk-bg';
// 
// useEffect(() => {
//   initCyberpunkBackground();
// }, []);