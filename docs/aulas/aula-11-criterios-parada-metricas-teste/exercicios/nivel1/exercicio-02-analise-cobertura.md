# Exercício 02 - Análise de Cobertura de Código 🔵

**Nível:** Básico  
**Tempo Estimado:** 25-35 minutos  
**Objetivo:** Analisar e interpretar dados reais de cobertura de código

## Contexto

Você recebeu relatórios de cobertura de código de três projetos diferentes e precisa analisá-los para determinar qual está pronto para release. Cada projeto tem características específicas e critérios de qualidade diferentes.

Como analista de qualidade, você deve interpretar os dados de cobertura não apenas numericamente, mas considerando o contexto de cada projeto e identificar pontos de atenção que podem indicar problemas ocultos.

## Cenário

### Projeto A - Sistema Bancário (Crítico)
**Contexto:** Sistema de transferências financeiras com regulamentação rigorosa  
**Critério de Cobertura:** Mínimo 95% para módulos críticos, 85% geral

```python
projeto_a_data = {
    "modulos": {
        "transferencia": {
            "lines_total": 450,
            "lines_covered": 441,
            "branches_total": 89,
            "branches_covered": 87,
            "functions_total": 23,
            "functions_covered": 23,
            "critico": True
        },
        "autenticacao": {
            "lines_total": 320,
            "lines_covered": 312,
            "branches_total": 56,
            "branches_covered": 54,
            "functions_total": 18,
            "functions_covered": 18,
            "critico": True
        },
        "relatorios": {
            "lines_total": 280,
            "lines_covered": 238,
            "branches_total": 34,
            "branches_covered": 29,
            "functions_total": 15,
            "functions_covered": 14,
            "critico": False
        },
        "configuracao": {
            "lines_total": 150,
            "lines_covered": 120,
            "branches_total": 12,
            "branches_covered": 9,
            "functions_total": 8,
            "functions_covered": 7,
            "critico": False
        }
    }
}
```

### Projeto B - E-commerce (Médio)
**Contexto:** Plataforma de vendas online com foco em experiência do usuário  
**Critério de Cobertura:** Mínimo 80% geral, 90% para checkout

```python
projeto_b_data = {
    "modulos": {
        "checkout": {
            "lines_total": 380,
            "lines_covered": 342,
            "branches_total": 67,
            "branches_covered": 62,
            "functions_total": 19,
            "functions_covered": 18,
            "critico": True
        },
        "catalogo": {
            "lines_total": 520,
            "lines_covered": 468,
            "branches_total": 78,
            "branches_covered": 71,
            "functions_total": 28,
            "functions_covered": 26,
            "critico": False
        },
        "usuario": {
            "lines_total": 290,
            "lines_covered": 247,
            "branches_total": 45,
            "branches_covered": 39,
            "functions_total": 16,
            "functions_covered": 15,
            "critico": False
        },
        "promocoes": {
            "lines_total": 180,
            "lines_covered": 126,
            "branches_total": 28,
            "branches_covered": 18,
            "functions_total": 12,
            "functions_covered": 9,
            "critico": False
        }
    }
}
```

### Projeto C - Blog (Baixo)
**Contexto:** Sistema de blog corporativo com requisitos relaxados  
**Critério de Cobertura:** Mínimo 70% geral

```python
projeto_c_data = {
    "modulos": {
        "posts": {
            "lines_total": 340,
            "lines_covered": 272,
            "branches_total": 42,
            "branches_covered": 35,
            "functions_total": 18,
            "functions_covered": 16,
            "critico": False
        },
        "comentarios": {
            "lines_total": 220,
            "lines_covered": 176,
            "branches_total": 31,
            "branches_covered": 26,
            "functions_total": 14,
            "functions_covered": 12,
            "critico": False
        },
        "admin": {
            "lines_total": 190,
            "lines_covered": 133,
            "branches_total": 24,
            "branches_covered": 17,
            "functions_total": 11,
            "functions_covered": 8,
            "critico": False
        }
    }
}
```

## Requisitos Funcionais

### RF01 - Cálculo de Cobertura por Módulo
Para cada módulo de cada projeto, calcular:
- Cobertura de linha (%)
- Cobertura de branch (%)  
- Cobertura de função (%)

### RF02 - Análise Agregada por Projeto
Para cada projeto, calcular:
- Cobertura geral ponderada por tamanho dos módulos
- Cobertura média dos módulos críticos
- Identificação de módulos abaixo do critério

### RF03 - Classificação de Qualidade
Classificar cada projeto como:
- ✅ **APROVADO:** Atende todos os critérios
- ⚠️ **ATENÇÃO:** Atende critérios mas tem pontos de atenção
- ❌ **REPROVADO:** Não atende critérios mínimos

### RF04 - Relatório de Recomendações
Para cada projeto, gerar recomendações específicas de melhoria.

## Estrutura de Código Base

```python
"""
coverage_analyzer.py

Analisador de cobertura de código para múltiplos projetos.
Calcula métricas e fornece recomendações contextualizadas.
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class ProjectStatus(Enum):
    """Status de aprovação do projeto baseado em cobertura."""
    APPROVED = "✅ APROVADO"
    ATTENTION = "⚠️ ATENÇÃO"
    REJECTED = "❌ REPROVADO"

@dataclass
class ModuleCoverage:
    """Cobertura calculada para um módulo específico."""
    name: str
    line_coverage: float
    branch_coverage: float
    function_coverage: float
    is_critical: bool
    meets_criteria: bool

@dataclass
class ProjectAnalysis:
    """Análise completa de cobertura para um projeto."""
    name: str
    overall_coverage: float
    critical_coverage: float
    module_analyses: List[ModuleCoverage]
    status: ProjectStatus
    recommendations: List[str]

class CoverageAnalyzer:
    """
    Analisador principal de cobertura de código.
    
    Responsável por calcular métricas, aplicar critérios
    contextualizados e gerar recomendações.
    """
    
    def __init__(self):
        """Inicializa analisador com configurações padrão."""
        self.precision = 2
        
    def analyze_project(self, project_name: str, 
                       project_data: Dict, 
                       criteria: Dict[str, float]) -> ProjectAnalysis:
        """
        Analisa cobertura completa de um projeto.
        
        Args:
            project_name: Nome do projeto
            project_data: Dados de cobertura dos módulos
            criteria: Critérios de cobertura (geral, crítico)
            
        Returns:
            ProjectAnalysis com análise completa
        """
        # TODO: Implementar análise completa
        pass
    
    def calculate_module_coverage(self, module_data: Dict[str, int]) -> Tuple[float, float, float]:
        """
        Calcula cobertura de um módulo específico.
        
        Args:
            module_data: Dados do módulo (lines, branches, functions)
            
        Returns:
            Tuple com (line_coverage, branch_coverage, function_coverage)
        """
        # TODO: Implementar cálculo de cobertura
        pass
    
    def calculate_weighted_coverage(self, modules_data: Dict) -> float:
        """
        Calcula cobertura geral ponderada pelo tamanho dos módulos.
        
        Args:
            modules_data: Dados de todos os módulos
            
        Returns:
            Cobertura ponderada (0-100)
        """
        # TODO: Implementar cálculo ponderado
        pass
    
    def determine_project_status(self, analysis: ProjectAnalysis, 
                               criteria: Dict[str, float]) -> ProjectStatus:
        """
        Determina status do projeto baseado nos critérios.
        
        Args:
            analysis: Análise calculada do projeto
            criteria: Critérios de aprovação
            
        Returns:
            ProjectStatus apropriado
        """
        # TODO: Implementar determinação de status
        pass
    
    def generate_recommendations(self, analysis: ProjectAnalysis) -> List[str]:
        """
        Gera recomendações específicas para melhoria.
        
        Args:
            analysis: Análise do projeto
            
        Returns:
            Lista de recomendações contextualizadas
        """
        # TODO: Implementar geração de recomendações
        pass
    
    def generate_detailed_report(self, analyses: List[ProjectAnalysis]) -> str:
        """
        Gera relatório detalhado comparativo entre projetos.
        
        Args:
            analyses: Lista de análises de projetos
            
        Returns:
            Relatório formatado em texto
        """
        # TODO: Implementar geração de relatório
        pass

def main():
    """Função principal para análise dos três projetos."""
    analyzer = CoverageAnalyzer()
    
    # Dados dos projetos (fornecidos no enunciado)
    projects = {
        "Sistema Bancário": {
            "data": projeto_a_data,
            "criteria": {"geral": 85.0, "critico": 95.0}
        },
        "E-commerce": {
            "data": projeto_b_data, 
            "criteria": {"geral": 80.0, "critico": 90.0}
        },
        "Blog": {
            "data": projeto_c_data,
            "criteria": {"geral": 70.0, "critico": 70.0}
        }
    }
    
    analyses = []
    
    print("=== ANÁLISE DE COBERTURA DE CÓDIGO ===")
    print()
    
    # TODO: Analisar cada projeto e gerar relatório
    # for name, config in projects.items():
    #     analysis = analyzer.analyze_project(name, config["data"], config["criteria"])
    #     analyses.append(analysis)
    #     print(f"Projeto: {analysis.name}")
    #     print(f"Status: {analysis.status.value}")
    #     print()
    
    # TODO: Gerar relatório comparativo final

if __name__ == "__main__":
    main()
```

## Tarefas Específicas

### Tarefa 1: Implementação dos Cálculos
Implemente todos os métodos de cálculo de cobertura seguindo as fórmulas da aula teórica.

### Tarefa 2: Análise Contextualizada  
Para cada projeto, considere:
- **Criticidade do domínio** (bancário vs. blog)
- **Módulos críticos** vs. não-críticos
- **Distribuição da cobertura** entre módulos

### Tarefa 3: Identificação de Anomalias
Identifique e reporte:
- Módulos com cobertura desbalanceada (alta em linha, baixa em branch)
- Diferenças significativas entre tipos de cobertura
- Módulos críticos abaixo do critério

### Tarefa 4: Recomendações Priorizadas
Para cada projeto com problemas, forneça recomendações priorizadas por impacto e esforço.

## Resultados Esperados

### Sistema Bancário
- **Status esperado:** ⚠️ ATENÇÃO
- **Problema principal:** Módulo "configuracao" abaixo do critério geral
- **Cobertura crítica:** Deve estar acima de 95%

### E-commerce  
- **Status esperado:** ⚠️ ATENÇÃO
- **Problema principal:** Módulo "promocoes" muito baixo (70%)
- **Checkout:** Verificar se atende critério de 90%

### Blog
- **Status esperado:** ✅ APROVADO
- **Observação:** Critérios mais relaxados devido ao contexto

## Critérios de Avaliação

| Aspecto | Peso | Descrição |
|---------|------|-----------|
| **Cálculos Corretos** | 35% | Fórmulas implementadas corretamente |
| **Análise Contextual** | 25% | Consideração adequada do contexto de cada projeto |
| **Identificação de Problemas** | 20% | Detecção de módulos problemáticos |
| **Recomendações Úteis** | 20% | Sugestões práticas e priorizadas |

## Dicas de Implementação

💡 **Ponderação por tamanho:** Use linhas totais como peso para cobertura geral  

💡 **Threshold de atenção:** Considere módulos com diferença >10% entre tipos de cobertura  

💡 **Priorização crítica:** Módulos críticos devem ter peso maior na análise  

💡 **Recomendações específicas:** Evite sugestões genéricas, foque em módulos específicos  

## Entregáveis

1. **`coverage_analyzer.py`** - Implementação completa do analisador
2. **`analysis_report.txt`** - Relatório de análise dos três projetos  
3. **`reflexao.md`** - Reflexão sobre:
   - Diferenças entre contextos críticos e não-críticos
   - Importância da análise qualitativa vs. quantitativa
   - Lições sobre interpretação de métricas

## Questões para Reflexão

🤔 **Por que cobertura 100% pode não ser desejável em todos os contextos?**

🤔 **Como balancear rigor técnico com pragmatismo comercial?**

🤔 **Qual a relação entre cobertura de branch e qualidade real dos testes?**

🤔 **Como priorizar esforços de melhoria com recursos limitados?**

---

**Foque na interpretação inteligente, não apenas no cálculo mecânico!** 🔍
