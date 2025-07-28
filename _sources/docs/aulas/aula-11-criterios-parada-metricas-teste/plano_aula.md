# Plano de Aula 11: Critérios de Parada e Métricas de Teste

## Objetivo Geral

Capacitar os alunos a **identificar, definir e aplicar critérios de parada de testes**, além de **compreender e utilizar métricas de teste** para avaliação da qualidade do software e do processo de teste. O objetivo é formar um pensamento crítico e analítico para tomadas de decisão informadas no processo de desenvolvimento e manutenção de software.

## Objetivos Específicos

1. **Definir critérios de parada em um processo de teste**, considerando qualidade, tempo e custo.
2. **Compreender a importância de métricas de teste para a gestão da qualidade do software.**
3. **Identificar diferentes métricas utilizadas na prática de testes de software.**
4. **Calcular e interpretar métricas como cobertura de código, taxa de detecção de defeitos, densidade de defeitos e DRE (Defect Removal Efficiency).**
5. **Compreender as relações entre critérios de parada e métricas no contexto de gestão de riscos.**
6. **Aplicar o conhecimento em simulações de cenários de projetos para decidir o momento de interrupção do ciclo de testes.**
7. **Analisar criticamente limitações das métricas e dos critérios de parada, evitando interpretações superficiais ou enviesadas.**
8. **Refletir sobre como o uso adequado de métricas contribui para práticas de melhoria contínua no desenvolvimento de software.**

## Conteúdo Programático Detalhado

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

Cobertura (%) = (Linhas executadas / Total de linhas de código) * 100

**4.2 Cálculo de DRE**

DRE (%) = (Defeitos removidos antes da entrega / (Defeitos removidos antes + depois da entrega)) * 100

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

## Metodologia

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
