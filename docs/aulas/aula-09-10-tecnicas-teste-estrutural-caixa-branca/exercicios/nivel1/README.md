# 🔵 Exercícios Nível 1 - Básico

## Objetivos Específicos

- Aplicar conceitos fundamentais de teste estrutural
- Praticar cálculo de complexidade ciclomática
- Implementar cobertura básica de instruções e decisões
- Identificar DU-pairs em funções simples

---

## Exercício 1.1: Análise de Função Simples com Condicionais 🔍

### Contexto
Você foi contratado para validar um sistema de classificação de idade para um parque temático. O sistema determina o tipo de ingresso baseado na idade do visitante.

### Especificação
Implemente e analise estruturalmente uma função que classifica visitantes:

**Regras de Negócio:**
- **Criança**: 0 a 12 anos (ingresso infantil)
- **Adolescente**: 13 a 17 anos (ingresso jovem)  
- **Adulto**: 18 a 64 anos (ingresso normal)
- **Idoso**: 65+ anos (ingresso com desconto)
- **Inválido**: idades negativas ou acima de 150 anos

### Tarefas

#### 1.1.1. Implementação
Crie o arquivo `classificador_idade.py` com:

```python
def classificar_visitante(idade: int) -> str:
    """
    Classifica visitante baseado na idade para determinar tipo de ingresso.
    
    TAREFA: Implemente esta função seguindo as regras de negócio.
    ATENÇÃO: Comente cada decisão explicando o critério estrutural.
    
    Args:
        idade (int): Idade do visitante
        
    Returns:
        str: Tipo de classificação ('crianca', 'adolescente', 'adulto', 'idoso', 'invalido')
        
    Raises:
        TypeError: Se idade não for um inteiro
    """
    # SEU CÓDIGO AQUI
    pass


# TEMPLATE PARA ANÁLISE ESTRUTURAL
def analisar_estrutura_classificador():
    """
    TAREFA: Complete esta análise estrutural da função classificar_visitante.
    """
    print("=== ANÁLISE ESTRUTURAL - CLASSIFICADOR DE IDADE ===")
    
    # 1. GRAFO DE FLUXO DE CONTROLE
    print("\n1. GRAFO DE FLUXO DE CONTROLE:")
    print("Nó 1: ??? ")
    print("Nó 2: ??? ")
    # Complete com todos os nós identificados
    
    # 2. COMPLEXIDADE CICLOMÁTICA  
    print("\n2. COMPLEXIDADE CICLOMÁTICA:")
    print("Número de decisões (D): ??? ")
    print("M = D + 1 = ??? ")
    
    # 3. IDENTIFICAÇÃO DE DU-PAIRS
    print("\n3. DU-PAIRS:")
    print("Variável 'idade':")
    print("  - Definições: ??? ")
    print("  - P-uses: ??? ")
    print("  - DU-pairs: ??? ")
    
    # 4. CASOS DE TESTE DERIVADOS
    print("\n4. CASOS DE TESTE PARA 100% COBERTURA:")
    print("Caminho 1: ??? ")
    print("Caminho 2: ??? ")
    # Complete com todos os caminhos
```

#### 1.1.2. Casos de Teste
Crie o arquivo `test_classificador_idade.py`:

```python
import pytest
from classificador_idade import classificar_visitante

def test_cobertura_instrucoes():
    """
    TAREFA: Implemente casos de teste para 100% cobertura de instruções.
    """
    # Caso 1: ??? (descreva o que testa)
    # Caso 2: ??? (descreva o que testa)
    # etc.
    pass

def test_cobertura_decisoes():
    """
    TAREFA: Implemente casos de teste para 100% cobertura de decisões.
    Cada decisão deve ser testada tanto True quanto False.
    """
    pass

def test_valores_limitrofes():
    """
    TAREFA: Teste valores nos limites das condições.
    """
    pass

def test_casos_erro():
    """
    TAREFA: Teste casos de entrada inválida.
    """
    pass
```

### Critérios de Avaliação Específicos
- [ ] Função implementada corretamente com todas as regras
- [ ] Análise estrutural completa (CFG, complexidade, DU-pairs)
- [ ] Casos de teste cobrem 100% das instruções
- [ ] Casos de teste cobrem 100% das decisões
- [ ] Comentários explicam decisões estruturais

### Dicas
- Desenhe o CFG no papel antes de implementar
- Use valores de teste que exerçam cada caminho exatamente uma vez
- Lembre-se: cada `if` cria duas saídas possíveis (True/False)

---

## Exercício 1.2: Cálculo de Complexidade Ciclomática 📊

### Contexto
Você precisa analisar a complexidade estrutural de diferentes funções para determinar o esforço de teste necessário.

### Especificação
Analise as funções fornecidas e calcule suas complexidades ciclomáticas usando ambos os métodos.

### Tarefas

#### 1.2.1. Análise de Função Simples
Crie o arquivo `complexidade_analise.py`:

```python
def calcular_desconto(valor_compra: float, categoria_cliente: str, cupom_ativo: bool) -> float:
    """
    Calcula desconto baseado em múltiplos critérios.
    """
    desconto = 0.0
    
    if valor_compra > 100.0:
        if categoria_cliente == "VIP":
            desconto = 0.15
        elif categoria_cliente == "PREMIUM":
            desconto = 0.10
        else:
            desconto = 0.05
    
    if cupom_ativo:
        desconto += 0.05
    
    if desconto > 0.25:
        desconto = 0.25
        
    return desconto


def analisar_complexidade_desconto():
    """
    TAREFA: Complete a análise de complexidade da função calcular_desconto.
    """
    print("=== ANÁLISE DE COMPLEXIDADE CICLOMÁTICA ===")
    
    # MÉTODO 1: Contagem de Decisões
    print("\nMÉTODO 1 - Contagem de Decisões:")
    print("Decisão 1: if valor_compra > 100.0")
    print("Decisão 2: ??? ")
    print("Decisão 3: ??? ")
    # Complete a identificação
    
    total_decisoes = 0  # CALCULE
    complexidade_metodo1 = total_decisoes + 1
    print(f"Total de decisões (D): {total_decisoes}")
    print(f"Complexidade (M = D + 1): {complexidade_metodo1}")
    
    # MÉTODO 2: Fórmula de Grafos (M = E - N + 2P)
    print("\nMÉTODO 2 - Fórmula de Grafos:")
    print("TAREFA: Desenhe o CFG e conte:")
    
    total_nos = 0      # CONTE os nós no CFG
    total_arestas = 0  # CONTE as arestas no CFG  
    componentes = 1    # Geralmente 1 para uma função
    
    complexidade_metodo2 = total_arestas - total_nos + (2 * componentes)
    
    print(f"Nós (N): {total_nos}")
    print(f"Arestas (E): {total_arestas}")
    print(f"Componentes (P): {componentes}")
    print(f"Complexidade (M = E - N + 2P): {complexidade_metodo2}")
    
    # VERIFICAÇÃO
    if complexidade_metodo1 == complexidade_metodo2:
        print(f"\n✅ VERIFICAÇÃO: Ambos os métodos concordam (M = {complexidade_metodo1})")
    else:
        print(f"\n❌ ERRO: Métodos discordam ({complexidade_metodo1} vs {complexidade_metodo2})")
```

#### 1.2.2. Análise Comparativa
Adicione ao mesmo arquivo:

```python
def validar_senha(senha: str) -> bool:
    """Valida senha com múltiplos critérios."""
    if len(senha) < 8:
        return False
    
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)  
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in "!@#$%^&*" for c in senha)
    
    criterios_atendidos = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])
    
    if criterios_atendidos >= 3:
        return True
    else:
        return False


def comparar_complexidades():
    """
    TAREFA: Compare as complexidades das duas funções e analise.
    """
    print("=== COMPARAÇÃO DE COMPLEXIDADES ===")
    
    print("\nFunção: calcular_desconto")
    print("Complexidade: ??? ")
    print("Interpretação: ??? ")
    
    print("\nFunção: validar_senha")
    print("Complexidade: ??? ")
    print("Interpretação: ??? ")
    
    print("\nANÁLISE COMPARATIVA:")
    print("Qual função é mais complexa de testar? ??? ")
    print("Justificativa: ??? ")
    print("Estratégia de teste recomendada: ??? ")
```

### Critérios de Avaliação Específicos
- [ ] Complexidade calculada corretamente pelos dois métodos
- [ ] CFG desenhado e documentado adequadamente
- [ ] Identificação precisa de todas as decisões
- [ ] Análise comparativa bem fundamentada
- [ ] Interpretação correta dos valores de complexidade

---

## Exercício 1.3: Cobertura de Instruções e Decisões 📈

### Contexto  
Uma startup precisa implementar um sistema de cálculo de frete para seu e-commerce. Você deve garantir cobertura estrutural completa.

### Especificação
Analise e teste um calculador de frete que considera múltiplos fatores.

### Tarefas

#### 1.3.1. Implementação Base
Crie o arquivo `calculador_frete.py`:

```python
def calcular_frete(peso: float, distancia: int, categoria_produto: str, cliente_premium: bool) -> dict:
    """
    Calcula frete baseado em peso, distância, categoria e status do cliente.
    
    Args:
        peso: Peso do produto em kg
        distancia: Distância em km  
        categoria_produto: 'eletronico', 'roupas', 'livros', 'outros'
        cliente_premium: Status premium do cliente
        
    Returns:
        dict: {'valor_frete': float, 'prazo_dias': int, 'transportadora': str}
    """
    # VALIDAÇÕES INICIAIS
    if peso <= 0 or distancia <= 0:
        raise ValueError("Peso e distância devem ser positivos")
    
    # CÁLCULO BASE DO FRETE
    valor_base = peso * 2.5 + distancia * 0.1
    
    # AJUSTE POR CATEGORIA
    if categoria_produto == "eletronico":
        multiplicador = 1.5
        prazo_base = 3
    elif categoria_produto == "roupas":
        multiplicador = 1.0
        prazo_base = 2
    elif categoria_produto == "livros":
        multiplicador = 0.8
        prazo_base = 5
    else:  # outros
        multiplicador = 1.2
        prazo_base = 4
    
    valor_frete = valor_base * multiplicador
    
    # DESCONTO PARA CLIENTE PREMIUM
    if cliente_premium:
        valor_frete *= 0.9  # 10% desconto
        prazo_base -= 1     # 1 dia a menos
    
    # AJUSTE DE PRAZO POR DISTÂNCIA
    if distancia > 500:
        prazo_final = prazo_base + 2
        transportadora = "Transportadora Expressa"
    elif distancia > 100:
        prazo_final = prazo_base + 1  
        transportadora = "Transportadora Regional"
    else:
        prazo_final = prazo_base
        transportadora = "Transportadora Local"
    
    return {
        'valor_frete': round(valor_frete, 2),
        'prazo_dias': max(1, prazo_final),  # Mínimo 1 dia
        'transportadora': transportadora
    }


def analisar_cobertura_frete():
    """
    TAREFA: Identifique todas as instruções e decisões para análise de cobertura.
    """
    print("=== ANÁLISE DE COBERTURA - CALCULADOR DE FRETE ===")
    
    print("\nINSTRUÇÕES IDENTIFICADAS:")
    print("1. if peso <= 0 or distancia <= 0:")
    print("2. raise ValueError(...)")
    print("3. valor_base = peso * 2.5 + distancia * 0.1")
    # TAREFA: Continue listando TODAS as instruções
    
    print("\nDECISÕES IDENTIFICADAS:")
    print("1. if peso <= 0 or distancia <= 0:")
    print("2. if categoria_produto == 'eletronico':")
    # TAREFA: Continue listando TODAS as decisões
    
    print("\nCÁLCULO DE COBERTURA:")
    total_instrucoes = 0  # CONTE todas as instruções
    total_decisoes = 0    # CONTE todas as decisões
    
    print(f"Total de instruções: {total_instrucoes}")
    print(f"Total de decisões: {total_decisoes}")
    print(f"Para 100% cobertura de decisões, precisa de casos que testem:")
    print("- Cada decisão como True E como False")
```

#### 1.3.2. Casos de Teste Estruturais
Crie o arquivo `test_calculador_frete.py`:

```python
import pytest
from calculador_frete import calcular_frete

class TestCoberturaInstrucoes:
    """Casos de teste focados em cobertura de instruções."""
    
    def test_caminho_eletronico_premium_longa_distancia(self):
        """
        TAREFA: Teste que exercita o máximo de instruções em um único caso.
        Caminho: eletrônico + premium + distância > 500
        """
        resultado = calcular_frete(
            peso=5.0,
            distancia=600, 
            categoria_produto="eletronico",
            cliente_premium=True
        )
        
        # TAREFA: Adicione assertions que validem o resultado
        # E documente quais instruções este teste exercita
        pass
    
    def test_caminho_erro_validacao(self):
        """
        TAREFA: Teste o caminho de erro (peso/distância inválidos).
        """
        pass
    
    def test_caminho_outros_nao_premium_curta_distancia(self):
        """
        TAREFA: Teste caminho alternativo para maximizar cobertura.
        """
        pass

class TestCoberturaDecisoes:
    """Casos de teste focados em cobertura de decisões."""
    
    def test_decisao_validacao_true_false(self):
        """
        TAREFA: Teste decisão de validação (True E False).
        """
        # Caso False (entrada válida)
        resultado_valido = calcular_frete(1.0, 50, "livros", False)
        assert resultado_valido is not None
        
        # Caso True (entrada inválida) 
        with pytest.raises(ValueError):
            calcular_frete(-1.0, 50, "livros", False)  # peso inválido
        
        # TAREFA: Teste também distância inválida
    
    def test_decisao_categoria_todas_opcoes(self):
        """
        TAREFA: Teste TODAS as opções da decisão de categoria.
        """
        # eletrônico
        resultado_elet = calcular_frete(1.0, 50, "eletronico", False)
        
        # roupas  
        resultado_roupas = calcular_frete(1.0, 50, "roupas", False)
        
        # TAREFA: Teste também "livros" e "outros"
        # Valide que cada categoria gera resultado diferente
    
    def test_decisao_cliente_premium_true_false(self):
        """
        TAREFA: Teste decisão premium (True E False).
        """
        pass
    
    def test_decisao_distancia_todas_faixas(self):
        """
        TAREFA: Teste TODAS as faixas de distância.
        """
        # <= 100
        resultado_curta = calcular_frete(1.0, 50, "livros", False)
        
        # 100 < distancia <= 500
        resultado_media = calcular_frete(1.0, 300, "livros", False)
        
        # > 500
        resultado_longa = calcular_frete(1.0, 600, "livros", False)
        
        # TAREFA: Valide que cada faixa gera transportadora diferente

def medir_cobertura():
    """
    TAREFA: Execute os testes e meça a cobertura.
    Execute: python -m pytest test_calculador_frete.py -v
    Execute: coverage run -m pytest test_calculador_frete.py
    Execute: coverage report -m
    """
    print("INSTRUÇÕES PARA MEDIR COBERTURA:")
    print("1. pip install coverage")
    print("2. coverage run -m pytest test_calculador_frete.py")
    print("3. coverage report -m")
    print("4. coverage html  # para relatório visual")
    print("5. Documente os resultados aqui:")
    print("   Cobertura de instruções: ____%")
    print("   Linhas não cobertas: ____")
```

### Critérios de Avaliação Específicos
- [ ] Identificação correta de todas as instruções e decisões
- [ ] Casos de teste atingem 100% de cobertura de instruções
- [ ] Casos de teste atingem 100% de cobertura de decisões  
- [ ] Medição de cobertura executada e documentada
- [ ] Análise dos resultados de cobertura

---

## Exercício 1.4: Identificação Básica de DU-Pairs 🔗

### Contexto
Uma empresa de jogos precisa implementar um sistema de pontuação que considera vários fatores. Você deve analisar o fluxo de dados para garantir qualidade.

### Especificação
Analise o fluxo de dados em um calculador de pontuação de jogo.

### Tarefas

#### 1.4.1. Implementação Base
Crie o arquivo `calculador_pontuacao.py`:

```python
def calcular_pontuacao_jogo(tempo_segundos: int, inimigos_derrotados: int, 
                           bonus_coletados: int, dificuldade: str) -> dict:
    """
    Calcula pontuação final baseada em performance do jogador.
    
    FOCO: Análise de fluxo de dados (definições e usos de variáveis).
    """
    # INICIALIZAÇÃO
    pontuacao_base = 0
    multiplicador = 1.0
    bonus_tempo = 0
    
    # CÁLCULO DA PONTUAÇÃO BASE
    pontuacao_base = inimigos_derrotados * 100 + bonus_coletados * 50
    
    # MULTIPLICADOR POR DIFICULDADE
    if dificuldade == "facil":
        multiplicador = 1.0
    elif dificuldade == "medio":
        multiplicador = 1.5
    elif dificuldade == "dificil": 
        multiplicador = 2.0
    else:
        multiplicador = 1.0  # padrão para entrada inválida
    
    # BÔNUS DE TEMPO (se completou rápido)
    if tempo_segundos < 300:  # menos de 5 minutos
        bonus_tempo = 1000
    elif tempo_segundos < 600:  # menos de 10 minutos
        bonus_tempo = 500
    else:
        bonus_tempo = 0
    
    # CÁLCULO FINAL
    pontuacao_final = (pontuacao_base + bonus_tempo) * multiplicador
    
    # PENALIDADE SE MUITO DEVAGAR
    if tempo_segundos > 1800:  # mais de 30 minutos
        pontuacao_final = pontuacao_final * 0.5
    
    return {
        'pontuacao_final': int(pontuacao_final),
        'pontuacao_base': pontuacao_base,
        'multiplicador': multiplicador,
        'bonus_tempo': bonus_tempo
    }


def analisar_du_pairs():
    """
    TAREFA: Identifique TODAS as definições e usos de cada variável.
    """
    print("=== ANÁLISE DE DU-PAIRS - CALCULADOR DE PONTUAÇÃO ===")
    
    print("\nVARIÁVEL: pontuacao_base")
    print("Definições (Def):")
    print("  Linha X: pontuacao_base = 0")
    print("  Linha Y: pontuacao_base = inimigos_derrotados * 100 + bonus_coletados * 50")
    print("Usos Computacionais (C-use):")
    print("  Linha Z: pontuacao_final = (pontuacao_base + bonus_tempo) * multiplicador")
    print("  Linha W: 'pontuacao_base': pontuacao_base  # no dicionário de retorno")
    print("Usos Predicativos (P-use):")
    print("  Nenhum")
    print("DU-Pairs:")
    print("  (X, Z): pontuacao_base definida na linha X, usada na linha Z")
    print("  (X, W): pontuacao_base definida na linha X, usada na linha W")
    print("  (Y, Z): pontuacao_base definida na linha Y, usada na linha Z")
    print("  (Y, W): pontuacao_base definida na linha Y, usada na linha W")
    
    print("\nVARIÁVEL: multiplicador")
    print("TAREFA: Complete a análise para a variável multiplicador")
    print("Definições (Def):")
    print("  ???")
    print("Usos Computacionais (C-use):")
    print("  ???")
    print("Usos Predicativos (P-use):")
    print("  ???")
    print("DU-Pairs:")
    print("  ???")
    
    print("\nVARIÁVEL: bonus_tempo")
    print("TAREFA: Complete a análise para a variável bonus_tempo")
    
    print("\nVARIÁVEL: pontuacao_final")
    print("TAREFA: Complete a análise para a variável pontuacao_final")
    
    print("\nVARIÁVEIS DE ENTRADA: tempo_segundos, inimigos_derrotados, bonus_coletados, dificuldade")
    print("TAREFA: Analise os usos dessas variáveis (apenas usos, não definições)")


def identificar_caminhos_du():
    """
    TAREFA: Para cada DU-pair, identifique o caminho livre de definição.
    """
    print("\n=== CAMINHOS LIVRES DE DEFINIÇÃO ===")
    
    print("\nDU-PAIR: (pontuacao_base linha X, uso linha Z)")
    print("Caminho: ??? ")
    print("É livre de definição? ??? (sim/não + justificativa)")
    
    print("\nDU-PAIR: (multiplicador linha Y, uso linha Z)")  
    print("TAREFA: Identifique o caminho e verifique se é livre de definição")
    
    # TAREFA: Complete para todos os DU-pairs identificados
```

#### 1.4.2. Casos de Teste para DU-Pairs
Crie o arquivo `test_du_pairs_pontuacao.py`:

```python
import pytest
from calculador_pontuacao import calcular_pontuacao_jogo

class TestDUPairsCoverage:
    """Casos de teste focados em cobrir todos os DU-pairs identificados."""
    
    def test_du_pair_pontuacao_base_inicial_para_calculo(self):
        """
        TAREFA: Teste DU-pair onde pontuacao_base mantém valor inicial (0).
        Isso acontece quando??? (identifique a condição)
        """
        # Como fazer pontuacao_base permanecer 0?
        # Resposta: inimigos_derrotados=0 e bonus_coletados=0
        
        resultado = calcular_pontuacao_jogo(
            tempo_segundos=100,
            inimigos_derrotados=0,
            bonus_coletados=0, 
            dificuldade="facil"
        )
        
        # Este teste exercita o DU-pair: pontuacao_base(def inicial) → uso no cálculo final
        assert resultado['pontuacao_base'] == 0
        
    def test_du_pair_pontuacao_base_calculada_para_uso(self):
        """
        TAREFA: Teste DU-pair onde pontuacao_base é calculada e depois usada.
        """
        resultado = calcular_pontuacao_jogo(
            tempo_segundos=100,
            inimigos_derrotados=5,  # Não zero
            bonus_coletados=3,      # Não zero
            dificuldade="facil"
        )
        
        # Este teste exercita: pontuacao_base(def calculada) → uso no cálculo final
        assert resultado['pontuacao_base'] == 5 * 100 + 3 * 50  # 650
    
    def test_du_pairs_multiplicador_todas_definicoes(self):
        """
        TAREFA: Teste todas as definições possíveis de multiplicador.
        """
        # Definição: multiplicador = 1.0 (fácil)
        resultado_facil = calcular_pontuacao_jogo(100, 1, 1, "facil")
        assert resultado_facil['multiplicador'] == 1.0
        
        # TAREFA: Teste também "medio", "dificil" e caso padrão
    
    def test_du_pairs_bonus_tempo_todas_definicoes(self):
        """
        TAREFA: Teste todas as definições possíveis de bonus_tempo.
        """
        # bonus_tempo = 1000 (< 300s)
        resultado_rapido = calcular_pontuacao_jogo(200, 1, 1, "facil")
        assert resultado_rapido['bonus_tempo'] == 1000
        
        # TAREFA: Teste também tempo médio (500) e tempo longo (0)
    
    def test_du_pair_pontuacao_final_sem_penalidade(self):
        """
        TAREFA: Teste DU-pair onde pontuacao_final é calculada e retornada sem penalidade.
        """
        pass
    
    def test_du_pair_pontuacao_final_com_penalidade(self):
        """
        TAREFA: Teste DU-pair onde pontuacao_final é redefinida pela penalidade.
        """
        # Tempo > 1800s para ativar penalidade
        resultado = calcular_pontuacao_jogo(2000, 10, 5, "dificil")
        
        # Calcule o valor esperado:
        # pontuacao_base = 10*100 + 5*50 = 1250
        # bonus_tempo = 0 (tempo > 600)
        # multiplicador = 2.0 (dificil)
        # pontuacao_antes_penalidade = (1250 + 0) * 2.0 = 2500
        # pontuacao_final = 2500 * 0.5 = 1250
        
        assert resultado['pontuacao_final'] == 1250

def validar_cobertura_du_pairs():
    """
    TAREFA: Execute os testes e valide se todos os DU-pairs foram cobertos.
    """
    print("=== VALIDAÇÃO DE COBERTURA DE DU-PAIRS ===")
    print("Execute os testes e marque os DU-pairs cobertos:")
    
    print("\n✅ DU-pairs cobertos:")
    print("[ ] pontuacao_base (def inicial) → uso final")  
    print("[ ] pontuacao_base (def calculada) → uso final")
    print("[ ] multiplicador (def facil) → uso final")
    print("[ ] multiplicador (def medio) → uso final")
    print("[ ] multiplicador (def dificil) → uso final")
    print("[ ] multiplicador (def padrão) → uso final")
    print("[ ] bonus_tempo (def 1000) → uso final")
    print("[ ] bonus_tempo (def 500) → uso final")
    print("[ ] bonus_tempo (def 0) → uso final")
    print("[ ] pontuacao_final (def inicial) → retorno")
    print("[ ] pontuacao_final (def com penalidade) → retorno")
    
    print("\n❌ DU-pairs ainda não cobertos:")
    print("TAREFA: Liste aqui os DU-pairs que ainda precisam de casos de teste")
```

### Critérios de Avaliação Específicos
- [ ] Identificação correta de todas as definições de variáveis
- [ ] Identificação correta de todos os usos (C-use e P-use)
- [ ] DU-pairs listados completamente e corretamente
- [ ] Casos de teste cobrem todos os DU-pairs identificados
- [ ] Análise de caminhos livres de definição está correta

---

## 🎯 Conclusão do Nível 1

Parabéns por completar os exercícios básicos! Você praticou:

- ✅ **Análise estrutural básica** com CFG e complexidade ciclomática
- ✅ **Cobertura de instruções e decisões** sistemática
- ✅ **Identificação de DU-pairs** e análise de fluxo de dados
- ✅ **Derivação de casos de teste** baseada em critérios estruturais

### Próximos Passos
- Compare suas soluções com os gabaritos em `../solucoes/nivel1/`
- Se se sentir confortável, avance para o [Nível 2](../nivel2/)
- Revise conceitos que ainda geram dúvidas no capítulo principal

### Autoavaliação
Antes de avançar, certifique-se que consegue:
- [ ] Desenhar CFG de funções simples
- [ ] Calcular complexidade ciclomática pelos dois métodos
- [ ] Identificar todas as instruções e decisões de uma função
- [ ] Listar DU-pairs sistematicamente
- [ ] Derivar casos de teste para cobertura específica

**Continue a jornada! O conhecimento em teste estrutural é construído progressivamente. 🚀**
