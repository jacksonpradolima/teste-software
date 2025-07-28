# Exercício 2.2 - Sistema de Mobile Banking 🟡

**Duração:** 75 minutos  
**Modalidade:** Duplas  
**Dificuldade:** Intermediário  

## 📋 Visão Geral

Você e seu(sua) parceiro(a) foram contratados como especialistas em teste para validar um novo aplicativo de **mobile banking** antes de seu lançamento. O sistema precisa atender rigorosos padrões de segurança, performance e compliance regulatório.

Este exercício integra múltiplos conceitos: **casos de teste de segurança**, **critérios de performance**, **rastreabilidade de compliance** e **análise de riscos**.

---

## 🎯 Objetivos de Aprendizagem

Ao final deste exercício, você será capaz de:

- ✅ **Elaborar casos de teste para sistemas críticos** com foco em segurança e compliance
- ✅ **Aplicar critérios específicos de mobile banking** incluindo regulamentações financeiras
- ✅ **Trabalhar colaborativamente** na análise de riscos e definição de estratégias
- ✅ **Integrar aspectos técnicos e regulatórios** em uma matriz de rastreabilidade completa
- ✅ **Priorizar testes baseado em análise de risco** considerando impacto financeiro

---

## 📱 Descrição do Sistema

### Funcionalidades Principais

**🔐 Módulo de Autenticação e Segurança**
- Login biométrico (digital, facial)
- Autenticação de dois fatores (SMS, email, token)
- Bloqueio automático por inatividade
- Criptografia end-to-end para todas as transações

**💰 Módulo de Transações Financeiras**
- Transferências PIX (instantâneas)
- Transferências TED/DOC
- Pagamento de boletos com leitura de código de barras
- Recarga de celular e cartões de transporte

**📊 Módulo de Consultas e Extratos**
- Saldo e extrato em tempo real
- Histórico de transações com filtros avançados
- Exportação de extratos (PDF, Excel)
- Gráficos de gastos por categoria

**⚙️ Módulo de Configurações e Perfil**
- Gerenciamento de limites de transação
- Configuração de notificações
- Cadastro de favoritos e frequentes
- Gerenciamento de cartões virtuais

**🛡️ Módulo de Compliance e Auditoria**
- Log de todas as ações do usuário
- Detecção de fraudes em tempo real
- Relatórios para órgãos reguladores
- Backup automático de dados críticos

---

## 👥 Metodologia Colaborativa

### Divisão de Responsabilidades

**👤 Testador A - Especialista em Segurança:**
- Foco nos módulos de Autenticação e Compliance
- Casos de teste para vulnerabilidades de segurança
- Análise de riscos relacionados a fraudes
- Validação de criptografia e proteção de dados

**👤 Testador B - Especialista em Negócio:**
- Foco nos módulos de Transações e Consultas
- Casos de teste para fluxos financeiros
- Análise de performance e usabilidade
- Validação de regulamentações bancárias

### Momentos de Sincronização

**🕐 15 min:** Planejamento conjunto e definição de estratégia  
**🕐 30 min:** Primeira sincronização - compartilhamento de casos críticos  
**🕐 60 min:** Segunda sincronização - revisão cruzada e integração  
**🕐 75 min:** Apresentação final e discussão de gaps identificados  

---

## 📋 Atividades Detalhadas

### Fase 1: Análise de Riscos e Planejamento (15 min)

**Atividade Conjunta:**

1. **Identifiquem os 5 principais riscos** do sistema de mobile banking:
   - Riscos de segurança (vazamento de dados, fraudes)
   - Riscos operacionais (indisponibilidade, lentidão)
   - Riscos regulatórios (não conformidade com BACEN, LGPD)
   - Riscos de usabilidade (interface confusa, acessibilidade)
   - Riscos técnicos (bugs críticos, integração falha)

2. **Priorizem os riscos** usando matriz de Impacto x Probabilidade:
   - **Alto Impacto + Alta Probabilidade:** Prioridade 1
   - **Alto Impacto + Baixa Probabilidade:** Prioridade 2  
   - **Baixo Impacto + Alta Probabilidade:** Prioridade 3
   - **Baixo Impacto + Baixa Probabilidade:** Prioridade 4

3. **Definam critérios específicos** para o mobile banking:
   ```
   Critérios de Segurança:
   - 100% dos casos de autenticação testados
   - Zero falhas em testes de penetração
   - Conformidade com PCI-DSS validada
   
   Critérios de Performance:
   - Login em < 3 segundos
   - Transações PIX em < 10 segundos
   - Disponibilidade > 99.9%
   
   Critérios de Compliance:
   - 100% aderência às normas BACEN
   - LGPD compliance verificado
   - Trilha de auditoria completa
   ```

### Fase 2: Desenvolvimento Individual (30 min)

**Cada testador trabalha em sua especialidade:**

#### Para o Testador A (Segurança):

**Crie 3 casos de teste detalhados:**

1. **CT_SEC_001 - Tentativa de Login com Força Bruta**
   - Validar bloqueio após múltiplas tentativas
   - Verificar logs de segurança
   - Testar diferentes padrões de ataque

2. **CT_SEC_002 - Interceptação de Dados em Transações**
   - Simular man-in-the-middle attack
   - Verificar criptografia end-to-end
   - Validar integridade dos dados

3. **CT_SEC_003 - Acesso com Credenciais Expiradas**
   - Testar tokens expirados
   - Verificar renovação automática
   - Validar logout forçado

#### Para o Testador B (Negócio):

**Crie 3 casos de teste detalhados:**

1. **CT_NEG_001 - Transferência PIX Acima do Limite**
   - Testar controles de limite
   - Verificar mensagens de erro
   - Validar logs de compliance

2. **CT_NEG_002 - Pagamento de Boleto Vencido**
   - Calcular juros e multas
   - Verificar integração bancária
   - Testar diferentes cenários

3. **CT_NEG_003 - Consulta de Extrato com Grande Volume**
   - Performance com 10.000+ transações
   - Paginação e filtros
   - Exportação de dados

### Fase 3: Sincronização e Integração (15 min)

**Atividade Conjunta:**

1. **Compartilhem os casos de teste** criados
2. **Identifiquem dependências** entre os módulos
3. **Criem 2 casos de teste integrados** que abrangem múltiplos módulos
4. **Definam a sequência de execução** considerando dependências

### Fase 4: Matriz de Rastreabilidade Avançada (15 min)

**Criem uma matriz que inclua:**

| **Regulamentação** | **Requisito** | **Risco** | **Caso de Teste** | **Evidência** | **Status** |
|-------------------|---------------|-----------|-------------------|---------------|------------|
| BACEN 4595 | Autenticação forte | Fraude | CT_SEC_001 | Log + Screenshot | 🟡 Pendente |
| LGPD Art. 46 | Criptografia dados | Vazamento | CT_SEC_002 | Certificado SSL | ✅ Passou |
| ... | ... | ... | ... | ... | ... |

---

## 🎯 Entregáveis

### 1. Documento de Estratégia de Teste (Conjunto)
```markdown
# Estratégia de Teste - Mobile Banking

## Riscos Identificados
[Lista priorizada com justificativas]

## Critérios Específicos
[Adaptados para mobile banking]

## Sequência de Execução
[Ordem lógica considerando dependências]
```

### 2. Casos de Teste Individuais (6 casos total)
- **3 casos do Testador A** (foco em segurança)
- **3 casos do Testador B** (foco em negócio)
- Cada caso deve seguir template completo da aula

### 3. Casos de Teste Integrados (2 casos)
- **CT_INT_001:** Fluxo completo de transferência com autenticação
- **CT_INT_002:** Detecção de fraude durante transação

### 4. Matriz de Rastreabilidade Regulatória
- Mapeamento regulamentação → risco → teste → evidência
- Pelo menos 10 linhas completas
- Status de conformidade atualizado

---

## 📊 Critérios de Avaliação

| **Aspecto** | **Peso** | **Critérios de Excelência** |
|-------------|----------|----------------------------|
| **🎯 Análise de Riscos** | 25% | Identificação precisa, priorização justificada, consideração de contexto mobile banking |
| **🔧 Qualidade dos Casos** | 25% | Casos detalhados, executáveis, alinhados com riscos, cobertura adequada |
| **🤝 Colaboração** | 25% | Divisão eficiente, sincronização produtiva, integração bem-sucedida |
| **📋 Compliance** | 25% | Rastreabilidade regulatória correta, evidências apropriadas, conformidade validada |

### Rubrica Detalhada

**🌟 Excelente (9-10 pontos):**
- Análise de riscos abrangente e estratégica
- Casos de teste detalhados e profissionais
- Colaboração fluida com excelente integração
- Matriz de compliance completa e precisa

**✅ Bom (7-8 pontos):**
- Boa identificação de riscos principais
- Casos adequados com detalhamento suficiente
- Colaboração efetiva com boa divisão
- Rastreabilidade correta com pequenas lacunas

**⚠️ Satisfatório (5-6 pontos):**
- Riscos básicos identificados
- Casos funcionais mas com lacunas
- Colaboração superficial
- Compliance parcial

---

## 💡 Dicas para Sucesso

### 🔒 **Para Casos de Segurança:**
- Considere diferentes vetores de ataque (OWASP Mobile Top 10)
- Valide não apenas a detecção, mas a resposta adequada
- Inclua cenários de engenharia social
- Teste em diferentes dispositivos e versões OS

### 💰 **Para Casos de Negócio:**
- Simule cenários reais de uso bancário
- Considere diferentes perfis de cliente
- Teste limites e exceções regulamentares
- Valide cálculos financeiros com precisão

### 🤝 **Para Colaboração Efetiva:**
- Definam nomenclatura padrão desde o início
- Usem templates consistentes
- Documentem dependências claramente
- Façam revisão cruzada dos casos críticos

### 📱 **Específico para Mobile Banking:**
- Teste em modo avião/conectividade limitada
- Valide comportamento durante chamadas
- Considere acessibilidade (VoiceOver, TalkBack)
- Teste rotação de tela e diferentes tamanhos

---

## 🔍 Extensões e Desafios Extras

**Para duplas que finalizarem antes do tempo:**

### 🚀 **Desafio 1: Automação**
Definam quais casos podem ser automatizados e criem pseudocódigo para automação dos casos críticos.

### 📈 **Desafio 2: Métricas Avançadas**
Proponham métricas específicas para mobile banking (ex: taxa de abandono em transações, tempo médio por operação).

### 🌐 **Desafio 3: Cenários Internacionais**
Adaptem os casos para funcionamento internacional (diferentes moedas, regulamentações, fusos horários).

### 🔮 **Desafio 4: Futuro da Tecnologia**
Considerem como Open Banking e PIX 2.0 impactariam os casos de teste criados.

---

## ❓ FAQ - Dúvidas Frequentes

**Q: Como priorizar entre segurança e usabilidade?**
A: Para mobile banking, segurança sempre prevalece, mas busquem soluções que não comprometam excessivamente a experiência do usuário.

**Q: Que evidências são necessárias para compliance?**
A: Screenshots, logs do sistema, certificados de teste, relatórios de ferramentas automatizadas e documentação detalhada.

**Q: Como testar sem acesso ao sistema real?**
A: Criem casos baseados em especificações, usem protótipos quando disponíveis, e foquem na estrutura e critérios dos testes.

**Q: E se não conhecemos todas as regulamentações?**
A: Concentrem-se nas principais (BACEN, LGPD) e indiquem onde buscariam informações adicionais para regulamentações específicas.

---

## 📚 Recursos de Apoio

### Regulamentações Relevantes:
- **BACEN:** Resolução 4.595 (autenticação), Circular 3.909 (limites)
- **LGPD:** Artigos 46-49 (proteção de dados)
- **PCI-DSS:** Padrões de segurança para dados de cartão

### Ferramentas Sugeridas:
- **OWASP ZAP:** Para testes de segurança
- **JMeter:** Para testes de performance
- **TestLink:** Para gestão de casos de teste
- **Confluence:** Para documentação colaborativa

### Templates de Apoio:
```markdown
## Template de Caso de Teste Segurança
**ID:** CT_SEC_XXX
**Vetor de Ataque:** [OWASP categoria]
**Impacto:** [Baixo/Médio/Alto/Crítico]
**Probabilidade:** [Baixa/Média/Alta]
**Evidência Necessária:** [Logs, screenshots, certificados]
```

---

**💪 Lembrem-se:** Vocês estão protegendo milhões de usuários e bilhões em transações. A qualidade do trabalho de vocês impacta diretamente a confiança no sistema financeiro!
