# Solução: Exercício 1.1 - Sistema de Login 🔵

**Exercício:** Sistema de Login com Validação Básica  
**Nível:** Básico (Individual)  
**Tempo de Resolução:** 20 minutos  
**Conceitos:** Estrutura de casos de teste, tipos básicos, critérios simples  

---

## 📋 Solução de Referência

### CT001 - Login Bem-sucedido com Credenciais Válidas

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT001 |
| **Título** | Login bem-sucedido de usuário cadastrado com credenciais válidas |
| **Funcionalidade** | Sistema de Autenticação |
| **Tipo** | Positivo |
| **Prioridade** | Alta |
| **Complexidade** | Básica |

#### Objetivo
Validar que usuários cadastrados conseguem acessar o sistema utilizando email e senha corretos, sendo redirecionados para o dashboard principal.

#### Pré-condições
- Sistema de login acessível e operacional
- Usuário "ana.silva@email.com" previamente cadastrado no sistema
- Senha definida como "MinhaSenh@2024"
- Base de dados operacional

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Email** | ana.silva@email.com | Email válido de usuário existente |
| **Senha** | MinhaSenh@2024 | Senha que atende critérios: 8+ chars, maiúscula, especial |

#### Passos de Execução
1. Abrir navegador e acessar a URL do sistema (ex: https://sistema.empresa.com/login)
2. Verificar se a página de login carregou corretamente (campos Email e Senha visíveis)
3. Inserir "ana.silva@email.com" no campo **Email**
4. Inserir "MinhaSenh@2024" no campo **Senha**
5. Clicar no botão **"Entrar"**

#### Resultado Esperado
- Sistema processa credenciais em tempo razoável (< 3 segundos)
- Usuário é redirecionado para página do dashboard
- Nome do usuário "Ana Silva" aparece na barra superior direita
- Mensagem de boas-vindas é exibida: "Bem-vinda, Ana!"
- URL da página muda para: https://sistema.empresa.com/dashboard
- Não há mensagens de erro visíveis

#### Critérios de Aceitação
- ✅ Autenticação concluída em menos de 3 segundos
- ✅ Redirecionamento correto sem erros de navegação
- ✅ Interface do dashboard carregada completamente
- ✅ Sessão do usuário estabelecida (cookies/tokens criados)

---

### CT002 - Tentativa de Login com Email Inexistente

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT002 |
| **Título** | Tentativa de login com email não cadastrado no sistema |
| **Funcionalidade** | Sistema de Autenticação |
| **Tipo** | Negativo |
| **Prioridade** | Alta |
| **Complexidade** | Básica |

#### Objetivo
Verificar que o sistema rejeita adequadamente tentativas de login com email não cadastrado, exibindo mensagem de erro apropriada sem revelar informações sensíveis.

#### Pré-condições
- Sistema de login acessível e operacional
- Email "usuario.inexistente@test.com" **NÃO** cadastrado no sistema
- Base de dados operacional

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Email** | usuario.inexistente@test.com | Email válido mas não cadastrado |
| **Senha** | QualquerSenh@123 | Senha no formato correto |

#### Passos de Execução
1. Acessar a página de login do sistema
2. Inserir "usuario.inexistente@test.com" no campo **Email**
3. Inserir "QualquerSenh@123" no campo **Senha**
4. Clicar no botão **"Entrar"**

#### Resultado Esperado
- Sistema retorna erro em tempo razoável (< 2 segundos)
- Mensagem de erro genérica exibida: "Email ou senha incorretos"
- Usuário permanece na página de login
- Campos de email e senha são limpos ou mantidos para nova tentativa
- **Não** é revelado se o email existe ou não no sistema
- Nenhum redirecionamento ou acesso é concedido

#### Critérios de Aceitação
- ✅ Mensagem de erro clara mas não específica (segurança)
- ✅ Tempo de resposta similar ao login válido (evita timing attacks)
- ✅ Interface permanece estável e funcional
- ✅ Nenhum acesso não autorizado concedido

---

### CT003 - Login com Senha Incorreta

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT003 |
| **Título** | Tentativa de login com email válido e senha incorreta |
| **Funcionalidade** | Sistema de Autenticação |
| **Tipo** | Negativo |
| **Prioridade** | Alta |
| **Complexidade** | Básica |

#### Objetivo
Validar que o sistema bloqueia acesso mesmo com email válido quando a senha está incorreta, implementando proteções contra ataques de força bruta.

#### Pré-condições
- Sistema de login acessível e operacional
- Usuário "ana.silva@email.com" cadastrado com senha "MinhaSenh@2024"
- Base de dados operacional
- Conta não bloqueada por tentativas anteriores

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Email** | ana.silva@email.com | Email válido de usuário existente |
| **Senha** | SenhaErrada123 | Senha incorreta mas no formato válido |

#### Passos de Execução
1. Acessar a página de login do sistema
2. Inserir "ana.silva@email.com" no campo **Email**
3. Inserir "SenhaErrada123" no campo **Senha**
4. Clicar no botão **"Entrar"**

#### Resultado Esperado
- Sistema retorna erro em tempo similar ao login válido (< 3 segundos)
- Mensagem de erro genérica: "Email ou senha incorretos"
- Contador de tentativas é incrementado (não visível ao usuário)
- Usuário permanece na página de login
- Campo senha é limpo, campo email pode ser mantido
- **Não** é revelado que o email existe no sistema

#### Critérios de Aceitação
- ✅ Mensagem de erro consistente com CT002
- ✅ Tentativa registrada em logs de segurança
- ✅ Tempo de resposta não revela existência do email
- ✅ Interface permanece funcional para nova tentativa

---

## 🎯 Análise das Soluções

### ✅ **Pontos Fortes Destacados:**

1. **Completude:** Todos os casos seguem estrutura completa
2. **Realismo:** Dados de teste verossímeis e apropriados
3. **Segurança:** Consideração de aspectos de segurança (timing, revelação de informações)
4. **Especificidade:** Resultados esperados detalhados e verificáveis
5. **Praticidade:** Passos executáveis por qualquer testador

### 📊 **Cobertura Alcançada:**

- **Fluxo Principal:** Login bem-sucedido (caminho feliz)
- **Validação de Email:** Email inexistente
- **Validação de Senha:** Senha incorreta
- **Aspectos de Segurança:** Proteção contra timing attacks e information disclosure

### 🔍 **Aspectos Técnicos Corretos:**

1. **Não-especificidade:** Mensagens de erro genéricas (boa prática de segurança)
2. **Timing:** Consideração de tempos de resposta consistentes
3. **Logs:** Menção à necessidade de auditoria
4. **Estados:** Consideração do estado da interface após cada ação

---

## 💡 Variações Aceitáveis

### 🔄 **Alternativas Válidas para CT001:**

**Dados Diferentes:**
- Outros formatos de email válidos
- Senhas com diferentes padrões de complexidade
- Nomes de usuário alternativos

**Verificações Adicionais:**
- Verificação de timestamp de último login
- Validação de menus/funcionalidades no dashboard
- Verificação de logout automático

**Detalhamento de Passos:**
- Validação visual de cada campo antes da inserção
- Verificação de feedback visual durante digitação
- Confirmação de carregamento de elementos da página

### 🔄 **Variações para Casos Negativos:**

**CT002 Alternativas:**
- Diferentes formatos de email inválidos
- Emails com domínios inexistentes
- Campos em branco

**CT003 Alternativas:**
- Senhas com diferentes tipos de erro (muito curta, sem caracteres especiais)
- Senhas completamente diferentes
- Campo senha vazio

---

## ⚠️ **Erros Comuns a Evitar**

### ❌ **Problemas Frequentes:**

1. **Dados Irrealistas:**
   ```
   ❌ Email: "test", Senha: "123"
   ✅ Email: "usuario@empresa.com", Senha: "MinhaSenh@123"
   ```

2. **Passos Vagos:**
   ```
   ❌ "Fazer login"
   ✅ "Inserir credenciais nos campos específicos e clicar em Entrar"
   ```

3. **Resultados Imprecisos:**
   ```
   ❌ "Login funciona"
   ✅ "Usuário é redirecionado para dashboard com nome exibido"
   ```

4. **Falta de Pré-condições:**
   ```
   ❌ Começar direto com inserção de dados
   ✅ Especificar estado inicial e dados necessários
   ```

### 🔧 **Melhorias Sugeridas:**

1. **Adicionar Mais Contexto:**
   - Especificar navegador/dispositivo
   - Incluir resolução de tela ou tamanho de janela
   - Mencionar conexão de rede

2. **Considerar Acessibilidade:**
   - Navegação por teclado
   - Compatibilidade com leitores de tela
   - Contraste de cores

3. **Aspectos de Performance:**
   - Tempos específicos de carregamento
   - Comportamento com conexão lenta
   - Uso de recursos do sistema

---

## 📚 **Recursos para Aprofundamento**

### 📖 **Conceitos Relacionados:**
- **Boundary Value Analysis:** Para testar limites de campos
- **Equivalence Partitioning:** Para agrupar casos similares
- **State Transition Testing:** Para fluxos com múltiplos estados
- **Security Testing:** Para aspectos de segurança mais avançados

### 🛠️ **Ferramentas Úteis:**
- **Postman/Insomnia:** Para testar APIs de autenticação
- **Selenium WebDriver:** Para automatizar casos de login
- **OWASP ZAP:** Para testes de segurança
- **BrowserStack:** Para testes em múltiplos navegadores

### 📚 **Leituras Recomendadas:**
- "The Art of Software Testing" - Glenford Myers
- "Agile Testing" - Lisa Crispin & Janet Gregory
- "OWASP Testing Guide" - Para aspectos de segurança

---

## 🎯 **Próximos Passos**

### 🚀 **Para Evoluir:**

1. **Pratique Variações:**
   - Implemente os 3 casos com dados diferentes
   - Adicione verificações extras
   - Considere casos de borda (edge cases)

2. **Expanda a Cobertura:**
   - Teste recuperação de senha
   - Validação de campos obrigatórios
   - Comportamento com JavaScript desabilitado

3. **Prepare-se para Nível 2:**
   - Estude integração entre sistemas
   - Pratique trabalho colaborativo
   - Desenvolva pensamento de rastreabilidade

**Continue praticando! A qualidade dos casos de teste melhora significativamente com experiência e atenção aos detalhes.** 🎓✨
