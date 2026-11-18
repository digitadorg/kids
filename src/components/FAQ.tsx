import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';

const faqData = [
  {
    id: 1,
    question: "Meu filho tem só 4 anos. Será que ele vai entender?",
    answer: "Vai sim. E vai amar. Criamos atividades específicas pra cada faixa etária, desde os 4 anos — usando jogos, histórias e brincadeiras que despertam foco e inteligência emocional desde cedo."
  },
  {
    id: 2,
    question: "Não tenho tempo. Preciso ficar junto nas atividades?",
    answer: "A maioria das atividades pode ser feita com autonomia. Você só precisa de 15 a 20 minutos por dia pra organizar e acompanhar de leve. Perfeito até pra quem tem rotina apertada."
  },
  {
    id: 3,
    question: "E se eu não gostar? Tem garantia?",
    answer: "Claro. Você tem 7 dias de teste pra conhecer tudo. Se não ver valor, devolvemos cada centavo. Simples assim. Aqui, ou você ama — ou não paga nada."
  },
  {
    id: 4,
    question: "Isso é só mais uma plataforma com videoaula?",
    answer: "Não. Aqui seu filho é protagonista. Cada atividade exige ação, criação e envolvimento. Não é sobre assistir passivamente. É sobre aprender de verdade enquanto se diverte."
  },
  {
    id: 5,
    question: "Funciona mesmo pra crianças tímidas ou que só querem celular?",
    answer: "Justamente pra elas que o Titi foi criado. As atividades são pensadas pra gerar pequenas vitórias diárias, estimular autoestima e desconectar aos poucos do excesso de tela."
  },
  {
    id: 6,
    question: "Meu filho tem necessidades especiais. Ele pode participar?",
    answer: "Sim. Temos educadores com formação inclusiva e plano adaptável. Entre em contato com a gente e montamos algo personalizado pra sua realidade."
  }
];

const FAQItem = ({ question, answer, isOpen, toggleOpen }) => {
  return (
    <div className="border-b border-gray-800 py-5">
      <button 
        className="flex justify-between items-center w-full text-left"
        onClick={toggleOpen}
      >
        <h3 className="text-lg font-medium">{question}</h3>
        {isOpen ? (
          <ChevronUp className="h-5 w-5 text-purple-400" />
        ) : (
          <ChevronDown className="h-5 w-5 text-purple-400" />
        )}
      </button>
      
      <div 
        className={`mt-3 text-gray-400 transition-all duration-300 overflow-hidden ${
          isOpen ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
        }`}
      >
        <p>{answer}</p>
      </div>
    </div>
  );
};

const FAQ = () => {
  const [openIndex, setOpenIndex] = useState(0);
  
  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? -1 : index);
  };
  
  return (
    <section id="faq" className="py-20 bg-black px-4">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Perguntas Frequentes</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6">Dúvidas Comuns</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Encontre respostas para as perguntas mais frequentes sobre nossas atividades e planos.
          </p>
        </div>
        
        <div className="bg-gray-900 rounded-2xl p-6 md:p-8">
          {faqData.map((faq, index) => (
            <FAQItem 
              key={faq.id}
              question={faq.question}
              answer={faq.answer}
              isOpen={openIndex === index}
              toggleOpen={() => toggleFAQ(index)}
            />
          ))}
        </div>
        
        <div className="text-center mt-8">
          <p className="text-gray-400">
            Não encontrou o que procurava? 
            <a href="#contact" className="text-purple-400 ml-1 hover:underline">Entre em contato</a>
          </p>
        </div>
      </div>
    </section>
  );
};

export default FAQ;