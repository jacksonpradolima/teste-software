# Exercício 01 - Calculadora de Métricas Fundamentais 🔵

**Nível:** Básico  
**Tempo Estimado:** 30-45 minutos  
**Objetivo:** Implementar cálculos básicos das métricas fundamentais de teste

## Contexto

Você foi contratado como engenheiro de qualidade junior em uma startup de tecnologia educacional. Sua primeira tarefa é implementar uma calculadora que compute as métricas fundamentais de teste para ajudar a equipe a tomar decisões de parada baseadas em dados.

A equipe já possui dados brutos dos testes, mas precisa de uma ferramenta que calcule automaticamente:
- Cobertura de código (linha, branch, função)
- Densidade de defeitos
- Eficiência de Remoção de Defeitos (DRE)
- Tempo Médio para Detecção (MTTD)

## Requisitos Funcionais

### RF01 - Cálculo de Cobertura
Implementar métodos para calcular diferentes tipos de cobertura:
- **Cobertura de linha:** (linhas executadas / total de linhas) × 100
- **Cobertura de branch:** (branches executados / total de branches) × 100  
- **Cobertura de função:** (funções testadas / total de funções) × 100

### RF02 - Cálculo de Densidade de Defeitos
Calcular densidade usando a fórmula:
- **Por KLOC:** (número de defeitos / linhas de código) × 1000
- **Por módulo:** defeitos encontrados em cada módulo

### RF03 - Cálculo de DRE (Defect Removal Efficiency)
Calcular eficiência usando:
- **Fórmula:** (defeitos pré-produção / (defeitos pré-produção + defeitos pós-produção)) × 100

### RF04 - Cálculo de MTTD (Mean Time to Detection)
Calcular tempo médio entre introdução e detecção de defeitos.

## Requisitos Técnicos

- **Linguagem:** Python 3.12+
- **Bibliotecas:** Apenas recursos nativos (typing, dataclasses, datetime, statistics)
- **Entrada:** Dicionários com dados estruturados
- **Saída:** Métricas calculadas com precisão de 2 casas decimais
- **Validação:** Verificar entradas inválidas e retornar mensagens de erro apropriadas

## Restrições

❌ **Não use** bibliotecas externas como numpy, pandas ou scipy  
❌ **Não implemente** interface gráfica (apenas linha de comando)  
❌ **Não arredonde** valores intermediários, apenas o resultado final  

## Dados de Entrada (Exemplo)

```python
# Dados de cobertura
coverage_data = {
    "lines_executed": 1247,
    "total_lines": 1580,
    "branches_executed": 89,
    "total_branches": 112,
    "functions_tested": 45,
    "total_functions": 52
}

# Dados de defeitos
defect_data = {
    "pre_production_defects": 23,
    "post_production_defects": 4,
    "total_lines_of_code": 15800,
    "defects_by_module": {
        "authentication": 5,
        "payment": 8,
        "user_interface": 7,
        "database": 3
    }
}

# Dados temporais para MTTD
time_data = [
    {"introduced": "2024-01-15", "detected": "2024-01-18"},
    {"introduced": "2024-01-20", "detected": "2024-01-25"},
    {"introduced": "2024-01-22", "detected": "2024-01-24"}
]
```

## Estrutura de Código Base

```python
"""
metrics_calculator.py

Calculadora de métricas fundamentais de teste.
Implementa cálculos básicos seguindo as fórmulas matemáticas
apresentadas na aula teórica.
"""

from typing import Dict, List, Union
from dataclasses import dataclass
from datetime import datetime, date
import statistics

@dataclass
class MetricResult:
    """
    Resultado de uma métrica calculada.
    
    Attributes:
        name: Nome da métrica
        value: Valor numérico calculado
        unit: Unidade de medida (%, defeitos/KLOC, dias, etc.)
        interpretation: Breve interpretação do resultado
    """
    name: str
    value: float
    unit: str
    interpretation: str

class BasicMetricsCalculator:
    """
    Calculadora de métricas fundamentais para critérios de parada.
    
    Esta classe implementa os cálculos básicos das quatro métricas
    principais: cobertura, densidade de defeitos, DRE e MTTD.
    """
    
    def __init__(self):
        """Inicializa a calculadora com configurações padrão."""
        self.precision = 2  # Casas decimais para resultados
        
    # TODO: Implementar método calculate_coverage
    def calculate_coverage(self, coverage_data: Dict[str, int]) -> Dict[str, MetricResult]:
        """
        Calcula métricas de cobertura de código.
        
        Args:
            coverage_data: Dict com dados de cobertura
            
        Returns:
            Dict com resultados de cobertura por tipo
            
        Raises:
            ValueError: Se dados de entrada são inválidos
        """
        pass  # IMPLEMENTAR
    
    # TODO: Implementar método calculate_defect_density
    def calculate_defect_density(self, defect_data: Dict) -> Dict[str, MetricResult]:
        """
        Calcula densidade de defeitos por KLOC e por módulo.
        
        Args:
            defect_data: Dict com dados de defeitos
            
        Returns:
            Dict com densidades calculadas
        """
        pass  # IMPLEMENTAR
    
    # TODO: Implementar método calculate_dre
    def calculate_dre(self, pre_production: int, post_production: int) -> MetricResult:
        """
        Calcula Defect Removal Efficiency (DRE).
        
        Args:
            pre_production: Defeitos encontrados antes da produção
            post_production: Defeitos encontrados após a produção
            
        Returns:
            MetricResult com DRE calculado
        """
        pass  # IMPLEMENTAR
    
    # TODO: Implementar método calculate_mttd
    def calculate_mttd(self, time_data: List[Dict[str, str]]) -> MetricResult:
        """
        Calcula Mean Time to Detection (MTTD).
        
        Args:
            time_data: Lista de dicts com datas de introdução e detecção
            
        Returns:
            MetricResult com MTTD em dias
        """
        pass  # IMPLEMENTAR
    
    def _validate_coverage_data(self, data: Dict[str, int]) -> None:
        """Valida dados de entrada para cobertura."""
        required_keys = [
            "lines_executed", "total_lines",
            "branches_executed", "total_branches", 
            "functions_tested", "total_functions"
        ]
        
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Chave obrigatória '{key}' não encontrada")
            if not isinstance(data[key], int) or data[key] < 0:
                raise ValueError(f"Valor para '{key}' deve ser inteiro não-negativo")
        
        # Validar que executados não excedem totais
        if data["lines_executed"] > data["total_lines"]:
            raise ValueError("Linhas executadas não podem exceder total")
        if data["branches_executed"] > data["total_branches"]:
            raise ValueError("Branches executados não podem exceder total")
        if data["functions_tested"] > data["total_functions"]:
            raise ValueError("Funções testadas não podem exceder total")

def main():
    """Função principal para demonstrar o uso da calculadora."""
    calculator = BasicMetricsCalculator()
    
    # Dados de exemplo
    coverage_data = {
        "lines_executed": 1247,
        "total_lines": 1580,
        "branches_executed": 89,
        "total_branches": 112,
        "functions_tested": 45,
        "total_functions": 52
    }
    
    defect_data = {
        "pre_production_defects": 23,
        "post_production_defects": 4,
        "total_lines_of_code": 15800,
        "defects_by_module": {
            "authentication": 5,
            "payment": 8,
            "user_interface": 7,
            "database": 3
        }
    }
    
    time_data = [
        {"introduced": "2024-01-15", "detected": "2024-01-18"},
        {"introduced": "2024-01-20", "detected": "2024-01-25"},
        {"introduced": "2024-01-22", "detected": "2024-01-24"}
    ]
    
    # TODO: Chamar métodos e exibir resultados
    print("=== CALCULADORA DE MÉTRICAS FUNDAMENTAIS ===")
    print()
    
    # Exemplo de uso:
    # coverage_results = calculator.calculate_coverage(coverage_data)
    # for metric_type, result in coverage_results.items():
    #     print(f"{result.name}: {result.value}{result.unit} - {result.interpretation}")

if __name__ == "__main__":
    main()
```

## Casos de Teste

Implemente e execute os seguintes casos de teste para validar sua implementação:

### Teste 1: Cobertura Perfeita
```python
perfect_coverage = {
    "lines_executed": 100,
    "total_lines": 100,
    "branches_executed": 50,
    "total_branches": 50,
    "functions_tested": 25,
    "total_functions": 25
}
# Resultado esperado: Todas as coberturas = 100.00%
```

### Teste 2: DRE Alto
```python
# 95 defeitos pré-produção, 5 pós-produção
# DRE esperado = (95/(95+5)) × 100 = 95.00%
```

### Teste 3: Densidade Alta
```python
# 50 defeitos em 10.000 linhas
# Densidade esperada = (50/10000) × 1000 = 5.00 defeitos/KLOC
```

### Teste 4: MTTD com Dados Variados
```python
# 3 defeitos: 3 dias, 5 dias, 2 dias para detecção
# MTTD esperado = (3+5+2)/3 = 3.33 dias
```

## Critérios de Avaliação

| Aspecto | Excelente (4) | Bom (3) | Satisfatório (2) | Insuficiente (1) |
|---------|---------------|---------|------------------|------------------|
| **Correção das Fórmulas** | Todas as métricas implementadas corretamente | 3-4 métricas corretas | 2 métricas corretas | ≤1 métrica correta |
| **Validação de Entrada** | Validação robusta com mensagens claras | Validação básica adequada | Validação parcial | Pouca ou nenhuma validação |
| **Organização do Código** | Código bem estruturado e legível | Estrutura clara | Estrutura adequada | Código desorganizado |
| **Documentação** | Docstrings completas e comentários explicativos | Documentação adequada | Documentação básica | Pouca documentação |

## Dicas de Implementação

💡 **Comece pela validação:** Implemente primeiro os métodos de validação para garantir entrada consistente  

💡 **Use type hints:** Aproveite as anotações de tipo para documentar interfaces  

💡 **Teste incrementalmente:** Teste cada método conforme implementa  

💡 **Trate edge cases:** Considere divisão por zero e valores extremos  

💡 **Mensagens informativas:** Forneça interpretações contextuais dos resultados  

## Entregáveis

1. **`metrics_calculator.py`** - Implementação completa da calculadora
2. **`test_calculator.py`** - Script com casos de teste demonstrando funcionamento
3. **`relatorio.md`** - Breve relatório (2-3 parágrafos) com:
   - Principais desafios encontrados
   - Lições aprendidas sobre as métricas
   - Reflexão sobre aplicabilidade em projetos reais

## Extensões Opcionais (Bônus)

Para ir além do básico:

🎯 **Relatório formatado:** Gere saída em formato tabular organizado  
🎯 **Gráfico ASCII:** Crie barras de progresso simples para visualizar coberturas  
🎯 **Comparação histórica:** Permita comparar métricas com resultados anteriores  
🎯 **Export JSON:** Salve resultados em formato estruturado para posterior análise  

---

**Tempo para começar! Lembre-se: a compreensão é mais importante que a velocidade.** 🚀
