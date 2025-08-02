# Exercício 01 - Sistema de Monitoramento de Métricas 🟡

**Nível:** Intermediário  
**Tempo Estimado:** 60-90 minutos  
**Objetivo:** Desenvolver sistema completo de monitoramento contínuo de métricas

## Contexto

Você foi contratado por uma empresa de tecnologia em crescimento para desenvolver um sistema de monitoramento que acompanhe métricas de teste em tempo real para múltiplos projetos. O sistema deve coletar dados automaticamente, detectar anomalias, e alertar a equipe quando critérios críticos estão sendo violados.

A empresa tem 3 projetos em desenvolvimento simultâneo com diferentes características e necessidades de monitoramento. O sistema deve ser flexível para acomodar diferentes tipos de projeto e extensível para futuras métricas.

## Requisitos do Sistema

### RF01 - Coleta Automática de Métricas
Implementar sistema que simule coleta automática de métricas:
- **Cobertura de código** (linha, branch, função)
- **Densidade de defeitos** por módulo
- **Tempo médio de detecção** de defeitos
- **Taxa de descoberta** de defeitos (defeitos/dia)
- **Performance de testes** (tempo de execução)

### RF02 - Detecção de Anomalias
Identificar automaticamente:
- **Degradação súbita** (queda >10% em métricas críticas)
- **Tendências negativas** (declínio consistente por 3+ medições)
- **Violação de thresholds** críticos
- **Padrões irregulares** (variabilidade excessiva)

### RF03 - Sistema de Alertas
Implementar alertas em três níveis:
- 🔴 **CRÍTICO:** Violação de critérios obrigatórios  
- 🟡 **ATENÇÃO:** Tendências preocupantes
- 🔵 **INFO:** Marcos atingidos ou melhorias detectadas

### RF04 - Dashboard Textual
Gerar dashboard em tempo real mostrando:
- Status atual de cada projeto
- Histórico de métricas (últimas 10 medições)
- Alertas ativos
- Tendências identificadas

### RF05 - Relatórios Periódicos
Gerar relatórios automáticos:
- **Diário:** Resumo de atividades e alertas
- **Semanal:** Análise de tendências e recomendações
- **Mensal:** Comparativo entre projetos e benchmarks

## Arquitetura do Sistema

```python
"""
metrics_monitor.py

Sistema de monitoramento contínuo de métricas de teste.
Coleta dados, detecta anomalias e gera alertas automaticamente.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import json
import statistics

class AlertLevel(Enum):
    """Níveis de alerta do sistema."""
    CRITICAL = "🔴 CRÍTICO"
    WARNING = "🟡 ATENÇÃO"  
    INFO = "🔵 INFO"

class TrendType(Enum):
    """Tipos de tendência detectados."""
    IMPROVING = "melhorando"
    STABLE = "estável"
    DEGRADING = "degradando"
    VOLATILE = "volátil"

@dataclass
class MetricSnapshot:
    """Snapshot de uma métrica em um momento específico."""
    timestamp: datetime
    value: float
    metadata: Dict = field(default_factory=dict)

@dataclass
class Alert:
    """Alerta gerado pelo sistema de monitoramento."""
    level: AlertLevel
    project: str
    metric: str
    message: str
    timestamp: datetime
    current_value: float
    threshold_value: Optional[float] = None
    recommendation: Optional[str] = None

@dataclass
class ProjectMetrics:
    """Conjunto de métricas para um projeto específico."""
    project_name: str
    coverage_line: List[MetricSnapshot]
    coverage_branch: List[MetricSnapshot]
    defect_density: List[MetricSnapshot]
    mttd: List[MetricSnapshot]
    discovery_rate: List[MetricSnapshot]
    test_performance: List[MetricSnapshot]
    last_updated: datetime

class MetricsCollector:
    """
    Simulador de coleta de métricas para desenvolvimento.
    Em produção, integraria com ferramentas reais.
    """
    
    def __init__(self):
        """Inicializa coletor com configurações base."""
        self.simulation_variance = 0.05  # 5% de variação simulada
        
    def collect_project_metrics(self, project_name: str, 
                               base_values: Dict[str, float]) -> Dict[str, float]:
        """
        Simula coleta de métricas com variação realística.
        
        Args:
            project_name: Nome do projeto
            base_values: Valores base para simulação
            
        Returns:
            Dict com métricas coletadas
        """
        # TODO: Implementar simulação realística de coleta
        pass
    
    def _add_realistic_variance(self, base_value: float, 
                               metric_type: str) -> float:
        """
        Adiciona variação realística baseada no tipo de métrica.
        
        Args:
            base_value: Valor base da métrica
            metric_type: Tipo de métrica para variação apropriada
            
        Returns:
            Valor com variação aplicada
        """
        # TODO: Implementar variação por tipo de métrica
        pass

class AnomalyDetector:
    """
    Detector de anomalias e tendências em métricas.
    Usa análise estatística simples para identificar padrões.
    """
    
    def __init__(self, min_data_points: int = 5):
        """
        Inicializa detector com parâmetros de análise.
        
        Args:
            min_data_points: Mínimo de pontos para análise de tendência
        """
        self.min_data_points = min_data_points
        self.anomaly_threshold = 2.0  # Desvios padrão para anomalia
        
    def detect_anomalies(self, snapshots: List[MetricSnapshot],
                        metric_name: str) -> List[Alert]:
        """
        Detecta anomalias em uma série temporal de métricas.
        
        Args:
            snapshots: Lista de snapshots históricos
            metric_name: Nome da métrica sendo analisada
            
        Returns:
            Lista de alertas gerados
        """
        # TODO: Implementar detecção de anomalias
        pass
    
    def analyze_trend(self, snapshots: List[MetricSnapshot]) -> TrendType:
        """
        Analisa tendência geral dos dados.
        
        Args:
            snapshots: Lista de snapshots para análise
            
        Returns:
            TrendType identificado
        """
        # TODO: Implementar análise de tendência
        pass
    
    def _detect_sudden_degradation(self, snapshots: List[MetricSnapshot]) -> bool:
        """
        Detecta degradação súbita (>10% queda entre medições consecutivas).
        
        Args:
            snapshots: Lista de snapshots para análise
            
        Returns:
            True se degradação súbita for detectada
        """
        # TODO: Implementar detecção de degradação súbita
        pass
    
    def _detect_threshold_violation(self, current_value: float,
                                  threshold: float,
                                  operator: str) -> bool:
        """
        Detecta violação de threshold configurado.
        
        Args:
            current_value: Valor atual da métrica
            threshold: Valor limite configurado
            operator: Operador de comparação (>=, <=, etc.)
            
        Returns:
            True se violação for detectada
        """
        # TODO: Implementar detecção de violação
        pass

class MetricsMonitor:
    """
    Sistema principal de monitoramento de métricas.
    Orquestra coleta, análise e geração de alertas.
    """
    
    def __init__(self):
        """Inicializa sistema de monitoramento."""
        self.projects: Dict[str, ProjectMetrics] = {}
        self.collector = MetricsCollector()
        self.detector = AnomalyDetector()
        self.thresholds = self._load_default_thresholds()
        self.active_alerts: List[Alert] = []
        
    def register_project(self, project_name: str, 
                        initial_config: Dict[str, float]) -> None:
        """
        Registra novo projeto para monitoramento.
        
        Args:
            project_name: Nome do projeto
            initial_config: Configuração inicial e valores base
        """
        # TODO: Implementar registro de projeto
        pass
    
    def update_project_metrics(self, project_name: str) -> List[Alert]:
        """
        Atualiza métricas de um projeto e detecta anomalias.
        
        Args:
            project_name: Nome do projeto a ser atualizado
            
        Returns:
            Lista de novos alertas gerados
        """
        # TODO: Implementar atualização e análise
        pass
    
    def get_project_status(self, project_name: str) -> Dict:
        """
        Retorna status atual completo de um projeto.
        
        Args:
            project_name: Nome do projeto
            
        Returns:
            Dict com status detalhado
        """
        # TODO: Implementar geração de status
        pass
    
    def generate_dashboard(self) -> str:
        """
        Gera dashboard textual com status de todos os projetos.
        
        Returns:
            Dashboard formatado em texto
        """
        # TODO: Implementar geração de dashboard
        pass
    
    def generate_daily_report(self) -> str:
        """
        Gera relatório diário de atividades.
        
        Returns:
            Relatório formatado
        """
        # TODO: Implementar relatório diário
        pass
    
    def _load_default_thresholds(self) -> Dict[str, Dict]:
        """
        Carrega thresholds padrão para detecção de anomalias.
        
        Returns:
            Dict com thresholds por métrica
        """
        return {
            "coverage_line": {"min": 80.0, "critical": 70.0},
            "coverage_branch": {"min": 75.0, "critical": 65.0},
            "defect_density": {"max": 5.0, "critical": 10.0},
            "mttd": {"max": 7.0, "critical": 14.0},  # dias
            "discovery_rate": {"min": 0.5, "max": 10.0},  # defeitos/dia
            "test_performance": {"max": 300.0, "critical": 600.0}  # segundos
        }

# Configuração dos projetos simulados
PROJECTS_CONFIG = {
    "E-commerce": {
        "coverage_line": 85.0,
        "coverage_branch": 78.0, 
        "defect_density": 3.2,
        "mttd": 4.5,
        "discovery_rate": 2.1,
        "test_performance": 180.0
    },
    "Mobile App": {
        "coverage_line": 72.0,
        "coverage_branch": 68.0,
        "defect_density": 4.8,
        "mttd": 6.2,
        "discovery_rate": 3.4,
        "test_performance": 95.0
    },
    "API Gateway": {
        "coverage_line": 92.0,
        "coverage_branch": 89.0,
        "defect_density": 1.8,
        "mttd": 2.1,
        "discovery_rate": 1.2,
        "test_performance": 45.0
    }
}

def main():
    """Função principal que demonstra o sistema de monitoramento."""
    monitor = MetricsMonitor()
    
    print("=== SISTEMA DE MONITORAMENTO DE MÉTRICAS ===")
    print()
    
    # Registrar projetos
    for project_name, config in PROJECTS_CONFIG.items():
        monitor.register_project(project_name, config)
        print(f"✓ Projeto '{project_name}' registrado para monitoramento")
    
    print()
    print("🔄 Iniciando simulação de monitoramento...")
    print()
    
    # TODO: Simular 24 horas de monitoramento com coletas periódicas
    # for hour in range(24):
    #     print(f"--- Hora {hour:02d}:00 ---")
    #     
    #     for project_name in PROJECTS_CONFIG.keys():
    #         alerts = monitor.update_project_metrics(project_name)
    #         if alerts:
    #             for alert in alerts:
    #                 print(f"{alert.level.value}: {alert.message}")
    #     
    #     # Exibir dashboard a cada 6 horas
    #     if hour % 6 == 0:
    #         print("\n📊 DASHBOARD ATUAL:")
    #         print(monitor.generate_dashboard())
    
    # TODO: Gerar relatório final
    # print("\n📋 RELATÓRIO DIÁRIO:")
    # print(monitor.generate_daily_report())

if __name__ == "__main__":
    main()
```

## Tarefas Específicas

### Tarefa 1: Implementação da Coleta Simulada
Crie simulação realística que:
- Varie métricas de forma coerente (cobertura não muda drasticamente)
- Introduza ocasionalmente "eventos" (picos de defeitos, degradação)
- Mantenha padrões consistentes com o tipo de projeto

### Tarefa 2: Detecção de Anomalias
Implemente algoritmos para detectar:
- **Anomalias estatísticas** (valores fora de 2 desvios padrão)
- **Tendências negativas** (regressão linear com slope negativo)
- **Violações de threshold** (valores absolutos críticos)
- **Variabilidade excessiva** (coeficiente de variação alto)

### Tarefa 3: Sistema de Alertas Inteligente
Desenvolva sistema que:
- **Priorize alertas** por criticidade e impacto
- **Evite spam** (não alerte repetidamente pelo mesmo problema)
- **Forneça contexto** (tendência histórica, comparação com outros projetos)
- **Sugira ações** específicas para cada tipo de problema

### Tarefa 4: Dashboard Informativo
Crie dashboard que mostre:
- **Status visual** de cada projeto (🟢🟡🔴)
- **Métricas atuais** vs. targets
- **Alertas ativos** organizados por prioridade
- **Tendências recentes** (últimas 5 medições)

## Cenários de Teste

### Cenário 1: Degradação Gradual
Simule projeto onde cobertura diminui gradualmente de 85% para 75% ao longo de 12 horas.
**Resultado esperado:** Alerta de tendência negativa após 3-4 medições consecutivas.

### Cenário 2: Pico de Defeitos
Simule descoberta súbita de 8 defeitos em uma medição (vs. média de 2).
**Resultado esperado:** Alerta crítico de anomalia estatística.

### Cenário 3: Melhoria Consistente
Simule projeto com melhoria constante em todas as métricas.
**Resultado esperado:** Alertas informativos de marcos atingidos.

### Cenário 4: Estabilidade com Ruído
Simule métricas estáveis com variação normal (±2%).
**Resultado esperado:** Nenhum alerta, status estável.

## Critérios de Avaliação

| Aspecto | Excelente (4) | Bom (3) | Satisfatório (2) | Insuficiente (1) |
|---------|---------------|---------|------------------|------------------|
| **Arquitetura do Sistema** | Bem estruturado, extensível e modular | Estrutura clara e funcional | Estrutura básica adequada | Estrutura confusa ou monolítica |
| **Detecção de Anomalias** | Algoritmos robustos e configuráveis | Detecção efetiva com alguns gaps | Detecção básica funcional | Detecção inadequada ou incorreta |
| **Sistema de Alertas** | Alertas inteligentes e acionáveis | Alertas úteis e bem categorizados | Alertas básicos funcionais | Alertas confusos ou irrelevantes |
| **Dashboard e Relatórios** | Interface clara e informativa | Apresentação adequada | Informação básica organizada | Apresentação pobre ou confusa |

## Dicas de Implementação

💡 **Comece simples:** Implemente funcionalidade básica antes de adicionar sofisticação  

💡 **Use estatísticas:** Aproveite o módulo `statistics` para cálculos de tendência  

💡 **Estado persistente:** Mantenha histórico das métricas para análise temporal  

💡 **Configurabilidade:** Permita ajustar thresholds e parâmetros de detecção  

💡 **Testes incrementais:** Teste cada componente separadamente primeiro  

## Entregáveis

1. **`metrics_monitor.py`** - Sistema completo de monitoramento
2. **`simulation_results.txt`** - Log de 24h de simulação mostrando alertas
3. **`dashboard_samples.txt`** - Exemplos de dashboard em diferentes momentos
4. **`architecture_doc.md`** - Documentação da arquitetura e decisões de design
5. **`reflexao.md`** - Reflexão sobre:
   - Desafios de detecção automática de anomalias
   - Balanceamento entre sensibilidade e ruído
   - Aplicabilidade em ambientes reais

## Extensões Opcionais (Bônus)

🎯 **Persistência em JSON:** Salve e carregue estado do sistema  
🎯 **Configuração externa:** Leia thresholds de arquivo de configuração  
🎯 **Correlação entre métricas:** Detecte quando múltiplas métricas degradam juntas  
🎯 **Previsão simples:** Use tendências para prever valores futuros  
🎯 **Exportação de relatórios:** Gere relatórios em formato JSON estruturado  

## Questões para Reflexão

🤔 **Como balancear sensibilidade vs. ruído em alertas automatizados?**

🤔 **Quais métricas são mais importantes para monitoramento contínuo?**

🤔 **Como adaptar thresholds para diferentes tipos de projeto?**

🤔 **Que outros tipos de anomalias poderiam ser detectados?**

🤔 **Como este sistema poderia integrar com ferramentas reais de CI/CD?**

---

**Foque na utilidade prática e na redução de ruído nos alertas!** 📊
