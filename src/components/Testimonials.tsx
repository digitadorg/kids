import React, { useState } from 'react';
import { ChevronLeft, ChevronRight, Quote } from 'lucide-react';

const testimonials = [
  {
    id: 1,
    content: "Meu filho era inquieto, disperso, não parava quieto nem pra comer. Com 2 semanas de Titi, ele já conseguia sentar e terminar uma tarefa com orgulho. Mudou nossa casa inteira.",
    author: "Juliana Martins",
    role: "Mãe do Caio, 7 anos",
    image: "https://images.pexels.com/photos/1181686/pexels-photo-1181686.jpeg?auto=compress&cs=tinysrgb&w=300",
  },
  {
    id: 2,
    content: "Achei que fosse marketing, mas hoje minha filha acorda pedindo pelas atividades. Ela criou confiança, fala com segurança e parou de se esconder quando alguém chega em casa.",
    author: "Marcelo Souza",
    role: "Pai da Alícia, 5 anos",
    image: "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=300",
  },
  {
    id: 3,
    content: "O antes e depois é gritante. Meu filho era 100% tela. Hoje ele desenha, escreve histórias e me surpreende com ideias. E o melhor: tudo isso sem eu precisar ficar brigando.",
    author: "Renata Lima",
    role: "Mãe do Gustavo, 8 anos",
    image: "https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&w=300",
  },
  {
    id: 4,
    content: "Sou pai solo e vivo na correria. O Titi virou meu aliado. Enquanto preparo o jantar, meus filhos tão aprendendo de verdade — e ainda se divertem. Mudou nossa rotina.",
    author: "Leandro Azevedo",
    role: "Pai da Lara e do Matheus",
    image: "https://images.pexels.com/photos/1681010/pexels-photo-1681010.jpeg?auto=compress&cs=tinysrgb&w=300",
  },
  {
    id: 5,
    content: "Ver meu filho programando no papel, com 9 anos, foi surreal. Eu nunca tive isso na minha infância. Titi dá ferramentas pra essa geração criar, não só consumir.",
    author: "Elaine Rocha",
    role: "Mãe do Enzo, 9 anos",
    image: "https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&w=300",
  },
];

const Testimonials = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  
  const nextTestimonial = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === testimonials.length - 1 ? 0 : prevIndex + 1
    );
  };
  
  const prevTestimonial = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === 0 ? testimonials.length - 1 : prevIndex - 1
    );
  };
  
  return (
    <section id="testimonials" className="py-20 bg-gradient-to-b from-gray-950 to-black px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Depoimentos</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6">O Que os Pais Dizem</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Veja o impacto positivo que nossas atividades têm na vida de milhares de crianças 
            através dos depoimentos de seus pais.
          </p>
        </div>
        
        <div className="relative max-w-4xl mx-auto">
          <div className="absolute -inset-x-6 -inset-y-6 md:-inset-x-10 md:-inset-y-10 bg-gradient-to-r from-purple-500/10 via-blue-500/10 to-purple-500/10 blur-xl opacity-50 rounded-3xl"></div>
          
          <div className="relative bg-gray-900 border border-gray-800 rounded-2xl p-8 md:p-12">
            <Quote className="h-12 w-12 text-purple-500/20 absolute top-8 left-8" />
            
            <div className="flex flex-col md:flex-row gap-8 md:gap-12 items-center">
              <div className="w-24 h-24 md:w-32 md:h-32 rounded-full overflow-hidden flex-shrink-0 border-2 border-purple-500/30">
                <img 
                  src={testimonials[currentIndex].image} 
                  alt={testimonials[currentIndex].author} 
                  className="w-full h-full object-cover"
                />
              </div>
              
              <div>
                <blockquote className="text-lg md:text-xl text-gray-300 italic mb-6">
                  "{testimonials[currentIndex].content}"
                </blockquote>
                <div>
                  <p className="font-semibold">{testimonials[currentIndex].author}</p>
                  <p className="text-sm text-gray-400">{testimonials[currentIndex].role}</p>
                </div>
              </div>
            </div>
            
            <div className="flex justify-between mt-8">
              <button 
                onClick={prevTestimonial}
                className="p-2 rounded-full bg-gray-800 hover:bg-gray-700 transition-colors"
              >
                <ChevronLeft className="h-6 w-6" />
              </button>
              
              <div className="flex gap-2">
                {testimonials.map((_, index) => (
                  <button
                    key={index}
                    onClick={() => setCurrentIndex(index)}
                    className={`w-3 h-3 rounded-full transition-all ${
                      index === currentIndex 
                        ? 'bg-purple-500 scale-110' 
                        : 'bg-gray-700 hover:bg-gray-600'
                    }`}
                  />
                ))}
              </div>
              
              <button 
                onClick={nextTestimonial}
                className="p-2 rounded-full bg-gray-800 hover:bg-gray-700 transition-colors"
              >
                <ChevronRight className="h-6 w-6" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Testimonials;