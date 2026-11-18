
import React, { useEffect, useState } from 'react';
import { ArrowRight, Sparkles, Star } from 'lucide-react';

const Hero = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <div className="relative min-h-screen flex items-center justify-center overflow-hidden bg-black pt-28 pb-16">
      {/* Background effects */}
      <div className="absolute inset-0">
        <div className="absolute inset-0 bg-gradient-radial from-purple-900/20 via-black to-black"></div>
        <div className="absolute top-20 left-0 w-72 h-72 bg-purple-500/10 rounded-full filter blur-3xl animate-pulse-slow"></div>
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl animate-pulse-slower"></div>
      </div>
      
      <div className="container px-4 mx-auto relative z-10">
        <div className="max-w-5xl mx-auto">
          <div 
            className={`transition-all duration-1000 transform ${
              isVisible ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'
            }`}
          >
            {/* Featured Badge */}
            <div className="flex justify-center mb-8">
              <div className="flex items-center gap-2 bg-white/5 backdrop-blur-sm px-4 py-2 rounded-full border border-purple-500/20">
                <Sparkles className="h-4 w-4 text-purple-400" />
                <span className="text-sm text-purple-300">+1.000 crianças impactadas | 98% dos pais relatam mudança visível em 30 dias</span>
                <Star className="h-4 w-4 text-yellow-400" />
              </div>
            </div>

            <h1 className="text-4xl md:text-6xl font-bold mb-8 text-center leading-tight text-white">
              Seu Filho Está Aprendendo… <span className="block mt-2 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-blue-500 to-purple-400 animate-gradient">Mas o Que Exatamente?</span>
            </h1>
            
            <p className="text-xl md:text-2xl text-gray-300 mb-12 text-center max-w-3xl mx-auto leading-relaxed">
              Descubra o plano secreto que pais inteligentes estão usando pra transformar crianças comuns em líderes antes dos 10 anos — sem tela, sem gritaria e com 15 minutos por dia.
              <br />
              Enquanto a maioria das crianças perde tempo em frente a telas, o seu filho pode estar desenvolvendo foco, criatividade e inteligência emocional — direto de casa e com resultados visíveis nas primeiras semanas.
            </p>
            
            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row justify-center gap-4 mb-12">
              <a 
                href="#pricing" 
                className="group relative px-8 py-4 bg-gradient-to-r from-purple-600 to-blue-600 rounded-full text-lg font-semibold hover:shadow-lg hover:shadow-purple-500/25 transition-all duration-300"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 rounded-full blur-lg opacity-50 group-hover:opacity-75 transition-opacity"></div>
                <span className="relative flex items-center justify-center">
                  Quero Desenvolver Meu Filho Agora
                  <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                </span>
              </a>
              
              <a 
                href="#activities" 
                className="px-8 py-4 bg-white/5 backdrop-blur-sm border border-purple-500/20 rounded-full text-lg font-semibold hover:bg-white/10 transition-all duration-300 text-center"
              >
                Ver Atividades
              </a>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto">
              <div className="text-center">
                <div className="text-3xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">1000+</div>
                <p className="text-gray-400 mt-1">Alunos Ativos</p>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">98%</div>
                <p className="text-gray-400 mt-1">Pais viram o filho mais focado em 30 dias</p>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">50+</div>
                <p className="text-gray-400 mt-1">Atividades Inéditas</p>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold bg-gradient-to-r from-purple-400 to-blue-400 bg-clip-text text-transparent">12</div>
                <p className="text-gray-400 mt-1">Anos de Experiência</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
