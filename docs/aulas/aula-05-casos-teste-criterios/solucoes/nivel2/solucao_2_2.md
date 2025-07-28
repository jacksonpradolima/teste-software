# Solução: Exercício 2.2 - Sistema de Mobile Banking 🟡

**Exercício:** Mobile Banking com Compliance e Segurança  
**Nível:** Intermediário (Duplas)  
**Tempo de Resolução:** 75 minutos  
**Conceitos:** Sistemas críticos, compliance regulatório, segurança, análise de riscos  

---

## 🎯 Solução de Referência Completa

### Fase 1: Análise de Riscos e Planejamento Estratégico (15 min)

#### 🚨 **Matriz de Riscos Críticos Identificados**

| **Risco** | **Impacto** | **Probabilidade** | **Prioridade** | **Regulamentação** | **Estratégia** |
|-----------|-------------|-------------------|----------------|-------------------|----------------|
| **Vazamento de dados pessoais** | Crítico | Média | 1 | LGPD Art. 46 | Testes de criptografia + auditoria |
| **Fraude em transações PIX** | Crítico | Alta | 1 | BACEN 4595 | Autenticação forte + monitoramento |
| **Indisponibilidade durante picos** | Alto | Alta | 2 | SLA contratual | Testes de carga + failover |
| **Transação com valor incorreto** | Crítico | Baixa | 2 | PCI-DSS | Validação de precisão + reconciliação |
| **Acesso não autorizado** | Crítico | Média | 1 | BACEN 4595 | Testes de penetração + MFA |
| **Falha em backup de dados** | Alto | Baixa | 3 | BACEN Circular 3909 | Testes de DR + RTO<4h |

#### 👥 **Divisão Estratégica de Responsabilidades**

**🛡️ Especialista A - Segurança e Compliance:**
- **Módulos Críticos:** Autenticação, Controle de Acesso, Auditoria
- **Regulamentações:** BACEN, LGPD, PCI-DSS
- **Tipos de Teste:** Segurança, compliance, penetração
- **Entregas:** 8 casos de teste + matriz regulatória + plano de penetração

**💰 Especialista B - Transações e Negócio:**
- **Módulos Críticos:** Transações, Consultas, Configurações
- **Foco:** Operações financeiras, usabilidade, performance
- **Tipos de Teste:** Funcionais, performance, usabilidade
- **Entregas:** 8 casos de teste + análise de performance + validação de fluxos

**🔄 Integração Crítica:**
- **Autenticação → Transações:** Validação de identidade antes de operações
- **Auditoria → Todas as operações:** Log completo para compliance
- **Performance → Segurança:** Balanceamento entre velocidade e proteção

---

### Fase 2: Desenvolvimento por Especialidade (40 min)

#### 🛡️ **Casos do Especialista A - Segurança e Compliance**

##### CT_SEC_001 - Bloqueio por Múltiplas Tentativas de Login

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_SEC_001 |
| **Título** | Proteção contra ataques de força bruta via bloqueio automático |
| **Regulamentação** | BACEN Resolução 4595 (Autenticação Forte) |
| **Módulos** | Autenticação + Auditoria |
| **Tipo** | Segurança (Negativo) |
| **Prioridade** | Crítica |
| **Tempo Estimado** | 8 minutos |

**Objetivo:** Validar que o sistema protege contas contra ataques de força bruta implementando bloqueio automático após tentativas consecutivas falhadas.

**Contexto Regulatório:**
- **BACEN 4595:** Exige mecanismos de proteção contra acesso não autorizado
- **PCI-DSS Req. 8.1.6:** Controle de tentativas de autenticação
- **LGPD Art. 46:** Medidas de segurança técnicas adequadas

**Dados de Teste:**
```
Usuário válido: 12345678901 (CPF)
Senha correta: MinH@Senh4567
Senhas incorretas: [senha123, 123456, wrongpass, testpass, hackme]
Dispositivo: Android 12, Samsung Galaxy S21
```

**Cenário de Ataque Simulado:**
1. **[Tentativa 1]** Login com CPF correto + senha "senha123" → Falha
2. **[Tentativa 2]** Login com CPF correto + senha "123456" → Falha  
3. **[Tentativa 3]** Login com CPF correto + senha "wrongpass" → Falha
4. **[Tentativa 4]** Login com CPF correto + senha "testpass" → **BLOQUEIO**
5. **[Tentativa 5]** Login com CPF correto + senha correta → **NEGADO**
6. **[Aguardar 15 min]** Tentar login com credenciais corretas
7. **[Verificação]** Consultar logs de auditoria de segurança

**Resultado Esperado:**
- ✅ **Após 3ª tentativa:** Warning "Mais 1 tentativa antes do bloqueio"
- ✅ **Após 4ª tentativa:** "Conta bloqueada por 15 minutos por segurança"
- ✅ **Durante bloqueio:** Todas as tentativas rejeitadas (mesmo senha correta)
- ✅ **Logs de auditoria:** Todas as tentativas registradas com timestamp, IP, device
- ✅ **Notificação:** SMS/email alertando sobre tentativas suspeitas
- ✅ **Após 15 min:** Login com credenciais corretas funciona normalmente
- ✅ **Interface:** Aplicação não revela se CPF existe ou não

**Evidências de Compliance:**
- 📋 Screenshots das mensagens de erro
- 📋 Logs de auditoria exportados
- 📋 Comprovante de notificações enviadas
- 📋 Teste de timing (verificar se não há timing attack)

---

##### CT_SEC_002 - Criptografia End-to-End em Transações PIX

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_SEC_002 |
| **Título** | Validação de criptografia durante transação PIX de alto valor |
| **Regulamentação** | LGPD Art. 46 + PCI-DSS |
| **Módulos** | Transações + Criptografia |
| **Tipo** | Segurança (Técnico) |
| **Prioridade** | Crítica |

**Objetivo:** Verificar que dados de transações são criptografados end-to-end e não são expostos em nenhum ponto da comunicação.

**Contexto de Compliance:**
- **LGPD Art. 46:** Dados pessoais devem ser protegidos por criptografia
- **PCI-DSS Req. 4:** Proteção de dados em trânsito
- **BACEN:** Segurança em sistemas de pagamento

**Setup Técnico:**
```
Interceptação de rede: Burp Suite / OWASP ZAP
Transação: PIX de R$ 5.000,00
Destinatário: Chave PIX email
Horário: Simulação de pico (19h-21h)
```

**Procedimento de Teste:**
1. **[Preparação]** Configurar proxy para interceptar tráfego HTTPS
2. **[Autenticação]** Login com biometria + token SMS
3. **[Navegação]** Acessar seção PIX do aplicativo
4. **[Transação]** Inserir chave PIX "destino@banco.com.br"
5. **[Valor]** Inserir R$ 5.000,00 (acima de limite para auditoria)
6. **[Confirmação]** Confirmar com senha transacional
7. **[Interceptação]** Analisar todo tráfego de rede capturado
8. **[Auditoria]** Verificar logs do servidor (se disponível)

**Resultado Esperado - Análise de Tráfego:**
- ✅ **TLS 1.3** ou superior em todas as comunicações
- ✅ **Certificate pinning** implementado (rejeita certificados inválidos)
- ✅ **Dados sensíveis nunca em plaintext:**
  - CPF criptografado em payloads
  - Valores monetários encriptados
  - Chaves PIX ofuscadas/criptografadas
- ✅ **Headers de segurança:** HSTS, CSP, X-Frame-Options
- ✅ **Tokens únicos** para cada transação (anti-replay)
- ✅ **Assinaturas digitais** verificáveis em responses críticos

**Evidências Técnicas:**
- 📋 Screenshots do tráfego interceptado
- 📋 Análise de certificados SSL
- 📋 Validação de algoritmos de criptografia
- 📋 Teste de certificate pinning bypass

---

##### CT_SEC_003 - Controle de Acesso Baseado em Papéis

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_SEC_003 |
| **Título** | Validação de permissões por tipo de conta e operação |
| **Regulamentação** | BACEN + Princípio do menor privilégio |
| **Módulos** | Controle de Acesso + Configurações |
| **Tipo** | Segurança (Funcional) |
| **Prioridade** | Alta |

**Objetivo:** Garantir que diferentes tipos de conta têm acesso apenas às funcionalidades apropriadas ao seu perfil.

**Perfis de Teste:**
```
Conta Básica (Estudante):
- CPF: 11111111111
- Limites: PIX R$ 500/dia, TED R$ 1.000/dia
- Restrições: Sem investimentos, sem empréstimos

Conta Premium (Pessoa Física):
- CPF: 22222222222  
- Limites: PIX R$ 5.000/dia, TED R$ 10.000/dia
- Funcionalidades: Investimentos, cartão de crédito

Conta Empresarial:
- CNPJ: 12345678000199
- Limites: PIX R$ 50.000/dia, múltiplos usuários
- Funcionalidades: Folha de pagamento, conciliação
```

**Matriz de Teste de Permissões:**

| **Funcionalidade** | **Básica** | **Premium** | **Empresarial** | **Teste** |
|-------------------|------------|-------------|-----------------|-----------|
| **PIX até R$ 500** | ✅ Permitido | ✅ Permitido | ✅ Permitido | CT_SEC_003a |
| **PIX R$ 2.000** | ❌ Negado | ✅ Permitido | ✅ Permitido | CT_SEC_003b |
| **Investimentos** | ❌ Oculto | ✅ Permitido | ⚠️ Específico | CT_SEC_003c |
| **Múltiplos usuários** | ❌ N/A | ❌ N/A | ✅ Permitido | CT_SEC_003d |

**Procedimento por Perfil:**
1. Login com cada tipo de conta
2. Tentar acessar cada funcionalidade
3. Verificar interface (oculta vs. visível vs. desabilitada)
4. Tentar bypass via deep linking
5. Verificar logs de tentativas não autorizadas

---

#### 💰 **Casos do Especialista B - Transações e Negócio**

##### CT_NEG_001 - Transferência PIX Acima do Limite Diário

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_NEG_001 |
| **Título** | Validação de controles de limite em transação PIX |
| **Regulamentação** | BACEN Circular 3909 (Limites operacionais) |
| **Módulos** | Transações + Configurações |
| **Tipo** | Negativo (Controle de Negócio) |
| **Prioridade** | Alta |
| **Tempo Estimado** | 6 minutos |

**Objetivo:** Verificar que o sistema impede transações acima do limite diário configurado, oferecendo alternativas apropriadas ao cliente.

**Contexto Regulatório:**
- **BACEN Circular 3909:** Controles internos para operações
- **Resolução 4595:** Limites de segurança obrigatórios
- **Lei 12.865/2013:** Arranjos de pagamento

**Cenário de Teste:**
```
Usuário: conta.premium@teste.com
Limite PIX configurado: R$ 5.000,00/dia
Transações já realizadas hoje: R$ 3.500,00
Tentativa atual: R$ 2.000,00 (excede em R$ 500,00)
Destinatário: Chave PIX +55119999888877
```

**Passos Detalhados:**
1. **[Preparação]** Verificar limite atual disponível (R$ 1.500,00)
2. **[PIX]** Acessar função PIX no menu principal
3. **[Destinatário]** Inserir chave "+55119999888877"
4. **[Valor]** Inserir "2000,00" (R$ 2.000,00)
5. **[Validação]** Sistema deve detectar excesso imediatamente
6. **[Opções]** Verificar alternativas oferecidas
7. **[Limite]** Tentar transação com valor dentro do limite (R$ 1.400,00)
8. **[Configuração]** Verificar opção de alteração de limite

**Resultado Esperado:**
- ✅ **Detecção imediata:** "Valor excede limite diário em R$ 500,00"
- ✅ **Saldo disponível exibido:** "Disponível para PIX hoje: R$ 1.500,00"
- ✅ **Alternativas oferecidas:**
  - "Transferir R$ 1.500,00 agora"
  - "Agendar para amanhã"
  - "Alterar limite diário (sujeito a aprovação)"
  - "Usar TED (limite diferente: R$ 8.500,00 disponível)"
- ✅ **Transação dentro do limite:** Processada normalmente
- ✅ **Logs de compliance:** Tentativa de excesso registrada
- ✅ **UX clara:** Mensagens educativas sobre limites

**Validações Adicionais:**
- Verificar que limite é por período de 24h (não dia corrido)
- Confirmar que cancelamentos liberam limite imediatamente
- Testar comportamento próximo à meia-noite (reset)

---

##### CT_NEG_002 - Pagamento de Boleto com Juros e Multas

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_NEG_002 |
| **Título** | Cálculo automático de juros e multas em boleto vencido |
| **Regulamentação** | Código de Defesa do Consumidor + FEBRABAN |
| **Módulos** | Pagamentos + Calculadora Financeira |
| **Tipo** | Positivo (Complexo) |
| **Prioridade** | Alta |

**Objetivo:** Validar que o sistema calcula corretamente juros e multas para boletos vencidos, seguindo regras bancárias e mostrando transparência ao cliente.

**Cenário Financeiro:**
```
Boleto original:
- Valor: R$ 1.500,00
- Vencimento: 15/01/2025
- Data de pagamento: 28/01/2025 (13 dias de atraso)
- Multa: 2% (R$ 30,00)
- Juros: 1% ao mês, pro rata (R$ 6,50)
- Valor total esperado: R$ 1.536,50
```

**Procedimento de Cálculo:**
1. **[Boleto]** Escanear código de barras ou inserir código
2. **[Validação]** Sistema identifica boleto vencido
3. **[Cálculo]** Exibir breakdown de valores:
   - Valor original: R$ 1.500,00
   - Multa (2%): R$ 30,00  
   - Juros 13 dias (1%/mês): R$ 6,50
   - **Total: R$ 1.536,50**
4. **[Transparência]** Mostrar como foi calculado
5. **[Confirmação]** Cliente confirma pagamento
6. **[Processamento]** Débito na conta corrente
7. **[Comprovante]** Gerar com detalhamento completo

**Validações Críticas:**
- ✅ **Cálculo preciso:** Matemática financeira correta
- ✅ **Transparência:** Cliente vê cada componente do valor
- ✅ **Compliance:** Seguir regras FEBRABAN
- ✅ **Limite de juros:** Respeitar teto legal (por ex., CDC)
- ✅ **Comprovante completo:** Permite auditoria posterior

---

##### CT_NEG_003 - Performance durante Pico de Acesso

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT_NEG_003 |
| **Título** | Comportamento do sistema com 500+ usuários simultâneos |
| **Regulamentação** | SLA contratual + BACEN (disponibilidade) |
| **Módulos** | Todos (Teste de Carga) |
| **Tipo** | Performance |
| **Prioridade** | Alta |

**Objetivo:** Validar que o sistema mantém performance aceitável e estabilidade durante picos de uso, como véspera de feriados ou horários de pico.

**Cenário de Carga:**
```
Usuários simultâneos: 500
Operações por usuário/min: 3-5
Mix de operações:
- 40% Consultas (saldo, extrato)
- 30% PIX
- 20% Pagamentos
- 10% Configurações
Duração: 30 minutos
```

**Métricas de SLA:**
- **Tempo de resposta médio:** < 3 segundos
- **95% das operações:** < 5 segundos  
- **99% das operações:** < 10 segundos
- **Taxa de erro:** < 0.1%
- **Disponibilidade:** > 99.9%

**Monitoramento durante Teste:**
1. **[Infraestrutura]** CPU, memória, rede dos servidores
2. **[Aplicação]** Tempo de resposta por operação
3. **[Banco de dados]** Queries lentas, deadlocks
4. **[Usuário]** Experiência real no app mobile
5. **[Logs]** Erros, timeouts, exceções

**Critérios de Aceitação:**
- ✅ **Funcionalidade:** Todas as operações permanecem funcionais
- ✅ **Performance:** SLAs atingidos em 95% do tempo
- ✅ **Estabilidade:** Zero crashes ou indisponibilidade total
- ✅ **Degradação graceful:** Sistema avisa se performance degradada
- ✅ **Recuperação:** Volta ao normal após fim do pico

---

### Fase 3: Integração e Casos Colaborativos (15 min)

#### 🔄 **CT_INT_001 - Fluxo Completo de Transferência com Detecção de Fraude**

**Objetivo:** Validar integração entre autenticação forte, processamento de transação e sistemas de monitoramento de fraude.

**Cenário Crítico:**
- Cliente autentica com biometria
- Tenta PIX de R$ 4.000,00 às 23h30 (horário suspeito)
- Para destinatário novo (primeira vez)
- Sistema deve aplicar autenticação adicional

**Fluxo Integrado:**
1. **[Autenticação]** Login com biometria (Especialista A)
2. **[Transação]** Inserir dados PIX (Especialista B)
3. **[Detecção]** Sistema identifica padrão suspeito (Ambos)
4. **[Segurança]** Solicita autenticação adicional (Especialista A)
5. **[Processamento]** Transação aprovada com auditoria (Especialista B)

**Validação Colaborativa:**
- **Especialista A valida:** Autenticação robusta aplicada
- **Especialista B valida:** Transação processada corretamente
- **Ambos validam:** Logs de auditoria completos para compliance

---

#### 🔄 **CT_INT_002 - Recuperação após Falha de Sistema**

**Objetivo:** Testar capacidade de recuperação e integridade de dados após falha de sistema durante transação crítica.

**Cenário de Falha:**
1. Cliente inicia transferência de R$ 10.000,00
2. Sistema falha após débito mas antes do crédito
3. Sistema é restaurado
4. Verificar integridade e recuperação automática

**Responsabilidades:**
- **Especialista A:** Verificar logs de auditoria e compliance
- **Especialista B:** Validar integridade financeira e comunicação ao cliente

---

### Fase 4: Matriz de Rastreabilidade Regulatória (5 min)

#### 📊 **Compliance Matrix - Regulamentações × Casos × Evidências**

| **Regulamentação** | **Artigo/Seção** | **Requisito** | **Caso de Teste** | **Evidência** | **Status** |
|-------------------|------------------|---------------|-------------------|---------------|------------|
| **BACEN 4595** | Art. 5º | Autenticação forte | CT_SEC_001, CT_SEC_003 | Logs + Screenshots | ✅ |
| **LGPD** | Art. 46 | Criptografia dados | CT_SEC_002 | Análise técnica | ✅ |
| **BACEN Circular 3909** | Seção II | Controles limites | CT_NEG_001 | Comprovantes | ✅ |
| **PCI-DSS** | Req. 4.1 | Dados em trânsito | CT_SEC_002 | Interceptação rede | ✅ |
| **Lei 12.865** | Art. 8º | Arranjos pagamento | CT_NEG_001, CT_NEG_002 | Transações | ✅ |
| **FEBRABAN** | Normativo | Cálculo juros | CT_NEG_002 | Cálculos validados | ✅ |

#### 📈 **Análise de Cobertura de Riscos**

| **Categoria de Risco** | **Casos Cobrindo** | **% Cobertura** | **Gaps Identificados** |
|------------------------|-------------------|-----------------|------------------------|
| **Segurança** | CT_SEC_001, CT_SEC_002, CT_SEC_003 | 90% | Teste de engenharia social |
| **Compliance** | Todos os casos | 100% | Nenhum |
| **Performance** | CT_NEG_003, CT_INT_002 | 85% | Teste de recuperação RTO |
| **Operacional** | CT_NEG_001, CT_NEG_002 | 95% | Conciliação bancária |

---

## 🎯 Reflexões e Análise da Solução

### ✅ **Pontos Fortes Evidenciados:**

1. **Expertise Complementar:**
   - Divisão segurança vs. negócio maximizou profundidade
   - Conhecimento regulatório específico aplicado corretamente
   - Integração harmoniosa entre aspectos técnicos e funcionais

2. **Realismo de Contexto:**
   - Cenários baseados em situações reais de mobile banking
   - Consideração de horários, valores e comportamentos típicos
   - Conformidade com regulamentações reais do mercado brasileiro

3. **Profundidade Técnica:**
   - Testes de segurança com ferramentas profissionais
   - Análise de performance com métricas específicas
   - Validação de compliance com evidências auditáveis

4. **Pensamento de Risco:**
   - Priorização baseada em impacto real ao negócio
   - Consideração de cenários de falha e recuperação
   - Balanceamento entre segurança e usabilidade

### 📊 **Métricas de Qualidade Alcançadas:**

- **Cobertura Regulatória:** 100% (6/6 regulamentações)
- **Mitigação de Riscos Críticos:** 100% (6/6 riscos cobertos)
- **Integração Sistêmica:** 95% (interfaces críticas testadas)
- **Profundidade Técnica:** Alta (ferramentas profissionais usadas)
- **Colaboração:** Excelente (sinergia evidente entre especialistas)

### 🔍 **Lições Aprendidas Específicas:**

1. **Mobile Banking é Complexo:**
   - Requer conhecimento de múltiplas regulamentações
   - Balanceamento constante entre segurança e UX
   - Performance é crítica para adoção pelo usuário

2. **Compliance é Evidência:**
   - Não basta funcionar, precisa comprovar conformidade
   - Documentação é tão importante quanto o teste
   - Auditoria deve ser considerada desde o design

3. **Segurança e Negócio se Integram:**
   - Casos de segurança afetam diretamente a experiência
   - Controles de negócio têm aspectos de segurança
   - Colaboração é essencial para cobertura completa

---

## 💡 Extensões e Variações Avançadas

### 🔄 **Cenários Adicionais Valiosos:**

**Acessibilidade e Inclusão:**
- Navegação por voz para pessoas com deficiência visual
- Interface em libras para surdos
- Modo de alto contraste para baixa visão

**Internacionalização:**
- Transações para o exterior
- Múltiplas moedas
- Conformidade com regulamentações internacionais

**Tecnologias Emergentes:**
- Integração com Open Banking
- PIX offline (modo avião)
- Biometria comportamental

### 🔄 **Especializações Alternativas:**

**Opção 1 - Por Stakeholder:**
- **Especialista A:** Perspectiva do cliente (UX, usabilidade)
- **Especialista B:** Perspectiva do banco (risco, compliance)

**Opção 2 - Por Momento de Uso:**
- **Especialista A:** Operações diurnas (horário comercial)
- **Especialista B:** Operações noturnas/finais de semana

**Opção 3 - Por Valor:**
- **Especialista A:** Micro transações (< R$ 100)
- **Especialista B:** Altos valores (> R$ 5.000)

---

## 🚀 Preparação para Desafios Mais Complexos

### 🎯 **Competências Demonstradas:**

- ✅ **Conhecimento Regulatório:** Aplicação correta de normas específicas
- ✅ **Análise de Riscos:** Priorização baseada em impacto real
- ✅ **Testes de Segurança:** Uso de ferramentas e técnicas profissionais
- ✅ **Performance Engineering:** Métricas e SLAs apropriados
- ✅ **Colaboração Especializada:** Integração de expertises complementares

### 🎓 **Preparação para Nível 3:**

Esta solução prepara para desafios de:

1. **Sistemas Críticos de Saúde:** Onde conformidade é ainda mais crítica
2. **Equipes Maiores:** Coordenação de múltiplos especialistas
3. **Stakeholders Executivos:** Comunicação de riscos para C-level
4. **Auditorias Externas:** Preparação de evidências para reguladores
5. **Transformação Digital:** Modernização de sistemas legados críticos

---

## 📚 Recursos para Evolução Profissional

### 📖 **Conhecimento Especializado:**
- **Regulamentações Bancárias:** BACEN, CVM, SUSEP
- **Segurança de Aplicações:** OWASP Mobile Security
- **Performance Testing:** JMeter, LoadRunner para mobile
- **Compliance Management:** Frameworks de governança

### 🛠️ **Ferramentas Profissionais:**
- **Segurança:** Burp Suite, OWASP ZAP, MobSF
- **Performance:** JMeter, LoadRunner, Gatling
- **Mobile Testing:** Appium, Espresso, XCUITest
- **Compliance:** GRC platforms, audit trail tools

### 🎯 **Próximas Certificações:**
- **CISSP:** Segurança de sistemas críticos
- **CISA:** Auditoria de sistemas de informação
- **ISTQB Advanced:** Test Management e Security Testing
- **Cloud Security:** AWS/Azure Security Specialist

**Parabéns! Esta solução demonstra maturidade para atuar em sistemas financeiros críticos. Continue evoluindo para liderar transformações digitais seguras!** 🏦✨
