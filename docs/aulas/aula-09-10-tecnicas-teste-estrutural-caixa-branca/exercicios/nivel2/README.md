# 🟡 Exercícios Nível 2 - Intermediário

## Objetivos Específicos
- Integrar múltiplos conceitos de teste estrutural
- Praticar análise de DU-pairs em sistemas com múltiplas funções
- Aplicar critérios de cobertura de condições compostas
- Desenvolver testes para fluxos de dados entre funções/classes

---

## Exercício 2.1: Sistema de Validação de Formulários 📝

### Contexto
Você está desenvolvendo um sistema de validação de formulários para um portal de inscrições. O sistema deve validar nome, e-mail, idade e senha, aplicando múltiplas regras e retornando mensagens de erro específicas.

### Especificação
Implemente um módulo `validador_formulario.py` com as funções:
- `validar_nome(nome: str) -> bool`
- `validar_email(email: str) -> bool`
- `validar_idade(idade: int) -> bool`
- `validar_senha(senha: str) -> bool`
- `validar_formulario(dados: dict) -> list[str]`

Cada função deve conter pelo menos 2 decisões. A função principal deve integrar todas as validações e retornar uma lista de mensagens de erro.

#### Tarefas
- Implemente todas as funções com comentários explicativos
- Desenhe o grafo de fluxo de controle da função principal
- Calcule a complexidade ciclomática de cada função
- Identifique DU-pairs relevantes (ex: variáveis de erro, flags)
- Implemente casos de teste para 100% de cobertura de decisões

#### Critérios de Avaliação
- [ ] Integração correta das funções
- [ ] Análise estrutural completa (CFG, complexidade, DU-pairs)
- [ ] Casos de teste cobrem todas as decisões
- [ ] Comentários pedagógicos presentes

---

## Exercício 2.2: Analisador de Logs com Múltiplos Critérios 📑

### Contexto
Uma empresa precisa analisar logs de acesso para identificar padrões suspeitos. O sistema deve processar uma lista de registros e classificar cada acesso como normal, suspeito ou crítico, com base em múltiplos critérios combinados.

### Especificação
Implemente o arquivo `analisador_logs.py` com:
- Função `classificar_acesso(ip: str, horario: str, tentativas: int, sucesso: bool) -> str`
- Função `processar_logs(logs: list[dict]) -> dict`

A função principal deve processar todos os logs e retornar um dicionário com contagem de cada tipo de acesso.

#### Tarefas
- Implemente as funções com pelo menos 3 decisões cada
- Desenhe o CFG da função de classificação
- Calcule a complexidade ciclomática
- Identifique DU-pairs para variáveis de contagem
- Implemente testes para cobrir todas as condições compostas

#### Critérios de Avaliação
- [ ] Cobertura de todas as condições
- [ ] Análise de DU-pairs e caminhos livres de definição
- [ ] Casos de teste para todos os tipos de acesso
- [ ] Documentação clara

---

## Exercício 2.3: Calculadora com Operações Complexas 🧮

### Contexto
Você deve implementar uma calculadora que realiza operações aritméticas e funções avançadas (potência, raiz, módulo), além de registrar o histórico das operações.

### Especificação
Implemente o arquivo `calculadora_avancada.py` com:
- Classe `CalculadoraAvancada` com métodos: `somar`, `subtrair`, `multiplicar`, `dividir`, `potencia`, `raiz`, `modulo`, `historico`
- Cada método deve validar entradas e registrar a operação no histórico

#### Tarefas
- Implemente todos os métodos com tratamento de exceções
- Desenhe o CFG do método `dividir` e de um método avançado
- Calcule a complexidade ciclomática dos métodos
- Identifique DU-pairs para variáveis de resultado e histórico
- Implemente testes para cobrir todos os fluxos

#### Critérios de Avaliação
- [ ] Métodos implementados corretamente
- [ ] Análise estrutural e DU-pairs completa
- [ ] Casos de teste para exceções e operações válidas
- [ ] Histórico funcionando corretamente

---

## Exercício 2.4: Fluxo de Dados em Sistema de Estoque 📦

### Contexto
Um sistema de estoque gerencia produtos, entradas e saídas. O objetivo é garantir que o fluxo de dados entre funções de entrada, saída e consulta seja seguro e testável.

### Especificação
Implemente o arquivo `sistema_estoque.py` com:
- Classe `Produto` (nome, quantidade)
- Classe `Estoque` com métodos: `adicionar_produto`, `remover_produto`, `consultar_produto`, `listar_estoque`

#### Tarefas
- Implemente as classes e métodos com validações
- Desenhe o CFG do método `remover_produto`
- Calcule a complexidade ciclomática dos métodos principais
- Identifique DU-pairs para variáveis de quantidade e estoque
- Implemente testes para fluxos normais e de erro

#### Critérios de Avaliação
- [ ] Fluxo de dados seguro entre métodos
- [ ] Análise de DU-pairs e CFG completa
- [ ] Casos de teste para todos os fluxos
- [ ] Comentários explicativos

---

## 🎯 Conclusão do Nível 2

Você praticou integração de múltiplos conceitos, análise de DU-pairs em sistemas maiores e cobertura de condições compostas. Avance para o Nível 3 para desafios de análise estrutural em sistemas complexos!

**Compare suas soluções com os gabaritos em `../solucoes/nivel2/` e revise os conceitos no capítulo principal sempre que necessário.**
