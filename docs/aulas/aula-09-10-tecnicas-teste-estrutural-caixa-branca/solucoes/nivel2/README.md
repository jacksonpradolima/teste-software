# Soluções Nível 2 - Exercícios Intermediários

> **Atenção:** Consulte estas soluções apenas após tentar resolver os exercícios. Analise cada justificativa, comentários e raciocínio estrutural.

---

## Exercício 2.1: Sistema de Validação de Formulários

### validador_formulario.py
```python
def validar_nome(nome: str) -> bool:
    return isinstance(nome, str) and len(nome.strip()) >= 3

def validar_email(email: str) -> bool:
    return isinstance(email, str) and "@" in email and "." in email

def validar_idade(idade: int) -> bool:
    return isinstance(idade, int) and 0 < idade < 150

def validar_senha(senha: str) -> bool:
    if not isinstance(senha, str) or len(senha) < 8:
        return False
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    return tem_maiuscula and tem_numero

def validar_formulario(dados: dict) -> list[str]:
    erros = []
    if not validar_nome(dados.get('nome', '')):
        erros.append('Nome inválido')
    if not validar_email(dados.get('email', '')):
        erros.append('Email inválido')
    if not validar_idade(dados.get('idade', 0)):
        erros.append('Idade inválida')
    if not validar_senha(dados.get('senha', '')):
        erros.append('Senha inválida')
    return erros
```

---

## Exercício 2.2: Analisador de Logs com Múltiplos Critérios

### analisador_logs.py
```python
def classificar_acesso(ip: str, horario: str, tentativas: int, sucesso: bool) -> str:
    if tentativas > 5 and not sucesso:
        return 'critico'
    if tentativas > 3:
        return 'suspeito'
    if ip.startswith('192.168.'):
        return 'normal'
    if horario < '06:00' or horario > '22:00':
        return 'suspeito'
    return 'normal'

def processar_logs(logs: list[dict]) -> dict:
    contagem = {'normal': 0, 'suspeito': 0, 'critico': 0}
    for log in logs:
        tipo = classificar_acesso(
            log['ip'], log['horario'], log['tentativas'], log['sucesso']
        )
        contagem[tipo] += 1
    return contagem
```

---

## Exercício 2.3: Calculadora com Operações Complexas

### calculadora_avancada.py
```python
class CalculadoraAvancada:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        r = a + b
        self.historico.append(f"{a}+{b}={r}")
        return r

    def subtrair(self, a, b):
        r = a - b
        self.historico.append(f"{a}-{b}={r}")
        return r

    def multiplicar(self, a, b):
        r = a * b
        self.historico.append(f"{a}*{b}={r}")
        return r

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero")
        r = a / b
        self.historico.append(f"{a}/{b}={r}")
        return r

    def potencia(self, a, b):
        r = a ** b
        self.historico.append(f"{a}^{b}={r}")
        return r

    def raiz(self, a):
        if a < 0:
            raise ValueError("Raiz de número negativo")
        r = a ** 0.5
        self.historico.append(f"raiz({a})={r}")
        return r

    def modulo(self, a):
        r = abs(a)
        self.historico.append(f"|{a}|={r}")
        return r

    def historico_operacoes(self):
        return self.historico
```

---

## Exercício 2.4: Fluxo de Dados em Sistema de Estoque

### sistema_estoque.py
```python
class Produto:
    def __init__(self, nome: str, quantidade: int):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome: str, quantidade: int):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
        else:
            self.produtos[nome] = Produto(nome, quantidade)

    def remover_produto(self, nome: str, quantidade: int):
        if nome not in self.produtos or self.produtos[nome].quantidade < quantidade:
            raise ValueError("Estoque insuficiente")
        self.produtos[nome].quantidade -= quantidade
        if self.produtos[nome].quantidade == 0:
            del self.produtos[nome]

    def consultar_produto(self, nome: str):
        return self.produtos.get(nome, None)

    def listar_estoque(self):
        return [(p.nome, p.quantidade) for p in self.produtos.values()]
```

---

**Compare cada solução com sua implementação e análise. Reflita sobre as diferenças e busque entender o raciocínio por trás de cada decisão de teste estrutural.**
