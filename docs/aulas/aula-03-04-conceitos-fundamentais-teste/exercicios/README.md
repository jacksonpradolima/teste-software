# Exercícios - Conceitos Fundamentais de Teste

Este conjunto de exercícios foi cuidadosamente elaborado para consolidar os conceitos fundamentais de teste de software estudados na aula. Os exercícios estão organizados em três níveis progressivos de dificuldade, permitindo uma jornada de aprendizado estruturada e incremental.

## 🎯 Objetivos Pedagógicos

Ao completar estes exercícios, você será capaz de:

1. **Aplicar a cadeia causal** erro → defeito → falha → incidente em cenários reais
2. **Distinguir precisamente** entre verificação e validação em contextos práticos
3. **Implementar sistemas resilientes** baseados nos conceitos fundamentais
4. **Analisar e otimizar** métricas de qualidade e performance de teste
5. **Projetar arquiteturas** que incorporem princípios preventivos de qualidade

## 📊 Estrutura dos Níveis

### 🔵 Nível 1 - Básico (Tempo estimado: 15-30 minutos)
**Foco**: Aplicação direta de conceitos individuais
- Identificação e classificação de problemas
- Implementação de validações básicas
- Análise de cenários simples

### 🟡 Nível 2 - Intermediário (Tempo estimado: 45-90 minutos)
**Foco**: Integração de múltiplos conceitos
- Sistemas com interações entre componentes
- Análise de trade-offs e métricas
- Design de soluções robustas

### 🔴 Nível 3 - Avançado (Tempo estimado: 2-4 horas)
**Foco**: Design complexo e tomada de decisões arquiteturais
- Sistemas distribuídos e microsserviços
- Análise de performance e otimização
- Integração com tecnologias emergentes

## 🧭 Guia de Utilização

### Para Estudantes
1. **Comece sempre pelo Nível 1** - mesmo que se sinta confiante
2. **Leia completamente** o enunciado antes de começar a implementar
3. **Teste sua solução** em diferentes cenários
4. **Compare** sua abordagem com as soluções fornecidas
5. **Reflita** sobre os trade-offs de sua implementação

### Para Instrutores
- Os exercícios incluem **critérios de avaliação claros**
- Cada nível possui **rubricas específicas** de avaliação
- **Soluções comentadas** estão disponíveis na pasta `solucoes/`
- **Variações dos exercícios** podem ser criadas alterando parâmetros específicos

## 🛠️ Configuração do Ambiente

### Requisitos Técnicos
```bash
# Python 3.12+ obrigatório
python --version  # Deve ser >= 3.12

# Dependências (apenas bibliotecas nativas do Python)
# Não há dependências externas - conceitos fundamentais usam apenas Python puro
```

### Estrutura Recomendada
```
meu_trabalho/
├── nivel1/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   └── testes_nivel1.py
├── nivel2/
│   ├── sistema_pedidos.py
│   ├── metricas_qualidade.py
│   └── testes_nivel2.py
└── nivel3/
    ├── arquitetura_distribuida/
    ├── analise_performance/
    └── testes_nivel3.py
```

## 🎨 Filosofia dos Exercícios

### Contextos Realistas
Todos os exercícios são baseados em **cenários do mundo real**:
- Sistema de e-commerce (pedidos, pagamentos, estoque)
- Plataforma bancária (transações, autenticação, auditoria)
- Sistema de saúde (prontuários, agendamentos, prescrições)

### Progressão Conceitual
Cada exercício **constrói sobre o anterior**:
- **Nível 1**: Conceitos isolados
- **Nível 2**: Integração e interações
- **Nível 3**: Sistemas complexos e otimização

### Aprendizado Prático
- **Código real**: Implementações funcionais, não pseudo-código
- **Testes incluídos**: Cada exercício vem com casos de teste
- **Reflexão guiada**: Perguntas que estimulam pensamento crítico

## 🔍 Metodologia de Avaliação

### Critérios Transversais (Todos os Níveis)
1. **Correção funcional** (25%)
2. **Qualidade do código** (25%)
3. **Aplicação dos conceitos** (25%)
4. **Análise reflexiva** (25%)

### Rubricas Específicas por Nível

#### Nível 1 - Critérios Básicos
- ✅ **Excelente**: Implementa corretamente todos os conceitos
- ✓ **Bom**: Implementa a maioria dos conceitos com pequenos erros
- ⚠️ **Satisfatório**: Implementa conceitos básicos, mas falta profundidade
- ❌ **Insuficiente**: Não demonstra compreensão dos conceitos

#### Nível 2 - Critérios Intermediários
- ✅ **Excelente**: Integra múltiplos conceitos com trade-offs bem analisados
- ✓ **Bom**: Boa integração com análise adequada de métricas
- ⚠️ **Satisfatório**: Integração básica sem análise profunda
- ❌ **Insuficiente**: Falha na integração ou análise de conceitos

#### Nível 3 - Critérios Avançados
- ✅ **Excelente**: Design arquitetural robusto com otimizações justificadas
- ✓ **Bom**: Arquitetura sólida com considerações de performance
- ⚠️ **Satisfatório**: Arquitetura funcional mas sem otimizações
- ❌ **Insuficiente**: Problemas fundamentais de design

## 📚 Recursos de Apoio

### Durante os Exercícios
- **Documentação Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **PEP 8 Style Guide**: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
- **Material da Aula**: Sempre consulte o README.md principal

### Para Aprofundamento
- **SWEBOK v3.0**: Referência oficial para engenharia de software
- **IEEE 829**: Padrão para documentação de teste
- **ISO/IEC 25010**: Modelo de qualidade de software

## ⚡ Dicas de Sucesso

### 🎯 Estratégias Eficazes
1. **Leia duas vezes** antes de codificar
2. **Comece simples** e refine iterativamente
3. **Teste frequentemente** durante o desenvolvimento
4. **Documente decisões** de design importantes
5. **Busque feedback** de colegas ou instrutores

### 🚫 Armadilhas Comuns
- **Não pular** a fase de análise conceitual
- **Não ignorar** casos extremos (edge cases)
- **Não subestimar** a importância da documentação
- **Não copiar** soluções sem compreender os conceitos

### 🔧 Debugging Eficaz
- Use **print statements** para rastrear fluxo de execução
- Implemente **logs estruturados** para análise posterior
- Teste **uma funcionalidade por vez** antes de integrar
- **Valide entradas** antes de processar

## 🚀 Próximos Passos

Após completar todos os exercícios:

1. **Auto-avaliação**: Use as rubricas para avaliar seu trabalho
2. **Revisão de pares**: Troque soluções com colegas
3. **Reflexão**: Escreva um resumo dos aprendizados principais
4. **Extensão**: Considere variações dos exercícios para prática adicional

---

**Lembre-se**: O objetivo não é apenas "fazer funcionar", mas **compreender profundamente** os conceitos fundamentais que tornarão você um profissional mais eficaz na área de qualidade de software.

**Boa jornada de aprendizado!** 🎓
