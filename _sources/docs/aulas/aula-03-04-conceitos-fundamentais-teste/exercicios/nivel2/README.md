# Exercícios Nível 2 - Intermediário 🟡

**Tempo Estimado**: 45-90 minutos por exercício  
**Objetivo**: Integração de múltiplos conceitos fundamentais  
**Complexidade**: Sistemas com interações entre componentes

## 📋 Visão Geral dos Exercícios

1. **Exercício 2.1**: Sistema de Pedidos com Análise de Métricas
2. **Exercício 2.2**: Arquitetura de Qualidade com Trade-offs
3. **Exercício 2.3**: Sistema de Monitoramento Integrado

---

## 🎯 Exercício 2.1 - Sistema de Pedidos: Integração da Cadeia Causal com Métricas

### Contexto
Você é o **Arquiteto de Qualidade** da **TechFood**, uma plataforma de delivery que processa 50.000 pedidos por dia. Recentemente, a empresa tem enfrentado problemas complexos que afetam múltiplos sistemas. Sua missão é criar um **Sistema Integrado de Qualidade** que:

1. **Monitore** a cadeia causal em tempo real
2. **Aplique** verificação e validação em múltiplas camadas
3. **Analise** métricas de qualidade e performance
4. **Otimize** trade-offs entre qualidade, performance e custo

### Cenário Realista
A TechFood tem três sistemas principais que precisam trabalhar em harmonia:
- **Sistema de Pedidos** (core business)
- **Sistema de Pagamento** (crítico para receita)
- **Sistema de Entrega** (impacta experiência do usuário)

Problemas recentes incluem:
- Pedidos sendo aceitos mas pagamentos falhando
- Pagamentos aprovados mas entregas não sendo agendadas
- Inconsistências entre sistemas causando perda de receita

### 📝 Sua Tarefa

Implementar um **Sistema de Qualidade Integrado** que demonstre como os conceitos fundamentais se aplicam em arquiteturas complexas com múltiplas interdependências.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_2_1.py

from typing import Dict, List, Optional, Tuple, Callable, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import json
import uuid
from collections import defaultdict

class StatusSistema(Enum):
    """Status dos sistemas integrados."""
    OPERACIONAL = "operacional"
    DEGRADADO = "degradado"
    FALHA = "falha"
    MANUTENCAO = "manutencao"

class TipoEvento(Enum):
    """Tipos de eventos no sistema integrado."""
    PEDIDO_CRIADO = "pedido_criado"
    PAGAMENTO_PROCESSADO = "pagamento_processado"
    ENTREGA_AGENDADA = "entrega_agendada"
    ERRO_DETECTADO = "erro_detectado"
    FALHA_SISTEMA = "falha_sistema"
    INCIDENTE_NEGOCIO = "incidente_negocio"

@dataclass
class MetricasQualidade:
    """Métricas consolidadas de qualidade do sistema."""
    timestamp: datetime
    taxa_sucesso_pedidos: float  # 0.0 a 1.0
    tempo_medio_processamento: float  # em segundos
    taxa_erro_pagamento: float
    taxa_falha_entrega: float
    latencia_causal_media: float  # tempo erro → incidente
    eficacia_deteccao: float  # defeitos detectados vs escapados
    custo_qualidade: float  # investimento em qualidade
    roi_qualidade: float  # retorno do investimento em qualidade

@dataclass
class EventoSistema:
    """Representa um evento no sistema integrado."""
    id: str
    tipo: TipoEvento
    timestamp: datetime
    sistema_origem: str
    dados: Dict[str, Any]
    correlation_id: str
    contexto_verificacao: Optional[Dict] = None
    contexto_validacao: Optional[Dict] = None

@dataclass
class PedidoCompleto:
    """Representa um pedido completo no sistema integrado."""
    id: str
    cliente_id: str
    itens: List[Dict]
    valor_total: float
    status_pedido: str
    status_pagamento: str
    status_entrega: str
    timestamps: Dict[str, datetime] = field(default_factory=dict)
    eventos: List[EventoSistema] = field(default_factory=list)

class SistemaPedidos:
    """
    Sistema de pedidos com verificação e validação integradas.
    
    CONCEITO APLICADO: Verificação (regras de negócio) + Validação (contexto do cliente)
    """
    
    def __init__(self, qualidade_manager):
        self.qualidade_manager = qualidade_manager
        self.pedidos: Dict[str, PedidoCompleto] = {}
        self.regras_verificacao = self._definir_regras_verificacao()
        self.politicas_validacao = self._definir_politicas_validacao()
    
    async def processar_pedido(self, dados_pedido: Dict) -> Tuple[bool, str, Optional[PedidoCompleto]]:
        """
        Processa pedido aplicando verificação E validação.
        
        Returns
        -------
        Tuple[bool, str, Optional[PedidoCompleto]]
            (sucesso, mensagem, pedido_criado)
        """
        # TODO: IMPLEMENTAR
        #
        # 1. VERIFICAÇÃO TÉCNICA:
        #    - Dados obrigatórios presentes?
        #    - Formatos corretos?
        #    - Valores dentro dos limites?
        #    - Itens disponíveis no estoque?
        #
        # 2. VALIDAÇÃO CONTEXTUAL:
        #    - Cliente tem histórico confiável?
        #    - Valor do pedido é consistente com perfil?
        #    - Localização de entrega é atendida?
        #    - Horário do pedido é adequado?
        #
        # 3. INTEGRAÇÃO COM QUALIDADE:
        #    - Registre evento no sistema de qualidade
        #    - Se falhar, identifique se é erro, defeito, falha ou incidente
        #    - Atualize métricas em tempo real
        #
        # DICA: Use correlation_id para rastrear fluxo completo
        pass
    
    def _definir_regras_verificacao(self) -> Dict[str, Callable]:
        """Define regras técnicas de verificação."""
        return {
            "dados_obrigatorios": lambda pedido: all(
                key in pedido for key in ["cliente_id", "itens", "endereco_entrega"]
            ),
            "valor_minimo": lambda pedido: pedido.get("valor_total", 0) >= 10.0,
            "valor_maximo": lambda pedido: pedido.get("valor_total", 0) <= 1000.0,
            "itens_validos": lambda pedido: len(pedido.get("itens", [])) > 0,
            "endereco_formato": lambda pedido: self._validar_formato_endereco(
                pedido.get("endereco_entrega", {})
            )
        }
    
    def _definir_politicas_validacao(self) -> Dict[str, Callable]:
        """Define políticas contextuais de validação."""
        return {
            "cliente_confiavel": lambda pedido, contexto: self._avaliar_confiabilidade_cliente(
                pedido.get("cliente_id"), contexto
            ),
            "valor_consistente": lambda pedido, contexto: self._validar_consistencia_valor(
                pedido, contexto
            ),
            "regiao_atendida": lambda pedido, contexto: self._validar_regiao_entrega(
                pedido.get("endereco_entrega"), contexto
            ),
            "horario_adequado": lambda pedido, contexto: self._validar_horario_pedido(
                pedido, contexto
            )
        }
    
    def _validar_formato_endereco(self, endereco: Dict) -> bool:
        """Valida formato do endereço."""
        # TODO: Implementar validação de formato
        pass
    
    def _avaliar_confiabilidade_cliente(self, cliente_id: str, contexto: Dict) -> bool:
        """Avalia confiabilidade do cliente baseado em histórico."""
        # TODO: Implementar análise de histórico do cliente
        pass
    
    def _validar_consistencia_valor(self, pedido: Dict, contexto: Dict) -> bool:
        """Valida se valor é consistente com perfil do cliente."""
        # TODO: Implementar validação de consistência
        pass
    
    def _validar_regiao_entrega(self, endereco: Dict, contexto: Dict) -> bool:
        """Valida se região é atendida."""
        # TODO: Implementar validação de região
        pass
    
    def _validar_horario_pedido(self, pedido: Dict, contexto: Dict) -> bool:
        """Valida se horário é adequado para entrega."""
        # TODO: Implementar validação de horário
        pass

class SistemaPagamento:
    """Sistema de pagamento com análise de risco integrada."""
    
    def __init__(self, qualidade_manager):
        self.qualidade_manager = qualidade_manager
        self.transacoes: Dict[str, Dict] = {}
    
    async def processar_pagamento(self, pedido: PedidoCompleto) -> Tuple[bool, str]:
        """
        Processa pagamento com análise de risco e qualidade.
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Análise de risco (validação contextual)
        # 2. Processamento técnico (verificação)
        # 3. Registro de eventos para cadeia causal
        # 4. Atualização de métricas
        pass

class SistemaEntrega:
    """Sistema de entrega com otimização de rotas."""
    
    def __init__(self, qualidade_manager):
        self.qualidade_manager = qualidade_manager
        self.entregas: Dict[str, Dict] = {}
    
    async def agendar_entrega(self, pedido: PedidoCompleto) -> Tuple[bool, str]:
        """
        Agenda entrega com otimização e validação.
        """
        # TODO: IMPLEMENTAR
        pass

class GerenciadorQualidade:
    """
    Gerenciador central de qualidade que integra todos os sistemas.
    
    CONCEITO APLICADO: Visão holística da qualidade em arquiteturas distribuídas
    """
    
    def __init__(self):
        self.eventos: List[EventoSistema] = []
        self.metricas_historico: List[MetricasQualidade] = []
        self.alertas_ativos: List[Dict] = []
        self.cadeia_causal_ativa: Dict[str, List[EventoSistema]] = defaultdict(list)
    
    def registrar_evento(self, evento: EventoSistema):
        """
        Registra evento e atualiza análise de cadeia causal.
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Adicione evento ao histórico
        # 2. Atualize cadeia causal para correlation_id
        # 3. Detecte padrões de erro → defeito → falha → incidente
        # 4. Calcule métricas em tempo real
        # 5. Dispare alertas se necessário
        pass
    
    def calcular_metricas_tempo_real(self) -> MetricasQualidade:
        """
        Calcula métricas de qualidade em tempo real.
        """
        # TODO: IMPLEMENTAR
        #
        # Calcule métricas baseadas em eventos recentes:
        # - Taxa de sucesso por sistema
        # - Latência causal (tempo erro → incidente)
        # - Eficácia de detecção
        # - ROI de qualidade
        pass
    
    def analisar_cadeia_causal(self, correlation_id: str) -> Dict:
        """
        Analisa cadeia causal completa para um fluxo específico.
        """
        # TODO: IMPLEMENTAR
        #
        # Para um correlation_id específico:
        # 1. Identifique todos os eventos relacionados
        # 2. Mapeie a progressão erro → defeito → falha → incidente
        # 3. Calcule tempo entre cada estágio
        # 4. Identifique pontos de intervenção
        pass
    
    def otimizar_tradeoffs(self, objetivos: Dict[str, float]) -> Dict[str, Any]:
        """
        Otimiza trade-offs entre qualidade, performance e custo.
        
        Parameters
        ----------
        objetivos : Dict[str, float]
            Pesos para objetivos: {"qualidade": 0.4, "performance": 0.4, "custo": 0.2}
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Analise métricas atuais
        # 2. Identifique gargalos e oportunidades
        # 3. Calcule cenários de otimização
        # 4. Recomende ajustes baseados nos pesos dos objetivos
        #
        # EXEMPLO: Se qualidade tem peso alto, sugira mais verificações
        #          Se custo tem peso alto, sugira otimizações de eficiência
        pass
    
    def gerar_relatorio_integrado(self) -> str:
        """
        Gera relatório integrado de qualidade do sistema.
        """
        # TODO: IMPLEMENTAR
        #
        # O relatório deve incluir:
        # - Métricas consolidadas de todos os sistemas
        # - Análise de cadeias causais identificadas
        # - Recomendações de melhoria
        # - Trade-offs atuais e oportunidades de otimização
        pass

class OrquestradorSistemaIntegrado:
    """
    Orquestrador que gerencia o fluxo completo pedido → pagamento → entrega.
    
    CONCEITO APLICADO: Gestão de qualidade em fluxos distribuídos
    """
    
    def __init__(self):
        self.qualidade = GerenciadorQualidade()
        self.sistema_pedidos = SistemaPedidos(self.qualidade)
        self.sistema_pagamento = SistemaPagamento(self.qualidade)
        self.sistema_entrega = SistemaEntrega(self.qualidade)
    
    async def processar_fluxo_completo(self, dados_pedido: Dict) -> Dict:
        """
        Processa fluxo completo com monitoramento de qualidade integrado.
        
        Returns
        -------
        Dict
            Resultado completo com análise de qualidade
        """
        correlation_id = str(uuid.uuid4())
        
        # TODO: IMPLEMENTAR
        #
        # 1. Processe pedido com verificação/validação
        # 2. Se sucesso, processe pagamento
        # 3. Se pagamento OK, agende entrega
        # 4. Monitore qualidade em cada etapa
        # 5. Analise cadeia causal completa
        # 6. Calcule métricas finais
        #
        # IMPORTANTE: Use correlation_id para rastrear fluxo completo
        pass
    
    async def simular_cenarios_falha(self) -> Dict:
        """
        Simula diferentes cenários de falha para análise de robustez.
        """
        # TODO: IMPLEMENTAR
        #
        # Simule cenários como:
        # - Falha no pagamento após pedido aceito
        # - Falha na entrega após pagamento processado
        # - Inconsistência entre sistemas
        # - Sobrecarga de um sistema específico
        #
        # Para cada cenário, analise:
        # - Como a cadeia causal se desenvolve
        # - Qual o impacto nas métricas
        # - Quais pontos de recuperação existem
        pass

# CENÁRIOS DE TESTE FORNECIDOS
async def test_sistema_integrado():
    """
    Testa sistema integrado com cenários realistas da TechFood.
    """
    orquestrador = OrquestradorSistemaIntegrado()
    
    print("🍕 TESTE SISTEMA INTEGRADO - TechFood")
    print("="*60)
    
    # Cenário 1: Fluxo normal bem-sucedido
    pedido_normal = {
        "cliente_id": "cliente_001",
        "itens": [
            {"id": "pizza_margherita", "quantidade": 2, "preco": 25.90},
            {"id": "refrigerante_coca", "quantidade": 1, "preco": 5.50}
        ],
        "endereco_entrega": {
            "rua": "Rua das Flores, 123",
            "bairro": "Centro",
            "cidade": "São Paulo",
            "cep": "01234-567"
        },
        "valor_total": 57.30,
        "metodo_pagamento": "cartao_credito"
    }
    
    print("\n🎯 CENÁRIO 1: Fluxo Normal")
    resultado1 = await orquestrador.processar_fluxo_completo(pedido_normal)
    print(f"Resultado: {resultado1}")
    
    # Cenário 2: Pedido com problemas de validação
    pedido_suspeito = {
        "cliente_id": "cliente_novo_002",
        "itens": [
            {"id": "pizza_premium", "quantidade": 10, "preco": 89.90}  # Quantidade suspeita
        ],
        "endereco_entrega": {
            "rua": "Rua Inexistente, 999",
            "bairro": "Bairro Não Atendido",
            "cidade": "São Paulo",
            "cep": "99999-999"
        },
        "valor_total": 899.00,  # Valor alto para cliente novo
        "metodo_pagamento": "cartao_credito"
    }
    
    print("\n⚠️ CENÁRIO 2: Pedido Suspeito")
    resultado2 = await orquestrador.processar_fluxo_completo(pedido_suspeito)
    print(f"Resultado: {resultado2}")
    
    # Cenário 3: Simulação de falhas
    print("\n💥 CENÁRIO 3: Simulação de Falhas")
    cenarios_falha = await orquestrador.simular_cenarios_falha()
    print(f"Análise de robustez: {cenarios_falha}")
    
    # Análise de métricas consolidadas
    print("\n📊 MÉTRICAS CONSOLIDADAS")
    metricas = orquestrador.qualidade.calcular_metricas_tempo_real()
    print(f"Taxa de sucesso: {metricas.taxa_sucesso_pedidos:.1%}")
    print(f"Tempo médio: {metricas.tempo_medio_processamento:.2f}s")
    print(f"Eficácia detecção: {metricas.eficacia_deteccao:.1%}")
    print(f"ROI qualidade: {metricas.roi_qualidade:.2f}")
    
    # Otimização de trade-offs
    print("\n⚖️ OTIMIZAÇÃO DE TRADE-OFFS")
    objetivos = {"qualidade": 0.5, "performance": 0.3, "custo": 0.2}
    otimizacao = orquestrador.qualidade.otimizar_tradeoffs(objetivos)
    print(f"Recomendações: {otimizacao}")
    
    # Relatório integrado
    print("\n📋 RELATÓRIO INTEGRADO")
    relatorio = orquestrador.qualidade.gerar_relatorio_integrado()
    print(relatorio)

if __name__ == "__main__":
    asyncio.run(test_sistema_integrado())
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Integra cadeia causal, verificação/validação e métricas perfeitamente
- [ ] Sistema robusto com tratamento de falhas e recuperação
- [ ] Análise profunda de trade-offs qualidade vs performance vs custo
- [ ] Métricas precisas e otimização baseada em dados
- [ ] Código bem arquitetado com separação clara de responsabilidades

#### ✓ Bom (75-89%)
- [ ] Boa integração dos conceitos principais
- [ ] Sistema funcional com tratamento básico de falhas
- [ ] Análise adequada de trade-offs
- [ ] Métricas implementadas corretamente
- [ ] Arquitetura sólida

#### ⚠️ Satisfatório (60-74%)
- [ ] Integração básica dos conceitos
- [ ] Sistema funciona mas falta robustez
- [ ] Trade-offs considerados superficialmente
- [ ] Métricas limitadas

#### ❌ Insuficiente (<60%)
- [ ] Falha na integração dos conceitos
- [ ] Sistema instável ou incompleto
- [ ] Não demonstra compreensão de trade-offs

### 💡 Dicas para Sucesso

1. **Pense em fluxos**, não apenas componentes isolados
2. **Use correlation_id** para rastrear jornadas completas
3. **Implemente circuit breakers** para resiliência
4. **Meça tudo** que é importante para o negócio
5. **Documente trade-offs** e justifique decisões

---

## 🎯 Exercício 2.2 - Arquitetura de Qualidade: Design Patterns para Teste

### Contexto
Como **Arquiteto Sênior** na **HealthTech Solutions**, você precisa projetar a arquitetura de qualidade para um sistema crítico de **Gestão de Prontuários Eletrônicos**. O sistema deve atender rigorosos padrões de segurança, disponibilidade e integridade de dados.

### Cenário Realista
O sistema HealthTech processa dados médicos sensíveis de 200 hospitais, com requisitos rígidos:
- **99.9% de disponibilidade** (máximo 8.7 horas de downtime por ano)
- **Zero perda de dados** médicos
- **Conformidade** com LGPD e normas médicas
- **Auditoria completa** de todas as operações

### 📝 Sua Tarefa

Projetar uma **Arquitetura de Qualidade** que incorpore design patterns específicos para teste e qualidade, demonstrando como os conceitos fundamentais se manifestam em decisões arquiteturais.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_2_2.py

from typing import Dict, List, Optional, Callable, Any, Protocol
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from abc import ABC, abstractmethod
import asyncio
import json
import logging
from contextlib import asynccontextmanager

class CriticidadeOperacao(Enum):
    """Níveis de criticidade para operações médicas."""
    BAIXA = "baixa"          # Consulta de dados não críticos
    MEDIA = "media"          # Atualizações de rotina
    ALTA = "alta"            # Operações que afetam tratamento
    CRITICA = "critica"      # Operações que afetam vida do paciente

class TipoVerificacao(Enum):
    """Tipos de verificação no sistema médico."""
    INTEGRIDADE_DADOS = "integridade_dados"
    CONFORMIDADE_LGPD = "conformidade_lgpd"
    VALIDACAO_MEDICA = "validacao_medica"
    SEGURANCA_ACESSO = "seguranca_acesso"
    AUDITORIA = "auditoria"

@dataclass
class ContextoMedico:
    """Contexto médico para validação."""
    paciente_id: str
    medico_id: str
    hospital_id: str
    especialidade: str
    urgencia: CriticidadeOperacao
    dados_sensibilidade: str  # "normal", "alto", "critico"

# PATTERN: Strategy para diferentes tipos de verificação
class VerificadorStrategy(ABC):
    """Strategy base para diferentes tipos de verificação."""
    
    @abstractmethod
    async def verificar(self, dados: Any, contexto: ContextoMedico) -> Tuple[bool, str]:
        """Executa verificação específica."""
        pass

class VerificadorIntegridadeDados(VerificadorStrategy):
    """Verificador de integridade de dados médicos."""
    
    async def verificar(self, dados: Any, contexto: ContextoMedico) -> Tuple[bool, str]:
        """
        Verifica integridade técnica dos dados médicos.
        
        CONCEITO APLICADO: Verificação = Conformidade com padrões técnicos
        """
        # TODO: IMPLEMENTAR
        #
        # Verifique:
        # - Dados obrigatórios presentes
        # - Formatos corretos (CPF, datas, códigos CID)
        # - Checksums e assinaturas digitais
        # - Consistência interna dos dados
        pass

class ValidadorContextoMedico(VerificadorStrategy):
    """Validador contextual para operações médicas."""
    
    async def verificar(self, dados: Any, contexto: ContextoMedico) -> Tuple[bool, str]:
        """
        Valida se operação é adequada ao contexto médico.
        
        CONCEITO APLICADO: Validação = Adequação ao propósito médico
        """
        # TODO: IMPLEMENTAR
        #
        # Valide:
        # - Médico tem permissão para a especialidade?
        # - Operação é apropriada para o paciente?
        # - Horário da operação é adequado?
        # - Dados são consistentes com histórico médico?
        pass

# PATTERN: Chain of Responsibility para cadeia de qualidade
class ProcessadorQualidade(ABC):
    """Base para processadores na cadeia de qualidade."""
    
    def __init__(self):
        self._proximo: Optional[ProcessadorQualidade] = None
    
    def definir_proximo(self, proximo: 'ProcessadorQualidade') -> 'ProcessadorQualidade':
        self._proximo = proximo
        return proximo
    
    @abstractmethod
    async def processar(self, operacao: Dict, contexto: ContextoMedico) -> bool:
        """Processa operação na cadeia de qualidade."""
        pass

class ProcessadorVerificacao(ProcessadorQualidade):
    """Processador de verificação técnica."""
    
    def __init__(self, verificadores: List[VerificadorStrategy]):
        super().__init__()
        self.verificadores = verificadores
    
    async def processar(self, operacao: Dict, contexto: ContextoMedico) -> bool:
        """Executa todas as verificações técnicas."""
        # TODO: IMPLEMENTAR
        #
        # 1. Execute todos os verificadores
        # 2. Se algum falhar, pare a cadeia
        # 3. Registre resultados para auditoria
        # 4. Se todos passarem, continue para próximo na cadeia
        pass

class ProcessadorValidacao(ProcessadorQualidade):
    """Processador de validação contextual."""
    
    async def processar(self, operacao: Dict, contexto: ContextoMedico) -> bool:
        """Executa validação contextual."""
        # TODO: IMPLEMENTAR
        pass

class ProcessadorAuditoria(ProcessadorQualidade):
    """Processador de auditoria e logging."""
    
    async def processar(self, operacao: Dict, contexto: ContextoMedico) -> bool:
        """Registra operação para auditoria."""
        # TODO: IMPLEMENTAR
        pass

# PATTERN: Observer para monitoramento de qualidade
class ObservadorQualidade(ABC):
    """Observer para eventos de qualidade."""
    
    @abstractmethod
    async def notificar_evento(self, evento: str, dados: Dict):
        """Processa evento de qualidade."""
        pass

class MonitorMetricas(ObservadorQualidade):
    """Observer que monitora métricas de qualidade."""
    
    def __init__(self):
        self.metricas: Dict[str, List[float]] = {}
    
    async def notificar_evento(self, evento: str, dados: Dict):
        """Atualiza métricas baseado em eventos."""
        # TODO: IMPLEMENTAR
        pass

class AlertasCriticos(ObservadorQualidade):
    """Observer que gerencia alertas críticos."""
    
    async def notificar_evento(self, evento: str, dados: Dict):
        """Processa alertas críticos em tempo real."""
        # TODO: IMPLEMENTAR
        pass

# PATTERN: Circuit Breaker para resiliência
class CircuitBreaker:
    """Circuit Breaker para proteção de sistemas críticos."""
    
    def __init__(self, limite_falhas: int = 5, timeout_segundos: int = 60):
        self.limite_falhas = limite_falhas
        self.timeout_segundos = timeout_segundos
        self.contador_falhas = 0
        self.estado = "fechado"  # fechado, aberto, meio_aberto
        self.ultimo_erro = None
    
    @asynccontextmanager
    async def proteger_operacao(self):
        """Context manager para proteger operações críticas."""
        # TODO: IMPLEMENTAR
        #
        # Estados do Circuit Breaker:
        # - FECHADO: Operações normais, conta falhas
        # - ABERTO: Rejeita operações rapidamente
        # - MEIO_ABERTO: Testa se sistema recuperou
        #
        # CONCEITO APLICADO: Prevenção de propagação de falhas
        # em sistemas distribuídos
        pass

# PATTERN: Factory para criação de verificadores
class FabricaVerificadores:
    """Factory para criar verificadores baseados no contexto."""
    
    @staticmethod
    def criar_verificadores(contexto: ContextoMedico) -> List[VerificadorStrategy]:
        """
        Cria verificadores apropriados para o contexto médico.
        
        CONCEITO APLICADO: Adaptação da verificação ao contexto
        """
        # TODO: IMPLEMENTAR
        #
        # Baseado na criticidade e tipo de operação:
        # - CRITICA: Todos os verificadores + extras
        # - ALTA: Verificadores essenciais + validação rigorosa
        # - MEDIA: Verificadores padrão
        # - BAIXA: Verificadores mínimos
        pass

class ArquiteturaQualidadeMedica:
    """
    Arquitetura principal que orquestra todos os patterns de qualidade.
    
    CONCEITO APLICADO: Integração sistêmica de todos os conceitos
    fundamentais em uma arquitetura coesa
    """
    
    def __init__(self):
        self.observadores: List[ObservadorQualidade] = []
        self.circuit_breaker = CircuitBreaker()
        self.cadeia_qualidade = self._construir_cadeia_qualidade()
        self.metricas_globais = {}
    
    def adicionar_observador(self, observador: ObservadorQualidade):
        """Adiciona observador ao sistema."""
        self.observadores.append(observador)
    
    async def notificar_observadores(self, evento: str, dados: Dict):
        """Notifica todos os observadores."""
        for observador in self.observadores:
            await observador.notificar_evento(evento, dados)
    
    def _construir_cadeia_qualidade(self) -> ProcessadorQualidade:
        """Constrói cadeia de responsabilidade para qualidade."""
        # TODO: IMPLEMENTAR
        #
        # Crie cadeia: Verificação → Validação → Auditoria
        # Cada processador deve poder interromper a cadeia se necessário
        pass
    
    async def executar_operacao_medica(self, operacao: Dict, 
                                     contexto: ContextoMedico) -> Dict:
        """
        Executa operação médica com garantias de qualidade.
        
        Returns
        -------
        Dict
            Resultado com análise completa de qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Use Circuit Breaker para proteger operação
        # 2. Execute cadeia de qualidade
        # 3. Monitore cadeia causal em tempo real
        # 4. Notifique observadores dos eventos
        # 5. Calcule métricas de qualidade
        # 6. Retorne resultado com análise completa
        #
        # IMPORTANTE: Esta é a integração de TODOS os conceitos
        pass
    
    async def analisar_impacto_arquitetural(self) -> Dict:
        """
        Analisa impacto das decisões arquiteturais na qualidade.
        
        CONCEITO APLICADO: Como patterns de design afetam
        a eficácia dos conceitos fundamentais
        """
        # TODO: IMPLEMENTAR
        #
        # Analise:
        # - Como Strategy pattern afeta verificação/validação
        # - Como Chain of Responsibility melhora detecção de problemas
        # - Como Observer pattern acelera resposta a incidentes
        # - Como Circuit Breaker previne propagação de falhas
        # - Trade-offs entre performance e qualidade
        pass
    
    def gerar_relatorio_arquitetural(self) -> str:
        """
        Gera relatório sobre eficácia da arquitetura de qualidade.
        """
        # TODO: IMPLEMENTAR
        pass

# CENÁRIOS DE TESTE FORNECIDOS
async def test_arquitetura_qualidade():
    """
    Testa arquitetura de qualidade com cenários médicos realistas.
    """
    arquitetura = ArquiteturaQualidadeMedica()
    
    # Adiciona observadores
    arquitetura.adicionar_observador(MonitorMetricas())
    arquitetura.adicionar_observador(AlertasCriticos())
    
    print("🏥 TESTE ARQUITETURA DE QUALIDADE - HealthTech")
    print("="*60)
    
    # Cenário 1: Operação crítica - Cirurgia cardíaca
    contexto_critico = ContextoMedico(
        paciente_id="PAC_12345",
        medico_id="MED_789",
        hospital_id="HOSP_001",
        especialidade="cardiologia",
        urgencia=CriticidadeOperacao.CRITICA,
        dados_sensibilidade="critico"
    )
    
    operacao_critica = {
        "tipo": "atualizacao_prontuario",
        "dados": {
            "prescricao": "Procedimento cirúrgico cardíaco de emergência",
            "medicamentos": ["Heparina 5000UI", "Propofol 200mg"],
            "alergias": ["Penicilina"],
            "comorbidades": ["Diabetes Tipo 2", "Hipertensão"]
        },
        "timestamp": datetime.now().isoformat()
    }
    
    print("\n💓 CENÁRIO 1: Operação Crítica - Cardiologia")
    resultado1 = await arquitetura.executar_operacao_medica(operacao_critica, contexto_critico)
    print(f"Resultado: {resultado1}")
    
    # Cenário 2: Operação rotineira - Consulta dermatologia
    contexto_rotina = ContextoMedico(
        paciente_id="PAC_67890",
        medico_id="MED_456",
        hospital_id="HOSP_002",
        especialidade="dermatologia",
        urgencia=CriticidadeOperacao.BAIXA,
        dados_sensibilidade="normal"
    )
    
    operacao_rotina = {
        "tipo": "consulta_historico",
        "dados": {
            "motivo": "Acompanhamento dermatológico de rotina",
            "periodo": "últimos 6 meses"
        },
        "timestamp": datetime.now().isoformat()
    }
    
    print("\n🔍 CENÁRIO 2: Operação Rotineira - Dermatologia")
    resultado2 = await arquitetura.executar_operacao_medica(operacao_rotina, contexto_rotina)
    print(f"Resultado: {resultado2}")
    
    # Cenário 3: Simulação de falhas e recuperação
    print("\n⚡ CENÁRIO 3: Teste de Resiliência")
    # TODO: Simule falhas no sistema e teste recovery
    
    # Análise arquitetural
    print("\n🏗️ ANÁLISE ARQUITETURAL")
    analise = await arquitetura.analisar_impacto_arquitetural()
    print(f"Impacto dos patterns: {analise}")
    
    # Relatório final
    print("\n📋 RELATÓRIO ARQUITETURAL")
    relatorio = arquitetura.gerar_relatorio_arquitetural()
    print(relatorio)

if __name__ == "__main__":
    asyncio.run(test_arquitetura_qualidade())
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Implementa todos os design patterns corretamente
- [ ] Integração perfeita entre verificação, validação e patterns
- [ ] Sistema resiliente com Circuit Breaker eficaz
- [ ] Análise profunda do impacto arquitetural na qualidade
- [ ] Código exemplar com separação clara de responsabilidades

#### ✓ Bom (75-89%)
- [ ] Boa implementação dos patterns principais
- [ ] Integração adequada dos conceitos
- [ ] Sistema funcional com resiliência básica
- [ ] Análise competente do impacto arquitetural

#### ⚠️ Satisfatório (60-74%)
- [ ] Implementação básica dos patterns
- [ ] Integração limitada dos conceitos
- [ ] Sistema funciona mas falta robustez

#### ❌ Insuficiente (<60%)
- [ ] Falha na implementação dos patterns
- [ ] Não demonstra compreensão da integração
- [ ] Sistema instável ou inadequado

### 💡 Dicas para Sucesso

1. **Cada pattern tem um propósito** específico na qualidade
2. **Strategy** permite adaptar verificação ao contexto
3. **Chain of Responsibility** garante processamento ordenado
4. **Observer** permite monitoramento reativo
5. **Circuit Breaker** previne cascata de falhas

---

## 🎯 Exercício 2.3 - Sistema de Monitoramento: Métricas Avançadas

### Contexto
Como **Especialista em Observabilidade** na **CryptoExchange**, você deve implementar um sistema de monitoramento que detecte problemas antes que se tornem incidentes críticos. A exchange processa $50 milhões em transações diárias e não pode ter downtime.

### Cenário Realista
A CryptoExchange enfrenta desafios únicos:
- **Volatilidade extrema** no volume de transações
- **Latência sub-segundo** é crítica para traders
- **Segurança** é fundamental (alvos de hackers)
- **Conformidade** com regulamentações financeiras

### 📝 Sua Tarefa

Implementar um **Sistema de Monitoramento Inteligente** que use os conceitos fundamentais para detectar, analisar e responder a problemas em tempo real.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_2_3.py

from typing import Dict, List, Optional, Callable, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import json
import statistics
import numpy as np
from collections import deque, defaultdict

class TipoAlerta(Enum):
    """Tipos de alertas no sistema."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class StatusSistema(Enum):
    """Status dos componentes do sistema."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    DOWN = "down"
    UNKNOWN = "unknown"

@dataclass
class MetricaTempo:
    """Métrica com timestamp para análise temporal."""
    valor: float
    timestamp: datetime
    contexto: Dict[str, Any] = field(default_factory=dict)

@dataclass
class EventoMonitoramento:
    """Evento detectado pelo sistema de monitoramento."""
    id: str
    timestamp: datetime
    tipo: TipoAlerta
    sistema: str
    metrica: str
    valor_atual: float
    valor_esperado: float
    desvio: float
    contexto: Dict[str, Any]

class DetectorAnomalias:
    """
    Detector de anomalias baseado em aprendizado estatístico.
    
    CONCEITO APLICADO: Detecção precoce de problemas antes
    que se manifestem como falhas visíveis
    """
    
    def __init__(self, janela_historico: int = 100):
        self.janela_historico = janela_historico
        self.historico_metricas: Dict[str, deque] = defaultdict(
            lambda: deque(maxlen=janela_historico)
        )
        self.modelos_baseline: Dict[str, Dict] = {}
    
    def treinar_baseline(self, metrica_nome: str, valores_historicos: List[float]):
        """
        Treina modelo baseline para uma métrica específica.
        
        CONCEITO APLICADO: Estabelece "normalidade" para detectar desvios
        """
        # TODO: IMPLEMENTAR
        #
        # Calcule estatísticas baseline:
        # - Média e desvio padrão
        # - Percentis (P50, P95, P99)
        # - Tendências sazonais
        # - Limites de controle estatístico
        #
        # DICA: Use conceitos de controle estatístico de qualidade
        pass
    
    def detectar_anomalia(self, metrica_nome: str, valor: float, 
                         contexto: Dict = None) -> Optional[EventoMonitoramento]:
        """
        Detecta se valor atual é anômalo baseado no baseline.
        
        Returns
        -------
        Optional[EventoMonitoramento]
            Evento se anomalia detectada, None caso contrário
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Compare valor com baseline da métrica
        # 2. Calcule z-score e outros indicadores
        # 3. Considere contexto (horário, dia da semana, etc.)
        # 4. Se anômalo, crie EventoMonitoramento
        # 5. Atualize histórico da métrica
        #
        # CRITÉRIOS DE ANOMALIA:
        # - Z-score > 3 (3 sigma)
        # - Percentil > P99 ou < P1
        # - Mudança súbita > threshold
        pass
    
    def analisar_tendencias(self, metrica_nome: str) -> Dict:
        """
        Analisa tendências temporais na métrica.
        
        CONCEITO APLICADO: Predição de problemas futuros
        baseado em padrões históricos
        """
        # TODO: IMPLEMENTAR
        #
        # Analise:
        # - Tendência de crescimento/decrescimento
        # - Sazonalidade
        # - Volatilidade
        # - Pontos de mudança
        pass

class AnalisadorCadeiaCanal:
    """
    Analisador que mapeia eventos para cadeia causal.
    
    CONCEITO APLICADO: Rastreamento de erro → defeito → falha → incidente
    em sistemas de alta performance
    """
    
    def __init__(self):
        self.eventos_correlacionados: Dict[str, List[EventoMonitoramento]] = {}
        self.cadeias_ativas: Dict[str, Dict] = {}
    
    def correlacionar_eventos(self, evento: EventoMonitoramento, 
                            janela_correlacao: timedelta = timedelta(minutes=5)) -> List[str]:
        """
        Correlaciona evento com outros eventos próximos no tempo.
        
        Returns
        -------
        List[str]
            Lista de IDs de eventos correlacionados
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Busque eventos na janela de tempo
        # 2. Analise correlações por:
        #    - Sistema afetado
        #    - Tipo de métrica
        #    - Padrão temporal
        # 3. Use heurísticas para identificar causalidade
        pass
    
    def identificar_cadeia_causal(self, eventos_correlacionados: List[EventoMonitoramento]) -> Dict:
        """
        Identifica cadeia causal completa a partir de eventos correlacionados.
        
        Returns
        -------
        Dict
            Análise da cadeia causal identificada
        """
        # TODO: IMPLEMENTAR
        #
        # Mapeie eventos para cadeia causal:
        # - ERRO: Primeiros sinais de problemas (latência alta, CPU alto)
        # - DEFEITO: Manifestação em componentes (timeout, exception)
        # - FALHA: Comportamento incorreto visível (transação falha)
        # - INCIDENTE: Impacto no usuário/negócio (perda de clientes)
        #
        # CALCULE:
        # - Tempo entre cada estágio
        # - Amplitude do impacto
        # - Sistemas afetados
        pass

class VerificadorSLA:
    """
    Verificador de SLA (Service Level Agreement).
    
    CONCEITO APLICADO: Verificação de conformidade com padrões de serviço
    """
    
    def __init__(self):
        self.slas_definidos = self._definir_slas()
        self.historico_violacoes: List[Dict] = []
    
    def _definir_slas(self) -> Dict:
        """Define SLAs para diferentes métricas."""
        return {
            "latencia_api": {"limite": 100.0, "unidade": "ms", "percentil": 95},
            "disponibilidade": {"limite": 99.9, "unidade": "%", "periodo": "mes"},
            "throughput": {"limite": 1000.0, "unidade": "req/s", "minimo": True},
            "taxa_erro": {"limite": 0.1, "unidade": "%", "maximo": True}
        }
    
    def verificar_sla(self, metrica_nome: str, valor: float, 
                     periodo: timedelta = timedelta(hours=1)) -> Tuple[bool, Dict]:
        """
        Verifica se métrica está em conformidade com SLA.
        
        CONCEITO APLICADO: Verificação = conformidade com especificações
        
        Returns
        -------
        Tuple[bool, Dict]
            (em_conformidade, detalhes_verificacao)
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Compare valor com SLA definido
        # 2. Considere tipo de limite (máximo, mínimo, percentil)
        # 3. Analise tendência no período
        # 4. Calcule margem até violação
        pass

class ValidadorContextoNegocio:
    """
    Validador que considera contexto de negócio.
    
    CONCEITO APLICADO: Validação = adequação ao propósito do negócio
    """
    
    def __init__(self):
        self.contextos_especiais = self._definir_contextos_especiais()
    
    def _definir_contextos_especiais(self) -> Dict:
        """Define contextos especiais do negócio."""
        return {
            "black_friday": {
                "periodo": "nov-25 a nov-27",
                "multiplicadores": {"throughput": 10, "latencia": 2}
            },
            "fork_bitcoin": {
                "indicadores": ["alta_volatilidade", "volume_extremo"],
                "tolerancias": {"latencia": 5, "taxa_erro": 0.5}
            },
            "manutencao_banco": {
                "horarios": ["02:00-04:00"],
                "sistemas_afetados": ["pagamentos", "saques"]
            }
        }
    
    def validar_contexto(self, metrica_nome: str, valor: float, 
                        timestamp: datetime) -> Tuple[bool, str]:
        """
        Valida se métrica é adequada considerando contexto de negócio.
        
        Returns
        -------
        Tuple[bool, str]
            (adequado_ao_contexto, justificativa)
        """
        # TODO: IMPLEMENTAR
        #
        # Considere:
        # - Horário da operação
        # - Eventos especiais em curso
        # - Sazonalidade do negócio
        # - Estado do mercado cripto
        #
        # VALIDAÇÃO ≠ VERIFICAÇÃO:
        # Uma métrica pode violar SLA técnico mas ser
        # adequada ao contexto de negócio atual
        pass

class SistemaMonitoramentoInteligente:
    """
    Sistema central que orquestra monitoramento inteligente.
    
    CONCEITO APLICADO: Integração de todos os conceitos fundamentais
    em um sistema de monitoramento proativo
    """
    
    def __init__(self):
        self.detector_anomalias = DetectorAnomalias()
        self.analisador_cadeia = AnalisadorCadeiaCanal()
        self.verificador_sla = VerificadorSLA()
        self.validador_contexto = ValidadorContextoNegocio()
        
        self.alertas_ativos: List[EventoMonitoramento] = []
        self.metricas_tempo_real: Dict[str, MetricaTempo] = {}
        self.dashboard_metricas: Dict[str, Any] = {}
    
    async def processar_metrica(self, nome: str, valor: float, 
                              contexto: Dict = None) -> Dict:
        """
        Processa métrica aplicando análise completa.
        
        Returns
        -------
        Dict
            Resultado completo da análise
        """
        timestamp = datetime.now()
        
        # TODO: IMPLEMENTAR
        #
        # 1. DETECÇÃO DE ANOMALIAS:
        #    - Use detector para identificar valores anômalos
        #
        # 2. VERIFICAÇÃO DE SLA:
        #    - Verifique conformidade técnica
        #
        # 3. VALIDAÇÃO DE CONTEXTO:
        #    - Valide adequação ao negócio
        #
        # 4. ANÁLISE DE CADEIA CAUSAL:
        #    - Correlacione com outros eventos
        #    - Identifique posição na cadeia causal
        #
        # 5. GERAÇÃO DE ALERTAS:
        #    - Crie alertas baseados em todos os fatores
        #
        # 6. ATUALIZAÇÃO DE DASHBOARD:
        #    - Atualize métricas tempo real
        pass
    
    async def analisar_saude_sistema(self) -> Dict:
        """
        Analisa saúde geral do sistema.
        
        CONCEITO APLICADO: Visão holística da qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # Calcule:
        # - Score geral de saúde (0-100)
        # - Sistemas em risco
        # - Tendências preocupantes
        # - Tempo estimado até próximo incidente
        # - Recomendações preventivas
        pass
    
    def calcular_metricas_qualidade(self) -> Dict:
        """
        Calcula métricas de qualidade do próprio sistema de monitoramento.
        
        CONCEITO APLICADO: Meta-qualidade - qualidade do sistema de qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # Metricas do sistema de monitoramento:
        # - Taxa de falsos positivos
        # - Taxa de falsos negativos  
        # - Tempo médio para detecção (MTTD)
        # - Tempo médio para resolução (MTTR)
        # - Cobertura de monitoramento
        # - Eficácia das predições
        pass
    
    def otimizar_thresholds(self) -> Dict:
        """
        Otimiza thresholds baseado em histórico de alertas.
        
        CONCEITO APLICADO: Melhoria contínua da qualidade
        """
        # TODO: IMPLEMENTAR
        #
        # Analise histórico para:
        # - Reduzir falsos positivos
        # - Melhorar sensibilidade para problemas reais
        # - Ajustar thresholds por contexto
        # - Balancear trade-off sensibilidade vs especificidade
        pass
    
    def gerar_relatorio_inteligencia(self) -> str:
        """
        Gera relatório de inteligência do sistema.
        """
        # TODO: IMPLEMENTAR
        pass

# CENÁRIOS DE TESTE FORNECIDOS
async def test_monitoramento_inteligente():
    """
    Testa sistema de monitoramento com cenários realistas da CryptoExchange.
    """
    sistema = SistemaMonitoramentoInteligente()
    
    print("₿ TESTE MONITORAMENTO INTELIGENTE - CryptoExchange")
    print("="*60)
    
    # Simula dados de treinamento
    print("🎯 Treinando baselines...")
    latencias_normais = np.random.normal(50, 10, 1000).tolist()  # 50ms ± 10ms
    sistema.detector_anomalias.treinar_baseline("latencia_api", latencias_normais)
    
    throughput_normal = np.random.normal(1500, 200, 1000).tolist()  # 1500 req/s ± 200
    sistema.detector_anomalias.treinar_baseline("throughput", throughput_normal)
    
    # Cenário 1: Operação normal
    print("\n✅ CENÁRIO 1: Operação Normal")
    resultado1 = await sistema.processar_metrica("latencia_api", 48.5, {"usuario": "trader_001"})
    print(f"Análise: {resultado1}")
    
    # Cenário 2: Anomalia detectada
    print("\n⚠️ CENÁRIO 2: Anomalia Detectada")
    resultado2 = await sistema.processar_metrica("latencia_api", 250.0, {"usuario": "trader_002"})
    print(f"Análise: {resultado2}")
    
    # Cenário 3: Simulação de cascata de falhas
    print("\n💥 CENÁRIO 3: Cascata de Falhas")
    # Simule sequência: latência alta → timeouts → falhas → incidentes
    eventos_cascata = [
        ("latencia_api", 180.0),
        ("timeout_database", 15.0),
        ("taxa_erro", 5.2),
        ("reclamacoes_usuarios", 50.0)
    ]
    
    for metrica, valor in eventos_cascata:
        await asyncio.sleep(0.1)  # Simula propagação temporal
        resultado = await sistema.processar_metrica(metrica, valor)
        print(f"{metrica}: {resultado.get('status', 'N/A')}")
    
    # Análise de saúde do sistema
    print("\n🏥 ANÁLISE DE SAÚDE DO SISTEMA")
    saude = await sistema.analisar_saude_sistema()
    print(f"Score de saúde: {saude}")
    
    # Métricas de qualidade do monitoramento
    print("\n📊 QUALIDADE DO MONITORAMENTO")
    qualidade_meta = sistema.calcular_metricas_qualidade()
    print(f"Métricas meta: {qualidade_meta}")
    
    # Otimização de thresholds
    print("\n🔧 OTIMIZAÇÃO DE THRESHOLDS")
    otimizacao = sistema.otimizar_thresholds()
    print(f"Recomendações: {otimizacao}")
    
    # Relatório final
    print("\n📋 RELATÓRIO DE INTELIGÊNCIA")
    relatorio = sistema.gerar_relatorio_inteligencia()
    print(relatorio)

if __name__ == "__main__":
    asyncio.run(test_monitoramento_inteligente())
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Sistema de detecção de anomalias sofisticado e preciso
- [ ] Análise completa da cadeia causal em tempo real
- [ ] Integração perfeita entre verificação SLA e validação de contexto
- [ ] Métricas avançadas de qualidade do próprio sistema
- [ ] Otimização automática baseada em aprendizado

#### ✓ Bom (75-89%)
- [ ] Boa detecção de anomalias com baixos falsos positivos
- [ ] Análise adequada da cadeia causal
- [ ] Integração competente dos conceitos
- [ ] Métricas de qualidade implementadas

#### ⚠️ Satisfatório (60-74%)
- [ ] Detecção básica de anomalias funcional
- [ ] Análise limitada da cadeia causal
- [ ] Conceitos implementados superficialmente

#### ❌ Insuficiente (<60%)
- [ ] Sistema de detecção inadequado ou incorreto
- [ ] Falha na análise da cadeia causal
- [ ] Não demonstra compreensão dos conceitos

### 💡 Dicas para Sucesso

1. **Baseline é fundamental** - sem ele, não há detecção confiável
2. **Contexto importa** - mesma métrica pode ter significados diferentes
3. **Correlação temporal** - eventos próximos podem estar relacionados
4. **Trade-off sensibilidade** - balance precisão vs recall
5. **Meta-monitoramento** - monitore a qualidade do monitoramento

---

## 🎯 Resumo do Nível 2

### Conceitos Integrados
- ✅ **Sistemas Distribuídos**: Aplicação dos conceitos em arquiteturas complexas
- ✅ **Design Patterns**: Como patterns suportam qualidade
- ✅ **Monitoramento Inteligente**: Detecção proativa de problemas
- ✅ **Trade-offs**: Balanceamento qualidade vs performance vs custo

### Habilidades Desenvolvidas
- 🔄 **Integração sistêmica** de múltiplos conceitos
- 🏗️ **Design arquitetural** orientado à qualidade
- 📊 **Análise quantitativa** de métricas complexas
- ⚖️ **Otimização** de trade-offs baseada em dados

### Preparação para Nível 3
No **Nível 3**, você enfrentará desafios arquiteturais complexos, tomará decisões estratégicas de alto nível e projetará sistemas que integrem tecnologias emergentes com os conceitos fundamentais estudados.

**Avance para o próximo nível!** 🚀
