# Exercício 02 - Otimização Multi-Objetivo e Performance 🔴

**Nível:** Avançado  
**Tempo Estimado:** 3-4 horas  
**Objetivo:** Desenvolver sistema de otimização que balança múltiplos objetivos conflitantes usando algoritmos genéticos e programação multi-objetivo

## Contexto

Como Chief Technology Officer de uma startup unicórnio de tecnologia, você enfrenta o dilema clássico da engenharia de software: como balancear qualidade, tempo, custo e recursos de forma otimizada? Projetos diferentes têm prioridades distintas, stakeholders com objetivos conflitantes e restrições únicas.

Você foi desafiado a criar um sistema revolucionário que automaticamente encontre o ponto ótimo de Pareto entre:
- **Qualidade vs Tempo:** Maximizar qualidade dentro de deadlines apertados
- **Cobertura vs Custo:** Otimizar ROI do investimento em testes
- **Confiabilidade vs Velocidade:** Balancear thoroughness com time-to-market
- **Recursos vs Resultado:** Otimizar alocação de equipe limitada

Este sistema será usado para orientar decisões estratégicas em portfólio de 50+ projetos simultâneos, cada um com características e restrições únicas.

## Problema de Otimização Multi-Objetivo

### Função Objetivo Principal

```
maximize: f(quality, speed, cost_efficiency, resource_utilization)

sujeito a:
- time_constraint: actual_time ≤ deadline
- budget_constraint: actual_cost ≤ budget
- resource_constraint: ∑resources ≤ available_resources
- quality_constraint: min_quality ≤ quality ≤ max_achievable
- regulatory_constraint: compliance_score ≥ required_compliance
```

### Objectives em Conflito

1. **Quality Maximization**
   ```
   Quality = w1×coverage + w2×dre + w3×security_score + w4×performance_score
   ```

2. **Time Minimization**
   ```
   Time = test_design_time + execution_time + analysis_time + rework_time
   ```

3. **Cost Efficiency**
   ```
   Cost_Efficiency = (quality_gained × business_value) / total_investment
   ```

4. **Resource Optimization**
   ```
   Resource_Utilization = productive_hours / total_available_hours
   ```

## Arquitetura do Sistema de Otimização

```python
"""
multi_objective_optimization.py

Sistema de otimização multi-objetivo para critérios de parada que
encontra soluções ótimas de Pareto balanceando qualidade, tempo,
custo e recursos usando algoritmos genéticos avançados.
"""

from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import math
import random
import copy
from abc import ABC, abstractmethod

class OptimizationObjective(Enum):
    """Objetivos de otimização disponíveis."""
    MAXIMIZE_QUALITY = "maximize_quality"
    MINIMIZE_TIME = "minimize_time"
    MAXIMIZE_COST_EFFICIENCY = "maximize_cost_efficiency"
    MAXIMIZE_RESOURCE_UTILIZATION = "maximize_resource_utilization"
    MINIMIZE_RISK = "minimize_risk"

class ConstraintType(Enum):
    """Tipos de restrições do problema."""
    HARD = "hard"        # Não pode ser violada
    SOFT = "soft"        # Pode ser violada com penalidade
    ELASTIC = "elastic"  # Pode ser ajustada dinamicamente

@dataclass
class OptimizationConstraint:
    """Restrição do problema de otimização."""
    name: str
    constraint_type: ConstraintType
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    penalty_function: Optional[Callable] = None
    flexibility: float = 0.0  # Para constraints elásticas

@dataclass
class ProjectParameters:
    """Parâmetros específicos do projeto."""
    domain: str
    criticality: str
    team_size: int
    deadline_days: int
    budget: float
    min_coverage: float
    min_dre: float
    regulatory_requirements: List[str]
    legacy_constraints: bool
    technology_stack: List[str]

@dataclass
class TestingStrategy:
    """Estratégia de teste representando um ponto no espaço de soluções."""
    coverage_target: float
    dre_target: float
    test_types: List[str]
    automation_level: float
    parallel_execution: bool
    team_allocation: Dict[str, float]
    time_allocation: Dict[str, int]
    tool_selection: List[str]
    
    # Métricas calculadas
    estimated_quality: float = 0.0
    estimated_time: int = 0
    estimated_cost: float = 0.0
    estimated_resource_usage: float = 0.0
    risk_score: float = 0.0

@dataclass
class ParetoSolution:
    """Solução no conjunto de Pareto."""
    strategy: TestingStrategy
    objective_values: Dict[OptimizationObjective, float]
    constraint_violations: Dict[str, float]
    dominance_rank: int = 0
    crowding_distance: float = 0.0
    feasible: bool = True

class ObjectiveFunction(ABC):
    """Classe abstrata para funções objetivo."""
    
    @abstractmethod
    def evaluate(self, strategy: TestingStrategy, 
                project_params: ProjectParameters) -> float:
        """Avalia uma estratégia de teste."""
        pass
    
    @abstractmethod
    def get_optimization_direction(self) -> str:
        """Retorna 'maximize' ou 'minimize'."""
        pass

class QualityMaximizationObjective(ObjectiveFunction):
    """Função objetivo para maximização de qualidade."""
    
    def __init__(self):
        """Inicializa função de qualidade."""
        self.weights = {
            'coverage': 0.3,
            'dre': 0.25,
            'automation': 0.2,
            'test_types_diversity': 0.15,
            'tool_quality': 0.1
        }
    
    def evaluate(self, strategy: TestingStrategy, 
                project_params: ProjectParameters) -> float:
        """
        Calcula score de qualidade baseado na estratégia.
        
        Args:
            strategy: Estratégia de teste
            project_params: Parâmetros do projeto
            
        Returns:
            Score de qualidade (0-100)
        """
        coverage_score = min(strategy.coverage_target, 100.0)
        dre_score = min(strategy.dre_target, 100.0)
        automation_score = strategy.automation_level * 100
        
        # Diversidade de tipos de teste
        test_diversity_score = min(len(strategy.test_types) * 10, 100)
        
        # Qualidade das ferramentas
        tool_quality_score = self._calculate_tool_quality(strategy.tool_selection)
        
        quality = (
            self.weights['coverage'] * coverage_score +
            self.weights['dre'] * dre_score +
            self.weights['automation'] * automation_score +
            self.weights['test_types_diversity'] * test_diversity_score +
            self.weights['tool_quality'] * tool_quality_score
        )
        
        return quality
    
    def get_optimization_direction(self) -> str:
        """Qualidade deve ser maximizada."""
        return "maximize"
    
    def _calculate_tool_quality(self, tools: List[str]) -> float:
        """Calcula score de qualidade das ferramentas."""
        tool_scores = {
            'pytest': 90,
            'selenium': 85,
            'cypress': 88,
            'junit': 80,
            'testng': 82,
            'manual': 60
        }
        
        if not tools:
            return 0.0
        
        avg_score = sum(tool_scores.get(tool, 50) for tool in tools) / len(tools)
        return avg_score

class TimeMinimizationObjective(ObjectiveFunction):
    """Função objetivo para minimização de tempo."""
    
    def evaluate(self, strategy: TestingStrategy, 
                project_params: ProjectParameters) -> float:
        """
        Calcula tempo total estimado da estratégia.
        
        Args:
            strategy: Estratégia de teste
            project_params: Parâmetros do projeto
            
        Returns:
            Tempo estimado em dias
        """
        # Tempo base por nível de cobertura
        base_time = strategy.coverage_target * 0.5  # 0.5 dias por % de cobertura
        
        # Ajuste por tipo de teste
        test_time_multipliers = {
            'unit': 1.0,
            'integration': 1.5,
            'system': 2.0,
            'acceptance': 2.5,
            'performance': 3.0,
            'security': 2.8,
            'usability': 2.2
        }
        
        test_time_factor = sum(test_time_multipliers.get(test_type, 1.0) 
                              for test_type in strategy.test_types) / len(strategy.test_types)
        
        # Ajuste por automação (automação reduz tempo de execução)
        automation_factor = 1.0 - (strategy.automation_level * 0.4)
        
        # Ajuste por paralelização
        parallel_factor = 0.6 if strategy.parallel_execution else 1.0
        
        # Ajuste por size da equipe
        team_factor = max(0.3, 1.0 / math.sqrt(project_params.team_size))
        
        total_time = base_time * test_time_factor * automation_factor * parallel_factor * team_factor
        
        return total_time
    
    def get_optimization_direction(self) -> str:
        """Tempo deve ser minimizado."""
        return "minimize"

class CostEfficiencyObjective(ObjectiveFunction):
    """Função objetivo para maximização de eficiência de custo."""
    
    def evaluate(self, strategy: TestingStrategy, 
                project_params: ProjectParameters) -> float:
        """
        Calcula eficiência de custo (qualidade/custo).
        
        Args:
            strategy: Estratégia de teste
            project_params: Parâmetros do projeto
            
        Returns:
            Razão qualidade/custo
        """
        # Calcular qualidade (reutilizar objective de qualidade)
        quality_obj = QualityMaximizationObjective()
        quality = quality_obj.evaluate(strategy, project_params)
        
        # Calcular custo
        cost = self._calculate_total_cost(strategy, project_params)
        
        if cost == 0:
            return 0.0
        
        return quality / cost
    
    def get_optimization_direction(self) -> str:
        """Eficiência deve ser maximizada."""
        return "maximize"
    
    def _calculate_total_cost(self, strategy: TestingStrategy, 
                            project_params: ProjectParameters) -> float:
        """Calcula custo total da estratégia."""
        # Custo de pessoal (por dia)
        daily_team_cost = project_params.team_size * 800  # R$ 800/dia por pessoa
        
        # Calcular tempo
        time_obj = TimeMinimizationObjective()
        time_days = time_obj.evaluate(strategy, project_params)
        
        personnel_cost = daily_team_cost * time_days
        
        # Custo de ferramentas
        tool_costs = {
            'pytest': 0,      # Open source
            'selenium': 0,    # Open source
            'cypress': 2000,  # Commercial license
            'loadrunner': 15000,
            'testcomplete': 8000
        }
        
        tools_cost = sum(tool_costs.get(tool, 1000) for tool in strategy.tool_selection)
        
        # Custo de infraestrutura (baseado em paralelização)
        infra_cost = 5000 if strategy.parallel_execution else 2000
        
        total_cost = personnel_cost + tools_cost + infra_cost
        return total_cost

class NSGA2Optimizer:
    """
    Implementação do algoritmo NSGA-II para otimização multi-objetivo.
    Non-dominated Sorting Genetic Algorithm II.
    """
    
    def __init__(self, population_size: int = 100, generations: int = 50):
        """
        Inicializa otimizador NSGA-II.
        
        Args:
            population_size: Tamanho da população
            generations: Número de gerações
        """
        self.population_size = population_size
        self.generations = generations
        self.objectives = []
        self.constraints = []
        self.mutation_rate = 0.1
        self.crossover_rate = 0.8
    
    def add_objective(self, objective: ObjectiveFunction) -> None:
        """Adiciona função objetivo."""
        self.objectives.append(objective)
    
    def add_constraint(self, constraint: OptimizationConstraint) -> None:
        """Adiciona restrição."""
        self.constraints.append(constraint)
    
    def optimize(self, project_params: ProjectParameters) -> List[ParetoSolution]:
        """
        Executa otimização multi-objetivo.
        
        Args:
            project_params: Parâmetros do projeto
            
        Returns:
            Conjunto de soluções de Pareto
        """
        # Inicializar população
        population = self._initialize_population(project_params)
        
        for generation in range(self.generations):
            # Avaliar objetivos
            self._evaluate_population(population, project_params)
            
            # Non-dominated sorting
            fronts = self._non_dominated_sorting(population)
            
            # Calcular crowding distance
            for front in fronts:
                self._calculate_crowding_distance(front)
            
            # Seleção, crossover e mutação
            if generation < self.generations - 1:
                population = self._evolve_population(population, fronts)
        
        # Retornar frente de Pareto
        return fronts[0] if fronts else []
    
    def _initialize_population(self, project_params: ProjectParameters) -> List[ParetoSolution]:
        """Inicializa população aleatória."""
        population = []
        
        for _ in range(self.population_size):
            strategy = self._generate_random_strategy(project_params)
            solution = ParetoSolution(strategy=strategy, objective_values={}, constraint_violations={})
            population.append(solution)
        
        return population
    
    def _generate_random_strategy(self, project_params: ProjectParameters) -> TestingStrategy:
        """Gera estratégia aleatória válida."""
        test_types = ['unit', 'integration', 'system', 'acceptance', 'performance']
        selected_types = random.sample(test_types, random.randint(2, len(test_types)))
        
        tools = ['pytest', 'selenium', 'cypress']
        selected_tools = random.sample(tools, random.randint(1, len(tools)))
        
        return TestingStrategy(
            coverage_target=random.uniform(project_params.min_coverage, 100.0),
            dre_target=random.uniform(project_params.min_dre, 100.0),
            test_types=selected_types,
            automation_level=random.uniform(0.3, 1.0),
            parallel_execution=random.choice([True, False]),
            team_allocation={'testing': random.uniform(0.5, 1.0), 'development': random.uniform(0.0, 0.5)},
            time_allocation={'design': random.randint(5, 15), 'execution': random.randint(10, 30)},
            tool_selection=selected_tools
        )
    
    def _evaluate_population(self, population: List[ParetoSolution], 
                           project_params: ProjectParameters) -> None:
        """Avalia toda a população."""
        for solution in population:
            # Avaliar objetivos
            for objective in self.objectives:
                obj_value = objective.evaluate(solution.strategy, project_params)
                solution.objective_values[type(objective)] = obj_value
            
            # Avaliar restrições
            solution.constraint_violations = self._evaluate_constraints(solution.strategy, project_params)
            solution.feasible = all(violation <= 0 for violation in solution.constraint_violations.values())
    
    def _evaluate_constraints(self, strategy: TestingStrategy, 
                            project_params: ProjectParameters) -> Dict[str, float]:
        """Avalia violações de restrições."""
        violations = {}
        
        # Exemplo: restrição de deadline
        time_obj = TimeMinimizationObjective()
        estimated_time = time_obj.evaluate(strategy, project_params)
        violations['deadline'] = max(0, estimated_time - project_params.deadline_days)
        
        # Exemplo: restrição de orçamento
        cost_obj = CostEfficiencyObjective()
        # Calcular custo total
        estimated_cost = self._calculate_strategy_cost(strategy, project_params)
        violations['budget'] = max(0, estimated_cost - project_params.budget)
        
        return violations
    
    def _calculate_strategy_cost(self, strategy: TestingStrategy, 
                               project_params: ProjectParameters) -> float:
        """Calcula custo de uma estratégia."""
        # TODO: Implementar cálculo detalhado de custo
        return 10000.0  # Placeholder
    
    def _non_dominated_sorting(self, population: List[ParetoSolution]) -> List[List[ParetoSolution]]:
        """Implementa non-dominated sorting."""
        fronts = []
        
        # Calcular dominância
        for solution in population:
            solution.dominance_rank = 0
            dominated_solutions = []
            domination_count = 0
            
            for other in population:
                if self._dominates(solution, other):
                    dominated_solutions.append(other)
                elif self._dominates(other, solution):
                    domination_count += 1
            
            if domination_count == 0:
                solution.dominance_rank = 0
                if not fronts:
                    fronts.append([])
                fronts[0].append(solution)
        
        # TODO: Implementar sorting completo das próximas frontes
        
        return fronts
    
    def _dominates(self, solution1: ParetoSolution, solution2: ParetoSolution) -> bool:
        """Verifica se solution1 domina solution2."""
        better_in_at_least_one = False
        
        for obj_type in solution1.objective_values:
            obj_class = obj_type
            direction = self.objectives[0].get_optimization_direction()  # Simplificado
            
            val1 = solution1.objective_values[obj_type]
            val2 = solution2.objective_values[obj_type]
            
            if direction == "maximize":
                if val1 < val2:
                    return False
                elif val1 > val2:
                    better_in_at_least_one = True
            else:  # minimize
                if val1 > val2:
                    return False
                elif val1 < val2:
                    better_in_at_least_one = True
        
        return better_in_at_least_one
    
    def _calculate_crowding_distance(self, front: List[ParetoSolution]) -> None:
        """Calcula crowding distance para uma frente."""
        if len(front) <= 2:
            for solution in front:
                solution.crowding_distance = float('inf')
            return
        
        # Inicializar distâncias
        for solution in front:
            solution.crowding_distance = 0.0
        
        # Para cada objetivo
        for obj_type in front[0].objective_values:
            # Ordenar por objetivo
            front.sort(key=lambda s: s.objective_values[obj_type])
            
            # Soluções extremas têm distância infinita
            front[0].crowding_distance = float('inf')
            front[-1].crowding_distance = float('inf')
            
            # Calcular distâncias para soluções intermediárias
            obj_range = (front[-1].objective_values[obj_type] - 
                        front[0].objective_values[obj_type])
            
            if obj_range > 0:
                for i in range(1, len(front) - 1):
                    distance = (front[i+1].objective_values[obj_type] - 
                              front[i-1].objective_values[obj_type]) / obj_range
                    front[i].crowding_distance += distance
    
    def _evolve_population(self, population: List[ParetoSolution], 
                          fronts: List[List[ParetoSolution]]) -> List[ParetoSolution]:
        """Evolui população para próxima geração."""
        # TODO: Implementar seleção, crossover e mutação
        return population  # Placeholder

def demonstrate_multi_objective_optimization():
    """Demonstra otimização multi-objetivo em ação."""
    print("=== OTIMIZAÇÃO MULTI-OBJETIVO ===")
    print()
    
    # Configurar projeto
    project = ProjectParameters(
        domain="fintech",
        criticality="high",
        team_size=8,
        deadline_days=60,
        budget=500000.0,
        min_coverage=85.0,
        min_dre=90.0,
        regulatory_requirements=["SOX", "PCI-DSS"],
        legacy_constraints=True,
        technology_stack=["Python", "React", "PostgreSQL"]
    )
    
    # Configurar otimizador
    optimizer = NSGA2Optimizer(population_size=50, generations=20)
    
    # Adicionar objetivos
    optimizer.add_objective(QualityMaximizationObjective())
    optimizer.add_objective(TimeMinimizationObjective())
    optimizer.add_objective(CostEfficiencyObjective())
    
    # Adicionar restrições
    deadline_constraint = OptimizationConstraint(
        name="deadline",
        constraint_type=ConstraintType.HARD,
        upper_bound=project.deadline_days
    )
    optimizer.add_constraint(deadline_constraint)
    
    print("🎯 Executando otimização multi-objetivo...")
    print(f"   Projeto: {project.domain} ({project.criticality})")
    print(f"   Equipe: {project.team_size} pessoas")
    print(f"   Deadline: {project.deadline_days} dias")
    print(f"   Orçamento: R$ {project.budget:,.2f}")
    print()
    
    # Executar otimização
    pareto_solutions = optimizer.optimize(project)
    
    print(f"✅ Otimização concluída!")
    print(f"   Soluções de Pareto encontradas: {len(pareto_solutions)}")
    
    # TODO: Exibir top soluções
    # TODO: Mostrar trade-offs identificados
    # TODO: Gerar visualização do espaço de soluções

def main():
    """Função principal demonstrando otimização."""
    demonstrate_multi_objective_optimization()
    
    print("\n🚀 Sistema de Otimização Multi-Objetivo demonstrado!")
    print("   - Balanceamento automático de objetivos conflitantes")
    print("   - Identificação de soluções ótimas de Pareto")
    print("   - Consideração de restrições hard e soft")
    print("   - Adaptação a diferentes contextos de projeto")

if __name__ == "__main__":
    main()
```

## Desafios Técnicos Específicos

### Desafio 1: Modelagem de Trade-offs Complexos
**Implementar modelagem matemática sofisticada:**
- **Pareto efficiency:** Encontrar soluções onde melhorar um objetivo piora outro
- **Nash equilibrium:** Balancear interesses de diferentes stakeholders
- **Multi-criteria decision analysis:** Usar AHP (Analytic Hierarchy Process)
- **Sensitivity analysis:** Entender robustez das soluções

### Desafio 2: Algoritmos de Otimização Avançados
**Implementar e comparar algoritmos:**
- **NSGA-II:** Non-dominated Sorting Genetic Algorithm
- **MOEA/D:** Multi-Objective Evolutionary Algorithm based on Decomposition
- **SPEA2:** Strength Pareto Evolutionary Algorithm
- **Particle Swarm Optimization:** Para espaços contínuos

### Desafio 3: Handling de Restrições Complexas
**Tratar diferentes tipos de restrições:**
- **Hard constraints:** Nunca podem ser violadas (regulamentações)
- **Soft constraints:** Podem ser violadas com penalidade (preferências)
- **Elastic constraints:** Podem ser ajustadas dinamicamente
- **Probabilistic constraints:** Com uncertainty e risk

### Desafio 4: Visualização de Espaços Multi-Dimensionais
**Criar visualizações interpretáveis:**
- **Pareto front visualization:** Em 2D, 3D e multi-dimensional
- **Parallel coordinates:** Para múltiplos objetivos
- **Radar charts:** Para comparar soluções
- **Interactive exploration:** Interface para explorar trade-offs

## Implementação Modular Avançada

### Módulo 1: Mathematical Foundation (60 min)
```python
class ParetoOptimality:
    """Implementação matemática de otimalidade de Pareto."""
    
    def is_pareto_optimal(self, solution: List[float], 
                         solution_set: List[List[float]]) -> bool:
        """Verifica se solução é Pareto-ótima."""
        pass
    
    def calculate_hypervolume(self, pareto_front: List[List[float]], 
                            reference_point: List[float]) -> float:
        """Calcula hypervolume da frente de Pareto."""
        pass
    
    def find_ideal_point(self, solutions: List[List[float]]) -> List[float]:
        """Encontra ponto ideal (melhor valor em cada objetivo)."""
        pass
    
    def find_nadir_point(self, solutions: List[List[float]]) -> List[float]:
        """Encontra ponto nadir (pior valor em cada objetivo)."""
        pass
```

### Módulo 2: Advanced Algorithms (90 min)
```python
class MOEADOptimizer:
    """Multi-Objective Evolutionary Algorithm based on Decomposition."""
    
    def decompose_problem(self, weights: List[List[float]]) -> List[Callable]:
        """Decompõe problema multi-objetivo em subproblemas."""
        pass
    
    def optimize_subproblem(self, subproblem: Callable, 
                          neighbors: List[int]) -> Any:
        """Otimiza um subproblema específico."""
        pass

class SPEA2Optimizer:
    """Strength Pareto Evolutionary Algorithm 2."""
    
    def calculate_strength(self, solution: Any, population: List[Any]) -> float:
        """Calcula strength de uma solução."""
        pass
    
    def environmental_selection(self, population: List[Any], 
                              archive: List[Any]) -> List[Any]:
        """Seleção ambiental para próxima geração."""
        pass
```

### Módulo 3: Constraint Handling (45 min)
```python
class ConstraintHandler:
    """Manipulador avançado de restrições."""
    
    def penalty_function(self, violations: Dict[str, float]) -> float:
        """Calcula penalidade por violações."""
        pass
    
    def repair_solution(self, solution: Any, constraints: List[Any]) -> Any:
        """Repara solução para satisfazer restrições."""
        pass
    
    def adaptive_penalty(self, generation: int, 
                        violation_history: List[float]) -> float:
        """Penalidade adaptativa baseada no histórico."""
        pass
```

### Módulo 4: Decision Support (45 min)
```python
class DecisionSupport:
    """Sistema de apoio à decisão para seleção de soluções."""
    
    def rank_solutions(self, pareto_front: List[Any], 
                      preferences: Dict[str, float]) -> List[Any]:
        """Rankeia soluções baseado em preferências."""
        pass
    
    def interactive_preference_elicitation(self) -> Dict[str, float]:
        """Elicita preferências do decision maker."""
        pass
    
    def generate_recommendations(self, solutions: List[Any]) -> List[str]:
        """Gera recomendações baseadas nas soluções."""
        pass
```

## Casos de Teste Avançados

### Caso 1: Startup de Alto Crescimento
```python
startup_project = ProjectParameters(
    domain="saas",
    criticality="medium",
    team_size=5,
    deadline_days=30,  # Muito apertado
    budget=100000.0,   # Budget limitado
    min_coverage=70.0,
    min_dre=80.0,
    regulatory_requirements=[],
    legacy_constraints=False,
    technology_stack=["Node.js", "React", "MongoDB"]
)
# Expectativa: Priorizar speed over quality
```

### Caso 2: Sistema Bancário Core
```python
banking_project = ProjectParameters(
    domain="banking",
    criticality="safety_critical",
    team_size=20,
    deadline_days=365,  # Longo prazo
    budget=5000000.0,   # Budget generoso
    min_coverage=95.0,
    min_dre=99.0,
    regulatory_requirements=["Basel III", "SOX", "PCI-DSS"],
    legacy_constraints=True,
    technology_stack=["Java", "Oracle", "Mainframe"]
)
# Expectativa: Priorizar quality over speed
```

### Caso 3: E-commerce Black Friday
```python
ecommerce_project = ProjectParameters(
    domain="ecommerce",
    criticality="business_critical",
    team_size=15,
    deadline_days=45,  # Deadline fixa (Black Friday)
    budget=800000.0,
    min_coverage=85.0,
    min_dre=92.0,
    regulatory_requirements=["LGPD"],
    legacy_constraints=True,
    technology_stack=["Python", "Django", "PostgreSQL", "Redis"]
)
# Expectativa: Balancear quality e performance para peak load
```

## Métricas de Avaliação Avançadas

### Qualidade das Soluções
- **Pareto dominance ratio:** % de soluções dominadas
- **Hypervolume indicator:** Volume do espaço coberto
- **Spread metric:** Diversidade das soluções
- **Convergence metric:** Proximidade ao ótimo teórico

### Performance do Algoritmo
- **Convergence speed:** Gerações para convergir
- **Computational complexity:** Tempo vs tamanho do problema
- **Memory efficiency:** Uso de memória
- **Scalability:** Performance com +objectives/constraints

### Business Value
- **Decision confidence:** Confiança na solução escolhida
- **Implementation feasibility:** Viabilidade prática
- **Stakeholder satisfaction:** Satisfação com trade-offs
- **Post-implementation validation:** Resultados reais vs preditos

## Entregáveis do Projeto

1. **`multi_objective_optimization.py`** - Sistema completo
2. **`pareto_analysis.py`** - Análise matemática de Pareto
3. **`advanced_algorithms.py`** - Implementação de NSGA-II, MOEA/D, SPEA2
4. **`constraint_handling.py`** - Sistema avançado de restrições
5. **`decision_support.py`** - Sistema de apoio à decisão
6. **`visualization_engine.py`** - Engine de visualização multi-dimensional
7. **`benchmark_suite.py`** - Suite de benchmarks para validação
8. **`case_studies.py`** - Casos de uso detalhados
9. **`performance_analysis.md`** - Análise de performance dos algoritmos
10. **`optimization_guide.pdf`** - Guia prático de uso

## Critérios de Avaliação

| Aspecto | Peso | Descrição |
|---------|------|-----------|
| **Implementação Matemática** | 30% | Precisão e robustez dos algoritmos |
| **Qualidade das Soluções** | 25% | Qualidade do conjunto de Pareto |
| **Eficiência Computacional** | 20% | Performance e escalabilidade |
| **Aplicabilidade Prática** | 15% | Viabilidade em cenários reais |
| **Inovação Técnica** | 10% | Originalidade das soluções |

---

**Transforme trade-offs em vantagens estratégicas! ⚡🎯**
