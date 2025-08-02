# Exercícios - Critérios de Parada e Métricas de Teste

## Visão Geral

Esta seção contém exercícios práticos organizados em três níveis de dificuldade, projetados para consolidar e aplicar os conceitos fundamentais de critérios de parada e métricas de teste apresentados na aula teórica.

## Objetivos Pedagógicos

Ao completar estes exercícios, você será capaz de:

✅ **Calcular e interpretar métricas fundamentais** de cobertura, densidade de defeitos, DRE e MTTD  
✅ **Implementar sistemas automatizados** para coleta e avaliação de métricas  
✅ **Projetar critérios de parada contextualizados** para diferentes tipos de sistema  
✅ **Identificar e evitar anti-padrões** comuns em métricas de teste  
✅ **Aplicar técnicas avançadas** como critérios adaptativos e otimizações de performance  

## Estrutura dos Exercícios

### 🔵 **Nível 1 - Básico (15-30 minutos cada)**
**Foco:** Aplicação direta de conceitos fundamentais
- Cálculo manual de métricas básicas
- Implementação de fórmulas matemáticas
- Interpretação de resultados simples

### 🟡 **Nível 2 - Intermediário (45-90 minutos cada)**  
**Foco:** Integração de múltiplos conceitos e decisões contextuais
- Sistemas de avaliação de critérios
- Análise comparativa de cenários
- Design de estratégias de teste

### 🔴 **Nível 3 - Avançado (2-4 horas cada)**
**Foco:** Design complexo e implementação de sistemas completos
- Critérios adaptativos com IA
- Otimizações de performance
- Análise de anti-padrões em contextos reais

## Metodologia de Trabalho

### Preparação
1. **Revise o conteúdo teórico** da aula antes de iniciar os exercícios
2. **Configure o ambiente Python 3.12+** com as bibliotecas nativas necessárias
3. **Leia completamente** o enunciado antes de começar a implementação

### Execução
- **Comece sempre pelo Nível 1** para consolidar fundamentos
- **Documente seu código** seguindo as convenções pedagógicas da aula
- **Teste suas implementações** com os casos de teste fornecidos
- **Reflita sobre os resultados** e compare com suas expectativas iniciais

### Validação
- **Compare suas soluções** com os gabaritos após completar cada exercício
- **Identifique pontos de melhoria** e refatore quando necessário
- **Discuta dúvidas** com colegas ou instrutores

## Recursos de Apoio

### Arquivos Base
Alguns exercícios incluem código-base ou datasets para acelerar o foco nos conceitos principais. Estes arquivos estão claramente identificados em cada enunciado.

### Bibliotecas Permitidas
Seguindo a filosofia da aula, os exercícios utilizam **apenas recursos nativos do Python 3.12+**:
- `typing` - Anotações de tipo
- `dataclasses` - Estruturas de dados
- `datetime` - Manipulação temporal
- `enum` - Constantes tipadas
- `json` - Serialização
- `math` - Operações matemáticas
- `statistics` - Estatísticas básicas
- `concurrent.futures` - Paralelização (apenas Nível 3)

### Critérios de Avaliação

Cada exercício será avaliado considerando:

| Critério | Peso | Descrição |
|----------|------|-----------|
| **Correção Funcional** | 40% | Implementação correta dos algoritmos e fórmulas |
| **Qualidade do Código** | 25% | Organização, legibilidade e boas práticas |
| **Documentação** | 20% | Comentários explicativos e docstrings |
| **Testes e Validação** | 15% | Verificação adequada dos resultados |

### Tempo Estimado Total
- **Nível 1:** 2-3 horas (4 exercícios)
- **Nível 2:** 4-6 horas (3 exercícios)  
- **Nível 3:** 6-8 horas (2 exercícios)
- **Total:** 12-17 horas

## Estrutura de Entrega

Para cada exercício completado:

1. **Código fonte** comentado seguindo as convenções da aula
2. **Arquivo de teste** demonstrando o funcionamento
3. **Relatório breve** (2-3 parágrafos) com análise dos resultados
4. **Reflexão crítica** sobre dificuldades encontradas e lições aprendidas

## Dicas para Sucesso

💡 **Comece simples:** Implemente a versão mais básica primeiro, depois adicione complexidade  
💡 **Use print statements:** Para debug e visualização de resultados intermediários  
💡 **Teste incrementalmente:** Não espere completar tudo para testar  
💡 **Leia os comentários:** Os gabaritos contêm insights pedagógicos valiosos  
💡 **Foque na compreensão:** O objetivo é aprender, não apenas "passar"  

---

## Lista de Exercícios

### Nível 1 - Básico 🔵
**Tempo:** 20-45 minutos cada  
**Foco:** Aplicação direta de conceitos fundamentais

1. [Calculadora de Métricas Fundamentais](nivel1/exercicio-01-calculadora-metricas.md)
   - Implementação de cálculos básicos de cobertura, DRE e densidade de defeitos
   
2. [Análise de Cobertura de Código](nivel1/exercicio-02-analise-cobertura.md)  
   - Análise de diferentes cenários de cobertura em projetos reais
   
3. [Avaliador de Critérios Simples](nivel1/exercicio-03-avaliador-criterios.md)
   - Sistema básico de avaliação de critérios de parada
   
4. [Interpretação de Resultados de DRE](nivel1/exercicio-04-interpretacao-dre.md)
   - Análise e interpretação de métricas DRE em múltiplos projetos

### Nível 2 - Intermediário 🟡
**Tempo:** 60-90 minutos cada  
**Foco:** Integração de múltiplos conceitos e arquitetura de sistemas

1. [Sistema de Monitoramento de Métricas](nivel2/exercicio-01-sistema-monitoramento.md)
   - Sistema completo com coleta, análise, alertas e dashboard
   
2. [Critérios Contextualizados por Domínio](nivel2/exercicio-02-criterios-contextualizados.md)
   - Adaptação inteligente de critérios baseada em contexto (aviação, fintech, e-commerce)
   
3. [Análise Comparativa Multi-Projeto](nivel2/exercicio-03-analise-comparativa.md)
   - Sistema de análise estatística e benchmarking entre projetos

### Nível 3 - Avançado 🔴
**Tempo:** 3-4 horas cada  
**Foco:** Pesquisa aplicada e inovação técnica

1. [Critérios Adaptativos com Machine Learning](nivel3/exercicio-01-criterios-adaptativos-ml.md)
   - Sistema inteligente que aprende e adapta critérios usando ML e pattern recognition
   
2. [Otimização Multi-Objetivo e Performance](nivel3/exercicio-02-otimizacao-multiobjetivo.md)
   - Algoritmos genéticos e otimização de Pareto para balancear objetivos conflitantes

---

**Boa sorte e bom aprendizado! 🚀**
