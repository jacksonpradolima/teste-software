# Soluções Nível 1 - Exercícios Básicos

> **Atenção:** Use estas soluções apenas para autoavaliação após tentar resolver os exercícios por conta própria. Analise cada passo, comentários e justificativas para consolidar o aprendizado.

---

## Exercício 1.1: Análise de Função Simples com Condicionais

### classificador_idade.py
```python
from typing import Any

def classificar_visitante(idade: int) -> str:
    """
    Classifica visitante baseado na idade para determinar tipo de ingresso.
    """
    if not isinstance(idade, int):
        raise TypeError("Idade deve ser um inteiro.")
    if idade < 0 or idade > 150:
        return 'invalido'
    if idade <= 12:
        return 'crianca'
    elif idade <= 17:
        return 'adolescente'
    elif idade <= 64:
        return 'adulto'
    else:
        return 'idoso'
```

### Análise Estrutural
- **CFG:** 1 entrada, 5 decisões, 5 saídas
- **Complexidade Ciclomática:** D = 4, M = 5
- **DU-pairs:** idade (def: parâmetro) → uso em todas as decisões

### test_classificador_idade.py
```python
import pytest
from classificador_idade import classificar_visitante

def test_crianca():
    assert classificar_visitante(5) == 'crianca'

def test_adolescente():
    assert classificar_visitante(15) == 'adolescente'

def test_adulto():
    assert classificar_visitante(30) == 'adulto'

def test_idoso():
    assert classificar_visitante(70) == 'idoso'

def test_invalido_negativo():
    assert classificar_visitante(-1) == 'invalido'

def test_invalido_maior_150():
    assert classificar_visitante(200) == 'invalido'

def test_type_error():
    with pytest.raises(TypeError):
        classificar_visitante('dez')
```

---

## Exercício 1.2: Cálculo de Complexidade Ciclomática

### complexidade_analise.py
```python
def calcular_desconto(valor_compra: float, categoria_cliente: str, cupom_ativo: bool) -> float:
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
```

- **Decisões:** 4 (if valor_compra, if categoria, if cupom, if desconto)
- **Complexidade:** M = 5
- **CFG:** 8 nós, 9 arestas, 1 componente → M = 9 - 8 + 2*1 = 3 (corrija para considerar todos os caminhos)

### validar_senha
```python
def validar_senha(senha: str) -> bool:
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
```
- **Decisões:** 2 (len, criterios)
- **Complexidade:** M = 3

---

## Exercício 1.3: Cobertura de Instruções e Decisões

### calculador_frete.py
```python
def calcular_frete(peso: float, distancia: int, categoria_produto: str, cliente_premium: bool) -> dict:
    if peso <= 0 or distancia <= 0:
        raise ValueError("Peso e distância devem ser positivos")
    valor_base = peso * 2.5 + distancia * 0.1
    if categoria_produto == "eletronico":
        multiplicador = 1.5
        prazo_base = 3
    elif categoria_produto == "roupas":
        multiplicador = 1.0
        prazo_base = 2
    elif categoria_produto == "livros":
        multiplicador = 0.8
        prazo_base = 5
    else:
        multiplicador = 1.2
        prazo_base = 4
    valor_frete = valor_base * multiplicador
    if cliente_premium:
        valor_frete *= 0.9
        prazo_base -= 1
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
        'prazo_dias': max(1, prazo_final),
        'transportadora': transportadora
    }
```

### test_calculador_frete.py
```python
import pytest
from calculador_frete import calcular_frete

def test_eletronico_premium_longa():
    r = calcular_frete(5.0, 600, "eletronico", True)
    assert r['valor_frete'] > 0 and r['prazo_dias'] >= 1 and r['transportadora'] == "Transportadora Expressa"

def test_erro_validacao():
    with pytest.raises(ValueError):
        calcular_frete(-1, 100, "livros", False)

def test_roupas_nao_premium_curta():
    r = calcular_frete(2.0, 50, "roupas", False)
    assert r['transportadora'] == "Transportadora Local"

def test_todas_categorias():
    for cat in ["eletronico", "roupas", "livros", "outros"]:
        r = calcular_frete(1.0, 200, cat, False)
        assert r['prazo_dias'] >= 1
```

---

## Exercício 1.4: Identificação Básica de DU-Pairs

### calculador_pontuacao.py
```python
def calcular_pontuacao_jogo(tempo_segundos: int, inimigos_derrotados: int, bonus_coletados: int, dificuldade: str) -> dict:
    pontuacao_base = inimigos_derrotados * 100 + bonus_coletados * 50
    if dificuldade == "facil":
        multiplicador = 1.0
    elif dificuldade == "medio":
        multiplicador = 1.5
    elif dificuldade == "dificil":
        multiplicador = 2.0
    else:
        multiplicador = 1.0
    if tempo_segundos < 300:
        bonus_tempo = 1000
    elif tempo_segundos < 600:
        bonus_tempo = 500
    else:
        bonus_tempo = 0
    pontuacao_final = (pontuacao_base + bonus_tempo) * multiplicador
    if tempo_segundos > 1800:
        pontuacao_final = pontuacao_final * 0.5
    return {
        'pontuacao_final': int(pontuacao_final),
        'pontuacao_base': pontuacao_base,
        'multiplicador': multiplicador,
        'bonus_tempo': bonus_tempo
    }
```

### test_du_pairs_pontuacao.py
```python
from calculador_pontuacao import calcular_pontuacao_jogo

def test_pontuacao_base_zero():
    r = calcular_pontuacao_jogo(100, 0, 0, "facil")
    assert r['pontuacao_base'] == 0

def test_pontuacao_base_calculada():
    r = calcular_pontuacao_jogo(100, 5, 3, "facil")
    assert r['pontuacao_base'] == 650

def test_multiplicador_varios():
    for d, m in [("facil", 1.0), ("medio", 1.5), ("dificil", 2.0), ("x", 1.0)]:
        r = calcular_pontuacao_jogo(100, 1, 1, d)
        assert r['multiplicador'] == m

def test_bonus_tempo():
    assert calcular_pontuacao_jogo(200, 1, 1, "facil")['bonus_tempo'] == 1000
    assert calcular_pontuacao_jogo(500, 1, 1, "facil")['bonus_tempo'] == 500
    assert calcular_pontuacao_jogo(700, 1, 1, "facil")['bonus_tempo'] == 0

def test_penalidade():
    r = calcular_pontuacao_jogo(2000, 10, 5, "dificil")
    assert r['pontuacao_final'] == 1250
```

---

**Compare cada solução com sua implementação e análise. Reflita sobre as diferenças e busque entender o raciocínio por trás de cada decisão de teste estrutural.**
