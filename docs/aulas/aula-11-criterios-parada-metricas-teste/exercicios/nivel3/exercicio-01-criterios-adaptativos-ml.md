# Exercício 01 - Sistema de Critérios Adaptativos com Machine Learning 🔴

**Nível:** Avançado  
**Tempo Estimado:** 3-4 horas  
**Objetivo:** Desenvolver sistema inteligente que aprende e adapta critérios de parada baseado em padrões históricos e feedback contínuo

## Contexto

Como Arquiteto de Qualidade em uma empresa multinacional de software, você foi desafiado a criar o próximo paradigma em critérios de parada: um sistema que aprende automaticamente com projetos anteriores e adapta seus critérios em tempo real baseado em padrões emergentes, contexto do projeto e feedback contínuo da produção.

O sistema deve ser capaz de:
- **Aprender** com dados históricos de centenas de projetos
- **Adaptar** critérios dinamicamente durante a execução dos testes
- **Predizer** riscos baseado em métricas em tempo real
- **Otimizar** continuamente baseado em feedback pós-release

Este é um projeto de pesquisa aplicada que pode revolucionar como a indústria aborda critérios de parada, transformando um processo tradicionalmente manual e baseado em heurísticas em um sistema inteligente e data-driven.

## Arquitetura do Sistema Inteligente

```python
"""
adaptive_criteria_ml.py

Sistema de critérios adaptativos usando Machine Learning que
aprende com dados históricos e adapta critérios em tempo real
baseado em padrões emergentes e feedback contínuo.
"""

from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import json
import math
import random
from datetime import datetime, timedelta

class ProjectPhase(Enum):
    """Fases do projeto para adaptação contextual."""
    PLANNING = "planning"
    DEVELOPMENT = "development" 
    INTEGRATION = "integration"
    SYSTEM_TEST = "system_test"
    ACCEPTANCE = "acceptance"
    PRE_RELEASE = "pre_release"

class RiskLevel(Enum):
    """Níveis de risco identificados pelo sistema."""
    VERY_LOW = "very_low"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class ProjectFeatures:
    """Features de um projeto para ML model."""
    domain: str
    team_size: int
    team_experience_avg: float
    code_complexity: float
    requirements_volatility: float
    technology_maturity: float
    time_pressure: float
    budget_constraints: float
    regulatory_requirements: bool
    legacy_integration: bool
    external_dependencies: int
    previous_similar_projects: int

@dataclass
class TestingState:
    """Estado atual do processo de teste."""
    current_phase: ProjectPhase
    elapsed_time: int  # dias
    remaining_time: int  # dias
    current_coverage: float
    current_dre: float
    defect_discovery_rate: float
    defect_closure_rate: float
    team_velocity: float
    recent_defect_severity: List[str]
    test_execution_trends: List[float]
    code_churn_rate: float

@dataclass
class AdaptationEvent:
    """Evento que triggera adaptação de critérios."""
    timestamp: datetime
    event_type: str
    severity: RiskLevel
    description: str
    affected_metrics: List[str]
    suggested_actions: List[str]
    confidence_score: float

@dataclass
class CriteriaRecommendation:
    """Recomendação adaptativa de critérios."""
    metric_name: str
    current_threshold: float
    recommended_threshold: float
    confidence: float
    reasoning: str
    risk_assessment: RiskLevel
    adaptation_urgency: str
    supporting_evidence: List[str]

class MLFeatureEngineering:
    """
    Engenharia de features para o modelo de ML que
    transforma dados brutos em features significativas.
    """
    
    def __init__(self):
        """Inicializa engenheiro de features."""
        self.feature_catalog = self._build_feature_catalog()
    
    def extract_features(self, project_data: Dict, 
                        testing_state: TestingState) -> List[float]:
        """
        Extrai features do estado atual para o modelo ML.
        
        Args:
            project_data: Dados do projeto
            testing_state: Estado atual dos testes
            
        Returns:
            Lista de features numéricas normalizadas
        """
        features = []
        
        # Features temporais
        features.extend(self._extract_temporal_features(testing_state))
        
        # Features de progresso
        features.extend(self._extract_progress_features(testing_state))
        
        # Features de qualidade
        features.extend(self._extract_quality_features(testing_state))
        
        # Features de contexto
        features.extend(self._extract_context_features(project_data))
        
        # Features derivadas (combinações)
        features.extend(self._extract_derived_features(testing_state))
        
        return features
    
    def _extract_temporal_features(self, state: TestingState) -> List[float]:
        """Extrai features relacionadas ao tempo."""
        return [
            state.elapsed_time / 365.0,  # Normalizado por ano
            state.remaining_time / 365.0,
            state.elapsed_time / (state.elapsed_time + state.remaining_time),
            math.sin(2 * math.pi * state.elapsed_time / 30),  # Padrão mensal
        ]
    
    def _extract_progress_features(self, state: TestingState) -> List[float]:
        """Extrai features de progresso dos testes."""
        return [
            state.current_coverage / 100.0,
            state.current_dre / 100.0,
            state.defect_discovery_rate,
            state.defect_closure_rate,
            state.team_velocity / 10.0,  # Normalizado
        ]
    
    def _extract_quality_features(self, state: TestingState) -> List[float]:
        """Extrai features de qualidade do código."""
        severity_weights = {"critical": 5, "high": 3, "medium": 2, "low": 1}
        avg_severity = sum(severity_weights.get(s, 0) 
                          for s in state.recent_defect_severity) / max(len(state.recent_defect_severity), 1)
        
        return [
            avg_severity / 5.0,  # Normalizado
            state.code_churn_rate,
            self._calculate_trend_direction(state.test_execution_trends),
        ]
    
    def _extract_context_features(self, project_data: Dict) -> List[float]:
        """Extrai features de contexto do projeto."""
        # TODO: Implementar extração de features contextuais
        return [0.5, 0.3, 0.8]  # Placeholder
    
    def _extract_derived_features(self, state: TestingState) -> List[float]:
        """Extrai features derivadas (combinações)."""
        coverage_velocity = state.current_coverage * state.team_velocity
        quality_momentum = state.current_dre * state.defect_closure_rate
        
        return [
            coverage_velocity / 1000.0,  # Normalizado
            quality_momentum / 100.0,
        ]
    
    def _calculate_trend_direction(self, values: List[float]) -> float:
        """Calcula direção da tendência (-1 a +1)."""
        if len(values) < 2:
            return 0.0
        
        # Regressão linear simples para trend
        n = len(values)
        x_mean = (n - 1) / 2
        y_mean = sum(values) / n
        
        numerator = sum((i - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((i - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return 0.0
        
        slope = numerator / denominator
        return max(-1.0, min(1.0, slope))  # Normalizado [-1, 1]
    
    def _build_feature_catalog(self) -> Dict:
        """Constrói catálogo de features disponíveis."""
        return {
            "temporal": ["elapsed_normalized", "remaining_normalized", "progress_ratio", "monthly_cycle"],
            "progress": ["coverage_normalized", "dre_normalized", "discovery_rate", "closure_rate", "velocity_normalized"],
            "quality": ["severity_avg", "churn_rate", "trend_direction"],
            "context": ["domain_encoding", "team_maturity", "complexity_factor"],
            "derived": ["coverage_velocity", "quality_momentum"]
        }

class PatternRecognitionEngine:
    """
    Engine de reconhecimento de padrões que identifica
    situações similares em dados históricos e aprende com outcomes.
    """
    
    def __init__(self):
        """Inicializa engine de reconhecimento."""
        self.historical_patterns = []
        self.pattern_outcomes = {}
        self.similarity_threshold = 0.8
    
    def learn_from_historical_data(self, historical_projects: List[Dict]) -> None:
        """
        Aprende padrões dos dados históricos.
        
        Args:
            historical_projects: Lista de projetos históricos com outcomes
        """
        for project in historical_projects:
            pattern = self._extract_pattern(project)
            outcome = self._extract_outcome(project)
            
            self.historical_patterns.append(pattern)
            self.pattern_outcomes[len(self.historical_patterns) - 1] = outcome
    
    def find_similar_patterns(self, current_features: List[float], 
                            top_k: int = 5) -> List[Tuple[int, float, Dict]]:
        """
        Encontra padrões similares ao estado atual.
        
        Args:
            current_features: Features do estado atual
            top_k: Número de padrões similares para retornar
            
        Returns:
            Lista de (pattern_id, similarity_score, outcome)
        """
        similarities = []
        
        for i, pattern in enumerate(self.historical_patterns):
            similarity = self._calculate_similarity(current_features, pattern)
            if similarity >= self.similarity_threshold:
                similarities.append((i, similarity, self.pattern_outcomes[i]))
        
        # Ordenar por similaridade e retornar top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
    
    def predict_outcome(self, current_features: List[float]) -> Dict:
        """
        Prediz outcome baseado em padrões similares.
        
        Args:
            current_features: Features do estado atual
            
        Returns:
            Predição com confidence score
        """
        similar_patterns = self.find_similar_patterns(current_features)
        
        if not similar_patterns:
            return {"prediction": "unknown", "confidence": 0.0}
        
        # Weighted average dos outcomes similares
        total_weight = sum(similarity for _, similarity, _ in similar_patterns)
        
        # TODO: Implementar agregação inteligente de predições
        # TODO: Calcular confidence baseado na consistência dos padrões
        
        return {"prediction": "success", "confidence": 0.75}  # Placeholder
    
    def _extract_pattern(self, project: Dict) -> List[float]:
        """Extrai padrão (features) de um projeto histórico."""
        # TODO: Implementar extração consistente de padrões
        return [0.5] * 15  # Placeholder
    
    def _extract_outcome(self, project: Dict) -> Dict:
        """Extrai outcome de um projeto histórico."""
        return {
            "success": project.get("post_release_defects", 0) < 10,
            "customer_satisfaction": project.get("customer_satisfaction", 0),
            "maintenance_cost": project.get("maintenance_cost", 0),
            "delivery_on_time": project.get("delivered_on_time", True)
        }
    
    def _calculate_similarity(self, features1: List[float], 
                            features2: List[float]) -> float:
        """Calcula similaridade entre dois conjuntos de features."""
        if len(features1) != len(features2):
            return 0.0
        
        # Distância euclidiana normalizada
        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(features1, features2)))
        max_distance = math.sqrt(len(features1))  # Distância máxima possível
        
        # Converter distância em similaridade (0-1)
        similarity = 1.0 - (distance / max_distance)
        return max(0.0, similarity)

class AdaptiveCriteriaEngine:
    """
    Engine principal que integra ML e pattern recognition
    para adaptar critérios dinamicamente.
    """
    
    def __init__(self):
        """Inicializa engine adaptativo."""
        self.feature_engineering = MLFeatureEngineering()
        self.pattern_recognition = PatternRecognitionEngine()
        self.adaptation_history = []
        self.current_criteria = {}
        self.base_criteria = {}
    
    def initialize_with_project_context(self, project_features: ProjectFeatures,
                                      base_criteria: Dict) -> None:
        """
        Inicializa sistema com contexto do projeto.
        
        Args:
            project_features: Características do projeto
            base_criteria: Critérios base iniciais
        """
        self.project_features = project_features
        self.base_criteria = base_criteria.copy()
        self.current_criteria = base_criteria.copy()
    
    def analyze_and_adapt(self, testing_state: TestingState) -> List[CriteriaRecommendation]:
        """
        Analisa estado atual e recomenda adaptações.
        
        Args:
            testing_state: Estado atual dos testes
            
        Returns:
            Lista de recomendações de adaptação
        """
        # Extrair features do estado atual
        current_features = self.feature_engineering.extract_features(
            self.project_features.__dict__, testing_state
        )
        
        # Encontrar padrões similares
        similar_patterns = self.pattern_recognition.find_similar_patterns(current_features)
        
        # Predizer outcome
        prediction = self.pattern_recognition.predict_outcome(current_features)
        
        # Gerar recomendações baseadas na análise
        recommendations = self._generate_recommendations(
            testing_state, similar_patterns, prediction
        )
        
        # Avaliar urgência e priorizar
        recommendations = self._prioritize_recommendations(recommendations)
        
        return recommendations
    
    def detect_anomalies(self, testing_state: TestingState) -> List[AdaptationEvent]:
        """
        Detecta anomalias que requerem adaptação imediata.
        
        Args:
            testing_state: Estado atual dos testes
            
        Returns:
            Lista de eventos de adaptação detectados
        """
        events = []
        
        # Detectar anomalias em métricas
        events.extend(self._detect_metric_anomalies(testing_state))
        
        # Detectar padrões de risco
        events.extend(self._detect_risk_patterns(testing_state))
        
        # Detectar desvios de cronograma
        events.extend(self._detect_schedule_anomalies(testing_state))
        
        return events
    
    def apply_adaptation(self, recommendation: CriteriaRecommendation) -> bool:
        """
        Aplica adaptação recomendada aos critérios.
        
        Args:
            recommendation: Recomendação a ser aplicada
            
        Returns:
            True se adaptação foi aplicada com sucesso
        """
        if recommendation.confidence < 0.6:
            return False
        
        # Aplicar adaptação
        self.current_criteria[recommendation.metric_name] = recommendation.recommended_threshold
        
        # Registrar adaptação no histórico
        adaptation_record = {
            "timestamp": datetime.now(),
            "metric": recommendation.metric_name,
            "old_value": recommendation.current_threshold,
            "new_value": recommendation.recommended_threshold,
            "reasoning": recommendation.reasoning,
            "confidence": recommendation.confidence
        }
        
        self.adaptation_history.append(adaptation_record)
        return True
    
    def _generate_recommendations(self, testing_state: TestingState,
                                similar_patterns: List, prediction: Dict) -> List[CriteriaRecommendation]:
        """Gera recomendações baseadas na análise."""
        recommendations = []
        
        # TODO: Implementar geração inteligente de recomendações
        # baseada em padrões similares e predições
        
        return recommendations
    
    def _prioritize_recommendations(self, recommendations: List[CriteriaRecommendation]) -> List[CriteriaRecommendation]:
        """Prioriza recomendações por urgência e impacto."""
        # TODO: Implementar algoritmo de priorização
        return sorted(recommendations, key=lambda r: r.confidence, reverse=True)
    
    def _detect_metric_anomalies(self, testing_state: TestingState) -> List[AdaptationEvent]:
        """Detecta anomalias em métricas individuais."""
        # TODO: Implementar detecção de anomalias usando statistical methods
        return []
    
    def _detect_risk_patterns(self, testing_state: TestingState) -> List[AdaptationEvent]:
        """Detecta padrões que indicam risco elevado."""
        # TODO: Implementar detecção de padrões de risco
        return []
    
    def _detect_schedule_anomalies(self, testing_state: TestingState) -> List[AdaptationEvent]:
        """Detecta desvios significativos no cronograma."""
        # TODO: Implementar detecção de anomalias de cronograma
        return []

def simulate_project_evolution():
    """Simula evolução de um projeto com adaptação em tempo real."""
    print("=== SIMULAÇÃO DE CRITÉRIOS ADAPTATIVOS ===")
    print()
    
    # Inicializar sistema
    engine = AdaptiveCriteriaEngine()
    
    # Contexto do projeto
    project_features = ProjectFeatures(
        domain="fintech",
        team_size=12,
        team_experience_avg=3.5,
        code_complexity=0.7,
        requirements_volatility=0.4,
        technology_maturity=0.8,
        time_pressure=0.6,
        budget_constraints=0.3,
        regulatory_requirements=True,
        legacy_integration=True,
        external_dependencies=8,
        previous_similar_projects=3
    )
    
    # Critérios base
    base_criteria = {
        "coverage": 85.0,
        "dre": 90.0,
        "defect_density": 2.0,
        "customer_satisfaction_target": 4.0
    }
    
    engine.initialize_with_project_context(project_features, base_criteria)
    
    # Simular fases do projeto
    phases = [
        ("Planejamento", ProjectPhase.PLANNING),
        ("Desenvolvimento", ProjectPhase.DEVELOPMENT),
        ("Integração", ProjectPhase.INTEGRATION),
        ("Teste de Sistema", ProjectPhase.SYSTEM_TEST),
        ("Aceitação", ProjectPhase.ACCEPTANCE)
    ]
    
    for phase_name, phase in phases:
        print(f"📋 Fase: {phase_name}")
        
        # Estado simulado da fase
        testing_state = TestingState(
            current_phase=phase,
            elapsed_time=random.randint(10, 60),
            remaining_time=random.randint(20, 40),
            current_coverage=random.uniform(50, 95),
            current_dre=random.uniform(70, 98),
            defect_discovery_rate=random.uniform(0.5, 3.0),
            defect_closure_rate=random.uniform(0.8, 2.5),
            team_velocity=random.uniform(15, 35),
            recent_defect_severity=["medium", "low", "high", "critical"],
            test_execution_trends=[0.8, 0.85, 0.82, 0.88, 0.90],
            code_churn_rate=random.uniform(0.1, 0.4)
        )
        
        # Analisar e adaptar
        recommendations = engine.analyze_and_adapt(testing_state)
        anomalies = engine.detect_anomalies(testing_state)
        
        print(f"  Estado: Coverage {testing_state.current_coverage:.1f}%, DRE {testing_state.current_dre:.1f}%")
        print(f"  Recomendações: {len(recommendations)}")
        print(f"  Anomalias detectadas: {len(anomalies)}")
        print("-" * 50)

def main():
    """Função principal demonstrando sistema adaptativo."""
    # Simular evolução do projeto
    simulate_project_evolution()
    
    print("\n🎯 Sistema de Critérios Adaptativos demonstrado!")
    print("   - Aprendizado com dados históricos")
    print("   - Adaptação baseada em padrões")
    print("   - Detecção de anomalias em tempo real")
    print("   - Recomendações inteligentes")

if __name__ == "__main__":
    main()
```

## Desafios Técnicos Avançados

### Desafio 1: Feature Engineering Inteligente
**Objetivo:** Criar features que capturem patterns sutis
- **Temporal patterns:** Sazonalidade, tendências, ciclos
- **Quality momentum:** Aceleração/desaceleração da qualidade
- **Team dynamics:** Produtividade, moral, comunicação
- **Technical debt:** Acúmulo e pagamento da dívida técnica

### Desafio 2: Pattern Recognition Sofisticado
**Objetivo:** Identificar patterns complexos em dados históricos
- **Multi-dimensional clustering:** Agrupar projetos similares
- **Sequence pattern mining:** Identificar sequências de eventos críticos
- **Anomaly detection:** Detectar situações incomuns
- **Causal inference:** Identificar causas vs correlações

### Desafio 3: Adaptive Learning Algorithm
**Objetivo:** Implementar aprendizado contínuo
- **Online learning:** Atualizar modelo com novos dados
- **Transfer learning:** Aplicar conhecimento entre domínios
- **Active learning:** Solicitar feedback em situações incertas
- **Reinforcement learning:** Otimizar decisões baseadas em rewards

### Desafio 4: Real-time Decision Making
**Objetivo:** Tomar decisões adapativas em tempo real
- **Stream processing:** Processar métricas em tempo real
- **Multi-criteria optimization:** Balancear objetivos conflitantes
- **Risk-aware decisions:** Considerar uncertainty e potential impact
- **Explainable AI:** Justificar decisões para stakeholders

## Implementação por Módulos

### Módulo 1: Data Pipeline (45 min)
```python
class DataPipeline:
    """Pipeline de dados para alimentar o sistema ML."""
    
    def collect_real_time_metrics(self) -> Dict:
        """Coleta métricas em tempo real dos sistemas."""
        pass
    
    def preprocess_features(self, raw_data: Dict) -> List[float]:
        """Preprocessa dados para o modelo ML."""
        pass
    
    def validate_data_quality(self, data: Dict) -> bool:
        """Valida qualidade dos dados coletados."""
        pass
```

### Módulo 2: ML Model (60 min)
```python
class AdaptiveCriteriaModel:
    """Modelo ML para predição e adaptação de critérios."""
    
    def train_on_historical_data(self, projects: List[Dict]) -> None:
        """Treina modelo com dados históricos."""
        pass
    
    def predict_outcome(self, features: List[float]) -> Dict:
        """Prediz outcome do projeto atual."""
        pass
    
    def recommend_criteria_adjustments(self, current_state: Dict) -> List[Dict]:
        """Recomenda ajustes nos critérios."""
        pass
    
    def update_model_online(self, new_feedback: Dict) -> None:
        """Atualiza modelo com feedback recente."""
        pass
```

### Módulo 3: Decision Engine (45 min)
```python
class DecisionEngine:
    """Engine de decisão para aplicar adaptações."""
    
    def evaluate_recommendation_risk(self, recommendation: Dict) -> float:
        """Avalia risco de aplicar uma recomendação."""
        pass
    
    def apply_gradual_adaptation(self, target_criteria: Dict) -> None:
        """Aplica adaptação gradual para evitar disruption."""
        pass
    
    def rollback_if_needed(self, performance_metrics: Dict) -> bool:
        """Faz rollback se adaptação causar problemas."""
        pass
```

### Módulo 4: Monitoring & Feedback (30 min)
```python
class AdaptationMonitor:
    """Monitor para acompanhar eficácia das adaptações."""
    
    def track_adaptation_performance(self) -> Dict:
        """Monitora performance das adaptações aplicadas."""
        pass
    
    def collect_stakeholder_feedback(self) -> Dict:
        """Coleta feedback de stakeholders."""
        pass
    
    def generate_adaptation_report(self) -> str:
        """Gera relatório de adaptações realizadas."""
        pass
```

## Métricas de Sucesso

### Métricas de Accuracy
- **Prediction accuracy:** >85% de acurácia nas predições
- **Pattern recognition:** >80% de patterns relevantes identificados
- **Anomaly detection:** <5% de falsos positivos
- **Adaptation effectiveness:** >70% de adaptações que melhoram outcomes

### Métricas de Performance
- **Response time:** <500ms para análise e recomendação
- **Throughput:** >1000 projetos analisados simultaneamente
- **Memory efficiency:** <2GB de RAM para modelo completo
- **Scalability:** Linear scaling até 10k projetos históricos

### Métricas de Business Value
- **ROI improvement:** >25% melhoria em ROI vs critérios estáticos
- **Risk reduction:** >40% redução em proyetos que falham
- **Time to market:** >15% redução no tempo para release
- **Customer satisfaction:** >20% melhoria na satisfação

## Entregáveis Avançados

1. **`adaptive_criteria_ml.py`** - Sistema completo com ML
2. **`feature_engineering.py`** - Pipeline de feature engineering
3. **`pattern_recognition.py`** - Engine de pattern recognition
4. **`decision_engine.py`** - Sistema de tomada de decisão
5. **`training_data.json`** - Dataset sintético para treinamento
6. **`evaluation_metrics.py`** - Métricas de avaliação do sistema
7. **`research_paper.md`** - Documentação estilo paper acadêmico
8. **`demo_presentation.py`** - Demonstração interativa
9. **`deployment_guide.md`** - Guia de deployment para produção
10. **`ethical_considerations.md`** - Considerações éticas do sistema

## Critérios de Avaliação

| Aspecto | Peso | Descrição Detalhada |
|---------|------|---------------------|
| **Inovação Técnica** | 25% | Originalidade das soluções ML/AI implementadas |
| **Implementação Robusta** | 20% | Qualidade do código, tratamento de edge cases |
| **Validação Experimental** | 15% | Experimentos convincentes demonstrando eficácia |
| **Aplicabilidade Prática** | 15% | Viabilidade de uso em ambiente real |
| **Documentação Científica** | 10% | Qualidade da documentação estilo research |
| **Impact Potential** | 15% | Potencial de impacto na indústria |

---

**Este é um projeto de pesquisa aplicada - pense como um cientista! 🔬🚀**
