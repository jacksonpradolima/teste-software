# 🔴 Exercícios Nível 3 - Avançado

## Objetivos Específicos
- Realizar análise estrutural completa em sistemas reais
- Otimizar casos de teste para máxima cobertura
- Identificar e tratar fluxos de dados complexos e múltiplas responsabilidades
- Praticar análise de sistemas legados e refatoração orientada a testes

---

## Exercício 3.1: Sistema de Gerenciamento de Biblioteca 📚

### Contexto
Você é responsável por testar um sistema de biblioteca com múltiplas entidades: livros, usuários, empréstimos e devoluções. O sistema possui regras de negócio para renovação, multas e reservas.

### Especificação
Implemente o arquivo `biblioteca.py` com:
- Classes: `Livro`, `Usuario`, `Emprestimo`, `Biblioteca`
- Métodos: cadastro, empréstimo, devolução, renovação, cálculo de multa, reserva

#### Tarefas
- Implemente as classes e métodos principais
- Desenhe o CFG do método de devolução e do fluxo de renovação
- Calcule a complexidade ciclomática dos métodos críticos
- Identifique DU-pairs para variáveis de status, datas e multas
- Implemente testes para todos os fluxos (normais, exceções, limites)

#### Critérios de Avaliação
- [ ] Cobertura estrutural completa dos fluxos principais
- [ ] Análise de DU-pairs e caminhos livres de definição
- [ ] Casos de teste para todos os cenários de negócio
- [ ] Comentários pedagógicos e documentação

---

## Exercício 3.2: Processador de Transações Bancárias 🏦

### Contexto
Um sistema bancário processa múltiplos tipos de transações (depósito, saque, transferência, pagamento de contas) com regras de validação, limites e auditoria.

### Especificação
Implemente o arquivo `processador_bancario.py` com:
- Classes: `Conta`, `Transacao`, `ProcessadorBancario`
- Métodos: processar_transacao, validar_transacao, auditar_transacao

#### Tarefas
- Implemente as classes e métodos principais
- Desenhe o CFG do método de processamento de transações
- Calcule a complexidade ciclomática dos métodos
- Identifique DU-pairs para variáveis de saldo, limites e logs
- Implemente testes para todos os tipos de transação e exceções

#### Critérios de Avaliação
- [ ] Cobertura de todos os tipos de transação
- [ ] Análise de DU-pairs e CFG completa
- [ ] Casos de teste para fluxos normais e de erro
- [ ] Documentação clara e comentários explicativos

---

## Exercício 3.3: Motor de Regras de Negócio Configurável ⚙️

### Contexto
Uma empresa precisa de um motor de regras flexível para aplicar diferentes políticas de negócio em tempo de execução, com regras configuráveis e múltiplos critérios de decisão.

### Especificação
Implemente o arquivo `motor_regras.py` com:
- Classe `MotorRegras` capaz de carregar, aplicar e auditar regras
- Suporte a múltiplos tipos de regra (ex: descontos, bloqueios, alertas)

#### Tarefas
- Implemente a classe e métodos principais
- Desenhe o CFG do método de aplicação de regras
- Calcule a complexidade ciclomática do motor
- Identifique DU-pairs para variáveis de configuração e resultado
- Implemente testes para diferentes conjuntos de regras e cenários

#### Critérios de Avaliação
- [ ] Flexibilidade e cobertura estrutural do motor
- [ ] Análise de DU-pairs e CFG completa
- [ ] Casos de teste para múltiplos cenários de regras
- [ ] Comentários pedagógicos

---

## Exercício 3.4: Análise Estrutural de Sistema Legacy 🏛️

### Contexto
Você recebeu um sistema legado sem documentação, com funções longas e pouco estruturadas. O objetivo é analisar, testar e propor refatorações orientadas a testes.

### Especificação
- Analise o arquivo legado `sistema_legacy.py` (fornecido pelo instrutor)
- Identifique funções críticas para análise estrutural

#### Tarefas
- Desenhe o CFG das funções selecionadas
- Calcule a complexidade ciclomática
- Identifique DU-pairs e fluxos de dados problemáticos
- Implemente testes para cobrir todos os caminhos identificados
- Proponha e implemente refatorações para melhorar testabilidade

#### Critérios de Avaliação
- [ ] Análise estrutural detalhada do sistema legado
- [ ] Propostas de refatoração justificadas
- [ ] Casos de teste para todos os caminhos
- [ ] Documentação do processo de análise e refatoração

---

## 🎯 Conclusão do Nível 3

Você enfrentou desafios reais de análise estrutural, integração de múltiplas responsabilidades e refatoração orientada a testes. Compare suas soluções com os gabaritos em `../solucoes/nivel3/` e utilize o capítulo principal como referência para dúvidas e aprofundamento.

**Parabéns por chegar ao nível avançado! O domínio de técnicas de teste estrutural é um diferencial para projetos de software robustos e confiáveis.**
