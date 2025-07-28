# Soluções Nível 1 - Exercícios Básicos 🔵

Este diretório contém as soluções de referência para os exercícios básicos (individuais) da Aula 05. As soluções demonstram a aplicação correta dos conceitos fundamentais de casos de teste e critérios.

---

## 🎯 Características das Soluções Nível 1

### 📋 **Estrutura Padrão:**
- **Caso de teste completo** seguindo template da aula
- **Justificativas** para cada decisão tomada
- **Variações aceitáveis** e alternativas válidas
- **Pontos de atenção** para evitar erros comuns
- **Critérios de avaliação** específicos

### ⏱️ **Tempo de Referência:**
- **Exercício 1.1:** 20 minutos (tempo médio esperado)
- **Exercício 1.2:** 15 minutos (mais direto)
- **Exercício 1.3:** 25 minutos (mais complexo)

### 🎓 **Nível de Detalhamento:**
- Foco em **conceitos fundamentais**
- Aplicação **direta** da teoria
- **Clareza** na estruturação
- **Precisão** técnica

---

## 📊 Critérios de Avaliação Nível 1

### ✅ **Elementos Obrigatórios (70%):**

| **Critério** | **Peso** | **Descrição** |
|--------------|----------|---------------|
| **Estrutura Completa** | 25% | Todos os campos do template preenchidos corretamente |
| **Qualidade dos Passos** | 20% | Passos claros, executáveis e em sequência lógica |
| **Resultado Esperado** | 15% | Específico, mensurável e alinhado com objetivo |
| **Dados de Teste** | 10% | Apropriados, realistas e abrangentes |

### 🌟 **Elementos de Excelência (20%):**

| **Critério** | **Peso** | **Descrição** |
|--------------|----------|---------------|
| **Clareza de Redação** | 8% | Linguagem precisa, sem ambiguidades |
| **Considerações Extras** | 7% | Aspectos não explícitos mas relevantes |
| **Organização** | 5% | Estrutura lógica e apresentação profissional |

### 📝 **Elementos de Reflexão (10%):**

| **Critério** | **Peso** | **Descrição** |
|--------------|----------|---------------|
| **Justificativas** | 6% | Explicação das escolhas feitas |
| **Alternativas** | 4% | Consideração de outras abordagens |

---

## 🔍 Pontos de Atenção Comuns

### ⚠️ **Erros Frequentes:**

1. **Passos Vagos:**
   - ❌ "Testar o login"
   - ✅ "Inserir email 'user@test.com' no campo Email"

2. **Resultados Imprecisos:**
   - ❌ "Sistema funciona corretamente"
   - ✅ "Sistema exibe mensagem 'Login realizado com sucesso' e redireciona para dashboard"

3. **Dados Irrealistas:**
   - ❌ Email: "abc", Senha: "123"
   - ✅ Email: "joao.silva@email.com", Senha: "MinhaSenh@123"

4. **Falta de Contexto:**
   - ❌ Começar direto com "Clicar em Entrar"
   - ✅ "Acessar página de login do sistema"

### 💡 **Dicas para Excelência:**

1. **Use Personas Realistas:**
   - Nomes, emails e dados verossímeis
   - Contexto de uso coerente
   - Cenários baseados em usuários reais

2. **Seja Específico em Mensagens:**
   - Textos exatos de mensagens de erro/sucesso
   - Elementos visuais específicos (botões, cores)
   - Comportamentos observáveis

3. **Considere Pré-condições:**
   - Estado inicial do sistema
   - Dados já existentes
   - Configurações necessárias

4. **Pense em Verificações Intermediárias:**
   - Validações durante o processo
   - Estados transitórios
   - Feedback visual contínuo

---

## 📚 Templates de Referência

### 📝 **Template Completo para Nível 1:**

```markdown
# CT_XX - [Título Descritivo do Caso de Teste]

## Metadados
| Campo | Valor |
|-------|-------|
| **ID** | CT_XX |
| **Título** | [Descrição clara e específica] |
| **Funcionalidade** | [Módulo/Feature sendo testada] |
| **Tipo** | [Positivo/Negativo/Limite] |
| **Prioridade** | [Alta/Média/Baixa] |
| **Complexidade** | [Básica/Intermediária] |

## Objetivo
[Descrição clara do que este teste visa validar]

## Pré-condições
- [Condição 1: Estado inicial necessário]
- [Condição 2: Dados que devem existir]
- [Condição 3: Configurações requeridas]

## Dados de Teste
| Campo | Valor | Observação |
|-------|-------|------------|
| [Campo 1] | [Valor específico] | [Motivo da escolha] |
| [Campo 2] | [Valor específico] | [Motivo da escolha] |

## Passos de Execução
1. [Passo específico e actionável]
2. [Passo seguinte com contexto]
3. [Verificação intermediária, se aplicável]
4. [Ação final que gera resultado]

## Resultado Esperado
- [Comportamento específico 1]
- [Comportamento específico 2]
- [Estado final do sistema]
- [Mensagens/feedback específicos]

## Critérios de Aceitação
- ✅ [Critério funcional específico]
- ✅ [Critério de usabilidade, se aplicável]
- ✅ [Critério de performance, se relevante]

## Observações
- [Considerações especiais]
- [Dependências com outros testes]
- [Variações possíveis]
```

### 🎯 **Template Simplificado (Mínimo Aceitável):**

```markdown
# CT_XX - [Título]

**Objetivo:** [O que está sendo testado]

**Pré-condições:** [Estado inicial necessário]

**Passos:**
1. [Ação específica]
2. [Ação específica]
3. [Ação específica]

**Resultado Esperado:** [Comportamento específico]

**Dados:** [Inputs necessários]
```

---

## 📈 Evolução de Qualidade

### 🥉 **Nível Básico (6.0-7.0):**
- Template preenchido corretamente
- Passos executáveis
- Resultado claro
- Dados apropriados

### 🥈 **Nível Intermediário (7.1-8.5):**
- Redação clara e profissional
- Consideração de pré-condições
- Verificações intermediárias
- Justificativas básicas

### 🥇 **Nível Avançado (8.6-10.0):**
- Casos abrangentes e detalhados
- Consideração de aspectos não óbvios
- Redação impecável
- Demonstração de pensamento crítico

---

## 🔄 Processo de Autorrevisão

### ✅ **Checklist antes da Entrega:**

**Completude:**
- [ ] Todos os campos obrigatórios preenchidos
- [ ] Passos numerados e em sequência lógica
- [ ] Resultado esperado específico e mensurável
- [ ] Dados de teste realistas e apropriados

**Qualidade:**
- [ ] Linguagem clara e sem ambiguidades
- [ ] Passos executáveis por terceiros
- [ ] Consideração de pré-condições necessárias
- [ ] Alinhamento com objetivo do teste

**Profissionalismo:**
- [ ] Formatação consistente
- [ ] Sem erros de ortografia/gramática
- [ ] Estrutura organizada e lógica
- [ ] Nível de detalhe apropriado

---

## 🎓 Preparação para Nível 2

### 🚀 **Competências a Desenvolver:**

Após dominar os exercícios de Nível 1, foque em:

1. **Análise de Integração:**
   - Como diferentes módulos interagem
   - Pontos de falha entre componentes
   - Fluxos de dados complexos

2. **Trabalho Colaborativo:**
   - Divisão eficiente de responsabilidades
   - Comunicação técnica clara
   - Integração de perspectivas diferentes

3. **Pensamento Sistêmico:**
   - Visão holística do sistema
   - Identificação de dependências
   - Priorização baseada em risco

4. **Documentação Avançada:**
   - Matrizes de rastreabilidade
   - Análise de cobertura
   - Justificativas técnicas detalhadas

---

**Continue praticando e refinando suas habilidades. A base sólida construída no Nível 1 é fundamental para o sucesso nos desafios mais complexos!** 🎯✨
