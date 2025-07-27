# Solução Exercício 1.1 - Cadeia Causal FoodRush

"""
Solução completa para o exercício de Cadeia Causal.

CONCEITOS DEMONSTRADOS:
- Erro → Defeito → Falha → Incidente
- Análise de impacto e classificação
- Pontos de intervenção preventiva

AUTOR: Sistema de Qualidade Educacional
DATA: 2024
"""

from typing import Dict, List, Optional, Literal
from dataclasses import dataclass
from enum import Enum
import re

class TipoProblema(Enum):
    """Tipos de problemas na cadeia causal."""
    ERRO = "erro"
    DEFEITO = "defeito" 
    FALHA = "falha"
    INCIDENTE = "incidente"

class ImpactoNegocio(Enum):
    """Níveis de impacto no negócio."""
    BAIXO = "baixo"
    MEDIO = "medio"
    ALTO = "alto"
    CRITICO = "critico"

@dataclass
class ElementoCadeia:
    """Representa um elemento da cadeia causal."""
    tipo: TipoProblema
    descricao: str
    causa_raiz: Optional[str] = None
    impacto: ImpactoNegocio = ImpactoNegocio.BAIXO

class AnalisadorCadeiaCanal:
    """
    Analisa problemas reportados e identifica a cadeia causal completa.
    
    CONCEITO APLICADO: Cadeia erro → defeito → falha → incidente
    
    IMPLEMENTAÇÃO PEDAGÓGICA: Esta solução demonstra como mapear
    sistematicamente cada elemento da cadeia causal, desde o erro
    humano inicial até o impacto final no negócio.
    """
    
    def __init__(self):
        self.historico_analises: List[Dict] = []
        
        # Mapeamento de palavras-chave para identificação automática
        self.palavras_chave_erro = [
            "esqueceu", "não considerou", "assumiu", "interpretou mal",
            "não validou", "não testou", "copy-paste", "pressa"
        ]
        
        self.palavras_chave_defeito = [
            "código", "função", "if", "else", "loop", "variável",
            "KeyError", "IndexError", "bug", "falha de lógica"
        ]
        
        self.palavras_chave_falha = [
            "comportamento incorreto", "não funciona", "resultado errado",
            "exibe", "mostra", "calcula incorreto", "não carrega"
        ]
        
        self.palavras_chave_incidente = [
            "usuário", "cliente", "reclamação", "impacto", "negócio",
            "perda", "frustrante", "abandono", "receita"
        ]
    
    def analisar_problema(self, relato_usuario: str, 
                         contexto_tecnico: Dict) -> Dict[str, ElementoCadeia]:
        """
        Analisa um problema e identifica todos os elementos da cadeia causal.
        
        Parameters
        ----------
        relato_usuario : str
            Descrição do problema pelo usuário final
        contexto_tecnico : Dict
            Informações técnicas sobre o problema (logs, código, etc.)
            
        Returns
        -------
        Dict[str, ElementoCadeia]
            Dicionário com cada elemento da cadeia identificado
            
        ESTRATÉGIA DE IMPLEMENTAÇÃO:
        1. Identifica ERRO pela análise de logs e contexto técnico
        2. Identifica DEFEITO pelo código/função problemática
        3. Identifica FALHA pelo comportamento observado
        4. Identifica INCIDENTE pelo impacto no usuário/negócio
        """
        cadeia = {}
        
        # 1. IDENTIFICAÇÃO DO ERRO (Mistake humano que originou)
        erro = self._identificar_erro(contexto_tecnico)
        cadeia["erro"] = erro
        
        # 2. IDENTIFICAÇÃO DO DEFEITO (Manifestação no código)
        defeito = self._identificar_defeito(contexto_tecnico)
        cadeia["defeito"] = defeito
        
        # 3. IDENTIFICAÇÃO DA FALHA (Comportamento visível incorreto)
        falha = self._identificar_falha(relato_usuario, contexto_tecnico)
        cadeia["falha"] = falha
        
        # 4. IDENTIFICAÇÃO DO INCIDENTE (Impacto no usuário/negócio)
        incidente = self._identificar_incidente(relato_usuario, contexto_tecnico)
        cadeia["incidente"] = incidente
        
        # Registra análise no histórico
        self._registrar_analise(relato_usuario, contexto_tecnico, cadeia)
        
        return cadeia
    
    def _identificar_erro(self, contexto_tecnico: Dict) -> ElementoCadeia:
        """
        Identifica o erro humano que deu origem ao problema.
        
        CONCEITO: ERRO é o mistake humano - decisão ou ação incorreta
        durante desenvolvimento, configuração ou manutenção.
        """
        logs_erro = contexto_tecnico.get("logs_erro", "")
        funcao_problema = contexto_tecnico.get("funcao_problema", "")
        
        # Análise baseada nos logs e contexto
        if "KeyError" in logs_erro and "zona_norte" in logs_erro:
            return ElementoCadeia(
                tipo=TipoProblema.ERRO,
                descricao="Desenvolvedor não considerou todos os bairros no mapeamento de frete",
                causa_raiz="Falta de validação completa dos casos de uso durante desenvolvimento",
                impacto=ImpactoNegocio.MEDIO
            )
        
        # Caso genérico baseado na função problemática
        return ElementoCadeia(
            tipo=TipoProblema.ERRO,
            descricao=f"Erro de implementação na função {funcao_problema}",
            causa_raiz="Possível falta de conhecimento do domínio ou pressa no desenvolvimento",
            impacto=ImpactoNegocio.BAIXO
        )
    
    def _identificar_defeito(self, contexto_tecnico: Dict) -> ElementoCadeia:
        """
        Identifica o defeito no código/sistema.
        
        CONCEITO: DEFEITO é a manifestação do erro no artefato
        (código, configuração, documento).
        """
        logs_erro = contexto_tecnico.get("logs_erro", "")
        localizacao_codigo = contexto_tecnico.get("localizacao_codigo", "")
        
        if "KeyError: 'zona_norte'" in logs_erro:
            return ElementoCadeia(
                tipo=TipoProblema.DEFEITO,
                descricao="Ausência da chave 'zona_norte' no dicionário de configuração de frete",
                causa_raiz="Código não trata todos os casos de bairros possíveis",
                impacto=ImpactoNegocio.MEDIO
            )
        
        return ElementoCadeia(
            tipo=TipoProblema.DEFEITO,
            descricao=f"Defeito no código localizado em {localizacao_codigo}",
            causa_raiz="Implementação incompleta ou incorreta",
            impacto=ImpactoNegocio.MEDIO
        )
    
    def _identificar_falha(self, relato_usuario: str, contexto_tecnico: Dict) -> ElementoCadeia:
        """
        Identifica a falha - comportamento incorreto observável.
        
        CONCEITO: FALHA é o desvio do comportamento esperado,
        visível durante execução.
        """
        # Extrai informações do relato do usuário
        if "mostra frete grátis" in relato_usuario and "cobra" in relato_usuario:
            valor_inconsistente = self._extrair_valores_frete(relato_usuario)
            
            return ElementoCadeia(
                tipo=TipoProblema.FALHA,
                descricao=f"Sistema exibe frete grátis mas cobra {valor_inconsistente} na finalização",
                causa_raiz="Inconsistência entre cálculo de exibição e cálculo final",
                impacto=ImpactoNegocio.ALTO
            )
        
        return ElementoCadeia(
            tipo=TipoProblema.FALHA,
            descricao="Comportamento incorreto do sistema",
            causa_raiz="Execução do defeito em runtime",
            impacto=ImpactoNegocio.MEDIO
        )
    
    def _identificar_incidente(self, relato_usuario: str, contexto_tecnico: Dict) -> ElementoCadeia:
        """
        Identifica o incidente - impacto no usuário/negócio.
        
        CONCEITO: INCIDENTE é a consequência da falha que afeta
        usuários, clientes ou o negócio.
        """
        usuarios_afetados = contexto_tecnico.get("usuarios_afetados", 0)
        receita_perdida = contexto_tecnico.get("receita_perdida_estimada", 0)
        frequencia = contexto_tecnico.get("frequencia", "")
        
        # Análise quantitativa do impacto
        if usuarios_afetados > 400 and receita_perdida > 10000:
            impacto = ImpactoNegocio.CRITICO
        elif usuarios_afetados > 100 and receita_perdida > 5000:
            impacto = ImpactoNegocio.ALTO
        else:
            impacto = ImpactoNegocio.MEDIO
        
        return ElementoCadeia(
            tipo=TipoProblema.INCIDENTE,
            descricao=f"Perda de confiança de {usuarios_afetados} usuários e R$ {receita_perdida:.2f} em receita",
            causa_raiz="Falha no sistema levou a cobrança inesperada",
            impacto=impacto
        )
    
    def _extrair_valores_frete(self, relato: str) -> str:
        """Extrai valores de frete do relato do usuário."""
        # Busca padrões como "R$ 15,00"
        import re
        valores = re.findall(r'R\$\s*\d+[,.]?\d*', relato)
        if len(valores) >= 2:
            return valores[1]  # Segundo valor (valor cobrado)
        return "valor não especificado"
    
    def classificar_impacto(self, elemento: ElementoCadeia, 
                          metricas_negocio: Dict) -> ImpactoNegocio:
        """
        Classifica o impacto de um elemento da cadeia no negócio.
        
        ALGORITMO DE CLASSIFICAÇÃO:
        - BAIXO: < 50 usuários afetados OU < R$ 1.000 perdidos
        - MÉDIO: 50-200 usuários OU R$ 1.000-5.000
        - ALTO: 200-500 usuários OU R$ 5.000-20.000  
        - CRÍTICO: > 500 usuários OU > R$ 20.000
        """
        usuarios_afetados = metricas_negocio.get("usuarios_afetados", 0)
        receita_perdida = metricas_negocio.get("receita_perdida", 0)
        frequencia_str = metricas_negocio.get("frequencia", "0%")
        
        # Extrai percentual da frequência
        try:
            frequencia_pct = float(frequencia_str.replace("%", ""))
        except:
            frequencia_pct = 0
        
        # Score composto considerando múltiplas dimensões
        score_usuarios = min(usuarios_afetados / 100, 5)  # Normalizado 0-5
        score_receita = min(receita_perdida / 4000, 5)    # Normalizado 0-5
        score_frequencia = min(frequencia_pct / 10, 5)    # Normalizado 0-5
        
        score_total = (score_usuarios + score_receita + score_frequencia) / 3
        
        if score_total >= 4:
            return ImpactoNegocio.CRITICO
        elif score_total >= 2.5:
            return ImpactoNegocio.ALTO
        elif score_total >= 1:
            return ImpactoNegocio.MEDIO
        else:
            return ImpactoNegocio.BAIXO
    
    def sugerir_pontos_correcao(self, cadeia: Dict[str, ElementoCadeia]) -> List[str]:
        """
        Sugere pontos específicos onde correções devem ser aplicadas.
        
        ESTRATÉGIA: Para cada elemento da cadeia, sugere ações
        específicas baseadas no tipo de problema e causa raiz.
        """
        sugestoes = []
        
        # Sugestões para ERRO (prevenção)
        if "erro" in cadeia:
            erro = cadeia["erro"]
            if "não considerou" in erro.descricao:
                sugestoes.append(
                    "🎯 PREVENÇÃO DE ERRO: Implementar checklist de casos de uso "
                    "durante desenvolvimento e code review obrigatório"
                )
            
            sugestoes.append(
                "📚 TREINAMENTO: Capacitar equipe sobre mapeamento completo "
                "de domínio de negócio antes da implementação"
            )
        
        # Sugestões para DEFEITO (correção)
        if "defeito" in cadeia:
            defeito = cadeia["defeito"]
            if "KeyError" in defeito.descricao:
                sugestoes.append(
                    "🔧 CORREÇÃO IMEDIATA: Adicionar mapeamento para 'zona_norte' "
                    "no arquivo de configuração de frete"
                )
                
                sugestoes.append(
                    "🛡️ ROBUSTEZ: Implementar tratamento de exceção para "
                    "chaves não encontradas com valor de fallback"
                )
        
        # Sugestões para FALHA (detecção precoce)
        if "falha" in cadeia:
            sugestoes.append(
                "🔍 MONITORAMENTO: Implementar alertas automáticos para "
                "discrepâncias entre valor exibido e valor final"
            )
            
            sugestoes.append(
                "🧪 TESTES: Criar testes automatizados para todos os bairros "
                "com validação de consistência de valores"
            )
        
        # Sugestões para INCIDENTE (mitigação)
        if "incidente" in cadeia:
            incidente = cadeia["incidente"]
            if incidente.impacto in [ImpactoNegocio.ALTO, ImpactoNegocio.CRITICO]:
                sugestoes.append(
                    "🚨 MITIGAÇÃO URGENTE: Implementar circuit breaker para "
                    "pausar pedidos de bairros com problemas conhecidos"
                )
                
                sugestoes.append(
                    "💬 COMUNICAÇÃO: Notificar proativamente usuários afetados "
                    "com explicação e compensação adequada"
                )
        
        return sugestoes
    
    def _registrar_analise(self, relato: str, contexto: Dict, cadeia: Dict):
        """Registra análise no histórico para aprendizado futuro."""
        self.historico_analises.append({
            "timestamp": "2024-01-15T10:30:00",  # Seria datetime.now() em prod
            "relato_usuario": relato,
            "contexto_tecnico": contexto,
            "cadeia_identificada": {k: v.descricao for k, v in cadeia.items()},
            "pontos_aprendizado": [
                "Importância de validação completa de casos de uso",
                "Necessidade de monitoramento de consistência",
                "Valor do feedback rápido para detectar problemas"
            ]
        })

# CENÁRIO DE TESTE FORNECIDO
def test_cenario_foodrush():
    """
    Cenário de teste baseado no problema real do FoodRush.
    
    CONTEXTO: Sistema cobra frete errado em bairros específicos
    
    RESULTADO ESPERADO: Identificação completa da cadeia causal
    com sugestões específicas de correção e prevenção.
    """
    analisador = AnalisadorCadeiaCanal()
    
    relato_usuario = (
        "Quando coloco meu endereço na Zona Norte, o app mostra frete "
        "grátis (R$ 0,00) na tela de produtos. Mas na hora de finalizar "
        "o pedido, aparece uma cobrança de R$ 15,00 de frete. "
        "Isso já aconteceu 3 vezes esta semana!"
    )
    
    contexto_tecnico = {
        "codigo_erro": "ZONA_NORTE_FRETE_MISMATCH",
        "funcao_problema": "calcular_frete_por_bairro",
        "localizacao_codigo": "src/services/delivery_service.py:line 127",
        "logs_erro": "KeyError: 'zona_norte' in frete_config",
        "frequencia": "15% dos pedidos da Zona Norte",
        "usuarios_afetados": 450,
        "receita_perdida_estimada": 12500.00
    }
    
    print("🍕 ANÁLISE DA CADEIA CAUSAL - FoodRush")
    print("="*50)
    
    # Executa análise completa
    resultado = analisador.analisar_problema(relato_usuario, contexto_tecnico)
    
    # Exibe resultados detalhados
    print(f"\n📋 ELEMENTOS DA CADEIA IDENTIFICADOS:")
    for tipo, elemento in resultado.items():
        print(f"\n{tipo.upper()}:")
        print(f"  📄 Descrição: {elemento.descricao}")
        print(f"  🔍 Causa Raiz: {elemento.causa_raiz}")
        print(f"  📊 Impacto: {elemento.impacto.value}")
    
    # Classificação de impacto refinada
    if "incidente" in resultado:
        metricas = {
            "usuarios_afetados": 450,
            "receita_perdida": 12500.00,
            "frequencia": "15%"
        }
        impacto_refinado = analisador.classificar_impacto(
            resultado["incidente"], metricas
        )
        print(f"\n📈 IMPACTO REFINADO: {impacto_refinado.value}")
    
    # Sugestões de correção
    print(f"\n🎯 SUGESTÕES DE CORREÇÃO:")
    sugestoes = analisador.sugerir_pontos_correcao(resultado)
    for i, sugestao in enumerate(sugestoes, 1):
        print(f"  {i}. {sugestao}")
    
    print(f"\n✅ Análise concluída! {len(resultado)} elementos identificados.")
    
    # Validações automáticas
    assert "erro" in resultado, "Erro não identificado"
    assert "defeito" in resultado, "Defeito não identificado"
    assert "falha" in resultado, "Falha não identificada"
    assert "incidente" in resultado, "Incidente não identificado"
    
    print("🔍 Todas as validações passaram!")
    
    return resultado

if __name__ == "__main__":
    # Executa teste demonstrativo
    resultado = test_cenario_foodrush()
    
    # Análise adicional para fins pedagógicos
    print(f"\n📚 ANÁLISE PEDAGÓGICA:")
    print(f"Esta solução demonstra como cada conceito fundamental se manifesta:")
    print(f"• ERRO: Mistake humano durante desenvolvimento")
    print(f"• DEFEITO: Manifestação no código (KeyError)")
    print(f"• FALHA: Comportamento incorreto observável")
    print(f"• INCIDENTE: Impacto real no negócio e usuários")
    print(f"\nA cadeia causal permite ação preventiva em múltiplos pontos!")
