# Plano de Aulas 9-10: Técnicas de Teste Estrutural (Caixa-Branca)

## Objetivo Geral

Capacitar os alunos a **compreender e aplicar técnicas de teste estrutural (caixa-branca)**, dominando os conceitos de **fluxo de controle** e **fluxo de dados**, para garantir uma cobertura eficiente do código-fonte por meio de critérios formais de teste, maximizando a detecção de defeitos lógicos e estruturais.

## Objetivos Específicos

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

## Conteúdo Programático Detalhado

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

## Metodologia

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
