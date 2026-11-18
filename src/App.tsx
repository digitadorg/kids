import React from 'react';
import Hero from './components/Hero';
import Activities from './components/Activities';
import Pricing from './components/Pricing';
import Testimonials from './components/Testimonials';
import Benefits from './components/Benefits';
import FAQ from './components/FAQ';
import Contact from './components/Contact';
import Footer from './components/Footer';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="font-sans bg-black text-white">
      <Navbar />
      <Hero />
      <Activities />
      <Benefits />
      <Pricing />
      <Testimonials />
      <FAQ />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;