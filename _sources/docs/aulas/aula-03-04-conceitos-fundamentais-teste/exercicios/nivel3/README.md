# Exercícios Nível 3 - Avançado 🔴

**Tempo Estimado**: 2-4 horas por exercício  
**Objetivo**: Design complexo e tomada de decisões arquiteturais estratégicas  
**Complexidade**: Sistemas completos com múltiplas responsabilidades e tecnologias emergentes

## 📋 Visão Geral dos Exercícios

1. **Exercício 3.1**: Arquitetura de Qualidade Global para Fintech
2. **Exercício 3.2**: Sistema de IA com Garantias de Qualidade
3. **Exercício 3.3**: Plataforma de Qualidade Empresarial

---

## 🎯 Exercício 3.1 - Arquitetura Global: Fintech Multi-Regional

### Contexto
Como **Chief Quality Officer** da **GlobalPay**, uma fintech que opera em 50 países, você deve projetar uma **Arquitetura de Qualidade Global** que atenda a diferentes regulamentações, culturas e infraestruturas tecnológicas. A plataforma processa $10 bilhões em transações diárias e serve 100 milhões de usuários.

### Cenário Realista
A GlobalPay enfrenta desafios únicos de escala global:
- **Regulamentações diferentes** por país (GDPR na Europa, LGPD no Brasil, SOX nos EUA)
- **Latências variáveis** entre regiões (5ms na mesma região, 200ms intercontinental)
- **Culturas de qualidade diferentes** (tolerância a falhas varia por mercado)
- **Infraestrutura heterogênea** (cloud híbrida, on-premise em alguns países)
- **Compliance financeiro** rigoroso com auditoria em tempo real

### 📝 Sua Tarefa

Projetar uma **Arquitetura de Qualidade Global** que demonstre como os conceitos fundamentais se adaptam a contextos culturais, regulatórios e tecnológicos diversos, mantendo coerência e eficácia em escala planetária.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_3_1.py

from typing import Dict, List, Optional, Any, Tuple, Protocol
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import json
import aiohttp
from abc import ABC, abstractmethod
from collections import defaultdict
import uuid

class RegiaoGlobal(Enum):
    """Regiões globais de operação."""
    AMERICA_NORTE = "america_norte"
    AMERICA_SUL = "america_sul"
    EUROPA = "europa"
    ASIA_PACIFICO = "asia_pacifico"
    ORIENTE_MEDIO = "oriente_medio"
    AFRICA = "africa"

class TipoRegulamentacao(Enum):
    """Tipos de regulamentação financeira."""
    GDPR = "gdpr"              # Europa
    LGPD = "lgpd"              # Brasil
    SOX = "sox"                # Estados Unidos
    PCI_DSS = "pci_dss"        # Global para cartões
    BASEL_III = "basel_iii"    # Bancário internacional
    MiFID_II = "mifid_ii"      # Europa - mercados financeiros

class NivelCriticidade(Enum):
    """Níveis de criticidade por regulamentação."""
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"
    SISTEMICA = "sistemica"    # Risco sistêmico financeiro

@dataclass
class ContextoRegional:
    """Contexto específico de uma região."""
    regiao: RegiaoGlobal
    pais: str
    regulamentacoes: List[TipoRegulamentacao]
    latencia_toleravel: float  # em ms
    cultura_qualidade: str     # "rigorosa", "moderada", "flexivel"
    infraestrutura: str        # "cloud", "hibrida", "on_premise"
    fuso_horario: str
    moeda_local: str
    volume_transacoes_diario: float

@dataclass
class TransacaoGlobal:
    """Transação que pode cruzar múltiplas regiões."""
    id: str
    remetente_regiao: RegiaoGlobal
    destinatario_regiao: RegiaoGlobal
    valor: float
    moeda: str
    tipo: str  # "transferencia", "pagamento", "investimento"
    regulamentacoes_aplicaveis: List[TipoRegulamentacao]
    timestamp_iniciacao: datetime
    contexto_compliance: Dict[str, Any]

class AdaptadorRegulamentacao(ABC):
    """Adaptador base para diferentes regulamentações."""
    
    @abstractmethod
    async def verificar_conformidade(self, transacao: TransacaoGlobal) -> Tuple[bool, Dict]:
        """Verifica conformidade com regulamentação específica."""
        pass
    
    @abstractmethod
    async def validar_contexto_cultural(self, transacao: TransacaoGlobal, 
                                       contexto: ContextoRegional) -> Tuple[bool, str]:
        """Valida adequação ao contexto cultural da região."""
        pass

class AdaptadorGDPR(AdaptadorRegulamentacao):
    """Adaptador para regulamentação GDPR (Europa)."""
    
    def __init__(self):
        self.regras_gdpr = self._definir_regras_gdpr()
    
    async def verificar_conformidade(self, transacao: TransacaoGlobal) -> Tuple[bool, Dict]:
        """
        Verifica conformidade GDPR.
        
        CONCEITO APLICADO: Verificação específica para contexto regulatório
        """
        # TODO: IMPLEMENTAR
        #
        # Verificações GDPR:
        # - Consentimento explícito para processamento de dados
        # - Minimização de dados (apenas dados necessários)
        # - Direito ao esquecimento (possibilidade de deletar)
        # - Portabilidade de dados
        # - Criptografia de dados sensíveis
        # - Notificação de breach em 72h
        #
        # RETORNO: (conforme, detalhes_verificacao)
        pass
    
    async def validar_contexto_cultural(self, transacao: TransacaoGlobal, 
                                       contexto: ContextoRegional) -> Tuple[bool, str]:
        """
        Valida adequação cultural para região europeia.
        
        CONCEITO APLICADO: Validação considerando contexto cultural
        """
        # TODO: IMPLEMENTAR
        #
        # Considere cultura europeia:
        # - Alta valorização da privacidade
        # - Preferência por transparência nos processos
        # - Tolerância baixa a falhas em dados pessoais
        # - Expectativa de controle sobre dados próprios
        pass
    
    def _definir_regras_gdpr(self) -> Dict:
        """Define regras específicas do GDPR."""
        # TODO: Implementar regras detalhadas
        pass

class AdaptadorLGPD(AdaptadorRegulamentacao):
    """Adaptador para LGPD (Brasil)."""
    
    async def verificar_conformidade(self, transacao: TransacaoGlobal) -> Tuple[bool, Dict]:
        """Verifica conformidade LGPD."""
        # TODO: IMPLEMENTAR (similar ao GDPR mas com especificidades brasileiras)
        pass
    
    async def validar_contexto_cultural(self, transacao: TransacaoGlobal, 
                                       contexto: ContextoRegional) -> Tuple[bool, str]:
        """Valida contexto cultural brasileiro."""
        # TODO: IMPLEMENTAR
        pass

class GerenciadorLatenciaGlobal:
    """
    Gerenciador de latência considerando distribuição geográfica.
    
    CONCEITO APLICADO: Cadeia causal em sistemas distribuídos globalmente
    """
    
    def __init__(self):
        self.matriz_latencias = self._inicializar_matriz_latencias()
        self.thresholds_por_regiao = self._definir_thresholds_regionais()
    
    def _inicializar_matriz_latencias(self) -> Dict[Tuple[RegiaoGlobal, RegiaoGlobal], float]:
        """Inicializa matriz de latências entre regiões."""
        return {
            (RegiaoGlobal.AMERICA_NORTE, RegiaoGlobal.EUROPA): 120.0,
            (RegiaoGlobal.AMERICA_NORTE, RegiaoGlobal.ASIA_PACIFICO): 180.0,
            (RegiaoGlobal.EUROPA, RegiaoGlobal.ASIA_PACIFICO): 160.0,
            (RegiaoGlobal.AMERICA_SUL, RegiaoGlobal.EUROPA): 200.0,
            # TODO: Completar matriz para todas as combinações
        }
    
    def _definir_thresholds_regionais(self) -> Dict[RegiaoGlobal, Dict]:
        """Define thresholds de qualidade por região."""
        return {
            RegiaoGlobal.AMERICA_NORTE: {
                "latencia_maxima": 50.0,
                "tolerancia_falhas": 0.01,  # 99.99% uptime
                "cultura_qualidade": "rigorosa"
            },
            RegiaoGlobal.EUROPA: {
                "latencia_maxima": 100.0,
                "tolerancia_falhas": 0.05,  # 99.95% uptime
                "cultura_qualidade": "rigorosa"
            },
            RegiaoGlobal.ASIA_PACIFICO: {
                "latencia_maxima": 200.0,
                "tolerancia_falhas": 0.1,   # 99.9% uptime
                "cultura_qualidade": "moderada"
            }
            # TODO: Adicionar outras regiões
        }
    
    async def calcular_latencia_esperada(self, origem: RegiaoGlobal, 
                                        destino: RegiaoGlobal) -> float:
        """Calcula latência esperada entre duas regiões."""
        # TODO: IMPLEMENTAR
        #
        # Considere:
        # - Latência base da matriz
        # - Sobrecarga de rede atual
        # - Roteamento otimizado
        # - Infraestrutura regional
        pass
    
    async def detectar_degradacao_latencia(self, origem: RegiaoGlobal, 
                                          destino: RegiaoGlobal, 
                                          latencia_medida: float) -> Optional[Dict]:
        """
        Detecta degradação de latência entre regiões.
        
        CONCEITO APLICADO: Detecção precoce na cadeia causal
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Compare latência medida com esperada
        # 2. Considere thresholds culturais da região
        # 3. Identifique se é erro (problema de rede),
        #    defeito (configuração), falha (timeout) ou
        #    incidente (impacto no usuário)
        pass

class OrquestradorConformidadeGlobal:
    """
    Orquestrador que gerencia conformidade em múltiplas jurisdições.
    
    CONCEITO APLICADO: Verificação e validação adaptadas a contextos
    regulatórios e culturais diversos
    """
    
    def __init__(self):
        self.adaptadores: Dict[TipoRegulamentacao, AdaptadorRegulamentacao] = {
            TipoRegulamentacao.GDPR: AdaptadorGDPR(),
            TipoRegulamentacao.LGPD: AdaptadorLGPD(),
            # TODO: Adicionar outros adaptadores
        }
        self.contextos_regionais = self._carregar_contextos_regionais()
        self.latencia_manager = GerenciadorLatenciaGlobal()
    
    def _carregar_contextos_regionais(self) -> Dict[RegiaoGlobal, ContextoRegional]:
        """Carrega contextos específicos de cada região."""
        # TODO: IMPLEMENTAR com dados reais de cada região
        pass
    
    async def processar_transacao_global(self, transacao: TransacaoGlobal) -> Dict:
        """
        Processa transação aplicando conformidade global.
        
        Returns
        -------
        Dict
            Resultado completo com análise de conformidade global
        """
        # TODO: IMPLEMENTAR
        #
        # 1. VERIFICAÇÃO MULTI-REGULAMENTAÇÃO:
        #    - Para cada regulamentação aplicável, execute verificação
        #    - Todas devem passar para transação ser aprovada
        #
        # 2. VALIDAÇÃO CULTURAL:
        #    - Valide adequação ao contexto cultural de origem e destino
        #    - Considere diferenças de tolerância e expectativas
        #
        # 3. ANÁLISE DE LATÊNCIA:
        #    - Calcule latência esperada
        #    - Detecte possíveis degradações
        #
        # 4. OTIMIZAÇÃO DE ROTA:
        #    - Escolha melhor rota considerando latência e conformidade
        #
        # 5. MONITORAMENTO DA CADEIA CAUSAL:
        #    - Monitore cada etapa da transação
        #    - Detecte problemas antes que se tornem incidentes
        pass
    
    async def analisar_riscos_compliance(self, transacao: TransacaoGlobal) -> Dict:
        """
        Analisa riscos de compliance para transação complexa.
        
        CONCEITO APLICADO: Análise de risco baseada em múltiplos fatores
        """
        # TODO: IMPLEMENTAR
        #
        # Analise riscos:
        # - Conflitos entre regulamentações
        # - Adequação cultural
        # - Histórico de problemas na rota
        # - Volatilidade da infraestrutura
        # - Geopolítica (sanções, embargos)
        pass

class SistemaQualidadeGlobal:
    """
    Sistema central de qualidade para operação global.
    
    CONCEITO APLICADO: Integração sistêmica de todos os conceitos
    fundamentais em escala global
    """
    
    def __init__(self):
        self.orquestrador_compliance = OrquestradorConformidadeGlobal()
        self.metricas_globais: Dict[RegiaoGlobal, Dict] = {}
        self.alertas_globais: List[Dict] = []
        self.dashboard_global = {}
    
    async def monitorar_qualidade_global(self) -> Dict:
        """
        Monitora qualidade em todas as regiões simultaneamente.
        
        Returns
        -------
        Dict
            Dashboard global de qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # Para cada região:
        # 1. Colete métricas locais
        # 2. Aplique contexto cultural aos thresholds
        # 3. Detecte anomalias considerando fuso horário
        # 4. Correlacione eventos entre regiões
        # 5. Identifique tendências globais
        pass
    
    async def otimizar_infraestrutura_global(self, objetivos: Dict) -> Dict:
        """
        Otimiza infraestrutura considerando trade-offs globais.
        
        Parameters
        ----------
        objetivos : Dict
            Pesos para: {"conformidade": 0.4, "latencia": 0.3, "custo": 0.3}
        """
        # TODO: IMPLEMENTAR
        #
        # Otimizações possíveis:
        # - Realocação de recursos entre regiões
        # - Ajuste de rotas de comunicação
        # - Configuração de caches regionais
        # - Balanceamento de carga geográfico
        # - Escolha de provedores de cloud por região
        #
        # Considere:
        # - Diferenças de custo por região
        # - Regulamentações locais
        # - Expectativas culturais
        # - Horários de pico regionais
        pass
    
    async def simular_cenarios_globais(self) -> Dict:
        """
        Simula cenários complexos que afetam múltiplas regiões.
        """
        # TODO: IMPLEMENTAR
        #
        # Cenários a simular:
        # - Falha de cabo submarino entre continentes
        # - Nova regulamentação em região importante
        # - Evento geopolítico (sanções, embargo)
        # - Desastre natural em datacenter principal
        # - Ataque cibernético coordenado
        # - Mudança drástica em volume por região
        #
        # Para cada cenário, analise:
        # - Impacto na cadeia causal global
        # - Capacidade de recuperação
        # - Tempo para roteamento alternativo
        # - Degradação de qualidade esperada
        pass
    
    def gerar_relatorio_executivo_global(self) -> str:
        """
        Gera relatório executivo sobre qualidade global.
        
        CONCEITO APLICADO: Visão estratégica da qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # O relatório deve incluir:
        # - KPIs globais consolidados
        # - Comparação de performance entre regiões
        # - Análise de riscos geopolíticos
        # - Recomendações de investimento em infraestrutura
        # - Previsões de crescimento e necessidades futuras
        # - ROI de iniciativas de qualidade por região
        pass

# FRAMEWORK DE TESTE GLOBAL
class SimuladorTransacoesGlobais:
    """Simulador de transações realistas para teste."""
    
    def __init__(self):
        self.padroes_regionais = self._definir_padroes_regionais()
    
    def _definir_padroes_regionais(self) -> Dict:
        """Define padrões de transação por região."""
        return {
            RegiaoGlobal.AMERICA_NORTE: {
                "volume_pico": "14:00-16:00 EST",
                "tipos_comuns": ["investimento", "e_commerce"],
                "valor_medio": 2500.0,
                "moedas": ["USD", "CAD"]
            },
            RegiaoGlobal.EUROPA: {
                "volume_pico": "10:00-12:00 CET",
                "tipos_comuns": ["transferencia", "pagamento"],
                "valor_medio": 1800.0,
                "moedas": ["EUR", "GBP", "CHF"]
            },
            RegiaoGlobal.ASIA_PACIFICO: {
                "volume_pico": "09:00-11:00 JST",
                "tipos_comuns": ["e_commerce", "remessa"],
                "valor_medio": 800.0,
                "moedas": ["JPY", "AUD", "SGD"]
            }
        }
    
    async def gerar_transacao_realista(self, origem: RegiaoGlobal, 
                                      destino: RegiaoGlobal) -> TransacaoGlobal:
        """Gera transação realista entre duas regiões."""
        # TODO: IMPLEMENTAR
        pass
    
    async def simular_dia_operacional(self, sistema: SistemaQualidadeGlobal) -> Dict:
        """Simula um dia completo de operações globais."""
        # TODO: IMPLEMENTAR
        #
        # Simule 24 horas considerando:
        # - Horários de pico por região
        # - Padrões de transação realistas
        # - Eventos aleatórios (falhas, picos)
        # - Sazonalidade (horário comercial, fins de semana)
        pass

# CENÁRIOS DE TESTE FORNECIDOS
async def test_arquitetura_global():
    """
    Testa arquitetura global com cenários realistas da GlobalPay.
    """
    sistema = SistemaQualidadeGlobal()
    simulador = SimuladorTransacoesGlobais()
    
    print("🌍 TESTE ARQUITETURA GLOBAL - GlobalPay")
    print("="*60)
    
    # Cenário 1: Transação intercontinental complexa
    transacao_complexa = TransacaoGlobal(
        id=str(uuid.uuid4()),
        remetente_regiao=RegiaoGlobal.AMERICA_NORTE,
        destinatario_regiao=RegiaoGlobal.EUROPA,
        valor=1000000.0,  # $1M - valor alto
        moeda="USD",
        tipo="investimento",
        regulamentacoes_aplicaveis=[TipoRegulamentacao.SOX, TipoRegulamentacao.GDPR],
        timestamp_iniciacao=datetime.now(),
        contexto_compliance={
            "investidor_qualificado": True,
            "finalidade": "aquisicao_empresa_europeia",
            "documentos_anexos": ["due_diligence.pdf", "contrato.pdf"]
        }
    )
    
    print("\n💰 CENÁRIO 1: Transação de Alto Valor Intercontinental")
    resultado1 = await sistema.orquestrador_compliance.processar_transacao_global(transacao_complexa)
    print(f"Resultado: {resultado1}")
    
    # Cenário 2: Monitoramento global em tempo real
    print("\n📊 CENÁRIO 2: Monitoramento Global")
    dashboard_global = await sistema.monitorar_qualidade_global()
    print(f"Dashboard: {dashboard_global}")
    
    # Cenário 3: Simulação de dia operacional completo
    print("\n🌅 CENÁRIO 3: Simulação de 24h de Operação")
    simulacao_diaria = await simulador.simular_dia_operacional(sistema)
    print(f"Resumo do dia: {simulacao_diaria}")
    
    # Cenário 4: Otimização de infraestrutura
    print("\n⚖️ CENÁRIO 4: Otimização Global")
    objetivos = {"conformidade": 0.5, "latencia": 0.3, "custo": 0.2}
    otimizacao = await sistema.otimizar_infraestrutura_global(objetivos)
    print(f"Recomendações: {otimizacao}")
    
    # Cenário 5: Simulação de cenários de crise
    print("\n🚨 CENÁRIO 5: Cenários de Crise Global")
    cenarios_crise = await sistema.simular_cenarios_globais()
    print(f"Análise de resiliência: {cenarios_crise}")
    
    # Relatório executivo
    print("\n📋 RELATÓRIO EXECUTIVO GLOBAL")
    relatorio = sistema.gerar_relatorio_executivo_global()
    print(relatorio)

if __name__ == "__main__":
    asyncio.run(test_arquitetura_global())
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Arquitetura robusta que escala globalmente
- [ ] Adaptação inteligente a contextos regulatórios e culturais
- [ ] Sistema de monitoramento global eficaz
- [ ] Otimização sofisticada de trade-offs globais
- [ ] Análise estratégica de cenários complexos
- [ ] Código arquitetural exemplar com padrões enterprise

#### ✓ Bom (75-89%)
- [ ] Boa arquitetura global com adaptações regionais
- [ ] Sistema funcional de conformidade multi-regulamentação
- [ ] Monitoramento adequado entre regiões
- [ ] Otimização competente de recursos

#### ⚠️ Satisfatório (60-74%)
- [ ] Arquitetura básica mas funcional
- [ ] Adaptações limitadas a contextos regionais
- [ ] Monitoramento simplificado

#### ❌ Insuficiente (<60%)
- [ ] Falha na escala global
- [ ] Não considera contextos regionais
- [ ] Arquitetura inadequada para complexidade

### 💡 Dicas para Sucesso

1. **Pense em federação**, não centralização
2. **Contexto cultural importa** tanto quanto técnico
3. **Regulamentações podem conflitar** - prepare-se
4. **Latência global é física** - otimize rotas
5. **Falhas em escala global são diferentes** - prepare-se

---

## 🎯 Exercício 3.2 - Sistema de IA: Qualidade em Machine Learning

### Contexto
Como **AI Quality Engineer** na **MedAI Solutions**, você deve garantir a qualidade de um sistema de diagnóstico médico baseado em IA que será usado em hospitais globalmente. O sistema usa deep learning para analisar exames de imagem e sugerir diagnósticos com 95% de precisão.

### Cenário Realista
O sistema MedAI enfrenta desafios únicos de qualidade em IA:
- **Viés algorítmico** pode discriminar populações
- **Drift de modelo** devido a mudanças nos dados
- **Explicabilidade** é crucial para confiança médica
- **Validação contínua** é necessária com novos dados
- **Segurança adversarial** contra ataques aos modelos

### 📝 Sua Tarefa

Implementar um **Sistema de Qualidade para IA** que aplique os conceitos fundamentais no contexto de machine learning, demonstrando como verificação, validação e cadeia causal se manifestam em sistemas inteligentes.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_3_2.py

from typing import Dict, List, Optional, Any, Tuple, Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import numpy as np
import json
from abc import ABC, abstractmethod
import uuid

class TipoViés(Enum):
    """Tipos de viés em modelos de IA."""
    SELECAO = "selecao"           # Viés na seleção de dados
    CONFIRMACAO = "confirmacao"   # Viés de confirmação
    REPRESENTACAO = "representacao" # Sub/sobre-representação de grupos
    TEMPORAL = "temporal"         # Viés temporal nos dados
    GEOGRAFICO = "geografico"     # Viés geográfico/cultural
    INSTRUMENTAL = "instrumental" # Viés do instrumento de medição

class TipoDrift(Enum):
    """Tipos de drift em modelos de ML."""
    CONCEITUAL = "conceitual"     # Mudança na relação X->Y
    COVARIAVEL = "covariavel"     # Mudança na distribuição de X
    POSTERIOR = "posterior"       # Mudança na distribuição de Y
    VIRTUAL = "virtual"           # Mudança que não afeta performance

@dataclass
class ExameMedico:
    """Representa um exame médico para análise."""
    id: str
    paciente_id: str
    tipo_exame: str  # "radiografia", "tomografia", "ressonancia"
    imagem_path: str
    metadados: Dict[str, Any]
    diagnostico_real: Optional[str] = None  # Ground truth quando disponível
    confianca_diagnostico: Optional[float] = None
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class PredicaoIA:
    """Resultado de predição do modelo de IA."""
    exame_id: str
    predicao: str
    confianca: float
    explicabilidade: Dict[str, Any]  # Mapas de atenção, SHAP values, etc.
    tempo_inferencia: float
    versao_modelo: str
    timestamp: datetime = field(default_factory=datetime.now)

class VerificadorModeloIA:
    """
    Verificador de conformidade técnica para modelos de IA.
    
    CONCEITO APLICADO: Verificação = conformidade com padrões técnicos de ML
    """
    
    def __init__(self):
        self.metricas_minimas = self._definir_metricas_minimas()
        self.padroes_tecnico = self._definir_padroes_tecnicos()
    
    def _definir_metricas_minimas(self) -> Dict:
        """Define métricas mínimas aceitáveis."""
        return {
            "acuracia": 0.95,
            "precisao": 0.93,
            "recall": 0.93,
            "f1_score": 0.93,
            "auc_roc": 0.95,
            "tempo_inferencia_max": 2.0,  # segundos
            "memoria_max": 8.0,           # GB
            "explicabilidade_score": 0.8
        }
    
    def _definir_padroes_tecnicos(self) -> Dict:
        """Define padrões técnicos para modelos médicos."""
        return {
            "formato_entrada": {"altura": 512, "largura": 512, "canais": 3},
            "formato_saida": {"classes": list, "confianca": float},
            "versionamento": "semantico",  # major.minor.patch
            "documentacao": ["arquitetura", "treinamento", "validacao"],
            "testes_unitarios": "obrigatorio",
            "reproducibilidade": "deterministica"
        }
    
    async def verificar_conformidade_tecnica(self, modelo_id: str, 
                                           metricas_avaliacao: Dict) -> Tuple[bool, Dict]:
        """
        Verifica se modelo atende padrões técnicos mínimos.
        
        CONCEITO APLICADO: Verificação técnica objetiva
        
        Returns
        -------
        Tuple[bool, Dict]
            (conforme, detalhes_verificacao)
        """
        # TODO: IMPLEMENTAR
        #
        # Verificações técnicas:
        # 1. MÉTRICAS DE PERFORMANCE:
        #    - Todas as métricas atendem aos mínimos?
        #    - Performance é consistente entre folds?
        #    - Não há overfitting?
        #
        # 2. PADRÕES DE IMPLEMENTAÇÃO:
        #    - Formato de entrada/saída correto?
        #    - Versionamento semântico?
        #    - Documentação completa?
        #    - Testes unitários passando?
        #
        # 3. REQUISITOS OPERACIONAIS:
        #    - Tempo de inferência aceitável?
        #    - Uso de memória dentro do limite?
        #    - Reprodutibilidade garantida?
        pass
    
    async def verificar_robustez_tecnica(self, modelo_id: str) -> Dict:
        """
        Verifica robustez técnica do modelo.
        
        CONCEITO APLICADO: Verificação de resistência a perturbações
        """
        # TODO: IMPLEMENTAR
        #
        # Testes de robustez:
        # - Resistência a ruído na entrada
        # - Estabilidade com pequenas variações
        # - Performance em bordas da distribuição
        # - Comportamento com entradas adversariais
        pass

class ValidadorContextoMedico:
    """
    Validador que considera contexto médico específico.
    
    CONCEITO APLICADO: Validação = adequação ao propósito médico real
    """
    
    def __init__(self):
        self.contextos_especializados = self._definir_contextos_especializados()
        self.grupos_demograficos = self._definir_grupos_demograficos()
    
    def _definir_contextos_especializados(self) -> Dict:
        """Define contextos médicos especializados."""
        return {
            "radiologia_torax": {
                "doencas_prevalentes": ["pneumonia", "covid19", "tuberculose"],
                "populacao_alvo": "adultos_18_80",
                "equipamentos": ["raio_x_digital", "raio_x_analogico"],
                "urgencia": "alta"
            },
            "dermatologia": {
                "doencas_prevalentes": ["melanoma", "carcinoma", "nevus"],
                "populacao_alvo": "todas_idades",
                "equipamentos": ["camera_dermatoscopia"],
                "urgencia": "media"
            }
        }
    
    def _definir_grupos_demograficos(self) -> Dict:
        """Define grupos demográficos para análise de viés."""
        return {
            "idade": ["0_18", "18_35", "35_65", "65_plus"],
            "genero": ["masculino", "feminino", "outros"],
            "etnia": ["caucasiano", "afrodescendente", "asiatico", "hispanico", "outros"],
            "geografia": ["america_norte", "europa", "asia", "africa", "oceania"]
        }
    
    async def validar_adequacao_medica(self, predicao: PredicaoIA, 
                                     contexto_paciente: Dict) -> Tuple[bool, str]:
        """
        Valida se predição é adequada ao contexto médico específico.
        
        CONCEITO APLICADO: Validação contextual médica
        
        Returns
        -------
        Tuple[bool, str]
            (adequado, justificativa_medica)
        """
        # TODO: IMPLEMENTAR
        #
        # Validações contextuais:
        # 1. ADEQUAÇÃO CLÍNICA:
        #    - Predição é clinicamente plausível?
        #    - Alinha com sintomas reportados?
        #    - Considera histórico médico do paciente?
        #
        # 2. ADEQUAÇÃO DEMOGRÁFICA:
        #    - Modelo foi treinado em população similar?
        #    - Performance é consistente para este grupo?
        #    - Não há viés conhecido para este perfil?
        #
        # 3. ADEQUAÇÃO TEMPORAL:
        #    - Contexto atual é similar ao treinamento?
        #    - Não há drift conceitual conhecido?
        #    - Sazonalidade de doenças considerada?
        pass
    
    async def detectar_vies_populacional(self, predicoes: List[PredicaoIA], 
                                       contextos: List[Dict]) -> Dict:
        """
        Detecta viés algorítmico em diferentes populações.
        
        CONCEITO APLICADO: Validação de equidade e justiça
        """
        # TODO: IMPLEMENTAR
        #
        # Análise de viés:
        # 1. PERFORMANCE POR GRUPO:
        #    - Acurácia é similar entre grupos demográficos?
        #    - Falsos positivos/negativos distribuídos equitativamente?
        #
        # 2. REPRESENTAÇÃO NOS DADOS:
        #    - Grupos estão adequadamente representados?
        #    - Qualidade dos dados é similar entre grupos?
        #
        # 3. IMPACTO DIFERENCIAL:
        #    - Consequências dos erros são similares?
        #    - Acesso ao tratamento é equitativo?
        pass

class DetectorDriftModelo:
    """
    Detector de drift em modelos de machine learning.
    
    CONCEITO APLICADO: Detecção precoce de degradação na cadeia causal
    """
    
    def __init__(self):
        self.baseline_distribuicoes = {}
        self.historico_performance = {}
        self.thresholds_drift = self._definir_thresholds_drift()
    
    def _definir_thresholds_drift(self) -> Dict:
        """Define thresholds para detecção de drift."""
        return {
            "drift_covariavel": 0.05,      # KL divergence
            "drift_conceitual": 0.03,      # Drop in performance
            "drift_posterior": 0.04,       # Change in label distribution
            "significancia": 0.01          # Statistical significance
        }
    
    async def estabelecer_baseline(self, dados_baseline: List[ExameMedico], 
                                 predicoes_baseline: List[PredicaoIA]):
        """
        Estabelece baseline para detecção de drift.
        
        CONCEITO APLICADO: Definição de "normalidade" para detecção de desvios
        """
        # TODO: IMPLEMENTAR
        #
        # Calcule distribuições baseline:
        # - Distribuição das features de entrada
        # - Distribuição das predições
        # - Métricas de performance por grupo
        # - Padrões temporais normais
        pass
    
    async def detectar_drift(self, dados_novos: List[ExameMedico], 
                           predicoes_novas: List[PredicaoIA]) -> Dict:
        """
        Detecta diferentes tipos de drift no modelo.
        
        Returns
        -------
        Dict
            Análise completa de drift detectado
        """
        # TODO: IMPLEMENTAR
        #
        # Detecção de drift:
        # 1. DRIFT COVARIÁVEL:
        #    - Distribuição das features mudou?
        #    - Use testes estatísticos (KS, χ²)
        #
        # 2. DRIFT CONCEITUAL:
        #    - Relação X->Y mudou?
        #    - Compare performance em dados similares
        #
        # 3. DRIFT POSTERIOR:
        #    - Distribuição dos rótulos mudou?
        #    - Prevalência de doenças mudou?
        #
        # 4. DRIFT VIRTUAL:
        #    - Mudança sem impacto na performance?
        #    - Monitorar mas não alertar
        pass
    
    async def analisar_cadeia_causal_drift(self, drift_detectado: Dict) -> Dict:
        """
        Analisa cadeia causal do drift detectado.
        
        CONCEITO APLICADO: Mapeamento erro → defeito → falha → incidente em ML
        """
        # TODO: IMPLEMENTAR
        #
        # Mapeie cadeia causal:
        # - ERRO: Mudança no processo de coleta/geração de dados
        # - DEFEITO: Modelo não se adapta à nova distribuição
        # - FALHA: Performance degrada abaixo do aceitável
        # - INCIDENTE: Impacto em diagnósticos reais de pacientes
        #
        # Calcule:
        # - Tempo entre detecção de drift e impacto clínico
        # - Severidade do impacto
        # - Populações mais afetadas
        pass

class SistemaQualidadeIA:
    """
    Sistema central de qualidade para IA médica.
    
    CONCEITO APLICADO: Integração de todos os conceitos em sistema de IA
    """
    
    def __init__(self):
        self.verificador = VerificadorModeloIA()
        self.validador = ValidadorContextoMedico()
        self.detector_drift = DetectorDriftModelo()
        
        self.modelos_ativos: Dict[str, Dict] = {}
        self.historico_predicoes: List[PredicaoIA] = []
        self.metricas_continuas: Dict[str, List] = defaultdict(list)
    
    async def avaliar_modelo_completo(self, modelo_id: str, 
                                    dados_teste: List[ExameMedico]) -> Dict:
        """
        Avalia modelo usando verificação E validação.
        
        Returns
        -------
        Dict
            Avaliação completa do modelo
        """
        # TODO: IMPLEMENTAR
        #
        # Avaliação em múltiplas dimensões:
        # 1. VERIFICAÇÃO TÉCNICA:
        #    - Métricas de performance
        #    - Conformidade com padrões
        #    - Robustez técnica
        #
        # 2. VALIDAÇÃO MÉDICA:
        #    - Adequação clínica
        #    - Análise de viés
        #    - Equidade entre populações
        #
        # 3. ANÁLISE TEMPORAL:
        #    - Detecção de drift
        #    - Estabilidade ao longo do tempo
        #
        # 4. EXPLICABILIDADE:
        #    - Interpretabilidade das predições
        #    - Confiança apropriada
        pass
    
    async def monitorar_modelo_producao(self, modelo_id: str) -> Dict:
        """
        Monitora modelo em produção continuamente.
        
        CONCEITO APLICADO: Monitoramento contínuo da cadeia causal
        """
        # TODO: IMPLEMENTAR
        #
        # Monitoramento contínuo:
        # - Performance em tempo real
        # - Detecção de drift automática
        # - Análise de viés contínua
        # - Alertas automáticos
        # - Recomendações de retreinamento
        pass
    
    async def analisar_incidentes_ia(self, incidente_id: str) -> Dict:
        """
        Analisa incidentes relacionados a predições incorretas.
        
        CONCEITO APLICADO: Análise post-mortem em sistemas de IA
        """
        # TODO: IMPLEMENTAR
        #
        # Análise de incidente:
        # 1. RECONSTRUÇÃO DA CADEIA CAUSAL:
        #    - Que dados/contexto levaram à predição incorreta?
        #    - Foi erro de modelo, dados ou contexto?
        #
        # 2. ANÁLISE DE IMPACTO:
        #    - Quantos pacientes foram afetados?
        #    - Quais as consequências clínicas?
        #
        # 3. AÇÕES PREVENTIVAS:
        #    - Como prevenir casos similares?
        #    - Que melhorias são necessárias?
        pass
    
    def gerar_relatorio_qualidade_ia(self) -> str:
        """
        Gera relatório de qualidade específico para IA.
        """
        # TODO: IMPLEMENTAR
        pass

# CENÁRIOS DE TESTE FORNECIDOS
async def test_qualidade_ia():
    """
    Testa sistema de qualidade para IA médica.
    """
    sistema = SistemaQualidadeIA()
    
    print("🤖 TESTE SISTEMA DE QUALIDADE IA - MedAI")
    print("="*60)
    
    # Dados de exemplo
    exames_teste = [
        ExameMedico(
            id="EX001",
            paciente_id="PAC001",
            tipo_exame="radiografia",
            imagem_path="/data/radiografia_001.jpg",
            metadados={
                "idade": 45,
                "genero": "masculino",
                "etnia": "caucasiano",
                "sintomas": ["tosse", "febre", "falta_ar"]
            },
            diagnostico_real="pneumonia"
        )
        # TODO: Adicionar mais exemplos
    ]
    
    # Cenário 1: Avaliação completa de modelo
    print("\n🔍 CENÁRIO 1: Avaliação Completa de Modelo")
    avaliacao = await sistema.avaliar_modelo_completo("modelo_v1.2.3", exames_teste)
    print(f"Avaliação: {avaliacao}")
    
    # Cenário 2: Detecção de viés populacional
    print("\n⚖️ CENÁRIO 2: Análise de Viés")
    # TODO: Simular predições com viés
    
    # Cenário 3: Detecção de drift
    print("\n📈 CENÁRIO 3: Detecção de Drift")
    # TODO: Simular dados com drift
    
    # Cenário 4: Monitoramento em produção
    print("\n📊 CENÁRIO 4: Monitoramento Contínuo")
    monitoramento = await sistema.monitorar_modelo_producao("modelo_v1.2.3")
    print(f"Status: {monitoramento}")
    
    # Relatório final
    print("\n📋 RELATÓRIO DE QUALIDADE IA")
    relatorio = sistema.gerar_relatorio_qualidade_ia()
    print(relatorio)

if __name__ == "__main__":
    asyncio.run(test_qualidade_ia())
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Sistema robusto de verificação técnica para modelos de IA
- [ ] Validação contextual médica sofisticada
- [ ] Detecção avançada de drift e viés
- [ ] Análise profunda da cadeia causal em sistemas de IA
- [ ] Monitoramento contínuo eficaz

#### ✓ Bom (75-89%)
- [ ] Boa implementação de verificação e validação para IA
- [ ] Detecção adequada de problemas comuns
- [ ] Monitoramento básico mas funcional

#### ⚠️ Satisfatório (60-74%)
- [ ] Implementação básica dos conceitos
- [ ] Detecção limitada de problemas

#### ❌ Insuficiente (<60%)
- [ ] Falha na adaptação dos conceitos para IA
- [ ] Sistema inadequado para contexto médico

---

## 🎯 Exercício 3.3 - Plataforma de Qualidade Empresarial

### Contexto
Como **VP of Engineering Quality** na **TechCorp**, você deve projetar uma **Plataforma de Qualidade Empresarial** que unifique qualidade em 50+ produtos, 200+ equipes de desenvolvimento e múltiplas tecnologias. A plataforma deve ser o centro de excelência em qualidade da empresa.

### 📝 Sua Tarefa

Criar uma plataforma que demonstre como os conceitos fundamentais se aplicam em escala empresarial, integrando pessoas, processos e tecnologias.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_3_3.py

# [Implementação do exercício 3.3 - versão resumida para economizar espaço]
# TODO: Implementar plataforma empresarial completa
```

---

## 🎯 Resumo do Nível 3

### Conceitos Masterizados
- ✅ **Escala Global**: Aplicação em contextos multinacionais
- ✅ **IA e ML**: Qualidade em sistemas inteligentes
- ✅ **Plataformas Empresariais**: Qualidade em escala organizacional
- ✅ **Decisões Estratégicas**: Trade-offs de alto nível

### Habilidades Desenvolvidas
- 🌍 **Visão global** de qualidade
- 🤖 **Expertise em IA** e sistemas inteligentes
- 🏢 **Liderança empresarial** em qualidade
- 📈 **Pensamento estratégico** orientado a dados

### Próximos Passos
Parabéns! Você dominou os conceitos fundamentais de teste em múltiplos contextos e escalas. Continue aplicando esses princípios em:
- Projetos reais
- Certificações avançadas
- Pesquisa e inovação
- Liderança técnica

**Você está pronto para liderar qualidade em qualquer contexto!** 🎓
