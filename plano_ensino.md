# Identificação

Disciplina: Teste de Software I

Carga Horária – 72 horas-aula

# Ementa

* Princípios e Técnicas de teste.
* Conceitos básicos de teste:
  + Defeito
  + Falha
  + casos de teste
  + critérios de teste.
* Técnicas de Teste:
  + funcional (caixa-preta)
  + estrutural (caixa branca).
* Estratégias de teste:
  + teste unitário
  + teste de integração
  + teste de regressão
  + desenvolvimento orientado a testes.

# Objetivos

## Objetivo Geral (prever a contribuição da disciplina em termos do conhecimento, habilidade e atitudes para formação do egresso)

Capacitar o aluno a compreender, aplicar e criticar os princípios, conceitos fundamentais e técnicas clássicas e modernas de Teste de Software, por meio de abordagens práticas e teóricas, visando assegurar a qualidade de produtos de software por meio da verificação sistemática, validação criteriosa e gestão eficaz de defeitos, promovendo habilidades práticas, competências analíticas e atitudes orientadas à melhoria contínua no desenvolvimento, integração e manutenção de sistemas computacionais.

## Objetivos Específicos

* Compreender os conceitos fundamentais de qualidade de software, incluindo defeito, falha, erro, incidente, verificação e validação.
* Conhecer e aplicar técnicas de teste funcional (caixa-preta), como particionamento de equivalência e análise de valor limite.
* Conhecer e aplicar técnicas de teste estrutural (caixa-branca), como cobertura de instruções, decisões e caminhos independentes.
* Identificar e aplicar as diferentes estratégias de testes: unitário, integração, regressão e de sistema.
* Aplicar o Desenvolvimento Orientado a Testes (TDD) em projetos simples, evidenciando os benefícios para o design do software.
* Conhecer e discutir práticas de Behavior-Driven Development (BDD) e Acceptance Test-Driven Development (ATDD) para melhoria da comunicação entre stakeholders e desenvolvedores.
* Elaborar e interpretar casos de teste, critérios de parada e métricas de qualidade, relacionando-os ao contexto real do desenvolvimento.
* Planejar, executar e gerenciar o processo de testes, incluindo a geração de dados de teste e a gestão de defeitos utilizando ferramentas adequadas.
* Desenvolver a habilidade de utilizar ferramentas de automação de testes e gestão de testes reconhecidas no mercado.
* Integrar os conhecimentos adquiridos na disciplina por meio do desenvolvimento de um projeto integrador final, aplicando de forma prática os conceitos de teste de software.
* Refletir criticamente sobre o papel estratégico do teste de software na engenharia de software e sua relação com as boas práticas de desenvolvimento e manutenção.

# Metodologia

* Aulas Expositivas Dialogadas: Explanação teórica acompanhada de discussões orientadas e exemplos práticos.
* Estudos de Caso: Análise de situações reais ou simuladas para aplicar conceitos e técnicas de testes.
* Práticas em Laboratório: Aplicação prática de técnicas de testes em projetos ou códigos fornecidos pelo professor, especialmente em testes unitários e integração.
* Demonstrações com Ferramentas de Mercado: Exposição prática das ferramentas utilizadas no mercado, como JUnit, PyTest, Postman, Selenium, etc.
* Seminários Temáticos: Apresentação de temas complementares pelos alunos, incentivando a pesquisa e o desenvolvimento da comunicação técnica.
* Projeto Integrador Final: Desenvolvimento de um projeto prático que abranja a aplicação completa das técnicas de testes aprendidas, gerando um artefato consolidado de qualidade de software.

# Avaliação

|  |  |  |
| --- | --- | --- |
| **Componente** | **Peso** | **Bimestre** |
| Prova Teórica I | 60% | 1 |
| Seminário Temático | 40% | 1 |
| Prova Teórica II | 50% | 2 |
| Projeto Integrador Final | 50% | 2 |

# Conteúdo Programático

|  |  |  |
| --- | --- | --- |
| **Aula** | **Tema** | **Conteúdo** |
| **1º Bimestre – Fundamentos, Técnicas e Estratégias de Teste** | | |
| 1-2 | * Apresentação da Disciplina * Introdução e Qualidade de Software | * Introdução ao Teste de Software: definição, histórico e evolução no contexto do desenvolvimento de software. * Conceitos de qualidade de software: definição, atributos segundo o modelo ISO/IEC 25010 (funcionalidade, confiabilidade, usabilidade, eficiência de desempenho, segurança, compatibilidade, manutenibilidade e portabilidade). * Importância dos testes no ciclo de vida do software. * Curva de Boehm: custo de correção de defeitos ao longo das fases de desenvolvimento. |
| 3-4 | Conceitos Fundamentais de Teste | * Definições e diferenças entre erro, falha, defeito e incidente. * Conceito de bug e sua categorização. * Validação vs Verificação: definições, exemplos práticos e importância no ciclo de testes. * Visão geral do SWEBOK e sua relação com a disciplina de testes. * Contextualização dos testes em modelos de processo de software tradicionais (Cascata, RUP) e modernos (Ágil, DevOps). |
| 5 | Casos de Teste e Critérios | * O que são casos de teste: elementos que o compõem (ID, entrada, ação, saída esperada). * Como criar casos de teste eficientes. * Conceito de critérios de teste: critérios de entrada e saída, critérios de cobertura. * Heurísticas para construção de bons casos de teste. * Exemplos de elaboração de casos de teste para sistemas reais. |
| 6-8 | Técnicas de Teste Funcional (Caixa-Preta) | * Técnicas baseadas na especificação ou requisitos do sistema: * - Particionamento de Equivalência: definição de classes de equivalência válidas e inválidas. * - Análise do Valor Limite: identificação de fronteiras críticas que devem ser testadas. * - Tabelas de Decisão: representação de lógica condicional complexa para definir combinações de entradas e saídas. * - Máquina de Estados: uso de diagramas de estados para modelar e criar casos de teste que abrangem transições possíveis. * - Testes Baseados em Casos de Uso: como derivar casos de teste diretamente das descrições dos requisitos. * Exemplos aplicados em sistemas de autenticação, sistemas bancários e e-commerce. |
| 9-10 | Técnicas de Teste Estrutural (Caixa-Branca) | * Critérios Baseados em Fluxo de Controle e em Fluxo de Dados * Técnicas baseadas no conhecimento da implementação e estrutura do código fonte: * - Cobertura de Instrução: garantir que cada linha de código seja executada pelo menos uma vez. * - Cobertura de Decisão: verificar que todas as decisões (if, while, for) tomem todas as possibilidades de caminho. * - Caminhos Independentes: identificação de caminhos únicos através do grafo de controle de fluxo para maximizar a cobertura lógica. * - Condições Combinadas: testes que garantem todas as combinações possíveis de condições dentro das decisões. * Apresentação de ferramentas que auxiliam na medição de cobertura de código (Ex: JaCoCo, Coverage.py). |
| 11 | Critérios de Parada e Métricas de Teste | * Quando parar de testar? Definição de critérios de parada: * - Cobertura de código atingida * - Quantidade de defeitos estabilizada * - Prazo ou custo limite alcançado. * Métricas de teste: * - Taxa de detecção de defeitos * - Taxa de cobertura de código * - Densidade de defeitos * - Defect Removal Efficiency (DRE) * Discussão sobre como interpretar essas métricas em projetos reais. |
| 12-14 | Estratégias de Teste: Unitário, Integração, Regressão | * Teste Unitário: foco na menor unidade testável do software. Conceitos, ferramentas (JUnit, PyTest, Jest), boas práticas de escrita de testes e isolamento com mocks e stubs. * Teste de Integração: testes que avaliam a interação entre módulos/sistemas. Estratégias de integração incremental (top-down, bottom-up, sanduíche) vs integração Big Bang. * Teste de Regressão: definição, importância, como organizar uma suíte de regressão eficiente, automação do processo para garantir qualidade contínua após mudanças. * Exemplos práticos e simulações com APIs simples e aplicações modulares. |
| 15-16 | Desenvolvimento Orientado a Testes (TDD, BDD, ATDD) | * Test-Driven Development (TDD): conceito e ciclo Red-Green-Refactor. * Impacto do TDD no design do software e manutenção. * Práticas de escrita de testes antes do código. * Behavior-Driven Development (BDD): extensão do TDD que enfatiza o comportamento esperado usando Gherkin, Cucumber. * Acceptance Test-Driven Development (ATDD): foco no desenvolvimento guiado por critérios de aceitação definidos em conjunto com o cliente. * Comparativo entre TDD, BDD e ATDD com exercícios simples para fixação. |
| 17 | Geração de Dados de Teste | * - Conceito de geração de dados sintéticos - Técnicas manuais e automáticas - Dados válidos vs inválidos - Ferramentas básicas * - Estratégias para testes funcionais e estruturais - Geração com base em modelos (Model-Based Generation) - Geração de massa de dados para testes de performance - Demonstração prática |
| 18 | Prova Teórica I | * Prova escrita presencial abordando todos os conteúdos do 1º bimestre. * Valor: 60% da nota do 1º bimestre. |
| 12-16 | Seminário Temático | * Ocorrerá ao longo das aulas 12 a 16. Cada grupo apresentará um tema previamente definido. * Valor: 40% da nota do 1º bimestre. |
| **2º Bimestre – Gestão de Testes, Ferramentas e Projeto Prático** | | |
| 19-20 | Gestão de Testes e Defeitos | * Planejamento de Testes: definição de objetivos, escopo, estratégia de testes, recursos e cronograma. * Plano de Testes: estrutura e exemplos. * Matriz de Rastreabilidade: ligação entre requisitos, casos de teste e defeitos. * Gestão de Defeitos: ciclo de vida do defeito, ferramentas de gestão como Jira e Azure DevOps, classificação e priorização de defeitos. |
| 21-22 | Métricas e Qualidade no CI/CD | * Métricas de Teste: Defect Density, Mean Time to Detect (MTTD), Mean Time to Repair (MTTR). * Quality Gates: o que são e como são aplicados no pipeline CI/CD. * Exemplos práticos do uso de métricas em pipelines de DevOps. * Conceitos de qualidade contínua e automação dos testes no fluxo de entrega contínua. |
| 23-24 | Testes Baseados em Modelos e Mutação | * Model-Based Testing (MBT): definição, construção de modelos de comportamento do sistema e geração automática de casos de teste. * Teste de Mutação: conceito, objetivos e exemplos com ferramentas como PIT e MutPy. * Importância do Teste de Mutação para a verificação da eficácia da suíte de testes. |
| 25-26 | Testes de Performance e Segurança | * Teste de Performance e Carga: conceitos, planejamento e execução com ferramentas como JMeter e k6. * Teste de Segurança: introdução ao OWASP Top 10, principais vulnerabilidades encontradas em aplicações web e técnicas de teste específicas para identificá-las. * Ferramentas básicas para iniciar a prática de testes de segurança. |
| 27-28 | Testes em Microserviços e Observabilidade | * Testes em Microserviços: desafios, estratégias, ferramentas de contract testing (Pact), integração contínua. * Observabilidade: conceitos de logs, métricas e traces, sua importância para identificar e diagnosticar falhas em ambientes produtivos. * Ferramentas como Prometheus, Grafana e Jaeger. |
| 29-30 | Ferramentas de Teste | * Apresentação prática de ferramentas utilizadas nas diferentes fases de teste: * - Testes Unitários: JUnit, PyTest * - Testes de Integração: Postman, REST Assured * - Testes Funcionais: Selenium, Cypress * - Gestão de Testes: TestLink, Zephyr * - Plugins e extensões úteis nos IDEs. * Discussão sobre critérios de escolha de ferramentas. |
| 31-33 | Projeto Integrador Final | * Orientações gerais sobre o escopo do projeto integrador. * Desenvolvimento prático em equipe com suporte do professor. * Aplicação dos conceitos aprendidos: * - Planejamento de testes * - Elaboração de casos de teste * - Aplicação de técnicas de teste (caixa-preta, caixa-branca, unitários, integração) * - Produção de relatório e documentação. * Preparação para apresentação final. |
| 34-35 | Apresentação do Projeto Integrador | * Apresentação formal dos projetos desenvolvidos pelas equipes. * Discussão dos resultados obtidos, problemas enfrentados e soluções aplicadas. * Valor: 50% da nota do 2º bimestre. |
| 36 | Prova Teórica II | * Prova escrita presencial abrangendo todos os conteúdos do 2º bimestre. * Valor: 50% da nota do 2º bimestre. |

A seguir, o **detalhamento** dos blocos.

**Detalhamento das Aulas**

## Aulas 1-2: Apresentação da Disciplina, Introdução ao Teste de Software e Qualidade de Software

### Objetivo Geral

Proporcionar aos alunos uma introdução aprofundada ao universo do Teste de Software, contextualizando sua relevância histórica, científica e mercadológica. Discutir conceitos de qualidade de software e apresentar o modelo de qualidade ISO/IEC 25010, estabelecendo as bases para o entendimento dos atributos que determinam um software confiável, funcional e alinhado às expectativas dos usuários e do mercado.

### Objetivos Específicos

1. **Compreender a importância histórica e prática do Teste de Software** no contexto do desenvolvimento de sistemas.
2. **Identificar os objetivos fundamentais dos testes de software**, incluindo prevenção de defeitos, verificação de funcionalidades e garantia de qualidade.
3. **Situar o Teste de Software dentro dos diferentes modelos de desenvolvimento de software**, reconhecendo seu papel em metodologias tradicionais e ágeis.
4. **Conhecer e analisar o modelo de qualidade de software ISO/IEC 25010**, incluindo cada um dos seus oito atributos principais.
5. **Estabelecer conexões entre qualidade de software e satisfação do usuário**, mercado e sustentabilidade do negócio.
6. **Explorar a Curva de Boehm** para demonstrar o impacto econômico de detecções tardias de defeitos no ciclo de desenvolvimento.
7. **Introduzir a disciplina aos alunos, estabelecendo expectativas, metodologia de avaliação e plano de ensino.**

### Conteúdo Programático Detalhado

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

### Metodologia

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

Perfeito. Iniciarei agora o desenvolvimento completo e detalhado da:

## Aulas 3-4: Conceitos Fundamentais de Teste

### Objetivo Geral

Capacitar os alunos a compreenderem profundamente os conceitos fundamentais que estruturam o campo do Teste de Software. Estabelecer uma base conceitual sólida que permita diferenciar os diversos termos utilizados na área — como erro, defeito, falha e incidente —, contextualizar o papel dos testes nas diversas fases do desenvolvimento de software e, principalmente, reconhecer a importância do teste como ferramenta para redução de riscos e melhoria contínua da qualidade.

### Objetivos Específicos

1. **Definir e diferenciar conceitos essenciais do Teste de Software**, como erro, falha, defeito e incidente, com exemplos práticos.
2. **Compreender o conceito de bug**, sua categorização e implicações em ambientes de produção.
3. **Distinguir entre verificação e validação**, apresentando suas definições, práticas associadas e contextos de aplicação.
4. **Explorar o papel do SWEBOK (Software Engineering Body of Knowledge)** na estruturação dos processos de teste.
5. **Identificar onde o teste de software se posiciona nos diferentes modelos de desenvolvimento de software**: tradicionais, iterativos, ágeis e DevOps.
6. **Analisar a evolução dos testes diante dos paradigmas modernos de desenvolvimento**, destacando mudanças de mentalidade e de abordagem.
7. **Fomentar o raciocínio crítico sobre o papel estratégico dos testes na redução de riscos, otimização de custos e aumento da qualidade percebida.**

### Conteúdo Programático Detalhado

**1. Definições Básicas em Teste de Software**

**1.1 O que é Teste de Software?**

* Definição formal segundo IEEE e ISTQB.
* Teste como processo sistemático e disciplinado de:
  + Exercitar o software
  + Identificar discrepâncias entre o comportamento esperado e o comportamento observado
  + Determinar a conformidade com os requisitos especificados

**1.2 O que NÃO é Teste de Software**

* Oposição a mitos comuns:
  + “Testar é só executar o sistema”
  + “Testar só serve para achar erro”
  + “Teste é responsabilidade exclusiva do QA”
  + “Teste é só no final”

**2. Conceitos Fundamentais**

**2.1 Erro (Mistake)**

* Definição: ação humana que produz um resultado incorreto.
* Exemplos práticos:
  + Um programador que implementa uma soma ao invés de uma multiplicação.
  + Um analista de requisitos que documenta um requisito com ambiguidade.

**2.2 Defeito (Fault ou Bug)**

* Definição: manifestação de um erro no código ou na documentação.
* Exemplos:
  + Um if com condição inversa.
  + Um endpoint com tratamento inadequado de autenticação.

**2.3 Falha (Failure)**

* Definição: comportamento incorreto ou inesperado do software em execução.
* Exemplo:
  + Um sistema de compras que cobra duas vezes pelo mesmo item devido a um defeito no controle de transações.

**2.4 Incidente**

* Definição: manifestação observável de uma falha que afeta o usuário ou o sistema.
* Exemplo:
  + O crash de uma aplicação durante o uso.

**2.5 Relação Causal**

* Erro ➡️ Defeito ➡️ Falha ➡️ Incidente
* Discussão sobre como erros podem não se manifestar imediatamente em falhas, dependendo do contexto de execução.

**3. O Conceito de Bug**

* Definição histórica e etimologia do termo (Grace Hopper e o primeiro "bug" físico).
* Diferença entre bug técnico e bug de usabilidade.
* Classificações de bugs:
  + Bugs críticos
  + Bugs bloqueantes
  + Bugs de prioridade baixa
* Discussão sobre bugs famosos que geraram prejuízos bilionários.

**4. Verificação, Validação e Teste**

**4.1 Verificação**

* Processo de garantir que o produto está sendo construído corretamente.
* Atividades associadas:
  + Revisões técnicas
  + Inspeções de código
  + Análise estática

**4.2 Validação**

* Processo de garantir que o produto certo está sendo construído.
* Atividades associadas:
  + Prototipagem
  + Testes de aceitação
  + Validação com usuários

**4.3 Diferenças e Complementaridades**

* Verificação = conformidade com a especificação.
* Validação = alinhamento com a necessidade do usuário.

| **Verificação** | **Validação** |
| --- | --- |
| O produto está certo? | O produto certo foi feito? |
| Conformidade técnica | Atende à necessidade? |
| Ex: Revisão de código | Ex: Teste de Aceitação |

**5. O SWEBOK e a Engenharia de Software**

**5.1 O que é o SWEBOK**

* Guide to the Software Engineering Body of Knowledge.
* Organização das áreas do conhecimento em Engenharia de Software.

**5.2 Área de Teste no SWEBOK**

* Definição dos objetivos do teste segundo o SWEBOK.
* Processos e práticas sugeridas.
* Papel do teste na garantia de qualidade.
* Benefícios de uma prática estruturada.

**5.3 Integração com outras áreas:**

* Engenharia de Requisitos
* Design de Software
* Construção de Software
* Manutenção

**6. Modelos de Desenvolvimento de Software e a Inserção do Teste**

**6.1 Modelos Tradicionais**

* **Modelo Cascata:** testes só no final ➡️ risco elevado.
* **Modelo V:** integração de verificação e validação desde o início.

**6.2 Modelos Iterativos e Incrementais**

* **RUP:** testes por iteração, evolução contínua da qualidade.

**6.3 Modelos Ágeis**

* **Scrum:** testes em cada sprint, conceito de Definition of Done.
* **XP:** práticas como TDD, integração contínua, testes automatizados.

**6.4 DevOps**

* Integração contínua + entrega contínua + monitoramento contínuo.
* Testes automatizados como parte do pipeline.

**6.5 Comparativo entre os Modelos**

| **Modelo** | **Quando Testa** | **Tipo de Teste** |
| --- | --- | --- |
| Cascata | Final | Manual, Sistemático |
| V | Paralelo | Manual + Automático |
| RUP | Iterativo | Focado em Requisitos |
| Scrum | Cada Sprint | Automático, Exploratório |
| DevOps | A cada commit | Automatizado, Monitoramento |

**7. Mudança de Mentalidade: Teste como Atividade Estratégica**

* De "teste como custo" para "teste como investimento".
* O papel do Teste na redução de riscos.
* Redução de custos com identificação precoce de erros.
* A cultura Shift-Left: testar cedo, testar sempre.
* Papel da equipe multidisciplinar.

**8. Exercício de Fixação**

* Criação de um fluxograma representando a relação entre erro, defeito, falha e incidente.
* Classificação de problemas reais (exemplos em apps populares) conforme os conceitos aprendidos.

### Metodologia

**1. Aula Expositiva Dialogada**

* Apresentação dos conceitos com apoio visual, gráficos e fluxogramas.
* Resgate histórico do teste de software.

**2. Estudo de Casos**

* Análise de grandes falhas de software que causaram prejuízos relevantes.
* Exemplos: bug do foguete Ariane 5, apagão do TSE, vulnerabilidade do Heartbleed.

**3. Discussão em Grupo**

* Divisão da turma para discutir experiências pessoais de falhas de software e tentar classificar em erro, defeito, falha ou incidente.

**4. Mapa Conceitual Coletivo**

* Construção de um mapa conceitual ao final da aula para consolidar os principais conceitos.

**5. Leitura Dirigida**

* Trechos selecionados do SWEBOK.
* Textos sobre modelos de desenvolvimento e o papel do teste.

**6. Prática Orientada**

* Exercício para que os alunos montem um comparativo dos modelos de desenvolvimento que já conhecem e como cada um integra ou não os testes.

Perfeito. Prosseguirei agora com a **Aula 3 — Casos de Teste e Critérios**, conforme solicitado, com:

* Objetivo Geral
* Objetivos Específicos
* Conteúdo Programático extremamente detalhado
* Metodologia completa

## Aula 5: Casos de Teste e Critérios

### Objetivo Geral

Capacitar o aluno a **compreender, construir e avaliar casos de teste a partir de requisitos de software**, aplicando critérios sólidos para criação, execução e encerramento dos testes. A aula buscará desenvolver no aluno o raciocínio sistemático e crítico para converter requisitos e comportamentos esperados em **casos de teste bem estruturados**, apoiando-se em critérios formais que assegurem a eficiência e eficácia da atividade de testes.

### Objetivos Específicos

1. **Definir o que são casos de teste**, suas partes constituintes e o papel que exercem no processo de validação de software.
2. **Identificar as principais características de um bom caso de teste**, segundo práticas e padrões reconhecidos pela área.
3. **Distinguir entre diferentes tipos de casos de teste**: positivos, negativos, exploratórios, regressivos.
4. **Compreender o papel dos critérios de teste**, tanto para a elaboração de casos quanto para o encerramento dos testes.
5. **Desenvolver a habilidade de criar casos de teste a partir de requisitos funcionais e não funcionais.**
6. **Refletir sobre a rastreabilidade dos casos de teste em relação aos requisitos.**
7. **Praticar a criação de casos de teste para cenários reais e simulados, com identificação de entradas, ações e saídas esperadas.**
8. **Estabelecer critérios para priorização de casos de teste em contextos com restrição de recursos.**

### Conteúdo Programático Detalhado

**1. O que é um Caso de Teste**

* Definição formal:
  + Um artefato que define um conjunto de condições ou variáveis sob as quais um testador determinará se um sistema ou parte dele funciona conforme o esperado.
* Função no ciclo de testes:
  + Serve como guia para a execução dos testes.
  + Ajuda na documentação do que foi testado e dos resultados esperados.
  + Promove consistência na atividade de teste.

**2. Componentes de um Caso de Teste**

| **Elemento** | **Descrição** |
| --- | --- |
| **Identificador (ID)** | Código único para o caso de teste. |
| **Título ou Descrição** | Breve descrição do objetivo do teste. |
| **Pré-condições** | Estado necessário do sistema antes da execução do teste. |
| **Entradas** | Dados ou ações fornecidos ao sistema. |
| **Passos de execução** | Passos ordenados a serem realizados. |
| **Resultado esperado** | O que o sistema deve retornar ou como deve se comportar. |
| **Resultado obtido** | O que ocorreu de fato durante o teste. |
| **Status** | Indica se o teste passou, falhou ou está bloqueado. |
| **Observações** | Comentários adicionais ou exceções. |

**3. Tipos de Casos de Teste**

* **Positivos**
  + Valida o comportamento esperado em condições ideais.
  + Exemplo: autenticar com credenciais válidas.
* **Negativos**
  + Verifica como o sistema reage a entradas inválidas ou ações não previstas.
  + Exemplo: tentar autenticar com senha incorreta.
* **Exploratórios**
  + Criados dinamicamente durante a exploração do sistema.
  + Exige alto nível de experiência do testador.
* **De Regressão**
  + Testa funcionalidades já existentes após mudanças no sistema para garantir que não houve efeitos colaterais.

**4. O Papel dos Critérios de Teste**

* Critérios orientam:
  + **Criação de casos de teste**
  + **Cobertura necessária**
  + **Encerramento do ciclo de testes**
* Principais tipos:
  + **Critérios de entrada:** pré-requisitos para iniciar o teste.
  + **Critérios de saída:** condições que definem quando um ciclo de teste pode ser encerrado.
  + **Critérios de seleção:** quais funcionalidades ou módulos devem ser priorizados para teste.
  + **Critérios de cobertura:** quais tipos de cobertura devem ser atendidos (exemplo: cobertura de decisão, condição múltipla).

**5. Rastreabilidade dos Casos de Teste**

* Definição:
  + Capacidade de relacionar cada caso de teste a um requisito específico.
* Importância:
  + Facilita auditoria de qualidade.
  + Permite identificar rapidamente o impacto de mudanças nos requisitos.
* Matriz de rastreabilidade:
  + Documento que correlaciona requisitos aos casos de teste correspondentes.

**6. Boas Práticas na Elaboração de Casos de Teste**

* Clareza e objetividade na descrição.
* Evitar ambiguidade nas instruções.
* Cobrir todos os fluxos principais e alternativos.
* Reutilização: criação de templates para casos de teste padronizados.
* Priorizar testes críticos para o negócio.
* Revisão cruzada dos casos de teste por pares.

**7. Exemplos Práticos**

* Sistema de autenticação:
  + Caso positivo: login com usuário e senha corretos.
  + Caso negativo: login com usuário inexistente.
  + Caso negativo: login com senha incorreta.
  + Caso de performance: login com simultaneidade elevada.
* E-commerce:
  + Caso positivo: adicionar produto ao carrinho.
  + Caso negativo: tentar comprar com estoque zero.
  + Caso exploratório: tentar realizar checkout sem endereço cadastrado.

**8. Critérios de Priorização de Casos de Teste**

* Risco associado ao módulo/teste.
* Frequência de uso da funcionalidade.
* Complexidade técnica.
* Histórico de falhas.
* Impacto para o negócio em caso de erro.

**9. Documentação dos Casos de Teste**

* Exemplos de ferramentas:
  + TestLink
  + Zephyr
  + Xray
* Modelos simples em Excel ou Google Sheets para pequenas equipes.

**10. Exercício de Fixação**

* A partir de um caso hipotético (ex: sistema de reservas de hotel), criar:
  + 2 casos de teste positivos
  + 2 negativos
  + 1 exploratório
* Associar cada caso de teste a um requisito descrito.

### Metodologia

**1. Aula Expositiva Dialogada**

* Apresentação de conceitos com uso de slides, fluxogramas e exemplos reais.
* Discussão sobre experiências dos alunos com testes ou falta deles.

**2. Exemplos Práticos Guiados**

* O professor demonstrará a elaboração de casos de teste com base em um sistema conhecido pelos alunos.

**3. Atividade em Grupo**

* Dividir a turma em grupos e solicitar a construção de um conjunto de casos de teste para um sistema fictício apresentado em sala.

**4. Discussão dos Critérios de Teste**

* Debate orientado sobre como decidir quando parar de testar.
* Exercício para definir critérios de entrada e saída para um projeto simples.

**5. Mapa Conceitual**

* Construção coletiva de um mapa conceitual dos tipos de casos de teste e seus usos.

**6. Leitura Recomendada**

* Trechos do ISTQB Foundation Level sobre casos de teste.
* Artigos sobre critérios de cobertura e estratégias de priorização.

Perfeito. A seguir o desenvolvimento completo da:

## Aula 6: Técnicas de Teste Funcional (Caixa-Preta) — Parte 1

Esta aula corresponde ao primeiro bloco do conjunto de aulas **6 a 8** no cronograma, dedicada ao estudo das técnicas de teste funcional. Ela foca no **Particionamento de Equivalência** e na **Análise do Valor Limite**, iniciando a construção do conhecimento prático dos alunos sobre técnicas derivadas diretamente da especificação e dos requisitos do sistema.

### Objetivo Geral

Capacitar o aluno a **identificar, interpretar e aplicar técnicas de teste funcional do tipo caixa-preta**, com foco específico em **Particionamento de Equivalência** e **Análise do Valor Limite**, permitindo a formulação de casos de teste capazes de verificar a conformidade do software em relação às suas especificações funcionais e aos comportamentos esperados.

### Objetivos Específicos

1. **Definir o que são técnicas de teste funcional (caixa-preta)** e como se diferenciam das técnicas estruturais (caixa-branca).
2. **Explicar o conceito de Particionamento de Equivalência**, suas regras, aplicação prática e limites.
3. **Explicar o conceito de Análise do Valor Limite**, suas aplicações e importância na detecção de defeitos em fronteiras de valores.
4. **Identificar quando aplicar cada técnica no processo de teste.**
5. **Desenvolver habilidades para construir casos de teste aplicando essas técnicas a partir de requisitos especificados.**
6. **Demonstrar a aplicabilidade das técnicas em sistemas reais como autenticação, transações financeiras, validações de formulários, etc.**
7. **Comparar a eficiência entre casos de teste criados empiricamente e casos de teste criados sistematicamente a partir das técnicas aprendidas.**
8. **Fomentar o pensamento crítico quanto à cobertura funcional e à eficiência dos testes gerados.**

### Conteúdo Programático Detalhado

**1. Revisão Breve: O que é Teste Funcional (Caixa-Preta)**

* Definição:
  + Testes baseados no comportamento do sistema especificado, sem conhecimento da implementação interna.
* Comparativo com caixa-branca:
  + O testador não precisa conhecer o código.
  + Foco em entradas e saídas.
* Vantagens:
  + Abordagem orientada ao usuário e aos requisitos.
  + Identificação de falhas de integração e de interface.
* Limitações:
  + Não garante cobertura total do código.
  + Pode não identificar falhas em lógicas internas não refletidas nas saídas observadas.

**2. Particionamento de Equivalência**

**2.1 Definição**

* Técnica que divide o domínio de entrada de um programa em classes de dados que são tratadas de maneira equivalente pelo sistema.
* Objetivo: minimizar o número de casos de teste necessários mantendo a cobertura adequada.

**2.2 Conceitos**

* **Classes de Equivalência Válidas:** dados que o sistema deve aceitar.
* **Classes de Equivalência Inválidas:** dados que o sistema deve rejeitar ou tratar como erro.
* Cada classe deve ser testada pelo menos uma vez.

**2.3 Regras de Identificação**

* Para cada condição de entrada com um intervalo ou conjunto de valores, criar:
  + Uma classe válida.
  + Uma ou mais classes inválidas.

**2.4 Exemplo Prático**

* Campo de idade válido entre 18 e 60 anos:
  + Válida: 18-60
  + Inválida: <18 e >60
* Gerar casos de teste:
  + Idade = 25 (válida)
  + Idade = 15 (inválida)
  + Idade = 65 (inválida)

**2.5 Benefícios**

* Redução drástica no número de testes.
* Cobertura eficiente do domínio de entrada.

**2.6 Limitações**

* Pode não capturar problemas em valores fronteiriços (exatamente nos limites válidos e inválidos).

**3. Análise do Valor Limite**

**3.1 Definição**

* Técnica que foca em valores nos limites das classes de equivalência.
* Justificativa: é nos limites que sistemas frequentemente falham.

**3.2 Aplicação**

* Para um intervalo definido, testar:
  + Limite inferior -1, limite inferior, limite inferior +1
  + Limite superior -1, limite superior, limite superior +1
* Exemplo:
  + Idade permitida: 18 a 60
  + Testes: 17, 18, 19, 59, 60, 61

**3.3 Comparativo com Particionamento**

| **Técnica** | **Foco** |
| --- | --- |
| Particionamento | Classes amplas de dados equivalentes |
| Valor Limite | Pontos críticos nas fronteiras |

**3.4 Exemplo Prático em Sistema Bancário**

* Limite de saque: R$50 a R$2000
* Testes:
  + R$49, R$50, R$51
  + R$1999, R$2000, R$2001

**3.5 Benefícios**

* Alta taxa de detecção de defeitos em validações.

**3.6 Limitações**

* Ineficaz se o problema estiver dentro da classe e não no limite.

**4. Estratégia Combinada: Particionamento + Valor Limite**

* Uso complementar para maximizar a detecção de falhas.
* Exemplo combinado em sistema de inscrição:
  + Campo idade: aplicar particionamento.
  + Número de dependentes: aplicar valor limite.

**5. Casos de Uso Comuns**

* Validações de formulários.
* Transações financeiras.
* Sistemas de autenticação.
* Sistemas de pontuação ou faixas de preços.

**6. Exercícios Práticos Orientados**

* Definir particionamento e valores limite para:
  + Sistema de validação de senha (mínimo 8 caracteres, máximo 20)
  + Sistema de notas acadêmicas (0 a 10)
  + Sistema de login com tentativas máximas (3 tentativas permitidas)

**7. Boas Práticas**

* Documentar sempre os critérios usados para criar o caso.
* Justificar a escolha dos valores testados.
* Revisar os limites sempre que requisitos mudarem.

**8. Problemas Frequentes ao Aplicar**

* Definir classes de equivalência incorretas ou incompletas.
* Ignorar limites extremos por falha na interpretação do requisito.

### Metodologia

**1. Aula Expositiva com Slides e Quadro**

* Apresentação teórica dos conceitos.
* Desenho de diagramas no quadro para ilustrar classes de equivalência.

**2. Exemplos Reais**

* O professor demonstrará testes escritos para sistemas reais simulados.

**3. Atividade em Duplas**

* Os alunos criarão juntos exemplos de particionamento e valor limite para um sistema escolhido pelo professor.

**4. Discussão Coletiva**

* Comparação das soluções propostas pelos grupos.
* Avaliação dos critérios adotados.

**5. Estudo de Caso**

* Aplicação das técnicas em um caso fictício completo fornecido pelo professor.

**6. Leitura Complementar**

* Capítulo específico do livro "Software Testing - A Craftsman's Approach" sobre técnicas de teste funcional.
* Leitura de material do ISTQB sobre o tema.

## Aulas 7-8: Técnicas de Teste Funcional (Caixa-Preta) — Parte 2

Esta aula é a continuidade do estudo aprofundado sobre técnicas de teste funcional (caixa-preta), abordando de forma detalhada:

* **Tabelas de Decisão**
* **Máquinas de Estado**
* **Testes Baseados em Casos de Uso**

### Objetivo Geral

Capacitar os alunos a aplicarem técnicas avançadas de teste funcional (caixa-preta), especialmente aquelas relacionadas à modelagem de regras de negócio complexas e fluxos de estado, promovendo uma visão sistemática e estratégica para o planejamento de testes que garantam cobertura completa dos requisitos e comportamentos esperados do sistema.

### Objetivos Específicos

1. **Compreender o que são e como construir Tabelas de Decisão** para representar regras de negócio complexas.
2. **Interpretar e construir Máquinas de Estado para modelar o comportamento dinâmico dos sistemas.**
3. **Relacionar requisitos e fluxos de interação do sistema com Casos de Uso e derivar testes a partir deles.**
4. **Aplicar as técnicas aprendidas para criar casos de teste que garantam cobertura adequada dos cenários mais críticos.**
5. **Desenvolver a capacidade de visualizar o comportamento sistêmico e as transições possíveis, reduzindo o risco de omitir condições importantes.**
6. **Estabelecer comparações entre as técnicas para saber quando aplicar cada uma delas.**
7. **Fomentar o pensamento crítico na identificação de regras e fluxos não previstos ou ambíguos nos requisitos.**
8. **Conectar as técnicas com práticas modernas de modelagem como BPMN, UML e fluxos de interação em sistemas reativos.**

### Conteúdo Programático Detalhado

**1. Revisão Breve: Técnicas Funcionais (Caixa-Preta)**

* Recordação das técnicas anteriores:
  + Particionamento de Equivalência
  + Análise de Valor Limite
* Introdução ao foco da aula:
  + Técnicas para tratar regras complexas e transições de estado.

**2. Tabelas de Decisão**

**2.1 Definição**

* Estrutura que organiza **condições e ações** de forma tabular, permitindo representar regras de decisão complexas de maneira sistemática.
* Muito utilizadas em sistemas que possuem diversas combinações possíveis de entradas.

**2.2 Componentes**

* **Condições:** perguntas ou critérios que podem ser verdadeiros ou falsos.
* **Ações:** operações ou respostas do sistema.
* **Regras:** combinações entre condições e as ações que devem ser tomadas.

**2.3 Estrutura de uma Tabela de Decisão**

| **Condições / Regras** | **Regra 1** | **Regra 2** | **Regra 3** | **...** |
| --- | --- | --- | --- | --- |
| Condição A | V | V | F |  |
| Condição B | F | V | V |  |
| ... |  |  |  |  |
| **Ação X** | X |  | X |  |
| **Ação Y** |  | X |  |  |

**2.4 Exemplo Prático**

* Sistema de concessão de crédito:
  + Condições:
    - Renda > R$5000
    - Nome limpo
    - Score de crédito > 700
  + Ações:
    - Crédito aprovado
    - Crédito condicionado
    - Crédito negado
* Construção da tabela e dos respectivos casos de teste derivados.

**2.5 Benefícios**

* Organiza regras complexas.
* Ajuda a identificar combinações não previstas.
* Facilita a validação de requisitos.

**2.6 Desvantagens**

* Crescimento exponencial de combinações em sistemas muito complexos.

**3. Máquinas de Estado**

**3.1 Definição**

* Modelos matemáticos que descrevem o comportamento de um sistema através de **estados e transições**.

**3.2 Componentes**

* **Estado:** condição atual do sistema.
* **Transição:** mudança de um estado para outro baseada em eventos ou condições.
* **Evento:** ação ou condição que dispara a transição.
* **Ação:** comportamento executado durante ou após a transição.

**3.3 Exemplo Prático**

* Sistema de autenticação:
  + Estados: Deslogado, Logando, Logado, Bloqueado
  + Transições: Login bem-sucedido, Tentativa falha, Limite de tentativas excedido
* Representação gráfica do modelo.

**3.4 Construção de Máquinas de Estado**

* Identificar os estados do sistema.
* Definir os eventos que causam transições.
* Mapear transições válidas e inválidas.
* Determinar ações associadas.

**3.5 Benefícios**

* Permite visualizar o comportamento do sistema ao longo do tempo.
* Facilita a identificação de transições incorretas ou estados inválidos.

**3.6 Limitações**

* Modelagem pode ser complexa para sistemas com muitos estados.

**4. Testes Baseados em Casos de Uso**

**4.1 Definição**

* Casos de Uso descrevem **interações entre o usuário e o sistema** para atingir um objetivo específico.
* A partir dos casos de uso, podem-se derivar cenários de teste que cobrem fluxos principais e alternativos.

**4.2 Estrutura de um Caso de Uso**

* **Ator:** quem interage com o sistema.
* **Fluxo principal:** caminho ideal para atingir o objetivo.
* **Fluxos alternativos:** variações ou exceções.
* **Pré-condições:** estado do sistema antes do uso.
* **Pós-condições:** estado esperado após o uso.

**4.3 Exemplo Prático**

* Sistema de reservas:
  + Caso de uso: Reservar Quarto
  + Ator: Cliente
  + Fluxo principal: Seleciona quarto > Insere dados > Confirma reserva
  + Fluxo alternativo: Falta de disponibilidade.

**4.4 Derivação de Casos de Teste**

* Criar casos para o fluxo principal.
* Criar casos para cada fluxo alternativo.
* Testar limites, exceções e condições de erro.

**4.5 Benefícios**

* Alta aderência ao comportamento esperado pelo usuário.
* Facilidade de comunicação com stakeholders.

**5. Comparação entre as Técnicas**

| **Técnica** | **Uso** |
| --- | --- |
| Tabela de Decisão | Regras complexas com múltiplas condições |
| Máquina de Estado | Sistemas com estados e transições definidos |
| Casos de Uso | Interação do usuário com o sistema |

**6. Exemplos de Aplicação em Sistemas Reais**

* Aplicativo bancário: autenticação, transações, bloqueio de conta.
* E-commerce: compra, cancelamento, troca.
* Sistemas industriais: controle de máquinas, modos de operação.

**7. Exercício Prático**

* Os alunos devem modelar:
  + Uma tabela de decisão para um sistema de concessão de crédito.
  + Uma máquina de estado para um sistema de controle de acesso.
  + Um caso de uso detalhado e respectivos testes para um sistema de login.

### Metodologia

**1. Aula Expositiva Visual**

* Uso de diagramas, fluxogramas e exemplos gráficos.
* Demonstração de ferramentas para desenhar máquinas de estado (ex: draw.io, Lucidchart).

**2. Estudo de Caso em Sala**

* Aplicação prática das técnicas a um sistema conhecido dos alunos.

**3. Atividade em Grupos**

* Cada grupo elabora um exemplo próprio de tabela de decisão ou máquina de estado.

**4. Apresentação dos Grupos**

* Compartilhamento dos modelos criados.
* Feedback colaborativo.

**5. Leitura Recomendada**

* SWEBOK capítulo sobre Model-Based Testing.
* Artigos sobre tabelas de decisão na área financeira.

Perfeito. A seguir o desenvolvimento completo da:

## Aulas 9-10: Técnicas de Teste Estrutural (Caixa-Branca)

Esta aula corresponde ao início do bloco de aulas **9-10** no cronograma, dedicadas às técnicas de teste estrutural. O foco será nos **Critérios Baseados em Fluxo de Controle** e **Critérios Baseados em Fluxo de Dados**, que são essenciais para garantir uma cobertura eficaz dos testes considerando a estrutura interna do código.

### Objetivo Geral

Capacitar os alunos a **compreender e aplicar técnicas de teste estrutural (caixa-branca)**, dominando os conceitos de **fluxo de controle** e **fluxo de dados**, para garantir uma cobertura eficiente do código-fonte por meio de critérios formais de teste, maximizando a detecção de defeitos lógicos e estruturais.

### Objetivos Específicos

1. **Diferenciar o teste funcional do teste estrutural**, compreendendo o papel específico de cada um no ciclo de vida dos testes.
2. **Definir e aplicar os principais critérios baseados em fluxo de controle**, como cobertura de instruções, decisões, caminhos independentes e condições combinadas.
3. **Compreender os critérios baseados em fluxo de dados**, incluindo definição de alcance, usos e critérios como all-definitions e all-uses.
4. **Construir grafos de fluxo de controle a partir de trechos de código ou pseudocódigo.**
5. **Calcular a complexidade ciclomática de um grafo de fluxo de controle.**
6. **Derivar casos de teste sistemáticos a partir do grafo para maximizar a cobertura.**
7. **Desenvolver habilidades práticas para aplicar essas técnicas em linguagens de programação reais.**
8. **Refletir criticamente sobre a relação entre cobertura de código e qualidade efetiva dos testes.**
9. **Conhecer ferramentas que auxiliam na medição da cobertura de código.**
10. **Simular a identificação de defeitos que não seriam detectados por testes funcionais, mas sim por testes estruturais.**

### Conteúdo Programático Detalhado

**1. Revisão: Teste Funcional vs Teste Estrutural**

* Revisão dos conceitos de caixa-preta (funcional) e introdução à caixa-branca (estrutural).
* Quando usar cada abordagem:
  + Funcional: valida requisitos e comportamentos externos.
  + Estrutural: explora o código internamente para validar sua lógica.
* Limitações de cada abordagem isolada.

**2. Fluxo de Controle**

**2.1 Definição**

* Representação gráfica da sequência de execução das instruções de um programa.
* Grafos de fluxo de controle: nós representam comandos/instruções, arcos representam o fluxo de execução.

**2.2 Critérios Baseados em Fluxo de Controle**

**2.2.1 Cobertura de Instrução (Statement Coverage)**

* Garante que **cada linha de código seja executada pelo menos uma vez**.
* Exemplo prático:
  + Código com if/else: é necessário ter casos que passem pelo if e pelo else.

**2.2.2 Cobertura de Decisão (Branch Coverage)**

* Garante que **cada decisão (condicional) seja avaliada tanto como verdadeira quanto como falsa**.
* Exemplo:
  + if (x > 10): deve haver um teste onde x > 10 e um onde x <= 10.

**2.2.3 Caminhos Independentes**

* Identificação de caminhos logicamente distintos no código.
* Cada caminho deve ser testado ao menos uma vez.

**2.2.4 Condições Combinadas**

* Para decisões compostas, cada combinação possível das condições deve ser testada.
* Exemplo:
  + if (A && B): testar A=true/B=true, A=true/B=false, A=false/B=true, A=false/B=false.

**2.3 Complexidade Ciclomática**

* Definição: medida do número de caminhos linearmente independentes em um programa.
* Fórmula: M = E - N + 2P
  + E = número de arestas
  + N = número de nós
  + P = número de componentes conectados
* Exemplo prático com cálculo para um grafo simples.

**2.4 Aplicação Prática**

* Gerar o grafo de fluxo de controle a partir de um código simples (ex: algoritmo de cálculo de fatorial).
* Determinar a complexidade ciclomática.
* Planejar casos de teste para cada caminho independente.

**3. Fluxo de Dados**

**3.1 Definição**

* Analisa como as variáveis são definidas, utilizadas e modificadas no fluxo do programa.
* Foco em identificar **definições e usos** das variáveis.

**3.2 Componentes**

* **Def (Definition):** onde a variável recebe um valor.
* **Use:** onde a variável é utilizada (em cálculo ou em decisões).
* **DU-pairs:** pares definição-uso.

**3.3 Critérios Baseados em Fluxo de Dados**

* **All-Defs:** cada definição de variável deve ser testada até pelo menos um uso.
* **All-Uses:** cada definição deve ser testada em todos os seus usos possíveis.
* **All-P-Uses/All-C-Uses:** todos os usos em predicados ou cálculos.

**3.4 Exemplo Prático**

* Analisar um código simples de média aritmética.
* Identificar todas as definições e usos das variáveis.
* Criar casos de teste que percorram todas as DU-pairs.

**4. Comparativo entre Fluxo de Controle e Fluxo de Dados**

| **Aspecto** | **Fluxo de Controle** | **Fluxo de Dados** |
| --- | --- | --- |
| Foco | Caminhos e decisões | Definição e uso de variáveis |
| Benefício | Cobertura lógica | Detecção de anomalias no uso de variáveis |
| Limitação | Não detecta todos os erros de dados | Pode não cobrir todas as decisões |

**5. Cobertura de Código na Prática**

* O que significa atingir 100% de cobertura de instrução?
* Ferramentas para medir cobertura:
  + **JaCoCo** (Java)
  + **Coverage.py** (Python)
  + **Istanbul** (JavaScript)
* Limitações da cobertura:
  + Ter alta cobertura não garante ausência de defeitos.
  + Qualidade do teste é tão importante quanto a quantidade.

**6. Exemplos de Defeitos Detectáveis por Teste Estrutural**

* Lógica inversa em uma condição.
* Variável não inicializada.
* Caminho do else nunca testado no funcional.

**7. Exercício Prático**

* O professor apresenta um algoritmo com if/else, for e while.
* Os alunos devem:
  + Construir o grafo de fluxo de controle.
  + Calcular a complexidade ciclomática.
  + Derivar casos de teste necessários.
  + Identificar definições e usos de variáveis para criar DU-pairs.

### Metodologia

**1. Aula Expositiva**

* Apresentação com slides e quadro para construção de grafos e cálculos.

**2. Exemplos Práticos**

* Demonstração de análise de código real.
* Aplicação de cobertura de código com ferramentas reais.

**3. Prática Guiada**

* Alunos constroem grafos e aplicam critérios em exemplos fornecidos.

**4. Discussão**

* Debate sobre casos onde mesmo com 100% de cobertura ainda há defeitos.
* Reflexão sobre a qualidade dos testes versus quantidade.

**5. Leitura Recomendada**

* Capítulo específico sobre testes estruturais em "The Art of Software Testing".
* Documentação oficial das ferramentas de cobertura.

## Aula 11: Critérios de Parada e Métricas de Teste

Essa aula aprofunda os aspectos estratégicos do processo de testes: quando parar de testar e como medir a eficiência e eficácia do processo através de métricas.

### Objetivo Geral

Capacitar os alunos a **identificar, definir e aplicar critérios de parada de testes**, além de **compreender e utilizar métricas de teste** para avaliação da qualidade do software e do processo de teste. O objetivo é formar um pensamento crítico e analítico para tomadas de decisão informadas no processo de desenvolvimento e manutenção de software.

### Objetivos Específicos

1. **Definir critérios de parada em um processo de teste**, considerando qualidade, tempo e custo.
2. **Compreender a importância de métricas de teste para a gestão da qualidade do software.**
3. **Identificar diferentes métricas utilizadas na prática de testes de software.**
4. **Calcular e interpretar métricas como cobertura de código, taxa de detecção de defeitos, densidade de defeitos e DRE (Defect Removal Efficiency).**
5. **Compreender as relações entre critérios de parada e métricas no contexto de gestão de riscos.**
6. **Aplicar o conhecimento em simulações de cenários de projetos para decidir o momento de interrupção do ciclo de testes.**
7. **Analisar criticamente limitações das métricas e dos critérios de parada, evitando interpretações superficiais ou enviesadas.**
8. **Refletir sobre como o uso adequado de métricas contribui para práticas de melhoria contínua no desenvolvimento de software.**

### Conteúdo Programático Detalhado

**1. Por Que Definir Critérios de Parada?**

* Problema prático: "Quando um software está suficientemente testado?"
* Riscos de testar indefinidamente:
  + Custo elevado
  + Atrasos em entregas
  + Diminuição do retorno sobre investimento (ROI)
* Riscos de encerrar prematuramente:
  + Defeitos críticos não detectados
  + Perda de credibilidade e confiança

**2. Tipos de Critérios de Parada**

**2.1 Baseados em Cobertura**

* Parar quando atingir uma determinada **cobertura de código**, como:
  + Cobertura de instrução: ex: 90%
  + Cobertura de decisões
  + Cobertura de condições combinadas

**2.2 Baseados em Defeitos**

* Parar após a identificação e correção de um número estabelecido de defeitos.
* Exemplo: "Encerrar quando o número de defeitos críticos restantes for 0 e de médios for inferior a 3."

**2.3 Baseados em Tempo**

* Limitação por prazo ou orçamento.
* Exemplo: "Encerrar testes ao fim de 4 semanas."

**2.4 Baseados em Taxa de Detecção de Defeitos**

* Quando a taxa de detecção se estabiliza ou diminui significativamente.
* Exemplo: "Nenhum defeito crítico encontrado nas últimas 100 execuções de teste."

**2.5 Baseados em Riscos**

* Definir um nível aceitável de risco residual.
* Exemplo: "Testar até que o risco de falha seja estimado abaixo de 1%."

**2.6 Baseados em Conformidade**

* Quando todos os critérios contratuais ou normativos forem atendidos.
* Exemplo: software médico que atende toda a regulamentação vigente.

**3. Métricas de Teste**

**3.1 Definição**

* Medidas quantitativas que ajudam a avaliar atributos do processo de teste, do produto de software ou da qualidade do processo de desenvolvimento.

**3.2 Métricas Fundamentais**

| **Métrica** | **Descrição** |
| --- | --- |
| **Cobertura de Código** | Percentual de código que foi executado pelos testes. |
| **Taxa de Detecção de Defeitos** | Defeitos encontrados por unidade de tempo ou execução. |
| **Densidade de Defeitos** | Número de defeitos por unidade de tamanho do software (ex: por mil linhas de código). |
| **Defect Removal Efficiency (DRE)** | Percentual de defeitos removidos antes da liberação em relação ao total de defeitos encontrados no software. |
| **MTTD (Mean Time to Detect)** | Tempo médio para detecção de um defeito após sua introdução. |
| **MTTR (Mean Time to Repair)** | Tempo médio para corrigir um defeito após sua detecção. |

**4. Cálculos Práticos**

**4.1 Cálculo de Cobertura**

* Fórmula:

Cobertura (%) = (Linhas executadas / Total de linhas de código) \* 100

**4.2 Cálculo de DRE**

DRE (%) = (Defeitos removidos antes da entrega / (Defeitos removidos antes + depois da entrega)) \* 100

**4.3 Densidade de Defeitos**

Densidade = Número de defeitos / KLOC (mil linhas de código)

**5. Interpretação das Métricas**

* Por que cobertura alta não significa qualidade?
* Exemplo: código com 95% de cobertura mas com lógica incorreta em 5% não coberto.
* A densidade de defeitos não é absoluta: depende da complexidade do sistema.
* O DRE acima de 90% é desejável, mas não garante perfeição.

**6. Métricas para Melhorias Contínuas**

* Estabelecimento de métricas ao longo de projetos para:
  + Identificar gargalos
  + Comparar produtividade de sprints
  + Avaliar eficácia dos testes automatizados

**7. Critérios de Parada x Métricas: Relação Estratégica**

| **Critério de Parada** | **Métrica Associada** |
| --- | --- |
| Cobertura | Cobertura de Código |
| Defeitos | Taxa de Detecção, Densidade |
| Tempo | MTTD, MTTR |
| Risco | Estimativas qualitativas + métricas quantitativas |

**8. Exercício de Simulação**

* Cenário: projeto com orçamento limitado e prazo de entrega próximo.
* Os alunos devem:
  + Definir critérios de parada.
  + Estabelecer quais métricas seriam usadas para monitorar o processo.
  + Simular decisões sobre continuar ou parar os testes diante de métricas hipotéticas.

### Metodologia

**1. Aula Expositiva**

* Introdução teórica aos conceitos com exemplos reais.

**2. Resolução Guiada de Exemplos**

* Aplicação de fórmulas de métricas com dados fictícios.

**3. Dinâmica de Grupo**

* Cada grupo define um plano de métricas para um projeto fictício.

**4. Discussão Dirigida**

* Debate sobre a suficiência ou não de critérios de parada em diferentes cenários.

**5. Leitura Recomendada**

* Artigos sobre métricas de teste em ambientes DevOps.
* Documentos de boas práticas do ISTQB.

## Aulas 12-14: Estratégias de Teste: Unitário, Integração e Regressão

Esta aula inaugura o bloco das **aulas 12-14**, abordando o planejamento e aplicação prática das **estratégias de teste** mais importantes do ciclo de desenvolvimento: testes unitários, de integração e de regressão.

### Objetivo Geral

Capacitar o aluno a **diferenciar, planejar e aplicar as principais estratégias de testes de software**, especificamente o **Teste Unitário, o Teste de Integração e o Teste de Regressão**, compreendendo os objetivos, técnicas, ferramentas e boas práticas envolvidas em cada abordagem para assegurar a qualidade do software em seus diversos níveis.

### Objetivos Específicos

1. **Definir os conceitos e objetivos do Teste Unitário, Teste de Integração e Teste de Regressão.**
2. **Identificar o papel de cada estratégia dentro do ciclo de vida de desenvolvimento e manutenção do software.**
3. **Aplicar práticas e ferramentas adequadas para a implementação de testes unitários em linguagens como Java, Python e JavaScript.**
4. **Compreender e aplicar as técnicas de integração incremental e Big Bang em Teste de Integração.**
5. **Planejar e executar testes de integração em APIs RESTful utilizando ferramentas como Postman e REST Assured.**
6. **Definir o que caracteriza um Teste de Regressão e planejar uma suíte eficiente e sustentável para garantir que correções ou novas implementações não impactem funcionalidades existentes.**
7. **Compreender o impacto da automação em cada uma dessas estratégias e a sua relação com práticas ágeis e DevOps.**
8. **Analisar criticamente a cobertura proporcionada por cada estratégia e suas limitações.**
9. **Construir um raciocínio estratégico para escolha e combinação das abordagens de teste, conforme o contexto e o tipo de sistema.**
10. **Elaborar exercícios práticos e colaborativos para cada uma das estratégias de teste abordadas.**

### Conteúdo Programático Detalhado

**1. Introdução às Estratégias de Teste**

* Definição de Estratégia de Teste:
  + Um plano de ação que descreve como os testes serão conduzidos para atingir objetivos específicos de qualidade.
* Importância de combinar diferentes estratégias para cobrir diferentes níveis e aspectos do software.

**2. Teste Unitário**

**2.1 Definição**

* Teste que verifica **individualmente** a menor unidade testável de um sistema, geralmente uma função, método ou classe.

**2.2 Objetivos**

* Garantir que cada unidade se comporta conforme o esperado isoladamente.
* Detectar defeitos precocemente no ciclo de desenvolvimento.

**2.3 Boas Práticas**

* Escrever testes pequenos e rápidos.
* Ter um único propósito por teste.
* Nomeação clara dos testes.
* Utilização de **mocks, stubs e spies** para isolar dependências.

**2.4 Ferramentas**

* **Java:** JUnit
* **Python:** PyTest, Unittest
* **JavaScript:** Jest, Mocha

**2.5 Exemplo Prático**

* Testar uma função que calcula o IMC:
  + Entrada: peso, altura
  + Saída: índice de IMC

**2.6 Métricas**

* Cobertura de código por testes unitários.
* Complexidade ciclomática aplicada a funções.

**3. Teste de Integração**

**3.1 Definição**

* Teste que verifica a interação entre **módulos ou componentes integrados**, validando a comunicação e o comportamento coletivo.

**3.2 Objetivos**

* Detectar falhas nas interfaces entre componentes.
* Garantir a compatibilidade entre módulos que foram testados isoladamente.

**3.3 Estratégias de Integração**

* **Incremental:** integração progressiva de módulos.
  + **Top-Down:** módulos de alto nível primeiro.
  + **Bottom-Up:** módulos de baixo nível primeiro.
  + **Sanduíche:** combinação dos dois anteriores.
* **Big Bang:** integração completa de todos os módulos ao mesmo tempo.

**3.4 Exemplo Prático**

* Sistema de pagamento integrado com serviço de autenticação e serviço de processamento de cartão.

**3.5 Ferramentas**

* **Postman:** para testar APIs manualmente.
* **REST Assured:** framework Java para testes automatizados de APIs REST.
* **TestContainers:** criar ambientes de integração reais em containers.

**4. Teste de Regressão**

**4.1 Definição**

* Teste que verifica se modificações no sistema (correções ou novas funcionalidades) não introduziram novos defeitos em partes que já funcionavam.

**4.2 Objetivos**

* Manter a estabilidade do sistema após mudanças.
* Assegurar que funcionalidades críticas continuam funcionando.

**4.3 Construção de Suíte de Regressão**

* Identificar as funcionalidades mais críticas.
* Automatizar sempre que possível.
* Manter atualizada com base nas mudanças no sistema.

**4.4 Estratégia de Manutenção**

* Refatoração contínua da suíte de regressão.
* Classificação dos testes por prioridade.

**4.5 Ferramentas**

* Selenium
* Cypress
* JUnit + MockMVC (para APIs REST em Spring Boot)

**4.6 Exemplo Prático**

* Após atualização de regras de desconto, executar todos os testes relacionados à lógica de preços.

**5. Comparativo entre as Estratégias**

| **Estratégia** | **Nível** | **Foco** | **Exemplo** |
| --- | --- | --- | --- |
| Unitário | Baixo | Função/método | Soma de dois números |
| Integração | Médio | Interação entre módulos | Serviço de pagamento + autenticação |
| Regressão | Todos | Garantia de não-regressão | Testar todo fluxo de compras após atualização |

**6. Impacto na Qualidade e no Processo Ágil**

* Teste unitário: alinhado ao TDD.
* Integração: essencial em integração contínua.
* Regressão: pilar para entrega contínua (CD).

**7. Exercícios Práticos**

1. Criar um teste unitário para uma função de cálculo de desconto.
2. Testar a integração entre dois módulos simples: autenticação e recuperação de senha.
3. Planejar uma suíte de regressão para um sistema de gestão de alunos.

### Metodologia

**1. Aula Expositiva**

* Apresentação com fluxogramas das estratégias.
* Vídeos curtos demonstrando ferramentas.

**2. Demonstração**

* Demonstração ao vivo de criação de teste unitário.
* Integração simples com Postman.
* Demonstração de regressão com Selenium.

**3. Prática Orientada**

* Cada aluno deve escrever um teste unitário em sua linguagem de escolha.
* Em duplas, simular integração entre APIs mockadas.

**4. Discussão**

* Qual estratégia aplicar primeiro?
* Como equilibrar tempo de escrita dos testes vs retorno em qualidade?

**5. Leitura Complementar**

* Capítulo sobre estratégias de teste em "Foundations of Software Testing".
* Artigos sobre integração contínua e testes automatizados.

Perfeito. A seguir o desenvolvimento completo da:

## Aulas 15-16: Desenvolvimento Orientado a Testes (TDD), Behavior-Driven Development (BDD) e Acceptance Test-Driven Development (ATDD)

Esta aula abre o bloco dedicado ao **Desenvolvimento Orientado a Testes**, essencial para aproximar a prática de desenvolvimento de software com qualidade garantida desde a origem do código.

### Objetivo Geral

Capacitar o aluno a **compreender, aplicar e diferenciar as práticas de TDD, BDD e ATDD**, integrando técnicas de teste diretamente ao processo de desenvolvimento de software, reforçando os pilares da qualidade, do design robusto e da comunicação entre times técnicos e de negócios.

### Objetivos Específicos

1. **Compreender o conceito de TDD (Test-Driven Development)**, seu ciclo de desenvolvimento e benefícios associados.
2. **Aprender o ciclo Red-Green-Refactor** característico do TDD e sua aplicação prática.
3. **Diferenciar TDD de outras abordagens de desenvolvimento com testes escritos após o código.**
4. **Compreender o conceito de BDD (Behavior-Driven Development)** como evolução do TDD orientado a comportamentos observáveis do sistema.
5. **Conhecer a sintaxe Gherkin e o framework Cucumber para aplicação do BDD.**
6. **Compreender o Acceptance Test-Driven Development (ATDD)** e sua utilização para alinhar expectativas com stakeholders.
7. **Estabelecer comparativos claros entre TDD, BDD e ATDD quanto aos objetivos, práticas e impactos no desenvolvimento.**
8. **Praticar a criação de testes TDD e BDD em exemplos reais.**
9. **Refletir sobre o impacto do desenvolvimento orientado a testes no design de software e na qualidade dos produtos entregues.**
10. **Discutir os desafios e limitações na adoção dessas práticas em projetos reais.**

### Conteúdo Programático Detalhado

**1. Introdução ao Desenvolvimento Orientado a Testes**

* Mudança de paradigma:
  + De: "codifique primeiro, teste depois"
  + Para: "teste antes de codificar"
* Importância na redução de defeitos.
* Papel no design de software: código mais simples, modular e testável.

**2. Test-Driven Development (TDD)**

**2.1 Definição**

* Prática de escrever primeiro o teste que **falhará**, depois o código mínimo necessário para passar o teste, seguido de refatoração.

**2.2 O Ciclo Red-Green-Refactor**

1. **Red:** escrever um teste que falha.
2. **Green:** escrever o código mínimo para passar o teste.
3. **Refactor:** melhorar o código mantendo o teste passando.

**2.3 Exemplo Prático**

* Criar uma função que soma dois números:
  1. Teste: soma(2,3) == 5 → falha.
  2. Implementar soma: return a + b.
  3. Refatorar se necessário.

**2.4 Benefícios**

* Feedback rápido.
* Design guiado por necessidades.
* Redução de defeitos.
* Confiança na refatoração.

**2.5 Desafios**

* Curva de aprendizado.
* Dificuldade em sistemas legados.
* Percepção de "lento" para prazos curtos.

**3. Behavior-Driven Development (BDD)**

**3.1 Definição**

* Extensão do TDD focada em **comportamentos do sistema observáveis externamente**.
* Comunicação facilitada entre devs, testers e negócios.

**3.2 Sintaxe Gherkin**

* Linguagem semiestruturada que descreve cenários de forma legível por humanos e máquinas.

**Feature**: Soma de números

**Scenario**: Somar dois números

    Given que tenho dois números 2 e 3

**When** eu somar esses números

**Then** o resultado deve ser 5

**3.3 Ferramentas**

* Cucumber
* SpecFlow (C#)
* Behave (Python)

**3.4 Exemplo Prático**

* Escrever feature Gherkin.
* Implementar step definitions.
* Validar o comportamento implementado.

**3.5 Benefícios**

* Melhora comunicação.
* Evita ambiguidades.
* Cria documentação viva.

**4. Acceptance Test-Driven Development (ATDD)**

**4.1 Definição**

* Variante do TDD orientada aos **critérios de aceitação** definidos em conjunto com o cliente ou Product Owner.

**4.2 Processo**

1. Negociação dos critérios de aceitação.
2. Escrever o teste de aceitação.
3. Desenvolver para passar no teste.

**4.3 Benefícios**

* Alinha expectativas.
* Garante o "Definition of Done".

**4.4 Exemplo Prático**

* Critério: "O usuário deve conseguir redefinir senha com link enviado por e-mail."
* Escrever o teste de aceitação antes de codificar.

**5. Comparativo entre TDD, BDD e ATDD**

| **Aspecto** | **TDD** | **BDD** | **ATDD** |
| --- | --- | --- | --- |
| Foco | Código | Comportamento | Critério de aceitação |
| Linguagem | Técnica | Semi-natural | Natural |
| Envolvidos | Devs | Devs + Testers | Devs + Testers + PO |
| Ferramentas | JUnit, PyTest | Cucumber | Cucumber, SpecFlow |

**6. Impacto no Design de Software**

* Código mais coeso.
* Melhor separação de responsabilidades.
* Menor acoplamento.

**7. Desafios de Adoção**

* Cultura organizacional.
* Maturidade da equipe.
* Custo inicial maior.

**8. Exercícios Práticos**

1. Criar um teste TDD para uma calculadora simples.
2. Escrever um cenário BDD para autenticação de usuário.
3. Simular um critério ATDD para fluxo de compra em e-commerce.

### Metodologia

**1. Aula Expositiva**

* Conceitos teóricos com exemplos incrementais.

**2. Demonstração**

* Exemplo prático ao vivo de TDD em código.

**3. Prática Dirigida**

* Os alunos implementam um pequeno módulo usando TDD.
* Em grupos, escreverem cenários BDD.

**4. Discussão**

* Pontos fortes e fracos percebidos nas abordagens.

**5. Leitura Complementar**

* "Growing Object-Oriented Software Guided by Tests"
* Documentação do Cucumber e Gherkin.

## Aula 17: Geração de Dados de Teste

Esta aula é dedicada a explorar de forma prática e teórica a **geração de dados de teste**, um tema transversal que impacta diretamente a eficácia dos testes funcionais, estruturais, de performance e de segurança. Os alunos aprenderão técnicas, ferramentas e boas práticas para **gerar dados adequados, válidos, inválidos, massivos e representativos** para os mais diversos cenários de teste.

### Objetivo Geral

Capacitar o aluno a **gerar, manipular e utilizar dados de teste adequados aos diferentes tipos de testes de software**, compreendendo o papel estratégico que os dados desempenham na validação eficaz de funcionalidades, comportamentos, limites e segurança dos sistemas.

### Objetivos Específicos

1. **Definir o que são dados de teste e por que sua qualidade impacta diretamente o sucesso dos testes de software.**
2. **Compreender os diferentes tipos de dados de teste:** válidos, inválidos, limite, massivos, anômalos.
3. **Explorar técnicas manuais e automáticas para geração de dados de teste.**
4. **Conhecer e aplicar ferramentas para geração de dados sintéticos e massivos.**
5. **Aprender estratégias para geração de dados realistas sem violar privacidade e segurança.**
6. **Entender como os dados de teste impactam testes funcionais, estruturais, de performance e de segurança.**
7. **Praticar a criação de dados para diferentes cenários de testes.**
8. **Compreender os desafios éticos e legais na manipulação e geração de dados, como privacidade e anonimização.**
9. **Refletir sobre as boas práticas de versionamento e manutenção de datasets de teste.**
10. **Simular um caso completo de preparação de dados para um ciclo de testes em diferentes níveis.**

### Conteúdo Programático Detalhado

**1. O que são Dados de Teste**

* Definição:
  + Dados utilizados para executar testes no software, simulando entradas, interações e comportamentos do usuário e do sistema.
* Função:
  + Validar funcionalidade
  + Testar limites e exceções
  + Detectar falhas de lógica
  + Avaliar performance e segurança

**2. Classificação dos Dados de Teste**

| **Tipo** | **Descrição** |
| --- | --- |
| **Válidos** | Dados que o sistema espera e deve processar corretamente. |
| **Inválidos** | Dados que o sistema deve rejeitar ou tratar com erro. |
| **Limite** | Valores nos extremos do permitido. |
| **Massivos** | Grandes volumes para stress e performance. |
| **Anômalos** | Dados incomuns ou inconsistentes que simulam erros ou fraudes. |

**3. Técnicas de Geração de Dados**

**3.1 Manual**

* Quando usar:
  + Cenários simples.
  + Controle total do que será testado.

**3.2 Automática**

* Scripts customizados
* Ferramentas específicas
* Algoritmos de randomização controlada

**3.3 Geração com Base em Modelos**

* Derivar dados diretamente de diagramas de classe, ER ou regras de negócio.

**3.4 Geração via TDD**

* Criar dados conforme o desenvolvimento dos testes.

**4. Ferramentas de Geração de Dados**

| **Ferramenta** | **Uso** |
| --- | --- |
| **Faker** | Geração de dados falsos realistas (nomes, emails, datas). |
| **Mockaroo** | Gerador de datasets customizados via web. |
| **DBMonster** | Inserção massiva de dados em bancos de dados. |
| **DataFactory** | Geração de massa para testes. |
| **Python faker library** | Automação de datasets em Python. |

**5. Boas Práticas para Dados de Teste**

* Diversidade de dados.
* Cobertura de cenários de erro.
* Reprodutibilidade dos datasets.
* Versionamento dos dados para garantir consistência nos testes.
* Anonimização de dados reais para evitar violação de privacidade.

**6. Geração de Dados em Testes de Performance**

* Workload com representatividade.
* Dados variados para evitar caching artificial.
* Consistência nos testes comparativos.

**7. Dados em Testes de Segurança**

* Injeções:
  + SQL Injection
  + XSS
  + Payloads maliciosos
* Fuzzing:
  + Envio massivo de entradas aleatórias.

**8. Aspectos Legais e Éticos**

* LGPD, GDPR: leis de proteção de dados.
* Anonimização e pseudonimização.
* Testes em ambiente separado da produção.

**9. Exercício Prático**

1. Criar um dataset com Faker para testes funcionais.
2. Gerar massa de dados com DBMonster para um banco PostgreSQL.
3. Simular inputs maliciosos para um formulário.

**10. Versionamento e Manutenção de Dados de Teste**

* Git para versionar scripts de geração.
* Armazenamento em bancos dedicados para testes.
* Automação na geração para cada ciclo de CI/CD.

### Metodologia

**1. Aula Expositiva**

* Explicação teórica com exemplos.

**2. Demonstração**

* Ferramentas Faker, Mockaroo, DBMonster.

**3. Prática em Grupo**

* Cada grupo cria um plano de geração para um sistema fictício.

**4. Discussão**

* Riscos legais na manipulação de dados.

**5. Leitura Complementar**

* Trechos sobre LGPD aplicados a TI.
* Documentação das bibliotecas apresentadas.

## Aula 18: Prova Teórica I

Nesta aula será realizada a **Prova Teórica I**, conforme previsto na avaliação do curso. Esta atividade formal tem como objetivo **avaliar os conhecimentos adquiridos pelos alunos durante o 1º bimestre**, abrangendo todos os conceitos, técnicas e práticas explorados nas aulas anteriores (Aulas 1 a 17).

### Objetivo Geral da Avaliação

Avaliar de forma sistemática e formal a **capacidade do aluno de compreender, aplicar e correlacionar os conceitos fundamentais de Teste de Software abordados no 1º bimestre**, incluindo princípios, técnicas, planejamento e práticas associadas ao ciclo de desenvolvimento de software.

### Competências Avaliadas

1. **Compreensão dos fundamentos do Teste de Software**: defeito, falha, erro, incidente.
2. **Conhecimento sobre qualidade de software e o modelo ISO/IEC 25010.**
3. **Capacidade de aplicação das técnicas de teste funcional (caixa-preta)**: particionamento de equivalência, análise do valor limite, tabelas de decisão, máquina de estados, casos de uso.
4. **Aplicação de técnicas de teste estrutural (caixa-branca)**: fluxo de controle, fluxo de dados, complexidade ciclomática.
5. **Planejamento de testes, elaboração de plano de testes e construção de matriz de rastreabilidade.**
6. **Compreensão e aplicação de critérios de parada e métricas de teste.**
7. **Conhecimento sobre TDD, BDD, ATDD e sua aplicação prática.**
8. **Geração de dados de teste adequados para diferentes contextos.**
9. **Escolha e entendimento do uso de ferramentas de teste.**

### Conteúdo Programático Avaliado

* Introdução ao Teste de Software, Qualidade e ISO/IEC 25010
* Conceitos fundamentais: erro, defeito, falha, incidente
* Técnicas de Teste Funcional:
  + Particionamento de Equivalência
  + Análise do Valor Limite
  + Tabelas de Decisão
  + Máquinas de Estado
  + Casos de Uso
* Técnicas de Teste Estrutural:
  + Cobertura de instrução, decisão
  + Caminhos independentes
  + Complexidade ciclomática
  + Fluxo de Dados (DU-pairs)
* Planejamento de Testes:
  + Plano de Testes
  + Matriz de Rastreabilidade
* Critérios de Parada e Métricas de Teste
* TDD, BDD, ATDD
* Geração de Dados de Teste
* Ferramentas apresentadas no curso

### Metodologia da Avaliação

**1. Estrutura da Prova**

A prova será composta por:

* **Questões dissertativas**: exigem explicações conceituais e aplicação teórica.
* **Estudos de caso**: cenários práticos para que o aluno aplique as técnicas aprendidas.
* **Exercícios de desenvolvimento e resolução**:
  + Criar caso de teste a partir de um requisito.
  + Desenhar uma tabela de decisão.
  + Elaborar uma matriz de rastreabilidade simplificada.
  + Cálculo de complexidade ciclomática a partir de um pseudocódigo.

**2. Critérios de Correção**

* Clareza conceitual.
* Aplicação prática correta das técnicas.
* Justificativa dos métodos utilizados.
* Capacidade de argumentação técnica.

### Objetivos de Aprendizagem

Após a avaliação, espera-se que o aluno:

1. Demonstre capacidade de articulação dos conceitos aprendidos.
2. Reflita sobre suas dificuldades e fortalezas nos tópicos trabalhados.
3. Tenha consolidado o conhecimento necessário para o aprofundamento no 2º bimestre.

### Orientações para os Alunos

* A prova terá duração de **2 horas**.
* Será permitido o uso de calculadora e régua para auxílio em diagramas.
* Não será permitido o uso de dispositivos eletrônicos ou consulta a materiais.

### Revisão Pré-Prova

Os alunos foram orientados previamente a revisar:

* Material das aulas 1 a 17.
* Exercícios e práticas realizados.
* Leituras indicadas.

### Próximos Passos

Após a aplicação da prova:

* Feedback detalhado será fornecido nas aulas seguintes.
* Correção orientada para que o aluno compreenda eventuais erros.
* Continuidade dos conteúdos do 2º bimestre com base no nível geral da turma.

Perfeito. Iniciarei agora o desenvolvimento completo da:

## Aulas 19-20: Gestão de Testes e Defeitos: Planejamento de Testes, Plano de Testes, Matriz de Rastreabilidade e Gestão de Defeitos

Estas aulas são dedicadas à **compreensão completa e prática do ciclo de gestão do processo de testes**, abrangendo desde o planejamento estratégico e tático até o monitoramento contínuo da qualidade do software. Os alunos serão conduzidos por todas as etapas formais e práticas de elaboração de um plano de testes, criação da matriz de rastreabilidade e gestão sistemática de defeitos, utilizando ferramentas de mercado e técnicas amplamente adotadas na indústria. Esta etapa do curso busca consolidar o entendimento de como o planejamento, o controle, o registro de defeitos e a rastreabilidade são fundamentais para garantir a entrega de produtos de software com qualidade, rastreáveis e auditáveis.

### Objetivo Geral

Capacitar o aluno a **planejar, documentar, executar, controlar e monitorar o processo de testes de software**, integrando técnicas de elaboração de um **plano de testes formal**, construção de uma **matriz de rastreabilidade completa** e condução da **gestão de defeitos durante o ciclo de vida do software**, com domínio de ferramentas, técnicas, métricas e boas práticas de qualidade.

### Objetivos Específicos

1. **Definir o planejamento de testes e compreender seu papel estratégico no ciclo de desenvolvimento de software.**
2. **Elaborar um plano de testes completo e formal com todos os componentes requeridos por padrões de mercado.**
3. **Construir e manter uma matriz de rastreabilidade que assegure a cobertura total dos requisitos e facilite a auditoria e manutenção dos testes.**
4. **Compreender o ciclo de vida de um defeito em projetos de software, desde a detecção até a resolução e verificação.**
5. **Aprender a documentar defeitos de forma eficiente, completa e clara, utilizando ferramentas de mercado como Jira, Bugzilla ou Mantis.**
6. **Classificar e priorizar defeitos com base em critérios técnicos e de impacto no negócio.**
7. **Aplicar métricas de qualidade relacionadas à gestão de testes e de defeitos para controle e tomada de decisão.**
8. **Gerenciar o processo de testes por meio de técnicas de controle, monitoramento contínuo e análise de riscos.**
9. **Integrar o planejamento, rastreabilidade e gestão de defeitos com práticas ágeis, DevOps e pipelines de CI/CD.**
10. **Simular em sala o ciclo completo de planejamento, execução, gestão de defeitos e entrega de relatórios gerenciais e técnicos.**

### Conteúdo Programático Detalhado

**1. Planejamento de Testes**

**1.1 O que é o Planejamento de Testes**

* Definição formal segundo IEEE 829.
* Diferença entre planejar e executar testes.
* Planejamento como estratégia de garantia da qualidade.
* Alinhamento do plano de testes ao plano do projeto.

**1.2 Finalidades do Planejamento**

* Determinar o escopo dos testes.
* Garantir cobertura adequada de requisitos.
* Prever recursos humanos, técnicos e financeiros.
* Estabelecer cronograma realista.
* Identificar riscos e restrições.
* Definir critérios de entrada e saída.

**1.3 Estrutura de um Planejamento Completo**

1. **Objetivos do Teste**
2. **Escopo**
3. **Abordagem (estratégias e técnicas adotadas)**
4. **Recursos Necessários**
   * Humanos
   * Infraestrutura
   * Ferramentas
5. **Cronograma**
6. **Critérios de Entrada e Saída**
7. **Riscos e Mitigação**
8. **Entregáveis**

**1.4 Boas Práticas no Planejamento**

* Participação multidisciplinar.
* Reuniões de alinhamento com stakeholders.
* Revisões incrementais do planejamento.
* Documentação versionada.

**2. Plano de Testes**

**2.1 Definição**

* Documento formal que detalha todas as ações planejadas para garantir a qualidade do software.

**2.2 Padrão IEEE 829**

* Referência histórica para estruturação de um plano de testes.

**2.3 Componentes de um Plano de Testes**

| **Componente** | **Descrição** |
| --- | --- |
| **Identificação** | Nome do projeto, responsáveis, versão do plano. |
| **Itens de Teste** | Componentes, módulos ou funcionalidades que serão testadas. |
| **Características a serem testadas** | Requisitos funcionais e não funcionais cobertos. |
| **Características que não serão testadas** | Delimitação do escopo negativo. |
| **Abordagem de Teste** | Estratégia adotada: técnicas, níveis de teste, ferramentas. |
| **Critérios de Entrada** | Condições mínimas para iniciar o teste. |
| **Critérios de Saída** | Condições para considerar o teste concluído com sucesso. |
| **Ambiente de Teste** | Hardware, software, redes, dados. |
| **Cronograma** | Prazos e marcos. |
| **Recursos** | Pessoas, ferramentas, ambientes. |
| **Riscos Identificados** | Problemas potenciais e planos de mitigação. |
| **Entregáveis** | Relatórios, métricas, evidências de execução. |

**2.4 Exemplo Prático**

* Construção de um plano de testes para um sistema de reservas online.

**2.5 Ferramentas de Apoio**

* Word, Excel, Google Docs
* TestLink, Zephyr, Xray

**3. Matriz de Rastreabilidade**

**3.1 Definição**

* Documento que **mapeia requisitos aos casos de teste, resultados e defeitos**.

**3.2 Importância**

* Assegura que todos os requisitos foram testados.
* Facilita auditoria de qualidade.
* Permite rápida identificação do impacto de mudanças.

**3.3 Construção**

| **Requisito** | **Caso de Teste** | **Resultado** | **Defeito** |
| --- | --- | --- | --- |
| REQ-001 | CT-01 | OK | - |
| REQ-002 | CT-02 | NOK | DEF-003 |

**3.4 Manutenção da Matriz**

* Versionamento controlado.
* Atualização contínua após sprints ou releases.

**3.5 Exemplos de Rastreabilidade em Metodologias Ágeis**

* Uso de Jira + Xray.

**4. Gestão de Defeitos**

**4.1 O que é um Defeito**

* Revisão conceitual: erro, defeito, falha, incidente.

**4.2 Ciclo de Vida de um Defeito**

1. Novo
2. Atribuído
3. Em progresso
4. Resolvido
5. Verificado
6. Fechado
7. Reaberto
8. Adiado/Rejeitado

**4.3 Registro de Defeitos**

* Informações obrigatórias:
  + ID
  + Descrição
  + Ambiente
  + Passos de reprodução
  + Severidade
  + Prioridade
  + Evidências

**4.4 Classificação**

* **Severidade:** técnica.
* **Prioridade:** negócio.

**4.5 Ferramentas**

* Jira
* Bugzilla
* MantisBT
* Redmine

**4.6 Métricas de Defeitos**

* Quantidade por severidade
* Taxa de reabertura
* MTTR (Mean Time To Repair)
* DRE (Defect Removal Efficiency)

**4.7 Gestão de Defeitos em Ágil**

* Defeitos como itens do backlog.
* Defeitos priorizados por impacto no sprint.

**5. Integração com Metodologias de Desenvolvimento**

| **Modelo** | **Característica** |
| --- | --- |
| Cascata | Gestão formal e sequencial de defeitos. |
| Ágil | Defeitos integrados ao fluxo de trabalho. |
| DevOps | Automação na identificação e registro de falhas via CI/CD. |

**6. Simulação e Exercício Completo**

1. Planejamento de testes para um sistema de delivery.
2. Elaboração de plano de testes documentado.
3. Criação de matriz de rastreabilidade.
4. Simulação de registro e gestão de 3 defeitos.

### Metodologia

**Aula 19**

* Exposição teórica completa.
* Demonstração de documentos reais de plano de testes e matriz.

**Aula 20**

* Oficina prática de elaboração de plano, matriz e gestão de defeitos.
* Discussão crítica sobre práticas observadas no mercado.
* Correção colaborativa dos planos elaborados.

**Leitura Complementar**

* IEEE 829 Standard for Software Test Documentation.
* ISTQB Foundation Level syllabus.
* Atlassian Jira documentation.

## Aulas 21-22: Métricas de Teste, Relatórios de Qualidade e Monitoramento Contínuo

Esta aula inaugura o bloco sobre **medição da qualidade de software via métricas de teste, produção de relatórios gerenciais e o papel do monitoramento contínuo em processos modernos de desenvolvimento e qualidade de software**, alinhando práticas de QA com modelos de DevOps e Engenharia de Software Moderna.

### Objetivo Geral

Capacitar o aluno a **definir, coletar, interpretar e utilizar métricas de teste para avaliação da qualidade do software**, integrando a produção de relatórios claros e objetivos que subsidiem a tomada de decisões técnicas e gerenciais, além de introduzir práticas de **monitoramento contínuo** como parte da garantia de qualidade.

### Objetivos Específicos

1. **Compreender o papel estratégico das métricas de teste na gestão da qualidade do software.**
2. **Identificar e aplicar as principais métricas utilizadas em testes de software.**
3. **Diferenciar métricas de produto, de processo e de projeto em contextos de qualidade.**
4. **Elaborar relatórios de qualidade com base em métricas coletadas, com foco em comunicação clara para stakeholders.**
5. **Compreender o papel do monitoramento contínuo na qualidade do produto pós-entrega.**
6. **Estabelecer a conexão entre métricas de teste e a melhoria contínua do processo de desenvolvimento.**
7. **Praticar a coleta de métricas com ferramentas de apoio.**
8. **Refletir criticamente sobre o uso de métricas para evitar métricas vaidosas (vanity metrics).**
9. **Simular a apresentação de um relatório de qualidade baseado em um projeto simulado.**
10. **Discutir como as métricas contribuem para decisões em pipelines de CI/CD e qualidade gates.**

### Conteúdo Programático Detalhado

**1. Importância das Métricas em Teste de Software**

* Por que medir?
  + Melhorar a previsibilidade do processo.
  + Diagnosticar problemas em desenvolvimento.
  + Apoiar decisões de liberação ou bloqueio de software.
* O que não se mede, não se gerencia — Deming.
* Riscos de desenvolver sem métricas:
  + Sobrecarga de bugs.
  + Falta de visibilidade do progresso.

**2. Classificação de Métricas**

| **Tipo** | **Descrição** |
| --- | --- |
| **De Produto** | Qualidade do próprio software. |
| **De Processo** | Eficiência do processo de desenvolvimento/teste. |
| **De Projeto** | Relacionadas ao progresso do projeto. |

**3. Métricas de Produto**

* **Cobertura de Código**
* **Densidade de Defeitos**
* **Severidade Média dos Defeitos**
* **Defect Removal Efficiency (DRE)**

**4. Métricas de Processo**

* **Velocidade de Detecção de Defeitos**
* **Taxa de Reabertura de Defeitos**
* **Tempo Médio para Correção (MTTR)**
* **Throughput de Testes Automatizados**

**5. Métricas de Projeto**

* **Burn down chart** (áreas ágeis)
* **Progresso das execuções de testes**
* **Número de bloqueios no pipeline de CI**

**6. Relatórios de Qualidade**

**6.1 Estrutura**

* Visão geral
* Status dos testes
* Defeitos encontrados e resolvidos
* Cobertura de código
* Indicadores de risco
* Recomendação sobre a liberação

**6.2 Públicos dos Relatórios**

* Gerentes de projeto
* Stakeholders
* Equipe técnica

**6.3 Boas Práticas**

* Visualização clara (gráficos, dashboards).
* Linguagem adequada ao público.
* Foco em dados acionáveis.

**7. Monitoramento Contínuo e Observabilidade**

* Conceitos:
  + Logs
  + Métricas
  + Traces
* Ferramentas:
  + Prometheus
  + Grafana
  + Elastic Stack
* Integração com qualidade:
  + Identificar degradações pós-deploy.
  + Validar performance em produção.

**8. Qualidade em Pipelines CI/CD**

* Quality Gates:
  + SonarQube para análise estática e cobertura.
  + Thresholds mínimos para permitir integração.
* Feedback rápido ao desenvolvedor.

**9. Exercício Prático**

1. Coletar métricas de testes unitários com ferramenta de cobertura.
2. Criar um relatório de qualidade fictício.
3. Criar um painel de monitoramento simples com Grafana (opcional/simulado).

### Metodologia

**1. Aula Expositiva**

* Teoria e importância das métricas.

**2. Demonstração**

* Relatórios reais de ferramentas como SonarQube e Jira.

**3. Prática Guiada**

* Coleta e cálculo de métricas.

**4. Discussão**

* Crítica sobre boas e más métricas.

**5. Leitura Complementar**

* "Software Metrics: A Rigorous and Practical Approach"

## Aulas 23-24: Teste Baseado em Modelos (Model-Based Testing) e Teste de Mutação

Esta aula é dedicada ao estudo de duas técnicas avançadas de teste de software: o **Teste Baseado em Modelos (MBT)** e o **Teste de Mutação**, fundamentais para ampliar o repertório dos alunos sobre formas sistemáticas e automatizadas de gerar casos de teste e verificar a qualidade dos próprios testes.

### Objetivo Geral

Capacitar o aluno a **compreender, aplicar e avaliar o Teste Baseado em Modelos (MBT)** e o **Teste de Mutação**, desenvolvendo habilidades para modelar comportamentos de sistemas e para validar a eficácia das suítes de teste por meio da introdução controlada de defeitos artificiais.

### Objetivos Específicos

1. **Definir o que é o Teste Baseado em Modelos (MBT)** e identificar os tipos de modelos utilizados.
2. **Entender o processo de geração automática de casos de teste a partir de modelos formais.**
3. **Aplicar o MBT em exemplos práticos e identificar seus benefícios e limitações.**
4. **Compreender o conceito de Teste de Mutação e sua finalidade na avaliação da qualidade dos testes.**
5. **Definir e aplicar o conceito de mutantes, operadores de mutação e taxa de mutantes mortos.**
6. **Explorar ferramentas de Teste de Mutação para linguagens como Java e Python.**
7. **Analisar criticamente os desafios e limitações do Teste de Mutação.**
8. **Comparar MBT e Teste de Mutação quanto ao propósito e aplicabilidade.**
9. **Praticar a aplicação combinada de MBT e Teste de Mutação para validar suítes de testes.**
10. **Refletir sobre o papel dessas técnicas em ambientes DevOps e qualidade contínua.**

### Conteúdo Programático Detalhado

**1. Teste Baseado em Modelos (MBT)**

**1.1 Definição**

* Técnica em que **um modelo formal do comportamento do sistema** é criado e utilizado para gerar automaticamente casos de teste.
* O modelo pode representar:
  + Fluxo de estados
  + Transições
  + Sequências de eventos

**1.2 Tipos de Modelos Utilizados**

* **Máquinas de Estado Finitas (FSM)**
* **Diagramas de Atividade UML**
* **Modelos de Fluxo de Dados**
* **Modelos de Processos de Negócio (BPMN)**

**1.3 Processo de MBT**

1. Criar o modelo do comportamento esperado.
2. Identificar todos os estados, transições, entradas e saídas.
3. Definir critérios de cobertura do modelo.
4. Gerar automaticamente os casos de teste.
5. Executar e validar.

**1.4 Exemplo Prático**

* Modelagem de um caixa eletrônico:
  + Estados: Início, Autenticado, Seleção de Operação, Saque, Depósito, Fim.
  + Transições baseadas nas interações do usuário.

**1.5 Benefícios**

* Automação na geração de testes.
* Cobertura sistemática do comportamento.
* Redução de erros humanos na criação de casos.

**1.6 Limitações**

* Custo de criação e manutenção dos modelos.
* Complexidade em sistemas muito dinâmicos.

**2. Teste de Mutação**

**2.1 Definição**

* Técnica para avaliar a qualidade da suíte de testes através da **introdução deliberada de defeitos artificiais (mutantes)** no código.

**2.2 Conceitos**

* **Mutantes:** versões ligeiramente modificadas do programa original.
* **Operadores de Mutação:** regras que definem as alterações:
  + Troca de operadores aritméticos (+ para -)
  + Alteração de condições (> para >=)
  + Substituição de variáveis

**2.3 Processo**

1. Gerar mutantes a partir do código fonte.
2. Executar a suíte de testes existente sobre os mutantes.
3. Avaliar:

* **Mutante morto:** o teste falhou, ou seja, detectou o defeito.
* **Mutante vivo:** o teste não detectou a alteração.

**2.4 Métrica**

* **Taxa de Mutantes Mortos:** *TMM = (Mutantes Mortos / Total de Mutantes) \* 100*
* Ideal: TMM próximo de 100%.

**2.5 Exemplo Prático**

* Código original:

def soma(a, b):

return a + b

* Mutante:

def soma(a, b):

return a - b

* Um bom teste detectará o erro.

**2.6 Ferramentas**

* **Java:** PIT Mutation Testing
* **Python:** MutPy
* **.NET:** Stryker

**2.7 Benefícios**

* Valida a qualidade da suíte de testes.
* Estimula a escrita de testes mais robustos.

**2.8 Limitações**

* Custo computacional elevado.
* Nem todos os mutantes são "vivos" por problemas na semântica.

**3. Comparativo entre MBT e Teste de Mutação**

| **Aspecto** | **MBT** | **Teste de Mutação** |
| --- | --- | --- |
| Objetivo | Gerar casos de teste | Avaliar a qualidade da suíte |
| Foco | Modelos comportamentais | Código fonte |
| Ferramentas | GraphWalker, Spec Explorer | PIT, MutPy |
| Desafio | Modelagem correta | Custo computacional |

**4. Aplicação Combinada**

* Usar MBT para gerar a suíte de testes.
* Aplicar Teste de Mutação para verificar a eficácia da suíte.

**5. Papel no DevOps**

* Automatização das duas técnicas em pipelines.
* Controle de qualidade contínuo.

**6. Exercício Prático**

1. Modelar um sistema simples (ex: controle de acesso) em máquina de estados.
2. Gerar casos de teste com MBT.
3. Aplicar MutPy em um código fornecido para medir TMM.

### Metodologia

**1. Aula Expositiva**

* Explicação teórica ilustrada com fluxogramas e diagramas.

**2. Demonstração**

* Uso real de ferramenta MBT e MutPy.

**3. Prática em Grupo**

* Grupos modelam um sistema e aplicam MBT.

**4. Discussão**

* Limitações percebidas e desafios práticos.

**5. Leitura Complementar**

* Papers acadêmicos sobre MBT e Mutação.

## Aulas 25-26: Testes de Performance, Carga e Segurança

Esta aula aprofunda o conhecimento dos alunos em **testes não funcionais**, especificamente em testes de performance, carga e segurança, que são cruciais para validar atributos de qualidade relacionados à robustez, estabilidade, escalabilidade e proteção do sistema frente a ataques e degradações sob condições adversas.

### Objetivo Geral

Proporcionar aos alunos o domínio teórico e prático dos **Testes de Performance, Carga e Segurança**, capacitando-os a planejar, executar, interpretar os resultados e propor melhorias para softwares que necessitam de eficiência sob pressão e resistência a falhas e ameaças de segurança.

### Objetivos Específicos

1. **Definir o que são testes de performance, carga e segurança e sua importância para sistemas críticos e comerciais.**
2. **Compreender os diferentes tipos de testes de performance: stress, carga, estabilidade, volume e escalabilidade.**
3. **Explorar ferramentas modernas para testes de performance e carga como JMeter, k6 e Gatling.**
4. **Aplicar práticas para definir workloads representativos e configurar cenários de teste realistas.**
5. **Compreender as principais vulnerabilidades de segurança em aplicações web segundo o OWASP Top 10.**
6. **Planejar e realizar testes de segurança básicos, simulando ataques comuns como SQL Injection e XSS.**
7. **Interpretar relatórios gerados pelos testes de performance e segurança.**
8. **Analisar os impactos das vulnerabilidades e gargalos de performance na experiência do usuário e no negócio.**
9. **Relacionar as práticas de testes não funcionais com processos de DevOps, SRE e pipelines de CI/CD.**
10. **Desenvolver senso crítico para sugerir melhorias técnicas baseadas nos resultados dos testes.**

### Conteúdo Programático Detalhado

**1. Testes de Performance**

**1.1 Definição**

* Validar o comportamento do sistema sob condições específicas de carga e volume de dados.
* Medir tempos de resposta, throughput, consumo de recursos.

**1.2 Tipos de Testes de Performance**

| **Tipo** | **Objetivo** |
| --- | --- |
| Carga | Determinar o comportamento com número crescente de usuários. |
| Stress | Avaliar limites de tolerância antes da falha. |
| Volume | Testar com grandes volumes de dados. |
| Estabilidade | Avaliar comportamento em longos períodos de operação contínua. |
| Escalabilidade | Verificar a capacidade de escalar horizontal ou verticalmente. |

**1.3 Ferramentas**

* **JMeter:** amplamente utilizado, suporta protocolos diversos.
* **k6:** focado em APIs e integração com DevOps.
* **Gatling:** focado em performance de aplicações web.

**1.4 Exemplo Prático**

* Simular 1000 usuários simultâneos acessando um sistema de reservas.
* Avaliar:
  + Tempo médio de resposta
  + Erros sob carga
  + Picos de consumo de CPU e memória

**2. Testes de Carga e Stress**

* Definição do workload representativo.
* Configuração de ramp-up e ramp-down.
* Identificação de gargalos:
  + Banco de dados
  + Servidor de aplicação
  + Redes

**2.1 KPIs Comuns**

* Latência
* Throughput
* Erros por segundo
* Percentil de resposta (ex: p95)

**3. Testes de Segurança**

**3.1 OWASP Top 10**

1. Injeção (SQL, NoSQL, OS)
2. Quebra de Autenticação
3. Exposição de Dados Sensíveis
4. XML External Entities
5. Controle de Acesso Quebrado
6. Configuração Incorreta de Segurança
7. Cross-Site Scripting (XSS)
8. Deserialização Insegura
9. Uso de Componentes com Vulnerabilidades Conhecidas
10. Log e Monitoramento Insuficientes

**3.2 Ferramentas de Segurança**

* **OWASP ZAP:** scanner de vulnerabilidades.
* **Burp Suite:** proxy para testes manuais e automáticos.
* **Nikto:** scanner de vulnerabilidades de servidores web.

**3.3 Exemplos de Ataques**

* **SQL Injection:** manipulação de query via input.
* **XSS:** injeção de scripts em páginas web.
* **Fuzzing:** envio massivo de entradas aleatórias para identificar falhas.

**4. Relatórios e Análises**

* Interpretação de gráficos de latência, throughput.
* Relatórios de vulnerabilidades categorizados por severidade.
* Sugestões de correção baseadas em evidências.

**5. Integração com DevOps e SRE**

* Automação dos testes não funcionais no CI/CD.
* Monitoramento contínuo pós-deploy.
* Práticas de SRE:
  + SLOs: Service Level Objectives
  + SLIs: Service Level Indicators

**6. Exercício Prático**

1. Configurar um teste de carga simples com JMeter ou k6.
2. Usar OWASP ZAP para escanear vulnerabilidades de uma aplicação de teste.
3. Criar um relatório executivo com os achados.

### Metodologia

**1. Aula Expositiva**

* Conceitos com diagramas e vídeos demonstrativos.

**2. Demonstração Prática**

* Uso de JMeter e OWASP ZAP em laboratório.

**3. Prática em Grupo**

* Configuração de cenário de teste de carga.
* Aplicação de scanner de segurança.

**4. Discussão**

* Debater impactos de não realizar testes não funcionais.

**5. Leitura Complementar**

* OWASP Top 10 completo.
* Documentação oficial do JMeter e k6.

## Aulas 27-28: Testes em Microserviços e Observabilidade Aplicada a Testes

Nesta aula os alunos irão explorar os **desafios de testar arquiteturas baseadas em microserviços** e as técnicas de observabilidade aplicadas à qualidade de software, essenciais em sistemas distribuídos modernos, particularmente em ambientes cloud-native e de alta escala.

### Objetivo Geral

Capacitar o aluno a **compreender os desafios e estratégias específicas para testar sistemas baseados em microserviços** e a **integrar práticas de observabilidade ao processo de testes**, garantindo qualidade em ambientes complexos e distribuídos.

### Objetivos Específicos

1. **Definir o que são microserviços e seus impactos na estratégia de testes.**
2. **Identificar os desafios de qualidade em arquiteturas distribuídas.**
3. **Diferenciar os níveis de testes aplicáveis a microserviços:** unitário, integração, contrato, ponta a ponta.
4. **Compreender o conceito de contract testing e como ele previne falhas em integrações entre serviços.**
5. **Explorar ferramentas para testes de microserviços como Pact, Postman e TestContainers.**
6. **Compreender o conceito de observabilidade e sua aplicação para o monitoramento da qualidade em produção.**
7. **Conhecer os pilares da observabilidade:** logs, métricas e traces.
8. **Utilizar ferramentas de observabilidade como Prometheus, Grafana e Jaeger no contexto de qualidade de software.**
9. **Relacionar práticas de testes e observabilidade no contexto DevOps e SRE (Site Reliability Engineering).**
10. **Praticar a elaboração de planos de teste e de monitoramento para aplicações de microserviços.**

### Conteúdo Programático Detalhado

**1. Arquitetura de Microserviços**

* Definição:
  + Arquitetura composta por pequenos serviços independentes, cada um responsável por uma funcionalidade específica.
* Características:
  + Independência de deploy
  + Comunicação via APIs
  + Escalabilidade isolada
* Exemplos de sistemas: Netflix, Spotify.

**2. Desafios de Testes em Microserviços**

| **Desafio** | **Descrição** |
| --- | --- |
| Testes Distribuídos | Componentes em ambientes diferentes, comunicação via rede. |
| Gestão de Estado | Cada serviço pode manter seu próprio estado. |
| Latência e Falhas de Rede | Imprevisibilidade da comunicação. |
| Versionamento de APIs | Quebra de compatibilidade entre serviços. |

**3. Estratégias de Testes para Microserviços**

**3.1 Testes Unitários**

* Garantir que cada microserviço funciona isoladamente.

**3.2 Testes de Integração**

* Verificar a comunicação entre microserviços conectados diretamente.

**3.3 Contract Testing**

* Garantir que a interface de comunicação (API) entre dois serviços segue um contrato definido.
* Ferramentas:
  + **Pact**
  + **Spring Cloud Contract**

**3.4 Testes End-to-End**

* Validar o fluxo completo do sistema com todos os serviços integrados.
* Mais custoso e sujeito a flutuações de ambiente.

**3.5 TestContainers**

* Criar ambientes controlados com containers para testes de integração realistas.

**4. Observabilidade Aplicada a Testes**

**4.1 Definição**

* Capacidade de entender o que está acontecendo internamente no sistema a partir de outputs externos.

**4.2 Pilares da Observabilidade**

| **Pilar** | **Descrição** | **Ferramenta Exemplo** |
| --- | --- | --- |
| Logs | Registro de eventos | Elastic Stack |
| Métricas | Medidas quantitativas (ex: tempo de resposta) | Prometheus |
| Traces | Rastreio de requisições entre serviços | Jaeger |

**4.3 Benefícios**

* Identificação de gargalos.
* Detecção de falhas de integração.
* Análise de impacto de deploys.

**5. Ferramentas**

* **Prometheus:** coleta e armazenamento de métricas.
* **Grafana:** visualização de métricas.
* **Jaeger:** tracing distribuído.
* **Elastic Stack:** gestão de logs.
* **Pact:** contract testing.

**6. Qualidade em DevOps e SRE**

* Práticas de SRE:
  + SLO (Service Level Objective)
  + SLI (Service Level Indicator)
* Feedback contínuo entre desenvolvimento, testes e operação.

**7. Exercício Prático**

1. Definir um plano de testes para um sistema com 3 microserviços integrados.
2. Configurar uma aplicação de exemplo com Prometheus + Grafana.
3. Simular contract testing com Pact.

### Metodologia

**1. Aula Expositiva**

* Teoria com diagramas arquiteturais.

**2. Demonstração**

* Contract testing em tempo real.
* Setup básico de observabilidade.

**3. Prática Guiada**

* Desenho de arquitetura de testes para microserviços.

**4. Discussão**

* Como balancear entre muitos testes end-to-end vs unitários + contract testing.

**5. Leitura Complementar**

* Site Reliability Engineering Book (Google).
* Documentação oficial do Pact.

## Aulas 29-30: Ferramentas de Teste: Unitário, Integração, Funcional e Gestão de Testes

Esta aula é dedicada a proporcionar aos alunos um panorama completo e prático das **principais ferramentas utilizadas em diferentes níveis de teste** e na **gestão de casos e ciclos de testes**, capacitando-os a escolher, configurar e utilizar essas ferramentas de forma eficaz em projetos reais.

### Objetivo Geral

Capacitar os alunos a **conhecer, configurar e utilizar ferramentas de testes de software** para diferentes níveis de teste (unitário, integração, funcional e regressão) e para a gestão e documentação dos testes, alinhando práticas com o que é utilizado no mercado e promovendo a adoção de técnicas modernas de qualidade de software.

### Objetivos Específicos

1. **Identificar e diferenciar ferramentas específicas para testes unitários, integração, funcionais e de regressão.**
2. **Conhecer as características, vantagens e limitações de cada ferramenta em seus respectivos contextos de uso.**
3. **Aprender a configurar ferramentas básicas de teste em linguagens como Java, Python e JavaScript.**
4. **Executar exemplos práticos utilizando ferramentas como JUnit, PyTest, Postman, REST Assured, Selenium e Cypress.**
5. **Explorar ferramentas de gestão de testes como TestLink, Zephyr e Xray.**
6. **Compreender a importância da documentação e rastreabilidade de testes dentro das ferramentas de gestão.**
7. **Aprender a integrar ferramentas de teste com pipelines de integração contínua (CI/CD).**
8. **Aplicar práticas de versionamento e manutenção de testes automatizados em repositórios de código.**
9. **Desenvolver senso crítico para escolha de ferramentas conforme o tipo de projeto, equipe e objetivos de qualidade.**
10. **Simular a criação de um ambiente completo de testes utilizando múltiplas ferramentas integradas.**

### Conteúdo Programático Detalhado

**1. Ferramentas de Teste Unitário**

**1.1 JUnit**

* Plataforma de testes unitários para Java.
* Anotações principais:
  + @Test
  + @BeforeAll, @BeforeEach
  + @AfterAll, @AfterEach
* Integração com Maven, Gradle e IDEs como IntelliJ.

**1.2 PyTest**

* Framework de testes unitários para Python.
* Recursos:
  + Parametrização
  + Fixtures
  + Plugins para relatórios

**1.3 Jest**

* Framework de testes para aplicações em JavaScript e TypeScript.
* Features:
  + Testes rápidos
  + Snapshots para garantir integridade de UI
  + Mocking integrado

**2. Ferramentas de Teste de Integração**

**2.1 Postman**

* Testes manuais e automatizados de APIs REST.
* Collections e environments.
* Scripts de automação com JavaScript.

**2.2 REST Assured**

* Testes automatizados de APIs REST para Java.
* Sintaxe fluente e simples.

**2.3 TestContainers**

* Bibliotecas para criar ambientes de teste com containers Docker.
* Testes com dependências reais como bancos de dados e filas.

**3. Ferramentas de Teste Funcional e de Regressão**

**3.1 Selenium**

* Automação de testes em browsers.
* Suporte multi-linguagem: Java, Python, C#.
* WebDriver para controle de browsers reais.

**3.2 Cypress**

* Framework moderno para testes end-to-end em aplicações web.
* Alta integração com o front-end.
* Testes rápidos e consistentes.

**4. Ferramentas de Gestão de Testes**

**4.1 TestLink**

* Ferramenta open source para documentação e gestão de casos de teste.
* Gestão de requisitos e rastreabilidade.

**4.2 Zephyr**

* Plugin do Jira para gestão de testes.
* Integração com gestão ágil.

**4.3 Xray**

* Solução robusta para gestão de testes dentro do Jira.
* Suporte a testes manuais e automatizados.

**5. Integração com CI/CD**

* Execução de testes automatizados em pipelines:
  + Jenkins
  + GitLab CI
  + GitHub Actions
* Publicação de relatórios automáticos.
* Triggers automáticos para execução de regressão.

**6. Versionamento de Testes**

* Práticas com Git para:
  + Versionar código de testes.
  + Versionar configurações e scripts de automação.

**7. Critérios para Escolha de Ferramentas**

| **Critério** | **Exemplo** |
| --- | --- |
| Linguagem do Projeto | Java: JUnit, REST Assured |
| Tipo de Aplicação | Web: Cypress, Selenium |
| Complexidade | Projetos grandes: integração com CI/CD necessária |
| Equipe | Conhecimento prévio influencia escolha |

**8. Demonstração Prática**

* Exemplo de:
  + Teste unitário com JUnit
  + Teste de API com Postman
  + Teste funcional com Cypress
  + Gestão de casos no TestLink

**9. Exercício Prático**

1. Criar um teste unitário para uma função simples.
2. Testar uma API pública usando Postman.
3. Criar um caso de teste funcional com Cypress.
4. Documentar um caso de teste no TestLink.

### Metodologia

**1. Aula Expositiva**

* Apresentação das ferramentas com slides ilustrativos.

**2. Demonstração**

* Execução prática ao vivo de cada ferramenta.

**3. Prática em Laboratório**

* Alunos instalam, configuram e executam exemplos básicos.

**4. Discussão**

* Quais ferramentas melhor atendem diferentes tipos de projetos.

**5. Leitura Complementar**

* Documentação oficial de cada ferramenta.
* Artigos comparativos entre frameworks.

## Aulas 31-33: Projeto Integrador Final — Orientação e Desenvolvimento

Estas aulas são dedicadas exclusivamente à **concepção, desenvolvimento e acompanhamento do Projeto Integrador Final** da disciplina, proporcionando aos alunos a oportunidade de **aplicar de forma prática e integrada todos os conhecimentos, técnicas e ferramentas estudados durante o curso**.

### Objetivo Geral

Orientar os alunos na **elaboração de um projeto prático completo de testes de software**, integrando planejamento, desenvolvimento de casos de teste, execução de diferentes técnicas de teste, automação, geração de dados de teste, análise de métricas e elaboração de relatórios, simulando o ciclo real de qualidade em projetos de software.

### Objetivos Específicos

1. **Consolidar os conhecimentos adquiridos em sala aplicados a um projeto prático real ou simulado.**
2. **Elaborar o planejamento completo de testes, incluindo escopo, abordagem, recursos, cronograma e critérios de entrada e saída.**
3. **Desenvolver e documentar casos de teste funcionais (caixa-preta) e estruturais (caixa-branca).**
4. **Aplicar técnicas de testes funcionais como particionamento de equivalência, análise de valor limite, tabelas de decisão e máquinas de estado.**
5. **Utilizar técnicas de testes estruturais incluindo fluxo de controle, fluxo de dados e complexidade ciclomática.**
6. **Elaborar e executar casos de teste unitários, de integração, regressão e segurança.**
7. **Gerar dados de teste apropriados para diferentes níveis de teste.**
8. **Aplicar ferramentas de automação de testes de forma prática.**
9. **Realizar o registro e gestão dos defeitos encontrados.**
10. **Elaborar a matriz de rastreabilidade ligando requisitos aos testes e defeitos.**
11. **Analisar métricas de testes coletadas e produzir relatórios técnicos e executivos.**
12. **Preparar a apresentação formal do projeto integrador.**

### Conteúdo Programático Detalhado

1. **Definição do Projeto Integrador**
   * Sistema ou aplicação alvo do projeto
   * Definição dos objetivos e escopo do teste
   * Identificação dos requisitos funcionais e não funcionais
2. **Planejamento dos Testes**
   * Plano de testes completo com escopo, abordagem, cronograma
   * Definição de papéis dentro do grupo
   * Identificação de riscos
3. **Desenvolvimento dos Casos de Teste**
   * Técnicas de caixa-preta:
     + Particionamento de equivalência
     + Análise do valor limite
     + Tabelas de decisão
     + Máquinas de estados
     + Casos de uso
   * Técnicas de caixa-branca:
     + Cobertura de instrução e decisão
     + Complexidade ciclomática
     + Fluxo de dados
4. **Execução dos Testes**
   * Testes unitários (JUnit, PyTest, Jest)
   * Testes de integração (Postman, REST Assured)
   * Testes funcionais (Selenium, Cypress)
   * Testes de segurança (OWASP ZAP)
   * Testes de performance (JMeter, k6)
5. **Geração e Uso de Dados de Teste**
   * Uso de Faker, Mockaroo, DBMonster
   * Gerar dados válidos, inválidos e de limites
6. **Automação de Testes**
   * Criação de scripts automáticos
   * Versionamento de testes no Git
7. **Registro e Gestão de Defeitos**
   * Uso de ferramentas como Jira ou planilha para registrar, priorizar e acompanhar defeitos
8. **Matriz de Rastreabilidade**
   * Requisitos mapeados aos testes
   * Testes relacionados aos defeitos detectados
9. **Análise de Métricas e Relatórios**
   * Cobertura de testes
   * Taxa de defeitos
   * DRE
   * Relatórios gerenciais e técnicos
10. **Preparação da Apresentação**
    * Estruturação do conteúdo a ser apresentado
    * Definição dos papéis de cada integrante durante a apresentação
    * Criação de slides, relatórios e evidências práticas

### Metodologia

**Aula 31**

* Revisão do escopo do Projeto Integrador
* Alinhamento de expectativas e cronograma interno do grupo
* Apoio do professor na definição do plano de testes
* Orientação sobre documentação necessária

**Aula 32**

* Acompanhamento do desenvolvimento dos casos de teste
* Suporte na execução prática com ferramentas
* Orientações sobre geração de dados e automação

**Aula 33**

* Revisão da matriz de rastreabilidade
* Consolidação dos relatórios de métricas
* Preparação da apresentação formal
* Dúvidas finais e sugestões de melhoria

## Aulas 34-35: Apresentação do Projeto Integrador Final

Estas aulas são reservadas para a **apresentação formal dos Projetos Integradores desenvolvidos pelos alunos**, com o objetivo de avaliar a aplicação prática dos conceitos de Teste de Software estudados durante o semestre, bem como as habilidades de planejamento, execução, documentação e comunicação técnica.

### Objetivo Geral

Permitir que os alunos **demonstrem a aplicação prática dos conhecimentos adquiridos sobre Teste de Software**, por meio da apresentação detalhada do Projeto Integrador Final, validando competências técnicas, metodológicas e comunicativas necessárias para o exercício profissional na área de qualidade de software.

### Objetivos Específicos

1. **Apresentar o escopo, objetivos e requisitos do sistema ou aplicação escolhida para o Projeto Integrador.**
2. **Descrever o planejamento de testes elaborado, incluindo escopo, cronograma, recursos e riscos.**
3. **Demonstrar a aplicação das técnicas de teste funcional (caixa-preta) e estrutural (caixa-branca).**
4. **Apresentar a documentação dos casos de teste e matriz de rastreabilidade.**
5. **Exibir a automação dos testes desenvolvidos e/ou ferramentas utilizadas no processo.**
6. **Demonstrar a geração e aplicação de dados de teste.**
7. **Apresentar os principais defeitos encontrados, sua classificação e gestão.**
8. **Exibir as métricas coletadas, como cobertura de código e DRE.**
9. **Compartilhar o relatório técnico e o relatório executivo do projeto.**
10. **Avaliar as habilidades de apresentação oral, trabalho em equipe, capacidade de síntese e argumentação técnica.**

### Roteiro para Apresentação

**1. Contextualização**

* Apresentação do sistema ou aplicação.
* Justificativa da escolha.
* Objetivos do projeto.

**2. Planejamento de Testes**

* Escopo dos testes.
* Plano de testes completo.
* Cronograma.
* Riscos identificados e mitigação.

**3. Casos de Teste e Técnicas Aplicadas**

* Apresentação dos casos de teste funcionais.
* Demonstração dos casos estruturais.
* Justificativa das técnicas aplicadas.

**4. Matriz de Rastreabilidade**

* Mapeamento dos requisitos aos casos de teste.
* Relação entre casos de teste e defeitos.

**5. Ferramentas Utilizadas**

* Ferramentas de automação.
* Ferramentas de gestão de defeitos.
* Geração de dados de teste.

**6. Execução dos Testes**

* Execução prática ou vídeo demonstrativo.
* Evidências dos testes executados.

**7. Métricas e Relatórios**

* Cobertura de testes.
* Defect Removal Efficiency.
* Relatório técnico.
* Relatório executivo para stakeholders.

**8. Dificuldades e Lições Aprendidas**

* Desafios enfrentados.
* Soluções adotadas.
* Melhorias propostas para o processo de teste.

### Critérios de Avaliação

| **Critério** | **Peso** |
| --- | --- |
| Aplicação correta das técnicas de teste | 20% |
| Documentação: plano de testes, casos de teste, matriz | 20% |
| Uso de ferramentas e automação | 20% |
| Análise de métricas e qualidade dos relatórios | 15% |
| Comunicação, clareza e organização da apresentação | 15% |
| Inovação, criatividade e profundidade técnica | 10% |

### Metodologia de Condução das Aulas

* Cada grupo terá um tempo de **20 a 30 minutos para apresentação**.
* Espaço reservado para perguntas e arguição do professor e colegas.
* Avaliação individual de cada integrante quanto à participação e domínio do conteúdo.
* Feedback imediato ao final de cada apresentação.

### Produtos Esperados

1. **Apresentação oral com apoio de slides.**
2. **Documentação completa entregue digitalmente:**
   * Plano de testes
   * Casos de teste
   * Matriz de rastreabilidade
   * Relatórios técnico e executivo
3. **Evidências de execução dos testes (prints, vídeos, logs).**
4. **Repositório de automação de testes, se aplicável.**

## Aula 36: Prova Teórica II

### Objetivo Geral

Avaliar formalmente a **capacidade dos alunos de integrar, aplicar e correlacionar os conceitos, técnicas, ferramentas e práticas avançadas de Teste de Software**, compreendendo o ciclo completo de qualidade desde o planejamento até a execução e análise de resultados.

### Objetivos Específicos

1. **Verificar o domínio conceitual do aluno sobre técnicas avançadas de teste.**
2. **Avaliar a capacidade do aluno de planejar um processo de testes em sistemas complexos.**
3. **Medir o entendimento sobre testes não funcionais como performance, segurança e testes de microserviços.**
4. **Verificar o conhecimento sobre gestão de qualidade e métricas associadas ao processo de testes.**
5. **Avaliar a habilidade de escolha e aplicação de ferramentas de automação, gestão e observabilidade.**
6. **Conferir a capacidade crítica do aluno em sugerir melhorias em processos de qualidade.**
7. **Avaliar a compreensão sobre geração de dados de teste e práticas de privacidade de dados.**
8. **Estimular a capacidade de síntese, argumentação técnica e comunicação clara de ideias.**

### Conteúdo Programático Avaliado

* Gestão do Processo de Testes
* Gestão de Defeitos
* Métricas de Teste, Relatórios de Qualidade e Monitoramento
* Teste Baseado em Modelos e Mutação
* Testes de Performance, Carga e Segurança
* Testes em Microserviços e Observabilidade
* Ferramentas de Teste
* Geração de Dados de Teste
* Projeto Integrador: aplicação prática dos conceitos
* Melhoria Contínua e Cultura de Qualidade

### Estrutura da Prova

**1. Questões Discursivas**

* Explicações conceituais aprofundadas.
* Aplicações práticas de conceitos.
* Exemplos solicitados sobre técnicas.

**2. Estudos de Caso**

* Cenários problemáticos onde o aluno deve:
  + Propor uma estratégia de testes completa.
  + Sugerir ferramentas e técnicas.
  + Definir dados de teste apropriados.
  + Estabelecer critérios de parada.

**3. Questões Práticas**

* Construção de exemplos:
  + Exemplo de matriz de rastreabilidade simplificada.
  + Esboço de plano de testes para microserviços.
  + Diagrama simplificado de observabilidade.

### Metodologia da Avaliação

* **Duração:** 2 horas.
* **Formato:** prova dissertativa e analítica.
* **Material:** prova fechada, sem consulta.
* **Ambiente:** presencial ou remoto supervisionado.

### Critérios de Correção

| **Critério** | **Peso** |
| --- | --- |
| Domínio conceitual | 30% |
| Aplicação prática | 30% |
| Clareza e argumentação | 20% |
| Organização da resposta | 10% |
| Originalidade e profundidade | 10% |

### Competências Desenvolvidas

* Pensamento crítico
* Aplicação prática
* Comunicação técnica
* Capacidade de planejamento
* Gestão de qualidade e processos

### Orientações Finais

* Leitura prévia recomendada:
  + Anotações de todas as aulas do 2º bimestre.
  + Relatórios e documentação do Projeto Integrador.
* A prova integra a avaliação total do bimestre com peso definido previamente.