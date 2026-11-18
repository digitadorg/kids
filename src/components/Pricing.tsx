import { Check, ArrowRight, Zap } from 'lucide-react';

const pricingPlans = [
  {
    id: 1,
    name: 'Plano Semente',
    price: 'R$99',
    period: '/mês',
    description: 'Para quem quer plantar o hábito do aprendizado — com impacto visível nas primeiras semanas.',
    features: [
      '3 atividades estratégicas por semana',
      'Material digital com orientação para pais',
      'Missões de foco e criatividade',
      'Certificado Titi de conclusão'
    ],
    color: 'from-blue-500 to-purple-500',
    popular: false,
    buttonText: 'Quero Começar Agora',
  },
  {
    id: 2,
    name: 'Plano Formação de Líderes',
    price: 'R$159',
    period: '/mês',
    description: 'O plano mais escolhido pelos pais que querem preparar seus filhos para liderar, não obedecer.',
    features: [
      'Acesso completo a todas as atividades',
      'Kits físicos enviados todo mês (sem custo extra)',
      'Aulas ao vivo com especialistas',
      'Mentoria comportamental e de rotina',
      'Grupo exclusivo de pais conscientes',
      'Atividades bônus de autoconhecimento'
    ],
    color: 'from-purple-500 to-pink-500',
    popular: true,
    buttonText: 'Transformar Meu Filho Agora',
  },
  {
    id: 3,
    name: 'Plano Legado Familiar',
    price: 'R$259',
    period: '/mês',
    description: 'Para famílias que entendem que educação de verdade é a maior herança que se pode deixar.',
    features: [
      'Tudo do plano Formação de Líderes',
      'Acesso completo para até 3 crianças',
      'Kits personalizados por idade',
      'Sessões individuais com educador',
      'Descontos vitalícios em eventos e cursos especiais'
    ],
    color: 'from-blue-500 to-cyan-500',
    popular: false,
    buttonText: 'Quero Esse Legado',
  }
];

const PricingCard = ({ plan }) => {
  return (
    <div className={`relative ${plan.popular ? 'lg:-mt-8' : ''}`}>
      {plan.popular && (
        <div className="absolute -top-5 inset-x-0 flex justify-center">
          <span className="inline-flex items-center px-4 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-purple-600 to-pink-600 text-white">
            <Zap className="h-4 w-4 mr-1" />
            Mais Popular
          </span>
        </div>
      )}
      
      <div className={`h-full bg-gray-900 border ${plan.popular ? 'border-purple-500/30' : 'border-gray-800'} rounded-2xl p-6 lg:p-8 flex flex-col transition-all duration-300 hover:border-purple-500/50 hover:shadow-xl hover:shadow-purple-900/20`}>
        <div className="mb-6">
          <h3 className="text-xl font-bold mb-2">{plan.name}</h3>
          <p className="text-gray-400 text-sm">{plan.description}</p>
        </div>
        
        <div className="mb-6">
          <div className="flex items-baseline">
            <span className="text-3xl font-bold">{plan.price}</span>
            <span className="text-gray-400 ml-1">{plan.period}</span>
          </div>
        </div>
        
        <ul className="space-y-3 mb-8 flex-grow">
          {plan.features.map((feature, index) => (
            <li key={index} className="flex items-start">
              <div className={`flex-shrink-0 flex items-center justify-center h-5 w-5 bg-gradient-to-r ${plan.color} rounded-full mr-2 mt-0.5`}>
                <Check className="h-3 w-3 text-white" />
              </div>
              <span className="text-gray-300 text-sm">{feature}</span>
            </li>
          ))}
        </ul>
        
        <div className="mt-auto">
          <a 
            href="#contact" 
            className={`w-full py-3 px-4 rounded-lg text-center font-semibold transition-all duration-300 flex items-center justify-center ${
              plan.popular 
                ? 'bg-gradient-to-r from-purple-600 to-pink-600 text-white hover:from-purple-700 hover:to-pink-700' 
                : 'bg-gray-800 text-white hover:bg-gray-700'
            }`}
          >
            {plan.buttonText}
            <ArrowRight className="ml-2 h-4 w-4" />
          </a>
        </div>
      </div>
    </div>
  );
};

const Pricing = () => {
  return (
    <section id="pricing" className="py-20 bg-black px-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400 font-semibold tracking-wider uppercase">Invista no Futuro do Seu Filho</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-3 mb-6 text-white">Uma Decisão Que Vai Te Orgulhar Daqui a 6 Meses</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            Os pais que mais se arrependem… são os que deixaram pra depois. Dê ao seu filho a chance de desenvolver o que realmente importa — enquanto a janela da infância ainda está aberta.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {pricingPlans.map(plan => (
            <PricingCard key={plan.id} plan={plan} />
          ))}
        </div>
        
        <div className="mt-16 bg-gray-900 border border-gray-800 rounded-2xl p-8 text-center">
          <h3 className="text-xl font-bold mb-4">Precisa de um plano personalizado?</h3>
          <p className="text-gray-400 mb-6">
            Entre em contato conosco para discutir opções personalizadas para escolas, 
            grupos ou necessidades específicas.
          </p>
          <a 
            href="#contact" 
            className="inline-flex items-center py-3 px-6 bg-gray-800 hover:bg-gray-700 rounded-lg text-white transition-all duration-300"
          >
            Falar com um Consultor
            <ArrowRight className="ml-2 h-5 w-5" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Pricing;