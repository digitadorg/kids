
import React from 'react';
import { BrainCircuit, UserPlus, Clock, Heart } from 'lucide-react';

const Benefits = () => {
  return (
    <section id="benefits" className="py-20 bg-gradient-to-b from-black to-gray-950 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Por Que os Pais Inteligentes Escolhem Titi</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6 text-white">O Que Seu Filho Vai Desenvolver Enquanto os Outros Estão Presos nas Telas</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Benefícios reais, visíveis, transformadores — em poucas semanas. A infância é uma janela curta, e cada atividade aqui dentro foi criada pra aproveitar ao máximo esse tempo.
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 gap-8 lg:gap-16">
          <div className="relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-purple-600 to-blue-600 rounded-3xl blur-xl opacity-50"></div>
            <div className="relative bg-gray-900 rounded-2xl overflow-hidden">
              <div className="aspect-w-4 aspect-h-3">
                <img 
                  src="https://images.pexels.com/photos/8535214/pexels-photo-8535214.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" 
                  alt="Crianças em atividades criativas" 
                  className="object-cover w-full h-full"
                />
              </div>
            </div>
          </div>
          
          <div className="flex flex-col justify-center">
            <ul className="space-y-6">
              <li className="flex">
                <div className="flex-shrink-0 flex items-center justify-center w-12 h-12 rounded-full bg-purple-900/30 text-purple-400">
                  <BrainCircuit className="h-6 w-6" />
                </div>
                <div className="ml-4">
                  <h3 className="text-xl font-semibold mb-1">Cérebro em Construção</h3>
                  <p className="text-gray-400">
                    Enquanto outras crianças estão passivas em frente a telas, aqui elas treinam foco, criatividade e lógica — preparando o terreno para um cérebro ágil e resiliente.
                  </p>
                </div>
              </li>
              
              <li className="flex">
                <div className="flex-shrink-0 flex items-center justify-center w-12 h-12 rounded-full bg-blue-900/30 text-blue-400">
                  <UserPlus className="h-6 w-6" />
                </div>
                <div className="ml-4">
                  <h3 className="text-xl font-semibold mb-1">Confiança Social</h3>
                  <p className="text-gray-400">
                    Interações que despertam empatia, liderança e comunicação. Em vez de timidez e isolamento, seu filho aprende a se conectar e se expressar com segurança.
                  </p>
                </div>
              </li>
              
              <li className="flex">
                <div className="flex-shrink-0 flex items-center justify-center w-12 h-12 rounded-full bg-green-900/30 text-green-400">
                  <Clock className="h-6 w-6" />
                </div>
                <div className="ml-4">
                  <h3 className="text-xl font-semibold mb-1">Rotina Sem Caos</h3>
                  <p className="text-gray-400">
                    Estrutura, organização e tarefas criativas. Com apenas 15 minutos por dia, seu filho desenvolve hábitos de disciplina que muitos adultos nunca conquistaram.
                  </p>
                </div>
              </li>
              
              <li className="flex">
                <div className="flex-shrink-0 flex items-center justify-center w-12 h-12 rounded-full bg-red-900/30 text-red-400">
                  <Heart className="h-6 w-6" />
                </div>
                <div className="ml-4">
                  <h3 className="text-xl font-semibold mb-1">Corpo e Mente em Sintonia</h3>
                  <p className="text-gray-400">
                    Atividades físicas leves e divertidas que fortalecem a coordenação motora, o vínculo com o corpo e a autoestima — sem academias, sem pressão.
                  </p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Benefits;
