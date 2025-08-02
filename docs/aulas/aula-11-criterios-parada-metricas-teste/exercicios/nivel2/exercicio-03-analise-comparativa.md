# Exercício 03 - Análise Comparativa Multi-Projeto 🟡

**Nível:** Intermediário  
**Tempo Estimado:** 80-90 minutos  
**Objetivo:** Desenvolver sistema de análise comparativa para avaliar eficácia de critérios entre projetos

## Contexto

Como líder técnico de uma empresa de consultoria em qualidade de software, você precisa demonstrar para um cliente o valor dos investimentos em testes e a importância de critérios de parada bem definidos. O cliente quer evidências concretas de como diferentes estratégias de teste impactam nos resultados finais.

Você possui dados históricos de 15 projetos similares que utilizaram estratégias diferentes de teste e precisa criar um sistema de análise comparativa que demonstre claramente a correlação entre rigor dos critérios de parada e sucesso do projeto em produção.

## Dataset Histórico

### Projetos de E-commerce (Setor Varejista)

```python
ecommerce_projects = [
    {
        "project_id": "ECOM-001",
        "project_name": "Loja Fashion Online",
        "criteria_approach": "minimal",
        "test_coverage": 45.2,
        "dre": 65.0,
        "test_execution_time": 15,  # dias
        "post_release_defects": 47,
        "customer_satisfaction": 3.2,
        "revenue_impact": -12.5,  # % de impacto
        "maintenance_cost": 85000,  # em R$
        "team_productivity": 2.1  # story points/sprint
    },
    {
        "project_id": "ECOM-002", 
        "project_name": "Marketplace B2B",
        "criteria_approach": "rigorous",
        "test_coverage": 91.8,
        "dre": 94.2,
        "test_execution_time": 45,
        "post_release_defects": 8,
        "customer_satisfaction": 4.6,
        "revenue_impact": +8.3,
        "maintenance_cost": 23000,
        "team_productivity": 3.8
    },
    {
        "project_id": "ECOM-003",
        "project_name": "App Mobile Shopping",
        "criteria_approach": "balanced",
        "test_coverage": 78.5,
        "dre": 87.1,
        "test_execution_time": 28,
        "post_release_defects": 19,
        "customer_satisfaction": 4.1,
        "revenue_impact": +2.7,
        "maintenance_cost": 41000,
        "team_productivity": 3.2
    },
    # TODO: Adicionar mais 12 projetos para análise robusta
]
```

### Projetos FinTech (Setor Financeiro)

```python
fintech_projects = [
    {
        "project_id": "FIN-001",
        "project_name": "Digital Banking Core",
        "criteria_approach": "ultra_rigorous",
        "test_coverage": 98.7,
        "dre": 99.1,
        "test_execution_time": 75,
        "post_release_defects": 2,
        "customer_satisfaction": 4.8,
        "revenue_impact": +15.2,
        "maintenance_cost": 12000,
        "team_productivity": 4.1,
        "security_incidents": 0,
        "compliance_issues": 0
    },
    {
        "project_id": "FIN-002",
        "project_name": "Payment Gateway",
        "criteria_approach": "minimal",
        "test_coverage": 52.3,
        "dre": 71.2,
        "test_execution_time": 18,
        "post_release_defects": 31,
        "customer_satisfaction": 2.9,
        "revenue_impact": -18.7,
        "maintenance_cost": 127000,
        "team_productivity": 1.8,
        "security_incidents": 3,
        "compliance_issues": 2
    }
    # TODO: Adicionar mais projetos FinTech
]
```

## Requisitos Funcionais

### RF01 - Análise de Correlação
Implementar análise estatística que identifique:
- **Correlação** entre métricas de teste e sucesso pós-release
- **Pontos de inflexão** onde investimento adicional não se justifica
- **Indicadores preditivos** de sucesso baseados em métricas de teste
- **Patterns de falha** em projetos com critérios inadequados

### RF02 - Comparação Multi-Dimensional
Desenvolver comparação que avalie:
- **Eficiência de custo** (ROI do investimento em testes)
- **Trade-offs** entre tempo de teste e qualidade
- **Impacto setorial** (E-commerce vs FinTech vs outros)
- **Maturidade de equipe** vs resultados obtidos

### RF03 - Visualização Interativa
Criar visualizações que mostrem:
- **Scatter plots** com correlações identificadas
- **Heatmaps** de performance por categoria
- **Trends** temporais de melhoria
- **Benchmarks** por setor e abordagem

### RF04 - Sistema de Recomendações
Implementar sistema que sugira:
- **Critérios otimizados** baseados em dados históricos
- **Investimento ideal** em testes para contexto específico
- **Risk vs Reward** analysis para diferentes estratégias
- **Learning path** para equipes menos maduras

## Arquitetura do Sistema

```python
"""
comparative_analysis.py

Sistema de análise comparativa multi-projeto para avaliação
da eficácia de diferentes critérios de parada e estratégias
de teste baseado em dados históricos reais.
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum
import statistics
import math

class TestingApproach(Enum):
    """Abordagens de teste utilizadas nos projetos."""
    MINIMAL = "minimal"
    BALANCED = "balanced"
    RIGOROUS = "rigorous"
    ULTRA_RIGOROUS = "ultra_rigorous"

class ProjectSector(Enum):
    """Setores dos projetos analisados."""
    ECOMMERCE = "ecommerce"
    FINTECH = "fintech"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    GAMING = "gaming"

@dataclass
class ProjectMetrics:
    """Métricas completas de um projeto."""
    project_id: str
    project_name: str
    sector: ProjectSector
    criteria_approach: TestingApproach
    
    # Métricas de teste
    test_coverage: float
    dre: float
    test_execution_time: int
    
    # Métricas pós-release
    post_release_defects: int
    customer_satisfaction: float
    revenue_impact: float
    maintenance_cost: float
    team_productivity: float
    
    # Métricas opcionais (setor-específicas)
    security_incidents: Optional[int] = None
    compliance_issues: Optional[int] = None
    performance_sla_breaches: Optional[int] = None

@dataclass
class CorrelationResult:
    """Resultado de análise de correlação."""
    metric1: str
    metric2: str
    correlation_coefficient: float
    p_value: float
    significance_level: str
    interpretation: str

@dataclass
class ComparativeAnalysis:
    """Resultado completo da análise comparativa."""
    total_projects: int
    approaches_compared: List[TestingApproach]
    correlation_results: List[CorrelationResult]
    roi_analysis: Dict[TestingApproach, Dict]
    risk_analysis: Dict[TestingApproach, Dict]
    recommendations: List[str]
    executive_summary: str

class StatisticalAnalyzer:
    """
    Analisador estatístico para correlações e significância
    entre métricas de teste e resultados de negócio.
    """
    
    def __init__(self):
        """Inicializa analisador estatístico."""
        pass
    
    def calculate_correlation(self, x_values: List[float], 
                            y_values: List[float]) -> Tuple[float, float]:
        """
        Calcula coeficiente de correlação de Pearson e p-value.
        
        Args:
            x_values: Valores da primeira variável
            y_values: Valores da segunda variável
            
        Returns:
            Tuple com (correlation_coefficient, p_value)
        """
        if len(x_values) != len(y_values) or len(x_values) < 3:
            return 0.0, 1.0
        
        # TODO: Implementar cálculo de correlação de Pearson
        # TODO: Implementar cálculo de p-value usando distribuição t
        pass
    
    def interpret_correlation(self, correlation: float, p_value: float) -> str:
        """
        Interpreta resultado da correlação em linguagem natural.
        
        Args:
            correlation: Coeficiente de correlação
            p_value: P-value da correlação
            
        Returns:
            Interpretação textual do resultado
        """
        # TODO: Implementar interpretação baseada em força e significância
        pass
    
    def identify_outliers(self, values: List[float]) -> List[int]:
        """
        Identifica outliers usando método IQR.
        
        Args:
            values: Lista de valores para análise
            
        Returns:
            Lista de índices dos outliers
        """
        # TODO: Implementar detecção de outliers
        pass

class ProjectComparator:
    """
    Comparador de projetos que analisa diferentes abordagens
    de teste e seus impactos nos resultados de negócio.
    """
    
    def __init__(self):
        """Inicializa comparador com analisador estatístico."""
        self.statistical_analyzer = StatisticalAnalyzer()
        self.projects: List[ProjectMetrics] = []
    
    def add_project(self, project: ProjectMetrics) -> None:
        """
        Adiciona projeto ao dataset para análise.
        
        Args:
            project: Métricas do projeto
        """
        self.projects.append(project)
    
    def add_projects_batch(self, projects: List[ProjectMetrics]) -> None:
        """
        Adiciona múltiplos projetos ao dataset.
        
        Args:
            projects: Lista de projetos
        """
        self.projects.extend(projects)
    
    def analyze_approach_effectiveness(self) -> ComparativeAnalysis:
        """
        Realiza análise completa comparando eficácia das abordagens.
        
        Returns:
            ComparativeAnalysis com resultados completos
        """
        if len(self.projects) < 5:
            raise ValueError("Mínimo de 5 projetos necessário para análise")
        
        # TODO: Implementar análise completa
        pass
    
    def _analyze_correlations(self) -> List[CorrelationResult]:
        """
        Analisa correlações entre métricas de teste e resultados.
        
        Returns:
            Lista de resultados de correlação
        """
        correlations = []
        
        # Correlações importantes para analisar
        test_metrics = ['test_coverage', 'dre', 'test_execution_time']
        business_metrics = ['post_release_defects', 'customer_satisfaction', 
                          'revenue_impact', 'maintenance_cost']
        
        # TODO: Calcular correlações entre todas as combinações
        # TODO: Interpretar resultados e identificar correlações significativas
        
        return correlations
    
    def _calculate_roi_by_approach(self) -> Dict[TestingApproach, Dict]:
        """
        Calcula ROI para cada abordagem de teste.
        
        Returns:
            Dict com ROI por abordagem
        """
        roi_results = {}
        
        for approach in TestingApproach:
            approach_projects = [p for p in self.projects 
                               if p.criteria_approach == approach]
            
            if not approach_projects:
                continue
            
            # TODO: Calcular métricas de ROI
            # - Custo de teste vs redução de manutenção
            # - Tempo investido vs satisfação do cliente
            # - Impacto na receita vs investimento em qualidade
            
        return roi_results
    
    def _analyze_risk_patterns(self) -> Dict[TestingApproach, Dict]:
        """
        Analisa padrões de risco por abordagem.
        
        Returns:
            Dict com análise de risco por abordagem
        """
        # TODO: Implementar análise de padrões de risco
        # - Probabilidade de defeitos críticos
        # - Variabilidade dos resultados
        # - Impacto de falhas em produção
        pass
    
    def _generate_recommendations(self, analysis: ComparativeAnalysis) -> List[str]:
        """
        Gera recomendações baseadas na análise comparativa.
        
        Args:
            analysis: Resultado da análise comparativa
            
        Returns:
            Lista de recomendações específicas
        """
        # TODO: Implementar geração de recomendações inteligentes
        # baseadas nos padrões identificados
        pass
    
    def _create_executive_summary(self, analysis: ComparativeAnalysis) -> str:
        """
        Cria resumo executivo dos resultados.
        
        Args:
            analysis: Resultado da análise
            
        Returns:
            Resumo executivo em formato narrative
        """
        # TODO: Implementar geração de resumo executivo
        pass

class VisualizationGenerator:
    """
    Gerador de visualizações para análise comparativa.
    Simula gráficos através de representações textuais.
    """
    
    def __init__(self):
        """Inicializa gerador de visualizações."""
        pass
    
    def generate_correlation_heatmap(self, correlations: List[CorrelationResult]) -> str:
        """
        Gera representação textual de heatmap de correlações.
        
        Args:
            correlations: Lista de correlações calculadas
            
        Returns:
            Representação textual do heatmap
        """
        # TODO: Implementar geração de heatmap textual
        pass
    
    def generate_roi_comparison(self, roi_data: Dict[TestingApproach, Dict]) -> str:
        """
        Gera comparação visual de ROI por abordagem.
        
        Args:
            roi_data: Dados de ROI por abordagem
            
        Returns:
            Visualização textual da comparação
        """
        # TODO: Implementar comparação visual de ROI
        pass
    
    def generate_trend_analysis(self, projects: List[ProjectMetrics]) -> str:
        """
        Gera análise de tendências temporais.
        
        Args:
            projects: Lista de projetos para análise
            
        Returns:
            Visualização de tendências
        """
        # TODO: Implementar análise de tendências
        pass

def load_historical_data() -> List[ProjectMetrics]:
    """
    Carrega dados históricos de projetos para análise.
    Em implementação real, viria de database ou API.
    
    Returns:
        Lista de projetos com métricas completas
    """
    projects = []
    
    # TODO: Converter dados dos dicts para ProjectMetrics
    # TODO: Adicionar mais projetos para dataset robusto
    # TODO: Incluir validação de dados
    
    return projects

def main():
    """Função principal demonstrando análise comparativa."""
    print("=== ANÁLISE COMPARATIVA MULTI-PROJETO ===")
    print()
    
    # Carregar dados históricos
    projects = load_historical_data()
    
    # Inicializar comparador
    comparator = ProjectComparator()
    comparator.add_projects_batch(projects)
    
    # Realizar análise completa
    print("📊 Realizando análise comparativa...")
    # analysis = comparator.analyze_approach_effectiveness()
    
    # TODO: Exibir resultados da análise
    # TODO: Mostrar correlações mais significativas
    # TODO: Apresentar recomendações baseadas em dados
    # TODO: Gerar visualizações dos resultados
    
    print("✅ Análise concluída!")

if __name__ == "__main__":
    main()
```

## Tarefas Específicas

### Tarefa 1: Análise Estatística
Implemente análise robusta que:
- **Calcule correlações** entre métricas de teste e sucesso
- **Determine significância** estatística dos resultados
- **Identifique outliers** que podem distorcer conclusões
- **Valide** premissas estatísticas antes dos cálculos

### Tarefa 2: ROI Analysis
Desenvolva cálculo de ROI que considere:
- **Custo de execução** de testes vs economia em manutenção
- **Tempo investido** vs melhoria na satisfação do cliente
- **Impacto na receita** vs investimento em qualidade
- **Long-term benefits** vs short-term costs

### Tarefa 3: Pattern Recognition
Implemente reconhecimento de padrões que identifique:
- **Sweet spots** de investimento em teste
- **Red flags** que indicam critérios inadequados
- **Success patterns** que podem ser replicados
- **Risk indicators** baseados em métricas históricas

### Tarefa 4: Recommendation Engine
Crie sistema de recomendações que:
- **Sugira estratégias** baseadas em contexto similar
- **Quantifique benefícios** esperados de mudanças
- **Identifique próximos passos** para melhoria
- **Priorize investimentos** baseado em ROI potencial

## Resultados Esperados

### Correlações Identificadas
- **Coverage vs Defects:** r = -0.74 (correlação forte negativa)
- **DRE vs Customer Satisfaction:** r = 0.68 (correlação positiva)
- **Test Time vs Revenue Impact:** Relação não-linear identificada

### ROI por Abordagem
- **Minimal:** ROI = -23% (prejuízo)
- **Balanced:** ROI = +45% (positivo)
- **Rigorous:** ROI = +89% (muito positivo)
- **Ultra-Rigorous:** ROI = +67% (decresce por over-testing)

## Critérios de Avaliação

| Aspecto | Peso | Descrição |
|---------|------|-----------|
| **Análise Estatística** | 30% | Precisão dos cálculos e interpretações |
| **Insights de Negócio** | 25% | Qualidade das descobertas e recomendações |
| **Visualização** | 20% | Clareza e utilidade das representações |
| **Robustez** | 25% | Tratamento de edge cases e validações |

## Entregáveis

1. **`comparative_analysis.py`** - Sistema completo
2. **`historical_data.json`** - Dataset expandido com 15+ projetos
3. **`correlation_report.md`** - Relatório detalhado das correlações
4. **`roi_calculator.py`** - Calculadora de ROI por estratégia
5. **`business_case.pdf`** - Apresentação executiva dos resultados

---

**Foque em insights acionáveis baseados em dados reais!** 📈
