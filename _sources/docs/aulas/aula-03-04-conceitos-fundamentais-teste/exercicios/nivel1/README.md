# Exercícios Nível 1 - Básico 🔵

**Tempo Estimado**: 15-30 minutos por exercício  
**Objetivo**: Aplicação direta de conceitos fundamentais individuais  
**Complexidade**: Uma única funcionalidade por exercício

## 📋 Visão Geral dos Exercícios

1. **Exercício 1.1**: Identificação e Classificação da Cadeia Causal
2. **Exercício 1.2**: Implementação de Verificação vs Validação
3. **Exercício 1.3**: Análise de Cenários de Teste Básicos

---

## 🎯 Exercício 1.1 - Cadeia Causal: Erro → Defeito → Falha → Incidente

### Contexto
Você foi contratado como analista de qualidade júnior em uma startup de delivery de comida chamada **FoodRush**. Seu primeiro trabalho é analisar problemas reportados pelos usuários e classificá-los corretamente usando a cadeia causal estudada na aula.

### Cenário Realista
O FoodRush tem recebido reclamações sobre o sistema de cálculo de frete. Alguns usuários relatam que:
- O valor do frete aparece como "R$ 0,00" na tela
- Mas na finalização, é cobrado R$ 15,00
- Isso acontece especificamente em bairros da "Zona Norte"

### 📝 Sua Tarefa

**Implementar** uma classe `AnalisadorCadeiaCanal` que:

1. **Identifique** cada elo da cadeia causal em um problema reportado
2. **Classifique** adequadamente: erro, defeito, falha, incidente
3. **Determine** o impacto no negócio
4. **Sugira** pontos de correção

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_1_1.py

from typing import Dict, List, Optional, Literal
from dataclasses import dataclass
from enum import Enum

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
    """
    
    def __init__(self):
        self.historico_analises: List[Dict] = []
    
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
            
        Example
        -------
        >>> analisador = AnalisadorCadeiaCanal()
        >>> relato = "Frete aparece R$ 0,00 mas cobra R$ 15,00"
        >>> contexto = {"codigo_erro": "ZONA_NORTE_BUG", "funcao": "calcular_frete"}
        >>> resultado = analisador.analisar_problema(relato, contexto)
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Identifique o ERRO (mistake humano que originou)
        # 2. Identifique o DEFEITO (manifestação no código)  
        # 3. Identifique a FALHA (comportamento visível incorreto)
        # 4. Identifique o INCIDENTE (impacto no usuário/negócio)
        #
        # DICA: Use o contexto_tecnico para deduzir informações técnicas
        # DICA: Use o relato_usuario para entender o impacto
        pass
    
    def classificar_impacto(self, elemento: ElementoCadeia, 
                          metricas_negocio: Dict) -> ImpactoNegocio:
        """
        Classifica o impacto de um elemento da cadeia no negócio.
        
        Parameters
        ----------
        elemento : ElementoCadeia
            Elemento da cadeia a ser classificado
        metricas_negocio : Dict
            Métricas relevantes (usuários afetados, receita perdida, etc.)
            
        Returns
        -------
        ImpactoNegocio
            Classificação do impacto
        """
        # TODO: IMPLEMENTAR
        #
        # Considere:
        # - Número de usuários afetados
        # - Receita potencialmente perdida
        # - Frequência do problema
        # - Tempo para resolução
        pass
    
    def sugerir_pontos_correcao(self, cadeia: Dict[str, ElementoCadeia]) -> List[str]:
        """
        Sugere pontos específicos onde correções devem ser aplicadas.
        
        Parameters
        ----------
        cadeia : Dict[str, ElementoCadeia]
            Cadeia causal completa identificada
            
        Returns
        -------
        List[str]
            Lista de sugestões de correção priorizadas
        """
        # TODO: IMPLEMENTAR
        #
        # Para cada elemento da cadeia, sugira:
        # - ERRO: Como prevenir (treinamento, processo, code review)
        # - DEFEITO: Como corrigir (patch, refactoring)
        # - FALHA: Como detectar mais cedo (testes, monitoramento)
        # - INCIDENTE: Como mitigar impacto (circuit breaker, fallback)
        pass

# CENÁRIO DE TESTE FORNECIDO
def test_cenario_foodrush():
    """
    Cenário de teste baseado no problema real do FoodRush.
    
    CONTEXTO: Sistema cobra frete errado em bairros específicos
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
    
    # Teste sua implementação
    resultado = analisador.analisar_problema(relato_usuario, contexto_tecnico)
    
    # Verificações esperadas (descomente após implementar)
    # assert "erro" in resultado
    # assert "defeito" in resultado  
    # assert "falha" in resultado
    # assert "incidente" in resultado
    
    print("✅ Análise concluída!")
    print("Elementos identificados:", list(resultado.keys()))
    
    # Teste classificação de impacto
    if "incidente" in resultado:
        impacto = analisador.classificar_impacto(
            resultado["incidente"], 
            {"usuarios_afetados": 450, "receita_perdida": 12500.00}
        )
        print(f"Impacto classificado como: {impacto.value}")
    
    # Teste sugestões
    sugestoes = analisador.sugerir_pontos_correcao(resultado)
    print("Sugestões de correção:")
    for i, sugestao in enumerate(sugestoes, 1):
        print(f"  {i}. {sugestao}")

if __name__ == "__main__":
    test_cenario_foodrush()
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Identifica corretamente todos os 4 elementos da cadeia
- [ ] Classificação de impacto precisa e bem justificada
- [ ] Sugestões de correção específicas e viáveis
- [ ] Código bem documentado com comentários pedagógicos

#### ✓ Bom (75-89%)
- [ ] Identifica pelo menos 3 elementos da cadeia corretamente
- [ ] Boa classificação de impacto
- [ ] Sugestões gerais mas relevantes
- [ ] Código funcional com documentação adequada

#### ⚠️ Satisfatório (60-74%)
- [ ] Identifica 2 elementos da cadeia
- [ ] Classificação básica de impacto
- [ ] Algumas sugestões relevantes
- [ ] Código funciona mas falta documentação

#### ❌ Insuficiente (<60%)
- [ ] Não demonstra compreensão da cadeia causal
- [ ] Classificação incorreta de elementos
- [ ] Sugestões irrelevantes ou genéricas

### 💡 Dicas para Sucesso

1. **Comece pela definição**: Releia as definições de erro, defeito, falha e incidente
2. **Use o contexto**: As informações técnicas contêm pistas importantes
3. **Pense como investigador**: Cada elemento causa o próximo na cadeia
4. **Seja específico**: Evite descrições genéricas, use o contexto do FoodRush

### 🔍 Perguntas para Reflexão

Após implementar, reflita sobre:

1. **Por que** é importante distinguir entre erro e defeito?
2. **Como** essa análise poderia prevenir problemas similares?
3. **Qual** elemento da cadeia é mais fácil de corrigir? Por quê?
4. **Onde** você investiria recursos para máximo impacto preventivo?

---

## 🎯 Exercício 1.2 - Verificação vs Validação: Sistema de Login

### Contexto
Você está trabalhando no desenvolvimento de um sistema de autenticação para um **Internet Banking**. O sistema precisa ser extremamente rigoroso, mas também user-friendly. Sua tarefa é implementar tanto a **verificação** (conformidade técnica) quanto a **validação** (adequação ao propósito).

### Cenário Realista
O banco **TechBank** tem regras específicas para senhas:
- **Verificação**: Cumpre regras técnicas (8+ chars, maiúscula, número, símbolo)
- **Validação**: Realmente protege a conta no contexto do usuário específico

### 📝 Sua Tarefa

Implementar um **Sistema de Autenticação Dupla** que demonstre claramente a diferença entre verificação e validação.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_1_2.py

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import re
import hashlib

@dataclass
class ResultadoVerificacao:
    """Resultado da verificação técnica."""
    aprovado: bool
    regras_cumpridas: List[str]
    regras_violadas: List[str]
    pontuacao_tecnica: float  # 0.0 a 1.0

@dataclass
class ResultadoValidacao:
    """Resultado da validação contextual."""
    adequado: bool
    fatores_positivos: List[str]
    fatores_negativos: List[str]
    nivel_protecao: str  # "baixo", "medio", "alto"

@dataclass
class PerfilUsuario:
    """Perfil do usuário para validação contextual."""
    id_usuario: str
    historico_senhas: List[str]  # hashes das últimas senhas
    tentativas_login_falharam: int
    data_ultimo_acesso: datetime
    tipo_conta: str  # "comum", "premium", "empresarial"
    valor_conta: float

class VerificadorTecnico:
    """
    Realiza verificação técnica de senhas (Building the product right).
    
    CONCEITO: Verificação = Conformidade com especificações técnicas
    """
    
    def __init__(self):
        self.regras_tecnicas = {
            "comprimento_minimo": 8,
            "comprimento_maximo": 128,
            "requer_maiuscula": True,
            "requer_minuscula": True,
            "requer_numero": True,
            "requer_simbolo": True,
            "proibe_sequencias": True,  # 123, abc, qwerty
            "proibe_repeticoes": True   # aaa, 111
        }
    
    def verificar_senha(self, senha: str) -> ResultadoVerificacao:
        """
        Verifica se senha cumpre todas as regras técnicas.
        
        Parameters
        ----------
        senha : str
            Senha a ser verificada
            
        Returns
        -------
        ResultadoVerificacao
            Resultado detalhado da verificação técnica
        """
        # TODO: IMPLEMENTAR
        #
        # Para cada regra em self.regras_tecnicas:
        # 1. Teste se a senha cumpre a regra
        # 2. Registre em regras_cumpridas ou regras_violadas
        # 3. Calcule pontuacao_tecnica (% de regras cumpridas)
        # 4. aprovado = True se TODAS as regras foram cumpridas
        #
        # DICA: Use regex para validações complexas
        # DICA: Teste sequências comuns como "123", "abc", "qwerty"
        pass
    
    def _verificar_comprimento(self, senha: str) -> bool:
        """Verifica se comprimento está dentro dos limites."""
        # TODO: Implementar
        pass
    
    def _verificar_caracteres_obrigatorios(self, senha: str) -> Dict[str, bool]:
        """Verifica presença de tipos de caracteres obrigatórios."""
        # TODO: Implementar
        # Retorne dict com chaves: maiuscula, minuscula, numero, simbolo
        pass
    
    def _verificar_sequencias_proibidas(self, senha: str) -> bool:
        """Verifica se contém sequências proibidas."""
        # TODO: Implementar
        # Teste: 123, 456, abc, qwerty, asdf, etc.
        pass

class ValidadorContextual:
    """
    Realiza validação contextual de senhas (Building the right product).
    
    CONCEITO: Validação = Adequação ao propósito real de segurança
    """
    
    def __init__(self):
        self.senhas_comuns = self._carregar_senhas_comuns()
        self.padroes_pessoais = [
            "data_nascimento", "nome_completo", "cpf", 
            "telefone", "endereco", "nome_pet"
        ]
    
    def validar_senha(self, senha: str, 
                     perfil: PerfilUsuario) -> ResultadoValidacao:
        """
        Valida se senha é adequada ao contexto do usuário específico.
        
        Parameters
        ----------
        senha : str
            Senha a ser validada
        perfil : PerfilUsuario
            Contexto específico do usuário
            
        Returns
        -------
        ResultadoValidacao
            Resultado da validação contextual
        """
        # TODO: IMPLEMENTAR
        #
        # Considere:
        # 1. Senha está na lista de senhas comuns?
        # 2. Senha é similar às anteriores do usuário?
        # 3. Senha contém informações pessoais do usuário?
        # 4. Força da senha é adequada ao valor da conta?
        # 5. Histórico de tentativas indica possível comprometimento?
        #
        # VALIDAÇÃO ≠ VERIFICAÇÃO:
        # - Uma senha pode passar na verificação técnica mas
        #   ser inadequada para o contexto específico do usuário
        pass
    
    def _senha_eh_comum(self, senha: str) -> bool:
        """Verifica se senha está na lista de senhas comuns."""
        # TODO: Implementar
        pass
    
    def _senha_similar_historico(self, senha: str, 
                               historico: List[str]) -> bool:
        """Verifica similaridade com senhas anteriores."""
        # TODO: Implementar
        # DICA: Use conceito de distância de edição ou hash similarity
        pass
    
    def _detectar_informacoes_pessoais(self, senha: str, 
                                     perfil: PerfilUsuario) -> List[str]:
        """Detecta informações pessoais na senha."""
        # TODO: Implementar
        # Simule verificação de data nascimento, nome, etc.
        pass
    
    def _calcular_forca_necessaria(self, perfil: PerfilUsuario) -> str:
        """Calcula força necessária baseada no perfil."""
        # TODO: Implementar
        # Conta empresarial ou alto valor = força maior
        pass
    
    def _carregar_senhas_comuns(self) -> List[str]:
        """Carrega lista de senhas mais comuns."""
        # Lista simplificada das senhas mais usadas
        return [
            "123456", "password", "123456789", "12345678", "12345",
            "qwerty", "abc123", "111111", "123123", "admin",
            "senha123", "123mudar", "senha", "1234567890"
        ]

class SistemaAutenticacaoDupla:
    """
    Sistema que combina verificação E validação para autenticação robusta.
    
    CONCEITO APLICADO: Verificação ∩ Validação = Segurança Real
    """
    
    def __init__(self):
        self.verificador = VerificadorTecnico()
        self.validador = ValidadorContextual()
    
    def avaliar_senha_completa(self, senha: str, 
                             perfil: PerfilUsuario) -> Dict:
        """
        Avalia senha usando tanto verificação quanto validação.
        
        Returns
        -------
        Dict
            Resultado completo com ambas as análises
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Execute verificação técnica
        # 2. Execute validação contextual  
        # 3. Determine aprovação final:
        #    - DEVE passar em ambas para ser aprovada
        #    - Forneça feedback específico sobre cada dimensão
        # 4. Calcule score de segurança final
        pass
    
    def gerar_relatorio_decisao(self, resultado_completo: Dict) -> str:
        """
        Gera relatório explicando a decisão de aceitar/rejeitar senha.
        
        OBJETIVO: Demonstrar claramente a diferença entre
        verificação e validação na tomada de decisão.
        """
        # TODO: IMPLEMENTAR
        #
        # O relatório deve explicar:
        # - Por que passou/falhou na verificação
        # - Por que passou/falhou na validação  
        # - Como isso impacta a decisão final
        # - Sugestões para melhoria
        pass

# CENÁRIOS DE TESTE FORNECIDOS
def test_verificacao_vs_validacao():
    """
    Testa cenários que demonstram a diferença entre verificação e validação.
    """
    sistema = SistemaAutenticacaoDupla()
    
    # Perfil de usuário exemplo
    perfil_joao = PerfilUsuario(
        id_usuario="joao123",
        historico_senhas=["$2b$hash_senha_anterior_1", "$2b$hash_senha_anterior_2"],
        tentativas_login_falharam=0,
        data_ultimo_acesso=datetime.now() - timedelta(days=1),
        tipo_conta="premium",
        valor_conta=150000.00
    )
    
    # CENÁRIO 1: Passa na verificação, falha na validação
    senha_tecnica = "TechB@nk123"  # Cumpre regras técnicas
    print("🔍 CENÁRIO 1: Senha tecnicamente correta")
    resultado1 = sistema.avaliar_senha_completa(senha_tecnica, perfil_joao)
    print(sistema.gerar_relatorio_decisao(resultado1))
    
    # CENÁRIO 2: Falha na verificação, validação não importa
    senha_fraca = "123456"  # Não cumpre regras técnicas
    print("\n🔍 CENÁRIO 2: Senha tecnicamente incorreta")
    resultado2 = sistema.avaliar_senha_completa(senha_fraca, perfil_joao)
    print(sistema.gerar_relatorio_decisao(resultado2))
    
    # CENÁRIO 3: Passa em ambas (senha ideal)
    senha_forte = "Meu&Gato$Mimi@2024!"  # Técnica + contextualmente adequada
    print("\n🔍 CENÁRIO 3: Senha ideal")
    resultado3 = sistema.avaliar_senha_completa(senha_forte, perfil_joao)
    print(sistema.gerar_relatorio_decisao(resultado3))

if __name__ == "__main__":
    test_verificacao_vs_validacao()
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Implementa verificação técnica rigorosa e completa
- [ ] Validação contextual considera múltiplos fatores do usuário
- [ ] Demonstra claramente quando verificação ≠ validação
- [ ] Relatório de decisão é didático e explicativo

#### ✓ Bom (75-89%)
- [ ] Boa implementação de verificação técnica
- [ ] Validação considera alguns fatores contextuais
- [ ] Mostra diferença básica entre verificação e validação
- [ ] Feedback adequado sobre decisões

#### ⚠️ Satisfatório (60-74%)
- [ ] Verificação básica implementada
- [ ] Validação simplificada mas funcional
- [ ] Entende conceitos mas implementação limitada

#### ❌ Insuficiente (<60%)
- [ ] Não distingue verificação de validação
- [ ] Implementação incorreta ou incompleta
- [ ] Não demonstra compreensão dos conceitos

### 💡 Dicas para Sucesso

1. **Verificação é binária**: Regra foi cumprida ou não
2. **Validação é contextual**: Depende da situação específica
3. **Ambas são necessárias**: Uma sem a outra é insuficiente
4. **Documente diferenças**: Comente por que cada verificação existe

---

## 🎯 Exercício 1.3 - Análise de Cenários SWEBOK

### Contexto
Como especialista em qualidade, você precisa **classificar diferentes atividades de teste** de acordo com a taxonomia do SWEBOK. Você trabalhará com cenários reais de uma empresa de software que desenvolve um sistema de **gestão hospitalar**.

### Cenário Realista
O **Hospital TechCare** está implementando um novo sistema e você precisa categorizar as atividades de teste seguindo as diretrizes do SWEBOK para garantir cobertura completa.

### 📝 Sua Tarefa

Implementar um **Classificador de Atividades de Teste** que organize atividades segundo a taxonomia SWEBOK.

### 🛠️ Implementação Requerida

```python
# Crie o arquivo: exercicio_1_3.py

from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from enum import Enum

class TipoTesteSWEBOK(Enum):
    """Tipos de teste segundo SWEBOK."""
    # Por objetivo
    ACEITACAO = "aceitacao"
    INSTALACAO = "instalacao"
    ALFA = "alfa"
    BETA = "beta"
    
    # Por nível
    UNITARIO = "unitario"
    INTEGRACAO = "integracao"
    SISTEMA = "sistema"
    
    # Por característica
    FUNCIONAL = "funcional"
    ESTRUTURAL = "estrutural"
    
    # Por propósito
    REGRESSAO = "regressao"
    PERFORMANCE = "performance"
    STRESS = "stress"
    VOLUME = "volume"
    USABILIDADE = "usabilidade"
    SEGURANCA = "seguranca"

@dataclass
class AtividadeTeste:
    """Representa uma atividade de teste a ser classificada."""
    id: str
    descricao: str
    contexto: str
    stakeholder: str
    ambiente: str
    criterio_sucesso: str

@dataclass
class ClassificacaoSWEBOK:
    """Classificação de uma atividade segundo SWEBOK."""
    atividade_id: str
    tipos_principais: List[TipoTesteSWEBOK]
    tipos_secundarios: List[TipoTesteSWEBOK]
    justificativa: str
    area_swebok: str
    nivel_confianca: float  # 0.0 a 1.0

class ClassificadorSWEBOK:
    """
    Classifica atividades de teste segundo a taxonomia SWEBOK.
    
    CONCEITO APLICADO: Organização sistemática do conhecimento de teste
    segundo padrões internacionais (SWEBOK).
    """
    
    def __init__(self):
        self.mapeamento_contexto = self._construir_mapeamento_contexto()
        self.regras_classificacao = self._construir_regras_classificacao()
    
    def classificar_atividade(self, atividade: AtividadeTeste) -> ClassificacaoSWEBOK:
        """
        Classifica uma atividade de teste segundo SWEBOK.
        
        Parameters
        ----------
        atividade : AtividadeTeste
            Atividade a ser classificada
            
        Returns
        -------
        ClassificacaoSWEBOK
            Classificação completa da atividade
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Analise a descrição da atividade
        # 2. Identifique palavras-chave que indicam tipo de teste
        # 3. Considere o contexto (quem faz, onde, quando)
        # 4. Aplique regras de classificação do SWEBOK
        # 5. Determine tipos principais e secundários
        # 6. Calcule nível de confiança na classificação
        #
        # DICA: Uma atividade pode ter múltiplos tipos (ex: teste de 
        #       integração + performance + regressão)
        pass
    
    def validar_completude_swebok(self, atividades: List[AtividadeTeste]) -> Dict:
        """
        Valida se conjunto de atividades cobre adequadamente SWEBOK.
        
        Returns
        -------
        Dict
            Análise de cobertura das categorias SWEBOK
        """
        # TODO: IMPLEMENTAR
        #
        # 1. Classifique todas as atividades
        # 2. Identifique lacunas na cobertura SWEBOK
        # 3. Calcule percentual de cobertura por categoria
        # 4. Sugira atividades faltantes
        pass
    
    def gerar_relatorio_conformidade(self, atividades: List[AtividadeTeste]) -> str:
        """
        Gera relatório de conformidade com SWEBOK.
        """
        # TODO: IMPLEMENTAR
        pass
    
    def _construir_mapeamento_contexto(self) -> Dict:
        """Constrói mapeamento entre contexto e tipos de teste."""
        return {
            "palavras_chave": {
                TipoTesteSWEBOK.UNITARIO: [
                    "função", "método", "classe", "componente isolado",
                    "mock", "stub", "unit test"
                ],
                TipoTesteSWEBOK.INTEGRACAO: [
                    "integração", "interface", "comunicação entre",
                    "API", "banco de dados", "serviço externo"
                ],
                TipoTesteSWEBOK.SISTEMA: [
                    "sistema completo", "end-to-end", "fluxo completo",
                    "cenário completo", "requisito funcional"
                ],
                TipoTesteSWEBOK.ACEITACAO: [
                    "usuário final", "cliente", "aceitação", "homologação",
                    "validação de negócio", "critério de aceite"
                ],
                TipoTesteSWEBOK.PERFORMANCE: [
                    "performance", "tempo de resposta", "throughput",
                    "latência", "velocidade", "carga"
                ],
                TipoTesteSWEBOK.SEGURANCA: [
                    "segurança", "autenticação", "autorização", "criptografia",
                    "vulnerabilidade", "invasão", "SQL injection"
                ],
                TipoTesteSWEBOK.USABILIDADE: [
                    "usabilidade", "interface usuário", "UX", "facilidade uso",
                    "navegação", "acessibilidade"
                ]
            },
            "stakeholders": {
                "desenvolvedor": [TipoTesteSWEBOK.UNITARIO, TipoTesteSWEBOK.INTEGRACAO],
                "tester": [TipoTesteSWEBOK.SISTEMA, TipoTesteSWEBOK.FUNCIONAL],
                "usuario_final": [TipoTesteSWEBOK.ACEITACAO, TipoTesteSWEBOK.USABILIDADE],
                "cliente": [TipoTesteSWEBOK.ACEITACAO, TipoTesteSWEBOK.BETA],
                "ops": [TipoTesteSWEBOK.INSTALACAO, TipoTesteSWEBOK.PERFORMANCE]
            }
        }
    
    def _construir_regras_classificacao(self) -> Dict:
        """Constrói regras de classificação baseadas em SWEBOK."""
        # TODO: IMPLEMENTAR
        # Defina regras que combinam contexto, stakeholder, ambiente
        # para determinar classificação final
        pass

# CENÁRIOS DE TESTE FORNECIDOS
def test_cenarios_hospital():
    """
    Testa classificação com cenários reais do Hospital TechCare.
    """
    classificador = ClassificadorSWEBOK()
    
    # Cenários reais de um sistema hospitalar
    atividades = [
        AtividadeTeste(
            id="HT001",
            descricao="Testar se a função calcular_dosagem_medicamento() "
                     "retorna dosagem correta para peso e idade do paciente",
            contexto="Desenvolvimento de módulo de prescrição médica",
            stakeholder="desenvolvedor",
            ambiente="IDE local com dados mock",
            criterio_sucesso="100% dos cálculos corretos para casos conhecidos"
        ),
        
        AtividadeTeste(
            id="HT002", 
            descricao="Validar fluxo completo: médico prescreve → farmácia "
                     "recebe → paciente retira medicamento",
            contexto="Integração entre sistemas médico e farmácia",
            stakeholder="tester",
            ambiente="Ambiente de teste com sistemas reais",
            criterio_sucesso="Fluxo completo sem erros em 95% dos casos"
        ),
        
        AtividadeTeste(
            id="HT003",
            descricao="Médico real utilizando sistema para atender pacientes "
                     "reais durante 1 semana, avaliando facilidade de uso",
            contexto="Piloto em hospital parceiro",
            stakeholder="usuario_final",
            ambiente="Produção controlada",
            criterio_sucesso="Satisfação > 8/10 e tempo de consulta não aumenta"
        ),
        
        AtividadeTeste(
            id="HT004",
            descricao="Simular 10.000 agendamentos simultâneos para verificar "
                     "se sistema suporta pico de demanda",
            contexto="Preparação para Black Friday da saúde",
            stakeholder="ops",
            ambiente="Ambiente de carga com dados sintéticos",
            criterio_sucesso="Tempo resposta < 2s para 95% das requisições"
        ),
        
        AtividadeTeste(
            id="HT005",
            descricao="Tentar acessar prontuários de outros pacientes usando "
                     "técnicas de SQL injection e bypass de autenticação",
            contexto="Auditoria de segurança antes do go-live",
            stakeholder="especialista_seguranca",
            ambiente="Ambiente isolado com dados anonimizados",
            criterio_sucesso="Nenhuma vulnerabilidade crítica encontrada"
        )
    ]
    
    print("🏥 ANÁLISE SWEBOK - Sistema Hospital TechCare")
    print("="*60)
    
    # Teste classificação individual
    for atividade in atividades:
        print(f"\n📋 Analisando: {atividade.id}")
        classificacao = classificador.classificar_atividade(atividade)
        
        print(f"Tipos principais: {[t.value for t in classificacao.tipos_principais]}")
        print(f"Tipos secundários: {[t.value for t in classificacao.tipos_secundarios]}")
        print(f"Justificativa: {classificacao.justificativa}")
        print(f"Confiança: {classificacao.nivel_confianca:.1%}")
    
    # Teste análise de completude
    print(f"\n📊 ANÁLISE DE COMPLETUDE SWEBOK")
    print("-"*40)
    completude = classificador.validar_completude_swebok(atividades)
    print(completude)
    
    # Teste relatório
    print(f"\n📋 RELATÓRIO DE CONFORMIDADE")
    print("-"*40)
    relatorio = classificador.gerar_relatorio_conformidade(atividades)
    print(relatorio)

if __name__ == "__main__":
    test_cenarios_hospital()
```

### 🎯 Critérios de Avaliação

#### ✅ Excelente (90-100%)
- [ ] Classifica corretamente todos os tipos de teste SWEBOK
- [ ] Identifica tipos principais e secundários adequadamente
- [ ] Análise de completude é precisa e útil
- [ ] Demonstra compreensão profunda da taxonomia SWEBOK

#### ✓ Bom (75-89%)
- [ ] Boa classificação da maioria dos cenários
- [ ] Entende diferenças entre tipos de teste
- [ ] Análise de completude básica mas adequada

#### ⚠️ Satisfatório (60-74%)
- [ ] Classificação básica funcional
- [ ] Compreensão limitada da taxonomia
- [ ] Análise superficial

#### ❌ Insuficiente (<60%)
- [ ] Classificação incorreta ou inconsistente
- [ ] Não demonstra compreensão do SWEBOK
- [ ] Implementação inadequada

### 💡 Dicas para Sucesso

1. **Estude a taxonomia**: Revise a seção SWEBOK da aula principal
2. **Analise o contexto**: Quem faz, onde, quando, por que
3. **Múltiplas dimensões**: Uma atividade pode ter vários tipos
4. **Seja específico**: Justifique suas classificações

### 🔍 Perguntas para Reflexão

1. **Por que** é importante ter uma taxonomia padronizada como SWEBOK?
2. **Como** a classificação correta impacta o planejamento de testes?
3. **Qual** a diferença prática entre teste de sistema e teste de aceitação?
4. **Onde** você vê gaps mais comuns na cobertura SWEBOK?

---

## 🎯 Resumo do Nível 1

### Conceitos Consolidados
- ✅ **Cadeia Causal**: Erro → Defeito → Falha → Incidente
- ✅ **Dualidade**: Verificação vs Validação
- ✅ **Taxonomia**: Classificação SWEBOK de atividades de teste

### Habilidades Desenvolvidas
- 🔍 **Análise sistemática** de problemas
- ⚖️ **Distinção precisa** entre conceitos similares
- 📋 **Classificação padronizada** segundo normas internacionais

### Preparação para Nível 2
Os exercícios do Nível 1 estabeleceram as bases conceituais. No **Nível 2**, você integrará esses conceitos em sistemas mais complexos, analisará trade-offs e tomará decisões arquiteturais baseadas nos fundamentos aqui estabelecidos.

**Continue sua jornada!** 🚀
