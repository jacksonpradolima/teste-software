# Exercícios Práticos - Técnicas de Teste Estrutural (Caixa-Branca)

## Instruções Gerais

Os exercícios estão organizados em três níveis de dificuldade progressiva, cada um focando em aspectos específicos das técnicas de teste estrutural. **Leia atentamente** os enunciados e **implemente as soluções completamente** antes de consultar os gabaritos.

### 📋 Objetivos dos Exercícios

- **Aplicar critérios de cobertura estrutural** em cenários realistas
- **Calcular complexidade ciclomática** e derivar casos de teste
- **Analisar fluxo de controle e fluxo de dados** sistematicamente
- **Identificar DU-pairs** e implementar cobertura completa
- **Desenvolver intuição prática** para análise estrutural de código

### 🎯 Estrutura de Dificuldade

#### 🔵 Nível 1 - Básico
- **Objetivo**: Aplicação direta de conceitos fundamentais
- **Complexidade**: Uma única funcionalidade por exercício
- **Tempo Estimado**: 15-30 minutos por exercício
- **Foco**: Cobertura de instruções, decisões básicas, cálculo de complexidade

#### 🟡 Nível 2 - Intermediário  
- **Objetivo**: Integração de múltiplos conceitos
- **Complexidade**: Sistema pequeno com 2-4 classes/funções
- **Tempo Estimado**: 45-90 minutos por exercício
- **Foco**: DU-pairs, critérios de fluxo de dados, condições combinadas

#### 🔴 Nível 3 - Avançado
- **Objetivo**: Design complexo e tomada de decisões arquiteturais
- **Complexidade**: Sistema completo com múltiplas responsabilidades
- **Tempo Estimado**: 2-4 horas por exercício
- **Foco**: Análise estrutural completa, otimização de casos de teste, cenários reais

### 📝 Critérios de Avaliação

Para cada exercício, sua solução será avaliada nos seguintes aspectos:

1. **Correção Funcional** (25%): O código funciona conforme especificado
2. **Análise Estrutural** (35%): Identificação correta de CFG, complexidade, DU-pairs
3. **Qualidade dos Casos de Teste** (25%): Cobertura adequada e casos bem escolhidos
4. **Documentação e Comentários** (15%): Explicação clara do processo de análise

### 🛠️ Ferramentas Recomendadas

- **Python 3.12+**: Linguagem base para implementação
- **pytest**: Framework de testes (instalar com `pip install pytest`)
- **coverage.py**: Medição de cobertura (instalar com `pip install coverage`)
- **Papel e caneta**: Para desenhar grafos de fluxo de controle manualmente

### 💡 Dicas para Sucesso

1. **Leia o enunciado completo** antes de começar a implementar
2. **Desenhe o grafo de fluxo de controle** no papel antes de codificar
3. **Calcule a complexidade ciclomática** para guiar o número de casos de teste
4. **Identifique DU-pairs sistematicamente** para cada variável
5. **Execute os testes** para verificar a cobertura real
6. **Documente sua análise** passo a passo nos comentários

### 📚 Material de Apoio

- **Capítulo principal**: Consulte as seções 2 e 3 do README.md da aula
- **Exemplos de referência**: Use os códigos demonstrativos como modelo
- **Fórmulas importantes**:
  - Complexidade Ciclomática: M = E - N + 2P ou M = D + 1
  - Cobertura de Instruções: (Instruções Executadas / Total) × 100%
  - Cobertura de Decisões: (Decisões Completamente Testadas / Total) × 100%

---

## 📂 Organização dos Exercícios

### [🔵 Nível 1 - Básico](./nivel1/)
- **Exercício 1.1**: Análise de Função Simples com Condicionais
- **Exercício 1.2**: Cálculo de Complexidade Ciclomática
- **Exercício 1.3**: Cobertura de Instruções e Decisões
- **Exercício 1.4**: Identificação Básica de DU-Pairs

### [🟡 Nível 2 - Intermediário](./nivel2/)
- **Exercício 2.1**: Sistema de Validação de Formulários
- **Exercício 2.2**: Analisador de Logs com Múltiplos Critérios
- **Exercício 2.3**: Calculadora com Operações Complexas
- **Exercício 2.4**: Fluxo de Dados em Sistema de Estoque

### [🔴 Nível 3 - Avançado](./nivel3/)
- **Exercício 3.1**: Sistema de Gerenciamento de Biblioteca
- **Exercício 3.2**: Processador de Transações Bancárias
- **Exercício 3.3**: Motor de Regras de Negócio Configurável
- **Exercício 3.4**: Análise Estrutural de Sistema Legacy

---

## 🚀 Como Começar

1. **Escolha seu nível**: Comece pelo Nível 1 se é iniciante, ou vá direto ao seu nível de conforto
2. **Leia as instruções específicas** na pasta do nível escolhido
3. **Implemente as soluções** seguindo as especificações
4. **Execute os testes** para verificar funcionalidade e cobertura
5. **Compare com os gabaritos** disponíveis na pasta `../solucoes/`
6. **Reflita sobre alternativas** e otimizações possíveis

---

## 📋 Checklist de Validação

Antes de considerar um exercício completo, verifique:

- [ ] Código implementado funciona corretamente
- [ ] Grafo de fluxo de controle desenhado e documentado
- [ ] Complexidade ciclomática calculada e verificada
- [ ] DU-pairs identificados para todas as variáveis relevantes
- [ ] Casos de teste derivados sistematicamente da análise
- [ ] Cobertura medida e documentada (instruções, decisões, caminhos)
- [ ] Código comentado pedagogicamente
- [ ] Testes executam sem erros

---

**Boa sorte e aproveite a jornada de aprendizado! 🎓**

*Lembre-se: o objetivo não é apenas "fazer funcionar", mas compreender profundamente como as técnicas de teste estrutural garantem qualidade e confiabilidade do software.*
