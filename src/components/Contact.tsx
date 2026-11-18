import React, { useState } from 'react';
import { Send, Mail, Phone, MapPin } from 'lucide-react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    childName: '',
    childAge: '',
    message: '',
  });
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    // Aqui seria a lógica para enviar o formulário
    alert('Obrigado pelo interesse! Entraremos em contato em breve.');
    // Reset do formulário
    setFormData({
      name: '',
      email: '',
      phone: '',
      childName: '',
      childAge: '',
      message: '',
    });
  };
  
  return (
    <section id="contact" className="py-20 bg-gradient-to-b from-black to-gray-950 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Inscrição</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6">Comece Hoje Mesmo</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Preencha o formulário abaixo para começar a jornada de aprendizado e diversão do seu filho.
            Nossa equipe entrará em contato em até 24 horas.
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 gap-16 items-center">
          <div className="relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-purple-600/30 to-blue-600/30 rounded-3xl blur-xl opacity-70"></div>
            <div className="relative bg-gray-900 border border-gray-800 rounded-2xl p-8">
              <h3 className="text-2xl font-bold mb-6">Entre em Contato</h3>
              
              <div className="space-y-6">
                <div className="flex items-start">
                  <Mail className="h-6 w-6 text-purple-400 mt-1 mr-4" />
                  <div>
                    <h4 className="font-semibold mb-1">Email</h4>
                    <p className="text-gray-400">contato@titi.com.br</p>
                  </div>
                </div>
                
                <div className="flex items-start">
                  <Phone className="h-6 w-6 text-purple-400 mt-1 mr-4" />
                  <div>
                    <h4 className="font-semibold mb-1">Telefone</h4>
                    <p className="text-gray-400">(11) 9999-9999</p>
                  </div>
                </div>
                
                <div className="flex items-start">
                  <MapPin className="h-6 w-6 text-purple-400 mt-1 mr-4" />
                  <div>
                    <h4 className="font-semibold mb-1">Endereço</h4>
                    <p className="text-gray-400">Av. Paulista, 1000 - São Paulo/SP</p>
                  </div>
                </div>
              </div>
              
              <div className="mt-8 pt-8 border-t border-gray-800">
                <h4 className="font-semibold mb-3">Horário de Atendimento</h4>
                <p className="text-gray-400 mb-1">Segunda a Sexta: 8h às 18h</p>
                <p className="text-gray-400">Sábado: 9h às 13h</p>
              </div>
            </div>
          </div>
          
          <div>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium mb-1">Seu Nome</label>
                  <input 
                    type="text" 
                    id="name" 
                    name="name" 
                    value={formData.name}
                    onChange={handleChange}
                    className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                    required
                  />
                </div>
                
                <div>
                  <label htmlFor="email" className="block text-sm font-medium mb-1">Seu Email</label>
                  <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    value={formData.email}
                    onChange={handleChange}
                    className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                    required
                  />
                </div>
              </div>
              
              <div>
                <label htmlFor="phone" className="block text-sm font-medium mb-1">Telefone</label>
                <input 
                  type="tel" 
                  id="phone" 
                  name="phone" 
                  value={formData.phone}
                  onChange={handleChange}
                  className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                  required
                />
              </div>
              
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <label htmlFor="childName" className="block text-sm font-medium mb-1">Nome da Criança</label>
                  <input 
                    type="text" 
                    id="childName" 
                    name="childName" 
                    value={formData.childName}
                    onChange={handleChange}
                    className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                    required
                  />
                </div>
                
                <div>
                  <label htmlFor="childAge" className="block text-sm font-medium mb-1">Idade da Criança</label>
                  <input 
                    type="number" 
                    id="childAge" 
                    name="childAge" 
                    value={formData.childAge}
                    onChange={handleChange}
                    className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                    required
                    min="0"
                    max="15"
                  />
                </div>
              </div>
              
              <div>
                <label htmlFor="message" className="block text-sm font-medium mb-1">Mensagem (Opcional)</label>
                <textarea 
                  id="message" 
                  name="message" 
                  value={formData.message}
                  onChange={handleChange}
                  rows={4} 
                  className="w-full p-3 rounded-lg bg-gray-900 border border-gray-800 text-white focus:border-purple-500 focus:ring-1 focus:ring-purple-500 transition-colors"
                ></textarea>
              </div>
              
              <div>
                <button 
                  type="submit" 
                  className="w-full py-3 px-6 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-semibold rounded-lg hover:from-purple-700 hover:to-blue-700 transition-all duration-300 flex items-center justify-center"
                >
                  Enviar Inscrição
                  <Send className="ml-2 h-5 w-5" />
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;