# Exercício 02 - Critérios Contextualizados por Domínio 🟡

**Nível:** Intermediário  
**Tempo Estimado:** 75-90 minutos  
**Objetivo:** Desenvolver sistema de critérios adaptativos baseados no contexto do projeto

## Contexto

Como especialista em qualidade de software, você foi contratado por uma consultoria que atende clientes de domínios muito diversos: desde sistemas críticos de aviação até aplicativos de entretenimento. Cada domínio tem características únicas que exigem critérios de parada completamente diferentes.

Você deve criar um sistema inteligente que automaticamente adapte critérios de parada baseado no domínio, criticidade, regulamentações e outros fatores contextuais, garantindo que cada projeto seja avaliado com critérios apropriados às suas necessidades específicas.

## Domínios de Aplicação

### Domínio 1: Aviação Civil (Crítico)
**Características:**
- Regulamentação DO-178C
- Tolerância zero para defeitos críticos
- Certificação obrigatória
- Rastreabilidade completa necessária

```python
aviation_context = {
    "domain": "aviation",
    "criticality": "safety_critical",
    "regulations": ["DO-178C", "RTCA"],
    "certification_required": True,
    "user_impact": "life_threatening",
    "development_time": 36,  # meses
    "team_experience": "expert",
    "legacy_constraints": False
}
```

### Domínio 2: Dispositivos Médicos (Crítico)
**Características:**
- FDA/CE/ANVISA compliance
- Validação clínica necessária
- Rastreabilidade de requisitos
- Processo controlado e auditável

```python
medical_context = {
    "domain": "medical",
    "criticality": "safety_critical", 
    "regulations": ["FDA_510k", "ISO_14155", "ANVISA"],
    "certification_required": True,
    "user_impact": "life_threatening",
    "development_time": 24,
    "team_experience": "senior",
    "legacy_constraints": True
}
```

### Domínio 3: Fintech/Banking (Alto)
**Características:**
- SOX, PCI-DSS compliance
- Auditoria financeira
- Segurança crítica
- Disponibilidade 99.9%+

```python
fintech_context = {
    "domain": "financial",
    "criticality": "business_critical",
    "regulations": ["SOX", "PCI_DSS", "GDPR"],
    "certification_required": False,
    "user_impact": "financial_loss",
    "development_time": 12,
    "team_experience": "senior",
    "legacy_constraints": True
}
```

### Domínio 4: E-commerce (Médio)
**Características:**
- LGPD/GDPR para dados pessoais
- Alta disponibilidade desejável
- Performance crítica para conversão
- Iterações rápidas

```python
ecommerce_context = {
    "domain": "ecommerce",
    "criticality": "business_important",
    "regulations": ["LGPD", "GDPR"],
    "certification_required": False,
    "user_impact": "business_impact",
    "development_time": 6,
    "team_experience": "mixed",
    "legacy_constraints": False
}
```

### Domínio 5: Gaming/Entertainment (Baixo)
**Características:**
- Foco em experiência do usuário
- Performance e fluidez críticas
- Tolerância alta para bugs menores
- Lançamento baseado em marketing

```python
gaming_context = {
    "domain": "entertainment",
    "criticality": "user_experience",
    "regulations": [],
    "certification_required": False,
    "user_impact": "user_satisfaction",
    "development_time": 18,
    "team_experience": "junior",
    "legacy_constraints": False
}
```

## Requisitos Funcionais

### RF01 - Sistema de Contextualização
Criar sistema que analise contexto do projeto e determine:
- **Nível de rigor** necessário
- **Métricas prioritárias** para o domínio
- **Thresholds apropriados** baseados em benchmarks
- **Critérios regulatórios** obrigatórios

### RF02 - Motor de Critérios Adaptativos
Implementar motor que:
- **Gere critérios** específicos para cada contexto
- **Ajuste pesos** de métricas baseado na criticidade
- **Adicione validações** regulatórias quando necessário
- **Considere restrições** de tempo e recursos

### RF03 - Validação Contextual
Desenvolver validação que verifique:
- **Compliance regulatório** obrigatório
- **Criticidade apropriada** para o domínio
- **Coerência** entre contexto e critérios
- **Viabilidade** dos critérios propostos

### RF04 - Sistema de Recomendações
Criar sistema que sugira:
- **Melhorias de processo** específicas do domínio
- **Ferramentas especializadas** recomendadas
- **Benchmarks da indústria** para comparação
- **Próximos passos** para certificação (quando aplicável)

## Arquitetura do Sistema

```python
"""
contextual_criteria.py

Sistema de critérios de parada contextualizados por domínio.
Adapta automaticamente critérios baseado nas características
específicas de cada projeto e domínio de aplicação.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json

class DomainType(Enum):
    """Tipos de domínio suportados."""
    AVIATION = "aviation"
    MEDICAL = "medical"
    FINANCIAL = "financial"
    ECOMMERCE = "ecommerce"
    ENTERTAINMENT = "entertainment"
    AUTOMOTIVE = "automotive"
    TELECOMMUNICATIONS = "telecommunications"

class CriticalityLevel(Enum):
    """Níveis de criticidade do sistema."""
    SAFETY_CRITICAL = "safety_critical"        # Vida humana em risco
    BUSINESS_CRITICAL = "business_critical"    # Impacto financeiro alto
    BUSINESS_IMPORTANT = "business_important"  # Impacto operacional
    USER_EXPERIENCE = "user_experience"        # Experiência do usuário
    CONVENIENCE = "convenience"                # Conveniência apenas

@dataclass
class ProjectContext:
    """Contexto completo de um projeto."""
    domain: DomainType
    criticality: CriticalityLevel
    regulations: List[str]
    certification_required: bool
    user_impact: str
    development_time_months: int
    team_experience: str  # expert, senior, mixed, junior
    legacy_constraints: bool
    custom_requirements: Dict = field(default_factory=dict)

@dataclass
class ContextualCriteria:
    """Critérios gerados para um contexto específico."""
    mandatory_criteria: Dict[str, Dict]
    conditional_criteria: Dict[str, Dict]
    escape_criteria: Dict[str, Dict]
    regulatory_requirements: List[str]
    recommended_tools: List[str]
    process_recommendations: List[str]
    justification: str

class DomainKnowledgeBase:
    """
    Base de conhecimento com características específicas
    de cada domínio e suas necessidades de qualidade.
    """
    
    def __init__(self):
        """Inicializa base de conhecimento com dados de domínios."""
        self.domain_profiles = self._load_domain_profiles()
        self.regulatory_requirements = self._load_regulatory_requirements()
        self.industry_benchmarks = self._load_industry_benchmarks()
    
    def get_domain_profile(self, domain: DomainType) -> Dict:
        """
        Retorna perfil específico de um domínio.
        
        Args:
            domain: Tipo de domínio
            
        Returns:
            Dict com características do domínio
        """
        return self.domain_profiles.get(domain.value, {})
    
    def get_regulatory_requirements(self, regulations: List[str]) -> List[Dict]:
        """
        Retorna requisitos específicos das regulamentações.
        
        Args:
            regulations: Lista de regulamentações aplicáveis
            
        Returns:
            Lista de requisitos regulatórios
        """
        requirements = []
        for regulation in regulations:
            if regulation in self.regulatory_requirements:
                requirements.append(self.regulatory_requirements[regulation])
        return requirements
    
    def _load_domain_profiles(self) -> Dict:
        """Carrega perfis de características por domínio."""
        return {
            "aviation": {
                "base_coverage": 100.0,
                "critical_coverage": 100.0,
                "max_defect_density": 0.1,
                "required_dre": 99.9,
                "traceability_required": True,
                "formal_methods": True,
                "priority_metrics": ["coverage", "traceability", "dre"]
            },
            "medical": {
                "base_coverage": 95.0,
                "critical_coverage": 100.0,
                "max_defect_density": 0.5,
                "required_dre": 99.0,
                "traceability_required": True,
                "clinical_validation": True,
                "priority_metrics": ["coverage", "dre", "traceability"]
            },
            "financial": {
                "base_coverage": 90.0,
                "critical_coverage": 98.0,
                "max_defect_density": 2.0,
                "required_dre": 95.0,
                "security_testing": True,
                "performance_testing": True,
                "priority_metrics": ["security", "performance", "coverage"]
            },
            "ecommerce": {
                "base_coverage": 80.0,
                "critical_coverage": 90.0,
                "max_defect_density": 5.0,
                "required_dre": 85.0,
                "performance_testing": True,
                "user_testing": True,
                "priority_metrics": ["performance", "user_experience", "coverage"]
            },
            "entertainment": {
                "base_coverage": 70.0,
                "critical_coverage": 80.0,
                "max_defect_density": 8.0,
                "required_dre": 80.0,
                "performance_testing": True,
                "user_testing": True,
                "priority_metrics": ["performance", "user_experience"]
            }
        }
    
    def _load_regulatory_requirements(self) -> Dict:
        """Carrega requisitos específicos por regulamentação."""
        # TODO: Implementar carregamento de requisitos regulatórios
        pass
    
    def _load_industry_benchmarks(self) -> Dict:
        """Carrega benchmarks da indústria por domínio."""
        # TODO: Implementar carregamento de benchmarks
        pass

class ContextualCriteriaGenerator:
    """
    Gerador de critérios contextualizados que adapta
    critérios baseado no domínio e características do projeto.
    """
    
    def __init__(self):
        """Inicializa gerador com base de conhecimento."""
        self.knowledge_base = DomainKnowledgeBase()
        self.adjustment_factors = self._load_adjustment_factors()
    
    def generate_criteria(self, context: ProjectContext) -> ContextualCriteria:
        """
        Gera critérios completos para um contexto específico.
        
        Args:
            context: Contexto do projeto
            
        Returns:
            ContextualCriteria adaptados ao contexto
        """
        # TODO: Implementar geração completa de critérios
        pass
    
    def _generate_mandatory_criteria(self, context: ProjectContext) -> Dict[str, Dict]:
        """
        Gera critérios obrigatórios baseados no contexto.
        
        Args:
            context: Contexto do projeto
            
        Returns:
            Dict com critérios obrigatórios
        """
        # TODO: Implementar geração de critérios obrigatórios
        pass
    
    def _generate_conditional_criteria(self, context: ProjectContext) -> Dict[str, Dict]:
        """
        Gera critérios condicionais baseados no contexto.
        
        Args:
            context: Contexto do projeto
            
        Returns:
            Dict com critérios condicionais
        """
        # TODO: Implementar geração de critérios condicionais
        pass
    
    def _apply_context_adjustments(self, base_criteria: Dict,
                                  context: ProjectContext) -> Dict:
        """
        Aplica ajustes contextuais aos critérios base.
        
        Args:
            base_criteria: Critérios base do domínio
            context: Contexto específico do projeto
            
        Returns:
            Critérios ajustados
        """
        # TODO: Implementar ajustes contextuais
        pass
    
    def _add_regulatory_compliance(self, criteria: Dict,
                                  regulations: List[str]) -> Dict:
        """
        Adiciona requisitos de compliance regulatório.
        
        Args:
            criteria: Critérios existentes
            regulations: Lista de regulamentações
            
        Returns:
            Critérios com compliance adicionado
        """
        # TODO: Implementar adição de compliance
        pass
    
    def _generate_recommendations(self, context: ProjectContext) -> Tuple[List[str], List[str]]:
        """
        Gera recomendações de ferramentas e processos.
        
        Args:
            context: Contexto do projeto
            
        Returns:
            Tuple com (ferramentas_recomendadas, processos_recomendados)
        """
        # TODO: Implementar geração de recomendações
        pass
    
    def _load_adjustment_factors(self) -> Dict:
        """Carrega fatores de ajuste para diferentes contextos."""
        return {
            "team_experience": {
                "expert": {"rigor_multiplier": 1.0, "complexity_tolerance": 1.2},
                "senior": {"rigor_multiplier": 1.1, "complexity_tolerance": 1.0},
                "mixed": {"rigor_multiplier": 1.2, "complexity_tolerance": 0.9},
                "junior": {"rigor_multiplier": 1.3, "complexity_tolerance": 0.8}
            },
            "development_time": {
                "short": {"flexibility": 0.1, "minimum_coverage": 0.9},
                "medium": {"flexibility": 0.15, "minimum_coverage": 0.85},
                "long": {"flexibility": 0.05, "minimum_coverage": 0.95}
            }
        }

def main():
    """Função principal demonstrando geração contextualizada."""
    generator = ContextualCriteriaGenerator()
    
    # Contextos de teste
    test_contexts = [
        ("Sistema Aviônico", aviation_context),
        ("Dispositivo Médico", medical_context),
        ("Plataforma Fintech", fintech_context),
        ("Loja Virtual", ecommerce_context),
        ("Jogo Mobile", gaming_context)
    ]
    
    print("=== GERADOR DE CRITÉRIOS CONTEXTUALIZADOS ===")
    print()
    
    for project_name, context_data in test_contexts:
        print(f"🎯 Analisando: {project_name}")
        
        # Converter dict para ProjectContext
        context = ProjectContext(
            domain=DomainType(context_data["domain"]),
            criticality=CriticalityLevel(context_data["criticality"]),
            regulations=context_data["regulations"],
            certification_required=context_data["certification_required"],
            user_impact=context_data["user_impact"],
            development_time_months=context_data["development_time"],
            team_experience=context_data["team_experience"],
            legacy_constraints=context_data["legacy_constraints"]
        )
        
        # TODO: Gerar e exibir critérios
        # criteria = generator.generate_criteria(context)
        # print(f"Domínio: {context.domain.value}")
        # print(f"Criticidade: {context.criticality.value}")
        # print(f"Critérios obrigatórios: {len(criteria.mandatory_criteria)}")
        # print(f"Justificativa: {criteria.justification}")
        print("-" * 60)

if __name__ == "__main__":
    main()
```

## Tarefas Específicas

### Tarefa 1: Base de Conhecimento
Implemente base de conhecimento robusta com:
- **Perfis de domínio** com características específicas
- **Mapeamento de regulamentações** para requisitos técnicos
- **Benchmarks da indústria** para comparação
- **Fatores de ajuste** baseados em contexto

### Tarefa 2: Algoritmo de Adaptação
Desenvolva algoritmo que:
- **Analise o contexto** e determine nível de rigor necessário
- **Ajuste thresholds** baseado na criticidade e experiência da equipe
- **Adicione critérios** específicos do domínio
- **Considere limitações** de tempo e recursos

### Tarefa 3: Validação de Coerência
Implemente validação que garanta:
- **Critérios realistas** para o contexto dado
- **Compliance** com regulamentações obrigatórias
- **Coerência** entre criticidade e critérios
- **Viabilidade** prática dos critérios

### Tarefa 4: Sistema de Justificativas
Crie sistema que explique:
- **Porque** cada critério foi escolhido
- **Como** o contexto influenciou as decisões
- **Quais alternativas** foram consideradas
- **Que riscos** são mitigados pelos critérios

## Resultados Esperados

### Sistema Aviônico
- **Cobertura:** 100% (criticidade máxima)
- **DRE:** 99.9% (tolerância zero)
- **Regulatório:** DO-178C compliance obrigatório
- **Ferramentas:** LDRA, VectorCAST, PolySpace

### Jogo Mobile
- **Cobertura:** 70% (foco em performance)
- **Performance:** <50ms response time
- **User Experience:** Beta testing obrigatório
- **Flexibilidade:** Alta para features não-críticas

## Critérios de Avaliação

| Aspecto | Peso | Descrição |
|---------|------|-----------|
| **Base de Conhecimento** | 25% | Completude e precisão dos perfis de domínio |
| **Adaptação Contextual** | 30% | Qualidade do algoritmo de adaptação |
| **Compliance Regulatório** | 20% | Tratamento correto de regulamentações |
| **Justificativas** | 25% | Clareza e fundamentação das decisões |

## Entregáveis

1. **`contextual_criteria.py`** - Sistema completo
2. **`domain_profiles.json`** - Base de conhecimento estruturada
3. **`test_scenarios.py`** - Demonstração dos 5 domínios
4. **`criteria_comparison.md`** - Comparação entre critérios gerados
5. **`domain_analysis.md`** - Análise das diferenças entre domínios

---

**Foque na adaptação inteligente baseada no contexto real!** 🎯
