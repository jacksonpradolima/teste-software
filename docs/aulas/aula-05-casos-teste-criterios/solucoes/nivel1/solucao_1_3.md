# Solução: Exercício 1.3 - Formulário de Contato 🔵

**Exercício:** Definição de Critérios de Teste e Rastreabilidade  
**Nível:** Básico (Individual)  
**Tempo de Resolução:** 25 minutos  
**Conceitos:** Critérios de entrada/saída, cobertura, rastreabilidade  

---

## 📋 Solução de Referência

### Parte A: Critérios de Teste Definidos

#### 🚀 **Critérios de Entrada**

| **Categoria** | **Critério** | **Descrição** | **Verificação** |
|---------------|--------------|---------------|-----------------|
| **Ambiente** | Formulário acessível | Sistema web funcionando em navegadores principais | Teste de acesso manual |
| **Dados** | Casos de teste preparados | Pelo menos 10 cenários diferentes documentados | Revisão da documentação |
| **Funcional** | Validações ativas | Campos obrigatórios e opcionais identificados | Análise da especificação |
| **Técnico** | Environment estável | Ambiente de teste sem alterações pendentes | Validação com DevOps |

#### 🎯 **Critérios de Cobertura**

| **Tipo de Cobertura** | **Meta** | **Medição** | **Justificativa** |
|-----------------------|----------|-------------|-------------------|
| **Campos Obrigatórios** | 100% | Todos os 4 campos testados | Funcionalidade crítica |
| **Validações de Formato** | 100% | Email, telefone validados | Qualidade dos dados |
| **Cenários de Erro** | 80% | Principais erros cobertos | Robustez do sistema |
| **Tipos de Usuário** | 100% | Pessoa física e jurídica | Completude funcional |
| **Navegadores** | 85% | Chrome, Firefox, Safari | Compatibilidade básica |

#### ✅ **Critérios de Saída**

| **Categoria** | **Critério** | **Threshold** | **Medição** |
|---------------|--------------|---------------|-------------|
| **Execução** | Casos executados | ≥ 95% | 19 de 20 casos executados |
| **Sucesso** | Taxa de aprovação | ≥ 90% | 18 de 20 casos passaram |
| **Defeitos** | Bugs críticos | 0 | Zero defeitos bloqueadores |
| **Defeitos** | Bugs altos | ≤ 2 | Máximo 2 defeitos de alta prioridade |
| **Performance** | Tempo de resposta | < 3 segundos | Submissão em tempo aceitável |
| **Usabilidade** | Aprovação UX | ≥ 8/10 | Avaliação de usabilidade positiva |

---

### Parte B: Casos de Teste Detalhados

#### CT001 - Envio Bem-sucedido com Dados Válidos

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT001 |
| **Título** | Envio bem-sucedido de formulário com todos os dados válidos |
| **Requisito** | RF001 - Captura de dados de contato |
| **Tipo** | Positivo |
| **Prioridade** | Crítica |

**Objetivo:** Validar que usuários conseguem enviar mensagens através do formulário quando todos os dados estão corretos e completos.

**Dados de Teste:**
```
Nome: Maria Oliveira Santos
Email: maria.santos@empresa.com.br
Telefone: (11) 99999-8888
Mensagem: Gostaria de receber mais informações sobre os serviços oferecidos pela empresa. Aguardo retorno.
```

**Passos:**
1. Acessar página com formulário de contato
2. Preencher campo "Nome" com "Maria Oliveira Santos"
3. Preencher campo "Email" com "maria.santos@empresa.com.br"
4. Preencher campo "Telefone" com "(11) 99999-8888"
5. Preencher campo "Mensagem" com texto da especificação
6. Clicar no botão "Enviar"

**Resultado Esperado:**
- Mensagem de sucesso exibida: "Mensagem enviada com sucesso!"
- Email de confirmação enviado ao usuário
- Dados salvos no banco de dados
- Formulário limpo para nova submissão
- Redirecionamento para página de agradecimento

---

#### CT002 - Validação de Email Inválido

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT002 |
| **Título** | Validação de formato de email inválido |
| **Requisito** | RNF002 - Validação de email |
| **Tipo** | Negativo |
| **Prioridade** | Alta |

**Objetivo:** Verificar que o sistema rejeita emails em formato inválido, exibindo mensagem de erro clara sem processar a submissão.

**Dados de Teste:**
```
Nome: João Silva
Email: joao.email.invalido  (sem @ e domínio)
Telefone: (11) 98765-4321
Mensagem: Teste de validação de email
```

**Passos:**
1. Acessar página com formulário de contato
2. Preencher todos os campos conforme especificado
3. Clicar no botão "Enviar"

**Resultado Esperado:**
- Mensagem de erro no campo email: "Por favor, insira um email válido"
- Campo email destacado com borda vermelha
- Submissão não é processada
- Usuário permanece na página
- Outros campos mantêm valores preenchidos
- Foco retorna ao campo email

---

#### CT003 - Campo Obrigatório Vazio

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT003 |
| **Título** | Tentativa de envio com campo obrigatório em branco |
| **Requisito** | RNF001 - Campos obrigatórios |
| **Tipo** | Negativo |
| **Prioridade** | Alta |

**Objetivo:** Validar que o sistema impede submissão quando campos obrigatórios estão vazios.

**Dados de Teste:**
```
Nome: (vazio)
Email: usuario@teste.com
Telefone: (11) 12345-6789
Mensagem: Mensagem de teste
```

**Passos:**
1. Acessar página com formulário
2. Deixar campo "Nome" vazio
3. Preencher os demais campos
4. Clicar em "Enviar"

**Resultado Esperado:**
- Mensagem de erro: "Nome é obrigatório"
- Campo nome destacado com indicação visual de erro
- Submissão bloqueada
- Foco direcionado ao campo nome
- Demais campos mantêm valores

---

#### CT004 - Limite de Caracteres na Mensagem

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT004 |
| **Título** | Teste de limite máximo de caracteres no campo mensagem |
| **Requisito** | RNF003 - Limite de caracteres |
| **Tipo** | Limite |
| **Prioridade** | Média |

**Objetivo:** Verificar comportamento do sistema quando mensagem atinge limite máximo de caracteres permitidos.

**Dados de Teste:**
```
Nome: Testador Sistema
Email: teste@sistema.com
Telefone: (11) 11111-1111
Mensagem: [String com exatamente 500 caracteres - assumindo limite de 500]
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis."
```

**Passos:**
1. Acessar formulário
2. Preencher campos básicos
3. Colar texto de 500 caracteres no campo mensagem
4. Verificar comportamento do contador (se houver)
5. Tentar digitar caracteres adicionais
6. Submeter formulário

**Resultado Esperado:**
- Texto aceito até o limite (500 caracteres)
- Contador de caracteres mostra 500/500 (se implementado)
- Caracteres adicionais são bloqueados ou cortados
- Submissão funciona normalmente
- Mensagem completa é processada

---

#### CT005 - Caracteres Especiais na Mensagem

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT005 |
| **Título** | Processamento de caracteres especiais e acentos |
| **Requisito** | RNF004 - Suporte a caracteres especiais |
| **Tipo** | Positivo |
| **Prioridade** | Média |

**Objetivo:** Validar que o sistema processa corretamente caracteres especiais, acentos e símbolos comuns na língua portuguesa.

**Dados de Teste:**
```
Nome: José da Conceição
Email: jose.conceicao@teste.com.br
Telefone: (11) 99999-0000
Mensagem: Olá! Tenho dúvidas sobre os preços & condições de pagamento. Meu orçamento é R$ 1.500,00. Vocês aceitam cartão de crédito? Aguardo retorno. Atenciosamente, José.
```

**Passos:**
1. Acessar formulário
2. Preencher todos os campos com dados especificados
3. Submeter formulário
4. Verificar confirmação de recebimento

**Resultado Esperado:**
- Todos os caracteres especiais (ç, ã, !, &, $, etc.) são aceitos
- Acentos mantidos corretamente
- Símbolos de moeda e pontuação preservados
- Submissão processada com sucesso
- Dados armazenados sem corrupção de caracteres

---

### Parte C: Matriz de Rastreabilidade

#### 📊 **Matriz Requisitos × Casos de Teste**

| **ID Requisito** | **Descrição do Requisito** | **Casos de Teste** | **Cobertura** | **Status** |
|------------------|----------------------------|-------------------|---------------|------------|
| **RF001** | Sistema deve capturar nome, email, telefone e mensagem | CT001, CT003 | 100% | ✅ Coberto |
| **RF002** | Sistema deve confirmar envio ao usuário | CT001 | 100% | ✅ Coberto |
| **RF003** | Sistema deve armazenar dados para análise | CT001, CT005 | 100% | ✅ Coberto |
| **RNF001** | Campos nome e email são obrigatórios | CT003 | 100% | ✅ Coberto |
| **RNF002** | Email deve ter formato válido | CT002 | 100% | ✅ Coberto |
| **RNF003** | Mensagem limitada a 500 caracteres | CT004 | 100% | ✅ Coberto |
| **RNF004** | Suporte a caracteres especiais pt-BR | CT005 | 100% | ✅ Coberto |

#### 📈 **Análise de Cobertura Detalhada**

| **Categoria** | **Total de Itens** | **Itens Cobertos** | **% Cobertura** | **Gaps Identificados** |
|---------------|-------------------|-------------------|-----------------|------------------------|
| **Requisitos Funcionais** | 3 | 3 | 100% | Nenhum |
| **Requisitos Não-Funcionais** | 4 | 4 | 100% | Nenhum |
| **Campos do Formulário** | 4 | 4 | 100% | Nenhum |
| **Tipos de Validação** | 3 | 3 | 100% | Nenhum |
| **Cenários de Erro** | 2 | 2 | 100% | Nenhum |

#### 🔍 **Rastreabilidade Reversa (Casos → Requisitos)**

| **Caso de Teste** | **Requisitos Validados** | **Tipo de Validação** | **Criticidade** |
|------------------|---------------------------|----------------------|-----------------|
| **CT001** | RF001, RF002, RF003 | Funcional principal | Crítica |
| **CT002** | RNF002 | Validação de formato | Alta |
| **CT003** | RNF001 | Validação obrigatória | Alta |
| **CT004** | RNF003 | Limite de sistema | Média |
| **CT005** | RNF004 | Suporte internacional | Média |

---

### Parte D: Análise de Critérios Aplicados

#### ✅ **Adequação dos Critérios Definidos**

**Critérios de Entrada - Análise:**
- ✅ **Completos:** Cobrem aspectos técnicos, funcionais e ambientais
- ✅ **Mensuráveis:** Cada critério tem verificação específica
- ✅ **Realistas:** Factíveis dentro do contexto do projeto
- ⚠️ **Melhoria:** Poderia incluir critérios de segurança (HTTPS, sanitização)

**Critérios de Cobertura - Análise:**
- ✅ **Abrangentes:** Incluem aspectos funcionais e técnicos
- ✅ **Quantificados:** Percentuais específicos definidos
- ✅ **Priorizados:** Metas mais altas para aspectos críticos
- ⚠️ **Melhoria:** Poderia incluir cobertura de acessibilidade

**Critérios de Saída - Análise:**
- ✅ **Balanceados:** Incluem qualidade, execução e performance
- ✅ **Específicos:** Thresholds numéricos claros
- ✅ **Realistas:** Metas atingíveis mas desafiadoras
- ⚠️ **Melhoria:** Poderia incluir critérios de documentação

#### 📊 **Eficácia da Rastreabilidade**

**Pontos Fortes:**
1. **Cobertura Completa:** 100% dos requisitos cobertos
2. **Bidirecional:** Requisitos → Casos e Casos → Requisitos
3. **Categorizada:** Distinção clara entre funcional e não-funcional
4. **Priorizada:** Casos críticos identificados

**Oportunidades de Melhoria:**
1. **Granularidade:** Poderia mapear sub-requisitos
2. **Histórico:** Incluir evolução dos requisitos
3. **Automação:** Links automatizados entre artefatos
4. **Métricas:** KPIs de qualidade da rastreabilidade

---

## 🎯 Aspectos Destacados da Solução

### 🏆 **Qualidades Exemplares:**

1. **Critérios SMART:**
   - **S**pecíficos: Cada critério tem definição clara
   - **M**ensuráveis: Métricas quantificáveis
   - **A**tingíveis: Metas realistas
   - **R**elevantes: Alinhados com objetivos
   - **T**emporais: Aplicáveis ao contexto do projeto

2. **Casos de Teste Robustos:**
   - Dados realistas e variados
   - Passos detalhados e executáveis
   - Resultados esperados específicos
   - Cobertura equilibrada de cenários

3. **Rastreabilidade Profissional:**
   - Mapeamento completo e bidirecional
   - Análise de gaps transparente
   - Categorização clara e útil
   - Facilita auditoria e manutenção

### 📈 **Métricas de Qualidade Atingidas:**

- **Cobertura de Requisitos:** 100%
- **Diversidade de Tipos:** 60% Positivos, 40% Negativos
- **Clareza de Critérios:** Alta (critérios específicos e mensuráveis)
- **Executabilidade:** Alta (passos detalhados)
- **Rastreabilidade:** Completa (bilateral)

---

## 💡 Variações e Extensões

### 🔄 **Critérios Alternativos Válidos:**

**Critérios de Entrada Adicionais:**
- Aprovação do plano de teste por stakeholders
- Disponibilidade de dados de teste representativos
- Configuração de ferramentas de automação
- Treinamento da equipe de teste concluído

**Critérios de Cobertura Estendidos:**
- Cobertura de dispositivos móveis (70%)
- Cobertura de acessibilidade WCAG (80%)
- Cobertura de cenários de segurança (90%)
- Cobertura de performance em diferentes loads (75%)

**Critérios de Saída Mais Rigorosos:**
- Zero defeitos de qualquer prioridade
- Aprovação formal de usuários finais
- Documentação 100% atualizada
- Plano de rollback testado e aprovado

### 🔄 **Casos de Teste Complementares:**

- **CT006:** Teste de acessibilidade (navegação por teclado)
- **CT007:** Comportamento em dispositivos móveis
- **CT008:** Teste de segurança (injection attacks)
- **CT009:** Performance com múltiplas submissões simultâneas
- **CT010:** Recuperação após perda de conexão

---

## ⚠️ **Armadilhas Evitadas**

### ❌ **Erros Comuns em Critérios:**

1. **Critérios Vagos:**
   ```
   ❌ "Sistema deve funcionar bem"
   ✅ "95% dos casos de teste executados com sucesso"
   ```

2. **Metas Irrealistas:**
   ```
   ❌ "100% de cobertura de código"
   ✅ "80% de cobertura dos módulos críticos"
   ```

3. **Falta de Mensuração:**
   ```
   ❌ "Boa performance"
   ✅ "Resposta em menos de 3 segundos"
   ```

### ❌ **Problemas de Rastreabilidade:**

1. **Mapeamento Incompleto:**
   ```
   ❌ Alguns requisitos sem casos de teste
   ✅ 100% dos requisitos cobertos
   ```

2. **Granularidade Inconsistente:**
   ```
   ❌ Misturar níveis de detalhe
   ✅ Nível consistente de mapeamento
   ```

3. **Falta de Manutenção:**
   ```
   ❌ Matriz desatualizada
   ✅ Processo de atualização definido
   ```

---

## 📚 Recursos para Evolução

### 📖 **Conceitos Avançados:**
- **Criteria-based Testing:** Desenvolvimento de critérios mais sofisticados
- **Traceability Matrix Management:** Ferramentas e processos para grandes projetos
- **Risk-based Testing:** Critérios baseados em análise de risco
- **Metrics-driven Testing:** KPIs avançados para qualidade de teste

### 🛠️ **Ferramentas Recomendadas:**
- **JIRA + Zephyr:** Para rastreabilidade automatizada
- **TestLink:** Para gestão de casos e rastreabilidade
- **Azure DevOps:** Para integração completa de artefatos
- **Confluence:** Para documentação colaborativa de critérios

### 🎯 **Próximos Desafios:**
- Aplicar critérios em sistemas mais complexos
- Desenvolver critérios para testes automatizados
- Integrar critérios com metodologias ágeis
- Criar métricas de qualidade para critérios de teste

**Parabéns! Você dominou os fundamentos de critérios e rastreabilidade. Continue praticando em contextos cada vez mais complexos!** 🎓✨
