import React, { useState, useEffect } from 'react';
import { Menu, X, ActivitySquare } from 'lucide-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav 
      className={`fixed top-0 w-full z-50 transition-all duration-300 ${
        scrolled ? 'bg-black shadow-lg' : 'bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <a href="#" className="flex items-center">
                <ActivitySquare className="h-8 w-8 text-purple-500" />
                <span className="ml-2 text-xl font-bold bg-gradient-to-r from-purple-500 to-blue-500 bg-clip-text text-transparent">Titi</span>
              </a>
            </div>
          </div>
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-8">
              <a href="#activities" className="hover:text-purple-400 px-3 py-2 rounded-md text-sm font-medium transition-colors">Atividades</a>
              <a href="#benefits" className="hover:text-purple-400 px-3 py-2 rounded-md text-sm font-medium transition-colors">Benefícios</a>
              <a href="#pricing" className="hover:text-purple-400 px-3 py-2 rounded-md text-sm font-medium transition-colors">Preços</a>
              <a href="#testimonials" className="hover:text-purple-400 px-3 py-2 rounded-md text-sm font-medium transition-colors">Depoimentos</a>
              <a href="#faq" className="hover:text-purple-400 px-3 py-2 rounded-md text-sm font-medium transition-colors">FAQ</a>
              <a href="#contact" className="bg-gradient-to-r from-purple-600 to-blue-500 text-white px-4 py-2 rounded-md text-sm font-medium hover:from-purple-700 hover:to-blue-600 transition-all">Inscreva-se</a>
            </div>
          </div>
          <div className="md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-800 focus:outline-none"
            >
              {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      <div className={`md:hidden ${isOpen ? 'block' : 'hidden'}`}>
        <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-gray-900">
          <a 
            href="#activities" 
            className="hover:bg-gray-800 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            Atividades
          </a>
          <a 
            href="#benefits" 
            className="hover:bg-gray-800 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            Benefícios
          </a>
          <a 
            href="#pricing" 
            className="hover:bg-gray-800 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            Preços
          </a>
          <a 
            href="#testimonials" 
            className="hover:bg-gray-800 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            Depoimentos
          </a>
          <a 
            href="#faq" 
            className="hover:bg-gray-800 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            FAQ
          </a>
          <a 
            href="#contact" 
            className="bg-gradient-to-r from-purple-600 to-blue-500 block px-3 py-2 rounded-md text-base font-medium"
            onClick={() => setIsOpen(false)}
          >
            Inscreva-se
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;