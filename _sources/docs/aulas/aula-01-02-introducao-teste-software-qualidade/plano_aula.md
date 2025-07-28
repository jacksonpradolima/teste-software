# Plano de Aulas 1-2: Apresentação da Disciplina, Introdução ao Teste de Software e Qualidade de Software

## Objetivo Geral

Proporcionar aos alunos uma introdução aprofundada ao universo do Teste de Software, contextualizando sua relevância histórica, científica e mercadológica. Discutir conceitos de qualidade de software e apresentar o modelo de qualidade ISO/IEC 25010, estabelecendo as bases para o entendimento dos atributos que determinam um software confiável, funcional e alinhado às expectativas dos usuários e do mercado.

## Objetivos Específicos

1. **Compreender a importância histórica e prática do Teste de Software** no contexto do desenvolvimento de sistemas.
2. **Identificar os objetivos fundamentais dos testes de software**, incluindo prevenção de defeitos, verificação de funcionalidades e garantia de qualidade.
3. **Situar o Teste de Software dentro dos diferentes modelos de desenvolvimento de software**, reconhecendo seu papel em metodologias tradicionais e ágeis.
4. **Conhecer e analisar o modelo de qualidade de software ISO/IEC 25010**, incluindo cada um dos seus oito atributos principais.
5. **Estabelecer conexões entre qualidade de software e satisfação do usuário**, mercado e sustentabilidade do negócio.
6. **Explorar a Curva de Boehm** para demonstrar o impacto econômico de detecções tardias de defeitos no ciclo de desenvolvimento.
7. **Introduzir a disciplina aos alunos, estabelecendo expectativas, metodologia de avaliação e plano de ensino.**

## Conteúdo Programático Detalhado

**1. Apresentação da Disciplina**

* Breve explanação do cronograma semestral.
* Critérios de avaliação: provas teóricas, seminário temático, projeto integrador.
* Metodologias de ensino: expositiva dialogada, estudos de caso, práticas orientadas.
* Objetivos esperados da disciplina.
* Discussão das expectativas dos alunos sobre o tema.

**2. Introdução ao Teste de Software**

* Definição do que é Teste de Software.
  + Origens do teste de software: das origens da programação procedural aos sistemas distribuídos modernos.
  + A evolução das práticas de teste frente à evolução dos paradigmas de desenvolvimento.
* Objetivos do Teste de Software:
  + Identificar e corrigir erros, falhas e defeitos.
  + Assegurar que o software cumpre com seus requisitos funcionais e não funcionais.
  + Reduzir o custo do ciclo de desenvolvimento ao prevenir erros.
  + Melhorar a qualidade percebida pelo usuário final.
  + Conformidade regulatória em setores críticos (ex.: saúde, financeiro, aeronáutico).
* Diferença entre **verificação**, **validação** e **teste**.
  + Verificação: o software está sendo desenvolvido corretamente?
  + Validação: o software desenvolvido atende as necessidades do cliente?
  + Teste: atividade prática para verificar e validar o software.

**3. O Papel dos Testes nos Modelos de Processo**

* Modelos Tradicionais:
  + Cascata (Waterfall): posição tardia dos testes e seus riscos.
  + Modelo V: paralelismo entre desenvolvimento e testes.
* Modelos Iterativos:
  + RUP: cada iteração inclui atividades de teste.
* Modelos Ágeis:
  + Scrum: testes contínuos a cada sprint.
  + XP: prática do TDD como método de desenvolvimento orientado a testes.
* DevOps:
  + Testes automatizados integrados às pipelines de integração e entrega contínua (CI/CD).
* Discussão sobre as diferenças de mentalidade: "desenvolver primeiro, testar depois" vs "desenvolver testando".

**4. Qualidade de Software**

* O que é qualidade em software?
  + Definições clássicas de qualidade: Juran, Deming.
  + Qualidade percebida vs qualidade intrínseca.
  + Fatores que afetam a qualidade: código, processos, equipe, ferramentas.
* O padrão ISO/IEC 25010:
  + Visão geral do padrão.
  + **Oito características de qualidade:**
    1. **Funcionalidade:** adequação, acurácia, interoperabilidade, segurança funcional.
    2. **Confiabilidade:** maturidade, disponibilidade, tolerância a falhas.
    3. **Usabilidade:** compreensão, aprendizado, operabilidade.
    4. **Eficiência de Desempenho:** tempos de resposta, consumo de recursos.
    5. **Segurança:** confidencialidade, integridade, autenticidade.
    6. **Compatibilidade:** coexistência, interoperabilidade.
    7. **Manutenibilidade:** modularidade, reusabilidade, analisabilidade.
    8. **Portabilidade:** adaptabilidade, instalabilidade, substituibilidade.
* Exemplos práticos para cada atributo.

**5. A Curva de Boehm**

* Introdução ao estudo econômico de Barry Boehm.
* A relação entre o custo de corrigir um defeito e o momento em que ele é identificado:
  + Requisitos
  + Design
  + Codificação
  + Testes
  + Produção
* Simulações com exemplos reais:
  + Custo médio de um erro encontrado em produção vs na codificação.
* Implicações para a cultura de testes precoces.

**6. Qualidade e o Mercado**

* Impacto direto da qualidade na percepção do cliente e na competitividade do negócio.
* Estudos de caso de empresas que falharam por baixa qualidade.
* Compliance e certificações que exigem práticas de qualidade e testes.
* Tendências de mercado:
  + DevOps e Quality Gates.
  + Quality Engineering vs Quality Assurance.
  + Testes integrados com observabilidade.

**7. Teste de Software como Atividade Multidisciplinar**

* Convergência com:
  + Engenharia de Software
  + Gestão de Projetos
  + Design de Experiência do Usuário (UX)
  + Segurança da Informação
  + Data Science e Inteligência Artificial (IA explicável e testabilidade)

## Metodologia

**1. Aula Expositiva Dialogada**

* Utilização de recursos audiovisuais para apresentar conceitos iniciais.
* Discussão aberta com a turma sobre:
  + O que eles entendem por qualidade de software?
  + Experiências anteriores com sistemas com falhas.
  + Exemplos reais trazidos pelos alunos.

**2. Estudo de Caso Coletivo**

* Análise conjunta de um caso real de falha em software e suas consequências (exemplo: Recall do software de freios em carros, incidentes em sistemas bancários).
* Reflexão sobre o impacto da qualidade deficiente.

**3. Exercício Conceitual**

* Divisão da turma em grupos para listar exemplos práticos de cada atributo da ISO/IEC 25010 com sistemas que conhecem ou utilizam.

**4. Exposição Visual da Curva de Boehm**

* Simulação prática e ilustrada dos custos de correção em diferentes fases.
* Discussão sobre prevenção versus correção.

**5. Discussão Dirigida**

* Debate sobre como o mercado trata a qualidade atualmente.
* Papel do QA moderno frente às práticas de DevOps.

**6. Mapa Mental**

* Construção coletiva de um mapa mental sobre qualidade de software, seus atributos e sua relação com os testes.

**7. Leitura Recomendada**

* Textos introdutórios sobre a ISO/IEC 25010.
* Artigos acadêmicos e relatos de empresas sobre problemas gerados por falhas em software.
