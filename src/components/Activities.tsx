import React from 'react';
import { Palette, BookOpen, Music, Code, Gamepad2, Brain, ArrowRight } from 'lucide-react';

const activityData = [
  {
    id: 1,
    title: 'Arte & Criatividade',
    description: 'Desenvolva habilidades artísticas e criativas através de pinturas, esculturas e projetos artísticos divertidos.',
    icon: <Palette className="h-10 w-10 text-purple-500" />,
    color: 'from-purple-500 to-pink-500',
  },
  {
    id: 2,
    title: 'Leitura & Escrita',
    description: 'Estimule o amor pela leitura e escrita através de atividades interativas e contação de histórias.',
    icon: <BookOpen className="h-10 w-10 text-blue-500" />,
    color: 'from-blue-500 to-cyan-500',
  },
  {
    id: 3,
    title: 'Música & Dança',
    description: 'Explore o mundo da música e dança através de jogos rítmicos, instrumentos e coreografias divertidas.',
    icon: <Music className="h-10 w-10 text-green-500" />,
    color: 'from-green-500 to-teal-500',
  },
  {
    id: 4,
    title: 'Programação & Tecnologia',
    description: 'Introdução ao mundo da tecnologia e programação através de jogos e atividades adequadas para cada idade.',
    icon: <Code className="h-10 w-10 text-orange-500" />,
    color: 'from-orange-500 to-amber-500',
  },
  {
    id: 5,
    title: 'Jogos & Diversão',
    description: 'Jogos educativos que promovem trabalho em equipe, raciocínio e coordenação motora.',
    icon: <Gamepad2 className="h-10 w-10 text-red-500" />,
    color: 'from-red-500 to-rose-500',
  },
  {
    id: 6,
    title: 'Raciocínio Lógico',
    description: 'Atividades que desenvolvem o raciocínio lógico e habilidades cognitivas através de enigmas e desafios.',
    icon: <Brain className="h-10 w-10 text-violet-500" />,
    color: 'from-violet-500 to-purple-500',
  },
];

const ActivityCard = ({ title, description, icon, color }) => {
  return (
    <div className="bg-gray-900 rounded-2xl p-6 transition-all duration-300 hover:translate-y-[-8px] hover:shadow-lg hover:shadow-purple-900/20">
      <div className={`bg-gradient-to-r ${color} w-16 h-16 rounded-xl flex items-center justify-center mb-6`}>
        {icon}
      </div>
      <h3 className="text-xl font-bold mb-3">{title}</h3>
      <p className="text-gray-400">{description}</p>
    </div>
  );
};

const Activities = () => {
  return (
    <section id="activities" className="py-20 bg-black px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Nossas Atividades</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6">Atividades Educativas e Divertidas</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Oferecemos uma variedade de atividades projetadas para desenvolver habilidades essenciais
            enquanto garantimos que seu filho esteja se divertindo e aprendendo.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {activityData.map(activity => (
            <ActivityCard 
              key={activity.id} 
              title={activity.title} 
              description={activity.description} 
              icon={activity.icon}
              color={activity.color}
            />
          ))}
        </div>
        
        <div className="text-center mt-12">
          <a 
            href="#pricing" 
            className="inline-flex items-center py-3 px-6 bg-gray-900 border border-gray-800 rounded-full text-purple-400 hover:bg-gray-800 transition-all duration-300"
          >
            Ver Todos os Planos
            <ArrowRight className="ml-2 h-5 w-5" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Activities;