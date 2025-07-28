# Soluções - Nível 3 (Debate e Estratégia)

## Questão 1: Quality Engineering vs. Quality Assurance

a) A diferença fundamental é a **proatividade versus a reatividade**.
*   **Quality Assurance (QA)** é uma abordagem tradicionalmente reativa, focada em "garantir a qualidade" através da detecção de defeitos *depois* que o software foi construído. O time de QA atua como um "gatekeeper" no final do processo, validando o que foi feito.
*   **Quality Engineering (QE)** é uma abordagem proativa, focada em "construir a qualidade" desde o início. Envolve a engenharia de processos, ferramentas e cultura para *prevenir* que os defeitos ocorram. O QE está integrado ao time de desenvolvimento e se preocupa com a qualidade em todas as fases, desde os requisitos até o deploy e monitoramento.

b) **Três ações práticas para a transição para QE:**
1.  **Implementar "Shift-Left Testing" através de TDD/BDD:** Em vez de esperar o software ficar pronto para testar, a equipe passa a escrever testes (unitários, de comportamento) *antes* ou *durante* o desenvolvimento. Isso previne bugs de lógica e de requisitos, pois força os desenvolvedores a pensarem nos critérios de sucesso antes de escreverem o código, além de garantir que o design seja testável.
2.  **Automatizar a Análise Estática de Código no Pipeline de CI:** Integrar ferramentas como SonarQube, lints (ESLint, Ruff) e analisadores de segurança no pipeline de integração contínua. Essas ferramentas analisam o código a cada commit e bloqueiam a integração se encontrarem "code smells", vulnerabilidades ou código fora do padrão. Isso previne que código de baixa qualidade chegue à base principal, agindo como um "guardião" automatizado da qualidade intrínseca.
3.  **Adotar Revisões de Código (Code Reviews) Obrigatórias e Estruturadas:** Instituir a prática de que nenhum código pode ser mesclado à branch principal sem a revisão e aprovação de pelo menos um outro membro da equipe. Isso não só detecta bugs, mas também dissemina conhecimento, melhora a qualidade do código e previne a introdução de lógica falha ou complexa demais. É uma forma de verificação humana e colaborativa.

c) Em uma cultura de Quality Engineering, **a qualidade é responsabilidade de todos**. Não é mais um silo.
*   O **Desenvolvedor** é responsável pela qualidade do seu código (testes unitários, código limpo).
*   O **Engenheiro de Qualidade (QE)** é responsável por construir e manter a infraestrutura de testes, definir estratégias e capacitar a equipe.
*   O **Product Owner (PO)** é responsável por escrever requisitos claros e critérios de aceitação testáveis.
*   O **Time de Operações (Ops)** é responsável por garantir que o ambiente de produção seja monitorável para detectar problemas de qualidade em tempo real.
A qualidade deixa de ser um "departamento" e se torna um valor cultural compartilhado por toda a equipe que constrói o produto.

## Questão 2: Estratégia de Qualidade para um Novo Produto

As quatro características mais críticas para uma plataforma de telemedicina seriam: **Segurança, Confiabilidade, Usabilidade e Adequação Funcional**.

---

**1. Característica Escolhida:** **Segurança**

*   **Justificativa:** A plataforma manipula dados de saúde extremamente sensíveis (prontuários, diagnósticos), protegidos por leis rigorosas como a LGPD no Brasil. Uma falha de segurança poderia expor dados de pacientes, levar a processos judiciais e destruir a reputação da empresa.
*   **Requisito de Exemplo:** "Toda a comunicação por vídeo e troca de dados entre paciente e médico deve ser criptografada de ponta a ponta, e os dados em repouso (no banco de dados) devem ser armazenados em formato criptografado."
*   **Tipo de Teste Essencial:** **Teste de Penetração (Pentest)** e **Análise de Vulnerabilidades Automatizada (SAST/DAST)** para identificar e explorar possíveis brechas de segurança.

---

**2. Característica Escolhida:** **Confiabilidade**

*   **Justificativa:** Médicos e pacientes dependem da plataforma para atendimentos de saúde. Uma falha durante uma consulta (ex: o sistema cai) pode interromper um diagnóstico importante. O sistema deve estar disponível e funcionar corretamente sempre que necessário.
*   **Requisito de Exemplo:** "O sistema deve ter uma disponibilidade de 99.9%, e em caso de falha em um servidor, o sistema de backup deve assumir a operação em menos de 1 minuto (tolerância a falhas)."
*   **Tipo de Teste Essencial:** **Teste de Carga e Estresse** para simular um grande número de consultas simultâneas e verificar a estabilidade do sistema. **Teste de Failover** para simular a queda de um servidor e garantir que o backup funcione como esperado.

---

**3. Característica Escolhida:** **Usabilidade**

*   **Justificativa:** O público-alvo é amplo e inclui pessoas com diferentes níveis de habilidade tecnológica, como idosos. Se a plataforma for difícil de usar, os pacientes não conseguirão se conectar às consultas ou acessar seus exames, tornando o serviço inútil.
*   **Requisito de Exemplo:** "Um usuário de primeira viagem, com mais de 65 anos, deve ser capaz de iniciar uma consulta por vídeo em menos de 3 cliques após fazer o login, sem a necessidade de um tutorial."
*   **Tipo de Teste Essencial:** **Teste de Usabilidade com Usuários Reais**, observando pessoas do público-alvo (incluindo idosos) interagindo com a plataforma para identificar pontos de confusão e dificuldade.

---

**4. Característica Escolhida:** **Adequação Funcional**

*   **Justificativa:** A precisão das funcionalidades é crítica. Uma falha na exibição de um prontuário ou na geração de uma prescrição digital pode levar a um erro médico grave. O software deve fazer exatamente o que é esperado dele, sem erros.
*   **Requisito de Exemplo:** "O sistema deve garantir que a prescrição digital gerada para o Paciente A seja visível apenas para o Paciente A e seu médico, e que os dados do medicamento (nome, dosagem) sejam exibidos com 100% de precisão."
*   **Tipo de Teste Essencial:** **Teste Funcional de ponta a ponta (End-to-End)**, criando casos de teste detalhados que simulam o fluxo completo de uma consulta, desde o login do paciente até a emissão e recebimento da prescrição, validando cada passo e cada dado exibido.

## Questão 3: O Dilema do Lançamento

a) **Argumento a favor de LANÇAR:**
"Deveríamos lançar na data prevista. O bug afeta um segmento muito pequeno de usuários (1%) em uma configuração técnica específica, e o impacto financeiro por transação é baixo (5% de desconto extra). O risco de adiar o lançamento e quebrar a promessa feita aos clientes na campanha de marketing é maior do que o risco do bug. Podemos mitigar o problema de forma proativa: 1) Implementar um monitoramento no backend para detectar e logar todas as transações que se encaixam nesse cenário. 2) Preparar um *hotfix* para ser lançado na próxima semana, já comunicando internamente que a correção é prioridade máxima. 3) Se necessário, podemos contatar os poucos clientes afetados e oferecer um crédito ou estorno, transformando um problema em uma experiência positiva de atendimento ao cliente. O custo do bug é controlável e menor do que o custo de oportunidade e de reputação de um adiamento."

b) **Argumento a favor de ADIAR:**
"Não podemos lançar com um bug conhecido que causa prejuízo financeiro, por menor que seja. Lançar com este defeito abre um precedente perigoso e degrada nossa cultura de qualidade. O risco não é apenas o 1% que conhecemos; não sabemos se essa mesma falha pode ter outras manifestações ainda não descobertas. Se os usuários descobrirem o bug antes de nós, ele pode ser explorado e divulgado em redes sociais, causando um dano de imagem muito maior do que um simples adiamento. Adiar o lançamento por uma semana e comunicar de forma transparente aos nossos clientes que estamos garantindo a qualidade e a segurança do sistema é uma atitude mais profissional e que, a longo prazo, constrói mais confiança do que lançar um produto com falhas. A integridade do nosso software deve ser a prioridade."

c) **Recomendação Final (Exemplo):**
"Minha recomendação é **adiar o lançamento**. Embora o impacto imediato do bug pareça pequeno e controlável, a decisão de lançar um software com um defeito financeiro conhecido corrói os padrões de qualidade da equipe e da empresa. A confiança do cliente é o nosso ativo mais valioso, e ela é mais bem preservada com transparência e um compromisso inabalável com a qualidade do que com o cumprimento de um prazo de marketing a qualquer custo. Devemos usar esta semana extra não apenas para corrigir o bug, mas também para realizar uma rodada de testes de regressão completa, garantindo que a correção não introduziu novos problemas. Comunicaremos o adiamento de forma honesta, reforçando nosso compromisso com a excelência. A perda de uma semana no cronograma é um preço pequeno a pagar pela integridade do nosso produto e pela confiança de nossos clientes a longo prazo."
