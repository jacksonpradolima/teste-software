# 🔵 Nível 1 - Exercícios Básicos

## Visão Geral

Os exercícios do Nível 1 focam na **aplicação direta** dos conceitos fundamentais apresentados na aula. Cada exercício é projetado para ser concluído individualmente em 15-30 minutos, permitindo assimilação gradual dos componentes estruturais de casos de teste.

## Exercício 1.1 - Estrutura de Casos de Teste
**Tempo Estimado**: 20 minutos  
**Competências**: Elaboração estruturada, componentes obrigatórios

## Exercício 1.2 - Classificação de Tipos
**Tempo Estimado**: 15 minutos  
**Competências**: Identificação de tipos, análise de propósito

## Exercício 1.3 - Critérios Básicos
**Tempo Estimado**: 25 minutos  
**Competências**: Definição de critérios, aplicação de thresholds

---

## 📋 Templates de Apoio

### Template de Caso de Teste
```markdown
**Caso de Teste CT[XXX]**

| Campo | Valor |
|-------|-------|
| **ID** | CT[XXX] |
| **Título** | [Descrição clara do objetivo] |
| **Requisito** | [ID do requisito validado] |
| **Tipo** | [Positivo/Negativo/Exploratório] |
| **Prioridade** | [Crítica/Alta/Média/Baixa] |
| **Pré-condições** | [Estado necessário antes da execução] |

**Dados de Entrada:**
- [Campo 1]: [Valor 1]
- [Campo 2]: [Valor 2]

**Passos de Execução:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Resultado Esperado:**
- [Comportamento específico esperado]
- [Saídas ou estados finais]

**Critérios de Aceitação:**
- [Critério 1]
- [Critério 2]
```

### Template de Análise de Cobertura
```markdown
**Análise de Cobertura**

| Requisito | Casos de Teste | Cobertura | Status |
|-----------|----------------|-----------|--------|
| [REQ01] | [CT001, CT002] | [%] | [✅/❌] |
| [REQ02] | [CT003] | [%] | [✅/❌] |

**Resumo:**
- Total de Requisitos: [X]
- Requisitos Cobertos: [Y]
- Taxa de Cobertura: [Y/X * 100]%
```

---

## 📝 Lista de Exercícios

1. **[Exercício 1.1 - Sistema de Login](./exercicio_1_1.md)**
2. **[Exercício 1.2 - Calculadora Online](./exercicio_1_2.md)**
3. **[Exercício 1.3 - Formulário de Contato](./exercicio_1_3.md)**

---

## ✅ Checklist de Qualidade - Nível 1

Antes de submeter cada exercício, verifique:

### Estrutura dos Casos de Teste
- [ ] ID único e sequencial
- [ ] Título claro e descritivo
- [ ] Rastreabilidade para requisito específico
- [ ] Tipo correto identificado
- [ ] Prioridade justificada
- [ ] Pré-condições explícitas

### Conteúdo dos Casos de Teste
- [ ] Dados de entrada especificados
- [ ] Passos executáveis e não ambíguos
- [ ] Resultado esperado verificável
- [ ] Critérios de aceitação mensuráveis

### Qualidade Geral
- [ ] Linguagem clara e objetiva
- [ ] Casos executáveis por terceiros
- [ ] Cobertura adequada aos requisitos
- [ ] Documentação profissional