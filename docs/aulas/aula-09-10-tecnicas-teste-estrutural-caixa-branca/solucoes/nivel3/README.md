# Soluções Nível 3 - Exercícios Avançados

> **Atenção:** Use estas soluções para autoavaliação e estudo aprofundado após tentar resolver os desafios. Analise cada justificativa, comentários e raciocínio estrutural.

---

## Exercício 3.1: Sistema de Gerenciamento de Biblioteca

### biblioteca.py (estrutura simplificada)
```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.renovacoes = 0

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar(self, livro, usuario, data):
        if not livro.disponivel:
            raise Exception("Livro indisponível")
        emprestimo = Emprestimo(livro, usuario, data)
        self.emprestimos.append(emprestimo)
        usuario.emprestimos.append(emprestimo)
        livro.disponivel = False
        return emprestimo

    def devolver(self, emprestimo, data):
        emprestimo.data_devolucao = data
        emprestimo.livro.disponivel = True

    def renovar(self, emprestimo):
        if emprestimo.renovacoes >= 2:
            raise Exception("Limite de renovações atingido")
        emprestimo.renovacoes += 1

    def calcular_multa(self, emprestimo, data_atual):
        # Exemplo: 1 real por dia de atraso
        if emprestimo.data_devolucao and emprestimo.data_devolucao < data_atual:
            dias_atraso = (data_atual - emprestimo.data_devolucao).days
            return max(0, dias_atraso)
        return 0
```

---

## Exercício 3.2: Processador de Transações Bancárias

### processador_bancario.py (estrutura simplificada)
```python
class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

class Transacao:
    def __init__(self, tipo, valor, destino=None):
        self.tipo = tipo  # 'deposito', 'saque', 'transferencia', 'pagamento'
        self.valor = valor
        self.destino = destino

class ProcessadorBancario:
    def processar_transacao(self, conta, transacao):
        if transacao.tipo == 'deposito':
            conta.saldo += transacao.valor
        elif transacao.tipo == 'saque':
            if conta.saldo < transacao.valor:
                raise Exception("Saldo insuficiente")
            conta.saldo -= transacao.valor
        elif transacao.tipo == 'transferencia':
            if conta.saldo < transacao.valor:
                raise Exception("Saldo insuficiente")
            conta.saldo -= transacao.valor
            transacao.destino.saldo += transacao.valor
        elif transacao.tipo == 'pagamento':
            if conta.saldo < transacao.valor:
                raise Exception("Saldo insuficiente")
            conta.saldo -= transacao.valor
        else:
            raise Exception("Tipo de transação inválido")
```

---

## Exercício 3.3: Motor de Regras de Negócio Configurável

### motor_regras.py (estrutura simplificada)
```python
class MotorRegras:
    def __init__(self):
        self.regras = []

    def carregar_regras(self, regras):
        self.regras = regras

    def aplicar(self, contexto):
        resultados = []
        for regra in self.regras:
            if regra['condicao'](contexto):
                resultados.append(regra['acao'](contexto))
        return resultados

    def auditar(self):
        return [r['nome'] for r in self.regras]
```

---

## Exercício 3.4: Análise Estrutural de Sistema Legacy

### sistema_legacy.py (exemplo de refatoração)
```python
def processar_dados(dados):
    # Função original longa e pouco estruturada
    resultado = 0
    for item in dados:
        if item > 0:
            resultado += item
        elif item == 0:
            resultado += 10
        else:
            resultado -= abs(item)
    return resultado

# Refatoração orientada a testes:
def processar_dados_refatorado(dados):
    resultado = 0
    for item in dados:
        if item > 0:
            resultado += item
        elif item == 0:
            resultado += 10
        else:
            resultado -= abs(item)
    return resultado
```

---

**Compare cada solução com sua implementação e análise. Reflita sobre as diferenças e busque entender o raciocínio por trás de cada decisão de teste estrutural.**
