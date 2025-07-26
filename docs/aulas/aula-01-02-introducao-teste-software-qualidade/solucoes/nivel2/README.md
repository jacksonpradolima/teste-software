# Soluções - Nível 2 (Análise de Cenários)

## Questão 1: Modelos de Processo e Teste

a) O modelo mais apropriado seria o **Modelo V**.
**Justificativa:** Este modelo é ideal para projetos onde os requisitos são estáveis e bem definidos, e onde a rigorosidade e a segurança são primordiais. O Modelo V formaliza a relação entre cada fase do desenvolvimento e sua correspondente fase de teste, garantindo que a verificação e a validação sejam planejadas e executadas de forma sistemática, o que é essencial para um sistema crítico como o de controle de tráfego aéreo.

b) **Organização dos Testes:** As atividades de teste seriam planejadas desde o início, em paralelo com o desenvolvimento.
*   **Teste de Unidade e Integração:** Realizados pelos desenvolvedores à medida que os componentes são construídos.
*   **Teste de Sistema:** Executado por uma equipe de teste independente após a integração de todos os componentes, para validar o sistema contra os requisitos funcionais e não funcionais.
*   **Teste de Aceitação:** Conduzido pelo cliente ou por órgãos reguladores para validar que o sistema atende a todos os critérios de segurança e operacionais.
A intensidade dos testes seria maior nas fases finais (Sistema e Aceitação), e a responsabilidade principal recairia sobre uma equipe de QA/Teste formal e, em última instância, sobre os stakeholders e reguladores.

c) O modelo mais adequado seria o **Ágil (Scrum ou Kanban)**.
**Justificativa:** O ambiente de uma startup de rede social é volátil e exige velocidade e adaptabilidade. O modelo Ágil permite o desenvolvimento em ciclos curtos (sprints), com feedback constante dos usuários, permitindo que a equipe ajuste a direção do produto rapidamente.

d) **Diferenças na Abordagem de Teste:**
*   **Frequência:** No sistema de tráfego aéreo (Modelo V), os grandes ciclos de teste ocorrem em fases distintas. Na startup (Ágil), o teste é uma **atividade diária e contínua** dentro de cada sprint.
*   **Automação:** No cenário Ágil, a **automação é essencial** para dar suporte à integração contínua e à entrega rápida. Testes unitários, de integração e de API são automatizados e rodam a cada commit. No Modelo V, a automação é importante, mas ainda pode haver uma dependência maior de testes manuais e documentação formal.
*   **Responsabilidade:** No Modelo V, a responsabilidade é mais segmentada (desenvolvedores fazem testes de unidade, equipe de QA faz testes de sistema). No modelo Ágil, a **qualidade é responsabilidade de toda a equipe** (*whole-team responsibility*). Desenvolvedores, QAs e Product Owners colaboram continuamente para garantir a qualidade.

## Questão 2: Análise de Qualidade de um Aplicativo

*(As respostas aqui são exemplares, usando o Spotify como base. As respostas dos alunos variarão.)*

a) **Exemplo de alta Usabilidade no Spotify:** A funcionalidade "Daily Mixes" ou "Descobertas da Semana". O aplicativo aprende com o que o usuário ouve e cria playlists personalizadas e relevantes. Isso demonstra alta **aprendizibilidade** e **satisfação**, pois o usuário descobre novas músicas de seu agrado com esforço zero.

b) **Exemplo de baixa qualidade:** Às vezes, ao abrir o aplicativo no celular, ele demora vários segundos para carregar a interface e se conectar à internet, mesmo com uma boa conexão. Durante esse tempo, a interface fica "congelada". Isso se relaciona primariamente com a **Eficiência de Desempenho** (sub-característica: comportamento em relação ao tempo), pois o tempo de resposta para a inicialização do app é lento, prejudicando a experiência do usuário.

c) **Nova funcionalidade:** "Sessão de Escuta em Grupo Sincronizada com Vídeo". Permitir que múltiplos usuários ouçam a mesma música ou podcast ao mesmo tempo e possam abrir uma janela de vídeo para conversar.
*   **Requisito de Eficiência de Desempenho:** A latência (atraso) na sincronização do áudio entre os participantes não deve exceder 200 milissegundos para garantir que todos ouçam a música praticamente ao mesmo tempo.
*   **Requisito de Segurança:** A comunicação por vídeo deve ser criptografada de ponta a ponta (end-to-end encryption) para garantir a **confidencialidade** da conversa dos usuários.

## Questão 3: O Custo Real da Baixa Qualidade

*(As respostas podem variar, usando o Mars Climate Orbiter como exemplo.)*

a) **Caso:** A sonda **Mars Climate Orbiter**, lançada pela NASA em 1998. A falha ocorreu porque um subsistema de software no solo, desenvolvido pela Lockheed Martin, calculava a força em unidades imperiais (libras-força), enquanto o sistema da sonda da NASA esperava os dados em unidades do sistema métrico (newtons). Essa discrepância fez com que a sonda entrasse na atmosfera de Marte em uma altitude muito mais baixa do que o planejado, desintegrando-se devido ao atrito atmosférico. A consequência foi a perda total da missão, com um prejuízo de cerca de US$ 125 milhões.

b) **Fases:** O defeito foi **introduzido** na fase de **Design/Codificação** do software de solo. Ele se **manifestou** apenas na fase de **Produção/Operação**, quando a sonda chegou a Marte, meses após o lançamento. Este é um exemplo clássico e dramático da Curva de Boehm, onde um erro simples de conversão, se detectado na Terra, teria um custo ínfimo, mas, ao se manifestar no espaço, causou a perda de toda a missão.

c) **Prevenção:** A falha poderia ter sido prevenida por uma atividade de **Verificação** durante o **Teste de Integração**. Um teste de integração adequado entre o software da Lockheed Martin e o da NASA deveria ter validado a interface de comunicação entre os dois sistemas, incluindo a verificação das unidades de medida dos dados trocados. Uma simples revisão dos requisitos de interface ou um teste de integração simulando a troca de dados teria exposto a inconsistência fatal.
