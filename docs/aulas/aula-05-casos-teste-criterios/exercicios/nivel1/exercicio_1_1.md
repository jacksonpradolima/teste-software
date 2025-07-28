# Exercício 1.1 - Sistema de Login 🔐

## 📋 Informações do Exercício

**Nível**: 🔵 Básico  
**Tempo Estimado**: 20 minutos  
**Modalidade**: Individual  
**Competências**: Elaboração estruturada de casos de teste, identificação de componentes obrigatórios

## 🎯 Objetivo

Desenvolver casos de teste estruturados para um sistema de login simples, aplicando todos os componentes obrigatórios estudados na teoria: identificação, pré-condições, dados de entrada, passos de execução, resultado esperado e critérios de aceitação.

## 📋 Cenário

Você foi contratado(a) para testar o sistema de login de uma plataforma de e-learning. O sistema possui as seguintes especificações:

### Requisitos Funcionais

**REQ01 - Autenticação de Usuário**
- O sistema deve permitir login com email e senha
- Email deve ser um endereço válido (formato: usuario@dominio.ext)
- Senha deve ter no mínimo 6 caracteres
- Login bem-sucedido redireciona para dashboard principal

**REQ02 - Tratamento de Credenciais Inválidas**
- Sistema deve exibir mensagem de erro para credenciais incorretas
- Mensagem deve ser: "Email ou senha incorretos"
- Usuário deve permanecer na tela de login
- Campos devem ser limpos após erro

**REQ03 - Validação de Formato**
- Sistema deve validar formato do email antes da submissão
- Email inválido deve exibir: "Formato de email inválido"
- Senha vazia deve exibir: "Senha é obrigatória"

### Interface do Sistema

```
┌─────────────────────────────────────┐
│         E-Learning Platform         │
├─────────────────────────────────────┤
│  Email: [________________]          │
│  Senha: [________________]          │
│                                     │
│            [  ENTRAR  ]             │
│                                     │
│  Esqueceu sua senha? [Clique aqui]  │
└─────────────────────────────────────┘
```

## 📝 Sua Tarefa

### Etapa 1: Análise dos Requisitos (5 minutos)
1. Identifique os diferentes cenários que devem ser testados
2. Classifique cada cenário como positivo, negativo ou exploratório
3. Determine a prioridade de cada cenário

### Etapa 2: Elaboração dos Casos de Teste (12 minutos)
Crie **pelo menos 4 casos de teste** cobrindo:
- **1 caso positivo**: Login bem-sucedido
- **2 casos negativos**: Credenciais incorretas e formato inválido
- **1 caso adicional**: À sua escolha (boundary, exploratório, etc.)

### Etapa 3: Análise de Cobertura (3 minutos)
1. Verifique se todos os requisitos estão cobertos
2. Identifique possíveis gaps na cobertura
3. Documente a análise de cobertura

## 📄 Template para Entrega

Use o template abaixo para documentar seus casos de teste:

```markdown
# Exercício 1.1 - Sistema de Login
**Estudante**: [Seu Nome]
**Data**: [Data de Realização]

## Análise de Requisitos

### Cenários Identificados
1. [Cenário 1] - Tipo: [Positivo/Negativo] - Prioridade: [Alta/Média/Baixa]
2. [Cenário 2] - Tipo: [Positivo/Negativo] - Prioridade: [Alta/Média/Baixa]
3. [Cenário 3] - Tipo: [Positivo/Negativo] - Prioridade: [Alta/Média/Baixa]
4. [Cenário 4] - Tipo: [Positivo/Negativo] - Prioridade: [Alta/Média/Baixa]

## Casos de Teste

### [Use o template padrão para cada caso]

## Análise de Cobertura

| Requisito | Casos de Teste | Cobertura | Status |
|-----------|----------------|-----------|--------|
| REQ01 | [CT001, CT002] | 100% | ✅ |
| REQ02 | [CT003] | 100% | ✅ |
| REQ03 | [CT004] | 100% | ✅ |

**Resumo da Cobertura:**
- Total de Requisitos: 3
- Requisitos Cobertos: [X]
- Taxa de Cobertura: [X/3 * 100]%

**Gaps Identificados:**
- [Descreva qualquer lacuna na cobertura]

## Reflexão
[1-2 parágrafos sobre desafios encontrados e aprendizados]
```

## 🔍 Critérios de Avaliação

### Estrutura dos Casos de Teste (40 pontos)
- **Excelente (36-40)**: Todos os componentes presentes e bem elaborados
- **Bom (31-35)**: Componentes presentes com pequenas inconsistências
- **Satisfatório (26-30)**: Componentes presentes mas com gaps significativos
- **Insatisfatório (0-25)**: Componentes ausentes ou incorretos

### Cobertura de Requisitos (30 pontos)
- **Excelente (27-30)**: 100% dos requisitos cobertos adequadamente
- **Bom (24-26)**: 80-99% dos requisitos cobertos
- **Satisfatório (21-23)**: 60-79% dos requisitos cobertos
- **Insatisfatório (0-20)**: <60% dos requisitos cobertos

### Qualidade da Documentação (20 pontos)
- **Excelente (18-20)**: Linguagem clara, profissional, executável
- **Bom (16-17)**: Pequenos problemas de clareza ou ambiguidade
- **Satisfatório (14-15)**: Problemas moderados de comunicação
- **Insatisfatório (0-13)**: Documentação confusa ou inadequada

### Análise Crítica (10 pontos)
- **Excelente (9-10)**: Reflexão profunda sobre processo e resultados
- **Bom (8)**: Boa análise com alguns insights
- **Satisfatório (6-7)**: Análise superficial mas adequada
- **Insatisfatório (0-5)**: Análise ausente ou inadequada

## 💡 Dicas para Sucesso

### ✅ Faça
- Leia os requisitos cuidadosamente antes de começar
- Use dados realistas mas não sensíveis
- Torne os passos específicos e executáveis
- Considere diferentes tipos de usuários e browsers
- Revise cada caso antes de prosseguir

### ❌ Evite
- Casos de teste genéricos demais ("Testar login")
- Passos vagos ("Insira dados válidos")
- Resultados esperados não verificáveis
- Negligenciar pré-condições importantes
- Copiar casos da aula sem adaptação

### 🔧 Ferramentas Úteis
- **Editor de Texto**: Para documentação estruturada
- **Navegador**: Para simular mentalmente a execução
- **Calculadora**: Para contagem de cobertura

## ❓ Perguntas Frequentes

**P: Quantos casos de teste devo criar?**
R: Mínimo 4 casos conforme especificado. Você pode criar mais se identificar cenários importantes não cobertos.

**P: Posso usar dados reais?**
R: Não use dados pessoais reais. Crie dados fictícios mas realistas (ex: joao.teste@email.com).

**P: Como sei se meu caso de teste está correto?**
R: Pergunte-se: "Outra pessoa conseguiria executar este teste exatamente como documentei?"

**P: E se eu identificar problemas nos requisitos?**
R: Documente suas observações na seção de reflexão. Em contexto real, você consultaria os stakeholders.

---

**Tempo restante?** Considere criar casos adicionais para cenários boundary (emails muito longos, caracteres especiais) ou exploratórios (diferentes navegadores, dispositivos móveis).
