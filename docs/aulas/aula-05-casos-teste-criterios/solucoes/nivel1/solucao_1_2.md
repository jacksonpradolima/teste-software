# Solução: Exercício 1.2 - Calculadora Online 🔵

**Exercício:** Classificação de Tipos de Casos de Teste  
**Nível:** Básico (Individual)  
**Tempo de Resolução:** 15 minutos  
**Conceitos:** Tipos de teste (positivo, negativo, limite), classificação de cenários  

---

## 📋 Solução de Referência

### CT001 - Operação de Soma com Números Positivos

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT001 |
| **Título** | Cálculo de soma entre dois números inteiros positivos |
| **Funcionalidade** | Operações Matemáticas - Soma |
| **Tipo** | **Positivo** |
| **Prioridade** | Alta |
| **Complexidade** | Básica |

#### Justificativa da Classificação
**Tipo: POSITIVO** - Este caso testa o funcionamento normal da calculadora em condições ideais, usando entradas válidas e esperadas pelo sistema. Valida o requisito funcional principal da operação de soma.

#### Objetivo
Verificar que a calculadora executa corretamente a operação de soma entre dois números inteiros positivos, exibindo o resultado correto na interface.

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Primeiro Número** | 25 | Número inteiro positivo |
| **Operação** | + (soma) | Operador aritmético básico |
| **Segundo Número** | 17 | Número inteiro positivo |
| **Resultado Esperado** | 42 | 25 + 17 = 42 |

#### Passos de Execução
1. Acessar a calculadora online
2. Inserir o número "25" usando teclado numérico ou cliques
3. Clicar no botão "+" (soma)
4. Inserir o número "17"
5. Clicar no botão "=" (igual)

#### Resultado Esperado
- Display exibe "42" corretamente
- Operação processada em tempo real (< 1 segundo)
- Interface permanece responsiva
- Nenhuma mensagem de erro é exibida

---

### CT002 - Divisão por Zero

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT002 |
| **Título** | Tentativa de divisão por zero |
| **Funcionalidade** | Operações Matemáticas - Divisão |
| **Tipo** | **Negativo** |
| **Prioridade** | Crítica |
| **Complexidade** | Básica |

#### Justificativa da Classificação
**Tipo: NEGATIVO** - Este caso testa uma situação matematicamente inválida (divisão por zero) que não deve ser permitida pelo sistema. Valida o tratamento de erros e robustez da aplicação.

#### Objetivo
Verificar que a calculadora trata adequadamente a tentativa de divisão por zero, exibindo mensagem de erro apropriada sem travar ou gerar comportamento inesperado.

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Primeiro Número** | 10 | Número válido qualquer |
| **Operação** | ÷ (divisão) | Operador de divisão |
| **Segundo Número** | 0 | Zero - valor que causa erro |
| **Resultado Esperado** | Erro | Mensagem de erro apropriada |

#### Passos de Execução
1. Acessar a calculadora online
2. Inserir o número "10"
3. Clicar no botão "÷" (divisão)
4. Inserir o número "0"
5. Clicar no botão "=" (igual)

#### Resultado Esperado
- Display exibe mensagem de erro: "Erro: Divisão por zero" ou "Indefinido"
- **Não** exibe "Infinity", "NaN" ou valores incorretos
- Sistema permanece estável e funcional
- Possível limpar o erro e iniciar nova operação
- Interface não trava ou se torna não responsiva

---

### CT003 - Número no Limite Máximo

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT003 |
| **Título** | Operação com número no limite máximo suportado |
| **Funcionalidade** | Operações Matemáticas - Limites |
| **Tipo** | **Limite (Boundary)** |
| **Prioridade** | Média |
| **Complexidade** | Básica |

#### Justificativa da Classificação
**Tipo: LIMITE/BOUNDARY** - Este caso testa o comportamento do sistema nos valores extremos suportados. Não é um caso puramente positivo (funcionalidade normal) nem negativo (erro esperado), mas sim um teste de fronteira que valida os limites operacionais.

#### Objetivo
Verificar como a calculadora se comporta ao operar com números muito grandes, próximos ao limite máximo de representação, garantindo que não ocorram overflows ou resultados incorretos.

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Primeiro Número** | 999999999 | Número próximo ao limite |
| **Operação** | × (multiplicação) | Operação que pode gerar overflow |
| **Segundo Número** | 999 | Multiplicador que causará resultado grande |
| **Resultado Esperado** | 999999999000 ou tratamento de limite | Resultado correto ou erro controlado |

#### Passos de Execução
1. Acessar a calculadora online
2. Inserir "999999999" (nove dígitos)
3. Clicar no botão "×" (multiplicação)
4. Inserir "999"
5. Clicar no botão "=" (igual)

#### Resultado Esperado
**Opção A - Suporte a números grandes:**
- Display exibe "999999999000" ou notação científica (9.99999999e+11)
- Resultado matematicamente correto

**Opção B - Limite controlado:**
- Mensagem informativa: "Resultado excede limite máximo"
- Sistema permanece estável
- Possibilidade de continuar com nova operação

**Critério de Falha:**
- Sistema trava ou se torna não responsivo
- Resultado incorreto sem aviso
- Display mostra valores inconsistentes

---

### CT004 - Entrada de Caracteres Inválidos

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT004 |
| **Título** | Tentativa de inserir letras em campo numérico |
| **Funcionalidade** | Validação de Entrada |
| **Tipo** | **Negativo** |
| **Prioridade** | Média |
| **Complexidade** | Básica |

#### Justificativa da Classificação
**Tipo: NEGATIVO** - Testa entrada inválida (caracteres não numéricos) que deve ser rejeitada pelo sistema. Valida a validação de entrada e robustez da interface.

#### Objetivo
Verificar que a calculadora rejeita adequadamente tentativas de inserir caracteres não numéricos, mantendo a integridade dos cálculos.

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Tentativa de Entrada** | "ABC" | Letras do alfabeto |
| **Método** | Teclado físico | Digitação direta |

#### Passos de Execução
1. Acessar a calculadora online
2. Tentar digitar "A" no campo/display
3. Tentar digitar "B" em sequência
4. Tentar digitar "C" em sequência
5. Observar comportamento do sistema

#### Resultado Esperado
**Comportamento Ideal:**
- Caracteres não numéricos são ignorados/rejeitados
- Display permanece vazio ou mantém valor anterior
- Nenhuma entrada inválida é aceita

**Comportamentos Aceitáveis:**
- Beep ou feedback visual indicando entrada inválida
- Mensagem temporária: "Apenas números são permitidos"
- Campo permanece focado para nova tentativa

**Critério de Falha:**
- Aceita caracteres não numéricos
- Sistema trava ou gera erro não tratado
- Display mostra caracteres inválidos

---

### CT005 - Sequência de Operações (Cadeia)

| **Campo** | **Valor** |
|-----------|-----------|
| **ID** | CT005 |
| **Título** | Execução de múltiplas operações em sequência |
| **Funcionalidade** | Operações Sequenciais |
| **Tipo** | **Positivo** |
| **Prioridade** | Alta |
| **Complexidade** | Básica |

#### Justificativa da Classificação
**Tipo: POSITIVO** - Testa funcionalidade normal da calculadora em um cenário mais complexo, validando que ela pode processar múltiplas operações corretamente seguindo ordem matemática.

#### Objetivo
Verificar que a calculadora executa corretamente uma sequência de operações matemáticas, respeitando precedência de operadores ou processando de forma sequencial conforme especificado.

#### Dados de Teste
| **Campo** | **Valor** | **Observação** |
|-----------|-----------|----------------|
| **Expressão** | 10 + 5 × 2 | Teste de precedência |
| **Resultado Esperado (Precedência)** | 20 | 10 + (5 × 2) = 10 + 10 = 20 |
| **Resultado Esperado (Sequencial)** | 30 | (10 + 5) × 2 = 15 × 2 = 30 |

#### Passos de Execução
1. Acessar a calculadora online
2. Inserir "10"
3. Clicar em "+"
4. Inserir "5"
5. Clicar em "×"
6. Inserir "2"
7. Clicar em "="

#### Resultado Esperado
**Dependendo da implementação:**
- **Calculadora científica:** 20 (respeitando precedência)
- **Calculadora simples:** 30 (processamento sequencial)
- **Ambos aceitáveis** desde que consistente com especificação

**Critérios Adicionais:**
- Resultado numericamente correto conforme tipo
- Processamento sem erros
- Interface responsiva durante operações

---

## 🎯 Análise da Classificação

### 📊 **Distribuição por Tipo:**

| **Tipo de Teste** | **Quantidade** | **Casos** | **Justificativa** |
|-------------------|----------------|-----------|-------------------|
| **Positivo** | 3 (60%) | CT001, CT005 | Funcionalidades principais e fluxos normais |
| **Negativo** | 2 (40%) | CT002, CT004 | Tratamento de erros e validações |
| **Limite** | 1 (20%) | CT003 | Comportamento em fronteiras |

### ✅ **Pontos Fortes da Classificação:**

1. **Cobertura Balanceada:** Boa distribuição entre tipos
2. **Casos Realistas:** Cenários que ocorrem frequentemente
3. **Criticidade Adequada:** Priorização baseada em impacto
4. **Justificativas Claras:** Razão específica para cada classificação

### 🔍 **Aspectos Importantes Demonstrados:**

1. **Testes Positivos** validam funcionalidade em condições normais
2. **Testes Negativos** garantem robustez e tratamento de erros
3. **Testes de Limite** verificam comportamento em extremos
4. **Classificação não é sempre binária** - existe área cinzenta

---

## 💡 Variações e Alternativas

### 🔄 **Outros Casos Positivos Possíveis:**

- **Operações com decimais:** 3.14 + 2.86 = 6.00
- **Números negativos:** (-5) + 3 = (-2)
- **Operações básicas restantes:** Subtração, divisão normal

### 🔄 **Outros Casos Negativos Possíveis:**

- **Múltiplos operadores:** 5 + + 3 (operador duplicado)
- **Operação incompleta:** 5 + = (segundo operando ausente)
- **Caracteres especiais:** Tentativa de inserir símbolos especiais

### 🔄 **Outros Casos de Limite:**

- **Número máximo de dígitos:** 999999999999999999
- **Precisão decimal:** 0.000000000000001
- **Resultado zero:** 5 - 5 = 0

---

## ⚠️ **Armadilhas Comuns na Classificação**

### ❌ **Erros Frequentes:**

1. **Confundir Negativo com Limite:**
   ```
   ❌ "Número muito grande" = Negativo
   ✅ "Número muito grande" = Limite (se há limite definido)
   ```

2. **Classificação Baseada em Resultado:**
   ```
   ❌ "Deu erro, então é Negativo"
   ✅ "Entrada inválida proposital, então é Negativo"
   ```

3. **Ignorar Contexto do Sistema:**
   ```
   ❌ Aplicar regras universais
   ✅ Considerar especificações do sistema específico
   ```

### 🔧 **Como Classificar Corretamente:**

1. **Analise a Intenção:**
   - Positivo: Testar funcionalidade normal
   - Negativo: Testar robustez e tratamento de erros
   - Limite: Testar comportamento em extremos

2. **Considere o Contexto:**
   - Tipo de aplicação (científica vs. básica)
   - Especificações do sistema
   - Expectativas do usuário

3. **Documente a Justificativa:**
   - Explique por que escolheu cada classificação
   - Considere classificações alternativas
   - Seja consistente na abordagem

---

## 📚 Recursos para Aprofundamento

### 📖 **Conceitos Relacionados:**
- **Equivalence Class Partitioning:** Agrupamento de casos similares
- **Boundary Value Analysis:** Foco sistemático em valores limites
- **Error Guessing:** Intuição baseada em experiência
- **Decision Table Testing:** Lógica complexa com múltiplas condições

### 🛠️ **Ferramentas para Prática:**
- **Calculadoras online** para comparação de comportamentos
- **Planilhas** para organizar classificações
- **Mind maps** para visualizar tipos de teste
- **Ferramentas de automação** para executar casos em massa

---

## 🎯 Próximos Passos

### 🚀 **Para Consolidar o Aprendizado:**

1. **Pratique com Outros Sistemas:**
   - Classifique casos para formulários web
   - Analise tipos em sistemas de login
   - Identifique padrões em diferentes domínios

2. **Refine os Critérios:**
   - Desenvolva sua própria "taxonomia" de tipos
   - Crie guidelines para classificação consistente
   - Documente decisões para referência futura

3. **Prepare-se para Complexidade:**
   - Estude casos que combinam múltiplos tipos
   - Entenda testes de integração entre componentes
   - Explore testes de regressão e automação

**Lembre-se: A classificação correta de casos de teste é fundamental para estratégias eficazes e comunicação clara com stakeholders!** 🎓✨
