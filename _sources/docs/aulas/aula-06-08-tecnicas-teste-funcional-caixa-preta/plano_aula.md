# Plano de Aulas 6-8: Técnicas de Teste Funcional (Caixa-Preta)

## Objetivo Geral

Capacitar o aluno a **identificar, interpretar e aplicar técnicas de teste funcional do tipo caixa-preta**, com foco específico em **Particionamento de Equivalência**, **Análise do Valor Limite**, **Tabelas de Decisão**, **Máquinas de Estado** e **Testes Baseados em Casos de Uso**, permitindo a formulação de casos de teste capazes de verificar a conformidade do software em relação às suas especificações funcionais e aos comportamentos esperados.

## Objetivos Específicos

1. **Definir o que são técnicas de teste funcional (caixa-preta)** e como se diferenciam das técnicas estruturais (caixa-branca).
2. **Explicar o conceito de Particionamento de Equivalência**, suas regras, aplicação prática e limites.
3. **Explicar o conceito de Análise do Valor Limite**, suas aplicações e importância na detecção de defeitos em fronteiras de valores.
4. **Compreender o que são e como construir Tabelas de Decisão** para representar regras de negócio complexas.
5. **Interpretar e construir Máquinas de Estado para modelar o comportamento dinâmico dos sistemas.**
6. **Relacionar requisitos e fluxos de interação do sistema com Casos de Uso e derivar testes a partir deles.**
7. **Identificar quando aplicar cada técnica no processo de teste.**
8. **Desenvolver habilidades para construir casos de teste aplicando essas técnicas a partir de requisitos especificados.**
9. **Demonstrar a aplicabilidade das técnicas em sistemas reais como autenticação, transações financeiras, validações de formulários, etc.**
10. **Comparar a eficiência entre casos de teste criados empiricamente e casos de teste criados sistematicamente a partir das técnicas aprendidas.**
11. **Fomentar o pensamento crítico quanto à cobertura funcional e à eficiência dos testes gerados.**

## Conteúdo Programático Detalhado

### Aula 6: Particionamento de Equivalência e Análise do Valor Limite

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

### Aulas 7-8: Tabelas de Decisão, Máquinas de Estado e Casos de Uso

**1. Tabelas de Decisão**

**1.1 Definição**

* Estrutura que organiza **condições e ações** de forma tabular, permitindo representar regras de decisão complexas de maneira sistemática.
* Muito utilizadas em sistemas que possuem diversas combinações possíveis de entradas.

**1.2 Componentes**

* **Condições:** perguntas ou critérios que podem ser verdadeiros ou falsos.
* **Ações:** operações ou respostas do sistema.
* **Regras:** combinações entre condições e as ações que devem ser tomadas.

**1.3 Estrutura de uma Tabela de Decisão**

| **Condições / Regras** | **Regra 1** | **Regra 2** | **Regra 3** | **...** |
| --- | --- | --- | --- | --- |
| Condição A | V | V | F |  |
| Condição B | F | V | V |  |
| ... |  |  |  |  |
| **Ação X** | X |  | X |  |
| **Ação Y** |  | X |  |  |

**1.4 Exemplo Prático**

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

**1.5 Benefícios**

* Organiza regras complexas.
* Ajuda a identificar combinações não previstas.
* Facilita a validação de requisitos.

**1.6 Desvantagens**

* Crescimento exponencial de combinações em sistemas muito complexos.

**2. Máquinas de Estado**

**2.1 Definição**

* Modelos matemáticos que descrevem o comportamento de um sistema através de **estados e transições**.

**2.2 Componentes**

* **Estado:** condição atual do sistema.
* **Transição:** mudança de um estado para outro baseada em eventos ou condições.
* **Evento:** ação ou condição que dispara a transição.
* **Ação:** comportamento executado durante ou após a transição.

**2.3 Exemplo Prático**

* Sistema de autenticação:
  + Estados: Deslogado, Logando, Logado, Bloqueado
  + Transições: Login bem-sucedido, Tentativa falha, Limite de tentativas excedido
* Representação gráfica do modelo.

**2.4 Construção de Máquinas de Estado**

* Identificar os estados do sistema.
* Definir os eventos que causam transições.
* Mapear transições válidas e inválidas.
* Determinar ações associadas.

**2.5 Benefícios**

* Permite visualizar o comportamento do sistema ao longo do tempo.
* Facilita a identificação de transições incorretas ou estados inválidos.

**2.6 Limitações**

* Modelagem pode ser complexa para sistemas com muitos estados.

**3. Testes Baseados em Casos de Uso**

**3.1 Definição**

* Casos de Uso descrevem **interações entre o usuário e o sistema** para atingir um objetivo específico.
* A partir dos casos de uso, podem-se derivar cenários de teste que cobrem fluxos principais e alternativos.

**3.2 Estrutura de um Caso de Uso**

* **Ator:** quem interage com o sistema.
* **Fluxo principal:** caminho ideal para atingir o objetivo.
* **Fluxos alternativos:** variações ou exceções.
* **Pré-condições:** estado do sistema antes do uso.
* **Pós-condições:** estado esperado após o uso.

**3.3 Exemplo Prático**

* Sistema de reservas:
  + Caso de uso: Reservar Quarto
  + Ator: Cliente
  + Fluxo principal: Seleciona quarto > Insere dados > Confirma reserva
  + Fluxo alternativo: Falta de disponibilidade.

**3.4 Derivação de Casos de Teste**

* Criar casos para o fluxo principal.
* Criar casos para cada fluxo alternativo.
* Testar limites, exceções e condições de erro.

**3.5 Benefícios**

* Alta aderência ao comportamento esperado pelo usuário.
* Facilidade de comunicação com stakeholders.

**4. Comparação entre as Técnicas**

| **Técnica** | **Uso** |
| --- | --- |
| Particionamento de Equivalência | Divisão de domínios de entrada |
| Análise do Valor Limite | Teste de fronteiras |
| Tabela de Decisão | Regras complexas com múltiplas condições |
| Máquina de Estado | Sistemas com estados e transições definidos |
| Casos de Uso | Interação do usuário with o sistema |

**5. Exemplos de Aplicação em Sistemas Reais**

* Aplicativo bancário: autenticação, transações, bloqueio de conta.
* E-commerce: compra, cancelamento, troca.
* Sistemas industriais: controle de máquinas, modos de operação.

## Metodologia

**Aula 6**
* Aula expositiva visual com slides e quadro para construção de partições
* Demonstração de análise de código real
* Prática guiada onde alunos constroem partições e aplicam critérios em exemplos

**Aulas 7-8**
* Aula expositiva visual com diagramas, fluxogramas e exemplos gráficos
* Demonstração de ferramentas para desenhar máquinas de estado
* Estudo de caso em sala aplicando as técnicas a um sistema conhecido
* Atividade em grupos onde cada grupo elabora exemplos próprios
* Apresentação dos grupos com feedback colaborativo

**Leitura Recomendada**

* Capítulo específico do livro "Software Testing - A Craftsman's Approach" sobre técnicas de teste funcional
* Leitura de material do ISTQB sobre o tema
* SWEBOK capítulo sobre Model-Based Testing
* Artigos sobre tabelas de decisão na área financeira
