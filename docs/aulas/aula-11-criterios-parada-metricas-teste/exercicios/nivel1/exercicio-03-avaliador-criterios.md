# Exercício 03 - Avaliador de Critérios Simples 🔵

**Nível:** Básico  
**Tempo Estimado:** 35-45 minutos  
**Objetivo:** Implementar sistema básico de avaliação de critérios de parada

## Contexto

Como engenheiro de qualidade em uma consultoria de software, você precisa criar uma ferramenta que automatize a avaliação de critérios de parada para diferentes clientes. Cada cliente tem critérios específicos, e você precisa de um sistema flexível que avalie automaticamente se um projeto está pronto para release.

A ferramenta deve ser simples mas robusta, permitindo configurar diferentes tipos de critérios (obrigatórios, condicionais, de escape) e fornecer decisões claras com justificativas detalhadas.

## Cenário de Uso

Você tem três clientes com perfis diferentes:

### Cliente A - Fintech (Rigoroso)
```python
criteria_fintech = {
    "mandatory": {
        "coverage_critical": {"target": 98.0, "operator": ">="},
        "coverage_general": {"target": 90.0, "operator": ">="},
        "critical_defects": {"target": 0, "operator": "=="},
        "security_vulnerabilities": {"target": 0, "operator": "=="}
    },
    "conditional": {
        "dre": {"target": 95.0, "operator": ">="},
        "performance_degradation": {"target": 5.0, "operator": "<="},
        "code_review_coverage": {"target": 100.0, "operator": "=="}
    },
    "escape": {
        "data_corruption_risk": {"target": True, "operator": "=="},
        "regulatory_compliance": {"target": False, "operator": "=="}
    },
    "conditional_threshold": 2  # Pelo menos 2 de 3 condicionais
}
```

### Cliente B - Startup (Balanceado)
```python
criteria_startup = {
    "mandatory": {
        "coverage_general": {"target": 75.0, "operator": ">="},
        "critical_defects": {"target": 0, "operator": "=="},
        "smoke_tests": {"target": True, "operator": "=="}
    },
    "conditional": {
        "dre": {"target": 85.0, "operator": ">="},
        "user_acceptance": {"target": 80.0, "operator": ">="},
        "performance_acceptable": {"target": True, "operator": "=="}
    },
    "escape": {
        "budget_exceeded": {"target": True, "operator": "=="},
        "deadline_critical": {"target": True, "operator": "=="}
    },
    "conditional_threshold": 2  # Pelo menos 2 de 3 condicionais
}
```

### Cliente C - Prototipo (Flexível)
```python
criteria_prototype = {
    "mandatory": {
        "basic_functionality": {"target": True, "operator": "=="},
        "core_features": {"target": 100.0, "operator": "=="}
    },
    "conditional": {
        "coverage_general": {"target": 60.0, "operator": ">="},
        "user_feedback": {"target": 70.0, "operator": ">="}
    },
    "escape": {
        "demo_deadline": {"target": True, "operator": "=="}
    },
    "conditional_threshold": 1  # Pelo menos 1 de 2 condicionais
}
```

## Dados de Teste

```python
# Dados do projeto Fintech atual
fintech_metrics = {
    "coverage_critical": 97.5,
    "coverage_general": 91.2,
    "critical_defects": 0,
    "security_vulnerabilities": 1,  # Problema!
    "dre": 96.8,
    "performance_degradation": 3.2,
    "code_review_coverage": 100.0,
    "data_corruption_risk": False,
    "regulatory_compliance": False
}

# Dados do projeto Startup atual  
startup_metrics = {
    "coverage_general": 78.5,
    "critical_defects": 0,
    "smoke_tests": True,
    "dre": 87.3,
    "user_acceptance": 82.1,
    "performance_acceptable": True,
    "budget_exceeded": False,
    "deadline_critical": False
}

# Dados do projeto Prototipo atual
prototype_metrics = {
    "basic_functionality": True,
    "core_features": 100.0,
    "coverage_general": 55.8,  # Abaixo do critério
    "user_feedback": 75.2,
    "demo_deadline": False
}
```

## Requisitos Funcionais

### RF01 - Avaliação de Critério Individual
Implementar função que avalia se uma métrica individual atende seu critério:
- Suporte a operadores: `>=`, `<=`, `==`, `!=`, `>`, `<`
- Tratamento de tipos: `int`, `float`, `bool`
- Retorno estruturado com detalhes da avaliação

### RF02 - Avaliação de Critérios por Tipo
Avaliar separadamente:
- **Obrigatórios:** Todos devem ser satisfeitos
- **Condicionais:** Pelo menos N de M devem ser satisfeitos  
- **Escape:** Qualquer um força parada imediata

### RF03 - Decisão Final de Parada
Combinar avaliações para decidir:
- **PARAR:** Todos obrigatórios + condicionais suficientes + sem escape negativo
- **CONTINUAR:** Qualquer falha nos critérios acima

### RF04 - Relatório Detalhado
Gerar relatório explicando:
- Status de cada critério individual
- Razão da decisão final
- Recomendações para critérios não atendidos

## Estrutura de Código Base

```python
"""
criteria_evaluator.py

Sistema de avaliação de critérios de parada flexível e configurável.
Suporta diferentes tipos de critérios e operadores lógicos.
"""

from typing import Dict, List, Any, Union
from dataclasses import dataclass
from enum import Enum

class CriteriaType(Enum):
    """Tipos de critérios suportados."""
    MANDATORY = "mandatory"
    CONDITIONAL = "conditional"  
    ESCAPE = "escape"

class DecisionType(Enum):
    """Tipos de decisão de parada."""
    STOP = "PARAR"
    CONTINUE = "CONTINUAR"

@dataclass
class CriterionResult:
    """Resultado da avaliação de um critério individual."""
    name: str
    type: CriteriaType
    current_value: Any
    target_value: Any
    operator: str
    satisfied: bool
    description: str

@dataclass
class EvaluationSummary:
    """Resumo da avaliação de critérios."""
    decision: DecisionType
    mandatory_passed: int
    mandatory_total: int
    conditional_passed: int
    conditional_total: int
    conditional_required: int
    escape_triggered: bool
    detailed_results: List[CriterionResult]
    justification: str
    recommendations: List[str]

class SimpleCriteriaEvaluator:
    """
    Avaliador simples de critérios de parada.
    
    Implementa lógica básica para combinar diferentes tipos
    de critérios e tomar decisões automatizadas.
    """
    
    def __init__(self):
        """Inicializa avaliador com operadores suportados."""
        self.supported_operators = {
            ">=": lambda current, target: current >= target,
            "<=": lambda current, target: current <= target,
            "==": lambda current, target: current == target,
            "!=": lambda current, target: current != target,
            ">": lambda current, target: current > target,
            "<": lambda current, target: current < target
        }
    
    def evaluate_single_criterion(self, name: str, 
                                 current_value: Any,
                                 criterion_config: Dict[str, Any],
                                 criterion_type: CriteriaType) -> CriterionResult:
        """
        Avalia um critério individual.
        
        Args:
            name: Nome do critério
            current_value: Valor atual da métrica
            criterion_config: Configuração do critério (target, operator)
            criterion_type: Tipo do critério
            
        Returns:
            CriterionResult com resultado da avaliação
        """
        # TODO: Implementar avaliação individual
        pass
    
    def evaluate_criteria_group(self, metrics: Dict[str, Any],
                               criteria_config: Dict[str, Dict],
                               criterion_type: CriteriaType) -> List[CriterionResult]:
        """
        Avalia um grupo de critérios do mesmo tipo.
        
        Args:
            metrics: Métricas atuais do projeto
            criteria_config: Configuração dos critérios
            criterion_type: Tipo dos critérios
            
        Returns:
            Lista de CriterionResult
        """
        # TODO: Implementar avaliação de grupo
        pass
    
    def evaluate_all_criteria(self, metrics: Dict[str, Any],
                            criteria_config: Dict) -> EvaluationSummary:
        """
        Avalia todos os critérios e toma decisão final.
        
        Args:
            metrics: Métricas atuais do projeto
            criteria_config: Configuração completa dos critérios
            
        Returns:
            EvaluationSummary com decisão e detalhes
        """
        # TODO: Implementar avaliação completa
        pass
    
    def _determine_final_decision(self, mandatory_results: List[CriterionResult],
                                conditional_results: List[CriterionResult],
                                escape_results: List[CriterionResult],
                                conditional_threshold: int) -> DecisionType:
        """
        Determina decisão final baseada em todas as avaliações.
        
        Args:
            mandatory_results: Resultados dos critérios obrigatórios
            conditional_results: Resultados dos critérios condicionais
            escape_results: Resultados dos critérios de escape
            conditional_threshold: Mínimo de condicionais necessários
            
        Returns:
            DecisionType apropriada
        """
        # TODO: Implementar lógica de decisão
        pass
    
    def _generate_justification(self, summary: EvaluationSummary) -> str:
        """
        Gera justificativa textual para a decisão.
        
        Args:
            summary: Resumo da avaliação
            
        Returns:
            Justificativa em linguagem natural
        """
        # TODO: Implementar geração de justificativa
        pass
    
    def _generate_recommendations(self, failed_criteria: List[CriterionResult]) -> List[str]:
        """
        Gera recomendações para critérios não atendidos.
        
        Args:
            failed_criteria: Lista de critérios que falharam
            
        Returns:
            Lista de recomendações específicas
        """
        # TODO: Implementar geração de recomendações
        pass
    
    def generate_detailed_report(self, summary: EvaluationSummary,
                               project_name: str) -> str:
        """
        Gera relatório detalhado da avaliação.
        
        Args:
            summary: Resumo da avaliação
            project_name: Nome do projeto avaliado
            
        Returns:
            Relatório formatado em texto
        """
        # TODO: Implementar geração de relatório
        pass

def main():
    """Função principal para testar os três cenários."""
    evaluator = SimpleCriteriaEvaluator()
    
    test_cases = [
        ("Fintech", fintech_metrics, criteria_fintech),
        ("Startup", startup_metrics, criteria_startup),
        ("Prototipo", prototype_metrics, criteria_prototype)
    ]
    
    print("=== AVALIADOR DE CRITÉRIOS DE PARADA ===")
    print()
    
    for project_name, metrics, criteria in test_cases:
        print(f"🔍 Avaliando projeto: {project_name}")
        
        # TODO: Avaliar critérios e exibir resultado
        # summary = evaluator.evaluate_all_criteria(metrics, criteria)
        # report = evaluator.generate_detailed_report(summary, project_name)
        # print(report)
        print("-" * 60)

if __name__ == "__main__":
    main()
```

## Tarefas Específicas

### Tarefa 1: Implementação dos Operadores
Implemente suporte robusto para todos os operadores lógicos com tratamento de tipos.

### Tarefa 2: Lógica de Combinação
Implemente a lógica para combinar critérios obrigatórios, condicionais e de escape.

### Tarefa 3: Tratamento de Erros
Adicione validação para:
- Métricas ausentes
- Operadores inválidos  
- Tipos incompatíveis
- Configurações malformadas

### Tarefa 4: Geração de Relatórios
Crie relatórios informativos e acionáveis que expliquem claramente as decisões.

## Resultados Esperados

### Projeto Fintech
- **Decisão:** CONTINUAR
- **Motivo:** 1 vulnerabilidade de segurança (critério obrigatório falhou)
- **Recomendação:** Corrigir vulnerabilidade antes de continuar

### Projeto Startup
- **Decisão:** PARAR
- **Motivo:** Todos os critérios atendidos
- **Observação:** Projeto pronto para release

### Projeto Prototipo  
- **Decisão:** PARAR
- **Motivo:** Critério de escape ativado (demo_deadline)
- **Observação:** Deadline força release mesmo com cobertura baixa

## Casos de Teste

```python
# Teste 1: Critério simples com números
assert evaluator.evaluate_single_criterion(
    "coverage", 85.5, {"target": 80.0, "operator": ">="}, 
    CriteriaType.MANDATORY
).satisfied == True

# Teste 2: Critério com booleanos
assert evaluator.evaluate_single_criterion(
    "tests_pass", True, {"target": True, "operator": "=="}, 
    CriteriaType.MANDATORY
).satisfied == True

# Teste 3: Operador incorreto
# Deve levantar ValueError

# Teste 4: Métrica ausente  
# Deve ser tratado graciosamente
```

## Critérios de Avaliação

| Aspecto | Excelente (4) | Bom (3) | Satisfatório (2) | Insuficiente (1) |
|---------|---------------|---------|------------------|------------------|
| **Lógica de Avaliação** | Todos os tipos de critérios implementados corretamente | Implementação sólida com pequenos gaps | Lógica básica funcional | Lógica incompleta ou incorreta |
| **Tratamento de Tipos** | Suporte robusto para int, float, bool | Suporte adequado com validação | Suporte básico funcional | Problemas com tipos diferentes |
| **Relatórios e Mensagens** | Relatórios claros e acionáveis | Relatórios informativos | Relatórios básicos mas úteis | Relatórios confusos ou inúteis |
| **Robustez** | Tratamento excelente de casos extremos | Boa validação e tratamento de erros | Validação básica adequada | Pouco ou nenhum tratamento de erros |

## Dicas de Implementação

💡 **Validação primeiro:** Implemente validação robusta antes da lógica principal  

💡 **Estruture a decisão:** Use enum para decisões e tipos para clareza  

💡 **Mensagens contextuais:** Personalize mensagens baseado no tipo de critério  

💡 **Teste incremental:** Teste cada tipo de critério separadamente primeiro  

💡 **Logs de debug:** Adicione prints para acompanhar o fluxo de decisão  

## Entregáveis

1. **`criteria_evaluator.py`** - Implementação completa do avaliador
2. **`test_scenarios.py`** - Script demonstrando os três cenários
3. **`evaluation_reports.txt`** - Relatórios dos três projetos
4. **`reflexao.md`** - Reflexão sobre:
   - Desafios de automatizar decisões subjetivas
   - Importância de configurabilidade vs. simplicidade
   - Lições sobre comunicação de decisões automatizadas

## Extensões Opcionais (Bônus)

🎯 **Critérios com peso:** Implemente pesos diferentes para critérios  
🎯 **Histórico de decisões:** Salve e compare decisões ao longo do tempo  
🎯 **Simulação de cenários:** Permita testar "e se" com métricas modificadas  
🎯 **Export para JSON:** Salve configurações e resultados estruturados  

---

**Foque na clareza da lógica e utilidade dos relatórios!** ⚖️
