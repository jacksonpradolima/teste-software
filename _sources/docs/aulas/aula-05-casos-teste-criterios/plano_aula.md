# Plano de Aula 5: Casos de Teste e Critérios

## Objetivo Geral

Capacitar o aluno a **compreender, construir e avaliar casos de teste a partir de requisitos de software**, aplicando critérios sólidos para criação, execução e encerramento dos testes. A aula buscará desenvolver no aluno o raciocínio sistemático e crítico para converter requisitos e comportamentos esperados em **casos de teste bem estruturados**, apoiando-se em critérios formais que assegurem a eficiência e eficácia da atividade de testes.

## Objetivos Específicos

1. **Definir o que são casos de teste**, suas partes constituintes e o papel que exercem no processo de validação de software.
2. **Identificar as principais características de um bom caso de teste**, segundo práticas e padrões reconhecidos pela área.
3. **Distinguir entre diferentes tipos de casos de teste**: positivos, negativos, exploratórios, regressivos.
4. **Compreender o papel dos critérios de teste**, tanto para a elaboração de casos quanto para o encerramento dos testes.
5. **Desenvolver a habilidade de criar casos de teste a partir de requisitos funcionais e não funcionais.**
6. **Refletir sobre a rastreabilidade dos casos de teste em relação aos requisitos.**
7. **Praticar a criação de casos de teste para cenários reais e simulados, com identificação de entradas, ações e saídas esperadas.**
8. **Estabelecer critérios para priorização de casos de teste em contextos com restrição de recursos.**

## Conteúdo Programático Detalhado

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

## Metodologia

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
