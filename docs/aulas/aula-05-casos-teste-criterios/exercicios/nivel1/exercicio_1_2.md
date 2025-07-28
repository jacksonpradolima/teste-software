# Exercício 1.2 - Calculadora Online 🧮

## 📋 Informações do Exercício

**Nível**: 🔵 Básico  
**Tempo Estimado**: 15 minutos  
**Modalidade**: Individual  
**Competências**: Classificação de tipos de teste, análise de propósito e cobertura

## 🎯 Objetivo

Praticar a classificação correta de casos de teste em diferentes tipos (positivos, negativos, exploratórios) e compreender como cada tipo contribui para a estratégia geral de validação do sistema.

## 📋 Cenário

Uma startup desenvolveu uma calculadora online simples para estudantes. Você recebeu alguns casos de teste já elaborados por outro testador e precisa analisá-los, classificá-los e completar a cobertura.

### Requisitos da Calculadora

**REQ01 - Operações Básicas**
- Deve suportar: adição (+), subtração (-), multiplicação (×), divisão (÷)
- Deve aceitar números inteiros e decimais
- Resultado deve ser exibido com até 2 casas decimais

**REQ02 - Tratamento de Erros**
- Divisão por zero deve exibir "Erro: Divisão por zero"
- Entrada inválida deve exibir "Erro: Entrada inválida"
- Operação sem segundo número deve aguardar entrada

**REQ03 - Interface e Funcionalidades**
- Botão "Limpar" deve zerar display e memória
- Deve suportar operações em sequência
- Display deve mostrar no máximo 10 dígitos

### Interface da Calculadora

```
┌─────────────────────────┐
│    [  123.45      ]     │  ← Display
├─────────────────────────┤
│  [C]  [±]  [%]  [÷]     │
│  [7]  [8]  [9]  [×]     │
│  [4]  [5]  [6]  [-]     │
│  [1]  [2]  [3]  [+]     │
│  [0]       [.]  [=]     │
└─────────────────────────┘
```

## 📝 Sua Tarefa

### Etapa 1: Análise dos Casos Existentes (8 minutos)

Analise os seguintes casos de teste e **classifique cada um** quanto ao tipo:

**Caso A**
- ID: CTA001
- Título: Soma de dois números positivos
- Dados: 15 + 25
- Resultado Esperado: 40
- **Tipo**: _______________

**Caso B**
- ID: CTA002
- Título: Divisão por zero
- Dados: 10 ÷ 0
- Resultado Esperado: "Erro: Divisão por zero"
- **Tipo**: _______________

**Caso C**
- ID: CTA003
- Título: Sequência de operações complexas
- Dados: 5 + 3 × 2 - 1 ÷ 4
- Objetivo: Verificar precedência e sequenciamento
- **Tipo**: _______________

**Caso D**
- ID: CTA004
- Título: Entrada de número com 15 dígitos
- Dados: 123456789012345
- Objetivo: Investigar comportamento com entrada extrema
- **Tipo**: _______________

**Caso E**
- ID: CTA005
- Título: Multiplicação resultando em decimal
- Dados: 2.5 × 3.2
- Resultado Esperado: 8.00
- **Tipo**: _______________

**Caso F**
- ID: CTA006
- Título: Clique rápido múltiplo no botão de igual
- Dados: 5 + 5 [=] [=] [=] [=]
- Objetivo: Verificar comportamento inesperado
- **Tipo**: _______________

### Etapa 2: Completar a Cobertura (7 minutos)

1. **Identifique gaps**: Quais tipos de teste estão sub-representados?
2. **Crie 2 novos casos** para balancear a cobertura
3. **Justifique** a escolha dos novos casos

## 📄 Template para Entrega

```markdown
# Exercício 1.2 - Calculadora Online
**Estudante**: [Seu Nome]
**Data**: [Data de Realização]

## Parte 1: Classificação dos Casos Existentes

| Caso | ID | Título | Tipo Identificado | Justificativa |
|------|----|---------|--------------------|---------------|
| A | CTA001 | Soma de dois números positivos | [Tipo] | [Por que é este tipo?] |
| B | CTA002 | Divisão por zero | [Tipo] | [Por que é este tipo?] |
| C | CTA003 | Sequência de operações complexas | [Tipo] | [Por que é este tipo?] |
| D | CTA004 | Entrada de número com 15 dígitos | [Tipo] | [Por que é este tipo?] |
| E | CTA005 | Multiplicação resultando em decimal | [Tipo] | [Por que é este tipo?] |
| F | CTA006 | Clique rápido múltiplo no botão igual | [Tipo] | [Por que é este tipo?] |

## Parte 2: Análise de Distribuição

**Contagem por Tipo:**
- Positivos: [X] casos
- Negativos: [Y] casos
- Exploratórios: [Z] casos

**Análise da Distribuição:**
[Descreva se a distribuição está balanceada ou não]

## Parte 3: Novos Casos para Completar Cobertura

### Caso Novo 1
**ID**: CTA007
**Título**: [Título descritivo]
**Tipo**: [Positivo/Negativo/Exploratório]
**Justificativa**: [Por que este caso é necessário?]
**Dados de Entrada**: [Dados específicos]
**Resultado Esperado**: [Comportamento esperado]

### Caso Novo 2
**ID**: CTA008
**Título**: [Título descritivo]
**Tipo**: [Positivo/Negativo/Exploratório]
**Justificativa**: [Por que este caso é necessário?]
**Dados de Entrada**: [Dados específicos]
**Resultado Esperado**: [Comportamento esperado]

## Reflexão sobre Tipos de Teste
[1-2 parágrafos sobre a importância de diferentes tipos e como eles se complementam]
```

## 🔍 Critérios de Avaliação

### Classificação Correta (50 pontos)
- **6 classificações corretas**: 45-50 pontos
- **5 classificações corretas**: 38-44 pontos
- **4 classificações corretas**: 30-37 pontos
- **3 ou menos corretas**: 0-29 pontos

### Justificativas (25 pontos)
- **Excelente**: Justificativas claras e técnicamente corretas
- **Bom**: Justificativas adequadas com pequenas imprecisões
- **Satisfatório**: Justificativas superficiais mas válidas
- **Insatisfatório**: Justificativas incorretas ou ausentes

### Novos Casos (25 pontos)
- **Excelente**: Casos relevantes que preenchem gaps reais
- **Bom**: Casos adequados com valor moderado
- **Satisfatório**: Casos válidos mas óbvios
- **Insatisfatório**: Casos irrelevantes ou duplicados

## 💡 Guia de Classificação

### 🟢 Testes Positivos
**Características:**
- Validam funcionalidade com entradas válidas
- Seguem o "caminho feliz" do usuário
- Verificam se requisitos são atendidos corretamente

**Exemplo**: Soma de dois números inteiros válidos

### 🔴 Testes Negativos
**Características:**
- Testam tratamento de erros e exceções
- Usam entradas inválidas ou situações de erro
- Verificam robustez e comportamento defensivo

**Exemplo**: Divisão por zero, entrada de texto em campo numérico

### 🟡 Testes Exploratórios
**Características:**
- Investigam comportamentos não documentados
- Testam limites e casos extremos
- Buscam descobrir defeitos inesperados

**Exemplo**: Sequências rápidas de cliques, entradas muito longas

## ❓ Perguntas Frequentes

**P: Um teste pode ser de múltiplos tipos?**
R: Em teoria sim, mas para este exercício, classifique pelo propósito **principal** do teste.

**P: Como diferenciar negativo de exploratório?**
R: Negativo testa erro **conhecido** e **documentado**. Exploratório investiga comportamento **não especificado**.

**P: E se eu discordar da classificação "óbvia"?**
R: Justifique bem sua escolha. Avaliação considerará a qualidade da justificativa, não apenas a classificação.

**P: Meus novos casos podem ser simples?**
R: Sim, desde que preencham um gap real na cobertura. Qualidade > Complexidade.

---

**Dica Extra**: Pense como um usuário real usaria a calculadora. Que erros ele poderia cometer? Que comportamentos ele esperaria?
