import React from 'react';
import { Facebook, Instagram, Youtube, Twitter, Mail, ActivitySquare } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gray-950 pt-16 pb-8 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
          <div>
            <div className="flex items-center mb-6">
              <ActivitySquare className="h-8 w-8 text-purple-500" />
              <span className="ml-2 text-xl font-bold bg-gradient-to-r from-purple-500 to-blue-500 bg-clip-text text-transparent">Titi</span>
            </div>
            
            <p className="text-gray-400 mb-6">
              Transformando o futuro através de atividades criativas e educativas para crianças de todas as idades.
            </p>
            
            <div className="flex space-x-4">
              <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                <Facebook className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                <Instagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                <Youtube className="h-5 w-5" />
              </a>
              <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                <Twitter className="h-5 w-5" />
              </a>
            </div>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-6">Links Rápidos</h3>
            <ul className="space-y-3">
              <li>
                <a href="#activities" className="text-gray-400 hover:text-purple-400 transition-colors">Atividades</a>
              </li>
              <li>
                <a href="#benefits" className="text-gray-400 hover:text-purple-400 transition-colors">Benefícios</a>
              </li>
              <li>
                <a href="#pricing" className="text-gray-400 hover:text-purple-400 transition-colors">Preços</a>
              </li>
              <li>
                <a href="#testimonials" className="text-gray-400 hover:text-purple-400 transition-colors">Depoimentos</a>
              </li>
              <li>
                <a href="#faq" className="text-gray-400 hover:text-purple-400 transition-colors">FAQ</a>
              </li>
              <li>
                <a href="#contact" className="text-gray-400 hover:text-purple-400 transition-colors">Contato</a>
              </li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-6">Atividades</h3>
            <ul className="space-y-3">
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Arte & Criatividade</a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Leitura & Escrita</a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Música & Dança</a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Programação & Tecnologia</a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Jogos & Diversão</a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">Raciocínio Lógico</a>
              </li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-6">Contato</h3>
            <ul className="space-y-3">
              <li className="flex items-start">
                <Mail className="h-5 w-5 text-purple-400 mr-2 mt-0.5" />
                <span className="text-gray-400">contato@titi.com.br</span>
              </li>
              <li>
                <span className="text-gray-400">(11) 9999-9999</span>
              </li>
              <li>
                <span className="text-gray-400">Av. Paulista, 1000 - São Paulo/SP</span>
              </li>
            </ul>
            
            <div className="mt-6">
              <h4 className="text-sm font-semibold mb-3">Assine Nossa Newsletter</h4>
              <form className="flex">
                <input 
                  type="email" 
                  placeholder="Seu e-mail" 
                  className="flex-1 p-2 rounded-l-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                />
                <button 
                  type="submit" 
                  className="bg-purple-600 text-white p-2 rounded-r-lg hover:bg-purple-700 transition-colors"
                >
                  <Mail className="h-5 w-5" />
                </button>
              </form>
            </div>
          </div>
        </div>
        
        <div className="border-t border-gray-800 pt-8 text-center text-gray-500 text-sm">
          <p>&copy; {new Date().getFullYear()} Titi. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;