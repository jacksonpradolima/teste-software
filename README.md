# Teste de Software I

[![Deploy Jupyter Book](https://github.com/jacksonpradolima/teste-software/actions/workflows/deploy-book.yml/badge.svg?branch=main)](https://github.com/jacksonpradolima/teste-software/actions/workflows/deploy-book.yml)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📚 Sobre

Este repositório reúne os materiais, exemplos, exercícios e recursos utilizados na disciplina **Teste de Software I**. O curso aborda fundamentos, técnicas, estratégias e ferramentas modernas para garantir a qualidade de produtos de software, com ênfase em práticas de verificação, validação, automação e gestão de defeitos.

### 🎯 Objetivo Geral

Capacitar o aluno a compreender, aplicar e criticar os princípios, conceitos fundamentais e técnicas clássicas e modernas de Teste de Software, promovendo habilidades práticas, competências analíticas e atitudes orientadas à melhoria contínua no desenvolvimento, integração e manutenção de sistemas computacionais.

#### Objetivos Específicos

- Compreender os conceitos fundamentais de qualidade de software, incluindo defeito, falha, erro, incidente, verificação e validação.
- Conhecer e aplicar técnicas de teste funcional (caixa-preta), como particionamento de equivalência e análise de valor limite.
- Conhecer e aplicar técnicas de teste estrutural (caixa-branca), como cobertura de instruções, decisões e caminhos independentes.
- Identificar e aplicar as diferentes estratégias de testes: unitário, integração, regressão e de sistema.
- Aplicar o Desenvolvimento Orientado a Testes (TDD) em projetos simples, evidenciando os benefícios para o design do software.
- Conhecer e discutir práticas de Behavior-Driven Development (BDD) e Acceptance Test-Driven Development (ATDD) para melhoria da comunicação entre stakeholders e desenvolvedores.
- Elaborar e interpretar casos de teste, critérios de parada e métricas de qualidade, relacionando-os ao contexto real do desenvolvimento.
- Planejar, executar e gerenciar o processo de testes, incluindo a geração de dados de teste e a gestão de defeitos utilizando ferramentas adequadas.
- Desenvolver a habilidade de utilizar ferramentas de automação de testes e gestão de testes reconhecidas no mercado.
- Integrar os conhecimentos adquiridos na disciplina por meio do desenvolvimento de um projeto integrador final, aplicando de forma prática os conceitos de teste de software.
- Refletir criticamente sobre o papel estratégico do teste de software na engenharia de software e sua relação com as boas práticas de desenvolvimento e manutenção.

## 🗓️ Estrutura do Curso

O curso está organizado conforme o cronograma de 36 aulas, abrangendo fundamentos, técnicas, estratégias, ferramentas e projeto integrador:

| **Aula** | **Tema**                                                                            | **Entregas / Observações**                                                                                 | **Status**            |
| -------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------- |
| 1-2      | Apresentação da Disciplina, Introdução ao Teste de Software e Qualidade de Software | \* Conceitos, histórico, ISO/IEC 25010, Curva de Boehm                                                     | ✅ Concluído          |
| 3-4      | Conceitos Fundamentais de Teste                                                     | \* Erro, defeito, falha, incidente, bug, verificação vs validação, SWEBOK, modelos de processo             | ✅ Concluído          |
| 5        | Casos de Teste e Critérios                                                          | \* Estrutura de casos de teste, critérios de entrada/saída, heurísticas, exemplos práticos                 | ✅ Concluído          |
| 6-8      | Técnicas de Teste Funcional (Caixa-Preta)                                           | \* Particionamento de equivalência, valor limite, tabelas de decisão, máquina de estados, casos de uso     | ✅ Concluído          |
| 9-10     | Técnicas de Teste Estrutural (Caixa-Branca)                                         | \* Cobertura de instrução, decisão, caminhos independentes, condições combinadas, ferramentas de cobertura | ✅ Concluído          |
| 11       | Critérios de Parada e Métricas de Teste                                             | \* Cobertura, estabilização de defeitos, métricas de qualidade, DRE                                        | ✅ Concluído          |
| 12-14    | Estratégias de Teste: Unitário, Integração, Regressão                               | \* Teste unitário, integração, regressão, automação, exemplos práticos                                     | 🔄 Em desenvolvimento |
| 15-16    | Desenvolvimento Orientado a Testes (TDD, BDD, ATDD)                                 | \* TDD, BDD, ATDD, comparativo, exercícios                                                                 | 🔄 Em desenvolvimento |
| 17       | Geração de Dados de Teste                                                           | \* Dados sintéticos, técnicas, ferramentas, geração baseada em modelos                                     | 🔄 Em desenvolvimento |
| 18       | Prova Teórica I                                                                     | \* Avaliação dos conteúdos do 1º bimestre                                                                  | -                     |
| 19-20    | Gestão de Testes e Defeitos                                                         | \* Planejamento, plano de testes, matriz de rastreabilidade, ciclo de vida do defeito                      | 🔄 Em desenvolvimento |
| 21-22    | Métricas e Qualidade no CI/CD                                                       | \* Defect Density, MTTD, MTTR, Quality Gates, automação em pipelines                                       | 🔄 Em desenvolvimento |
| 23-24    | Testes Baseados em Modelos e Mutação                                                | \* Model-Based Testing, Teste de Mutação, ferramentas                                                      | 🔄 Em desenvolvimento |
| 25-26    | Testes de Performance e Segurança                                                   | \* Teste de carga, OWASP Top 10, ferramentas básicas                                                       | 🔄 Em desenvolvimento |
| 27-28    | Testes em Microserviços e Observabilidade                                           | \* Estratégias, contract testing, logs, métricas, traces                                                   | 🔄 Em desenvolvimento |
| 29-30    | Ferramentas de Teste                                                                | \* Unitários, integração, funcionais, gestão, plugins                                                      | 🔄 Em desenvolvimento |
| 31-33    | Projeto Integrador Final                                                            | \* Planejamento, execução, documentação, apresentação                                                      | 🔄 Em desenvolvimento |
| 34-35    | Apresentação do Projeto Integrador                                                  | \* Apresentação formal, discussão de resultados                                                            | -                     |
| 36       | Prova Teórica II                                                                    | \* Avaliação dos conteúdos do 2º bimestre                                                                  | -                     |

## 💻 Tecnologias Utilizadas

- **Python 3.12+**
- **pytest**
- **Coverage.py**
- **Ferramentas de automação e gestão de testes** (ex: Jira, Azure DevOps, Selenium, Postman, JMeter, k6, Pact, Prometheus, Grafana, Jaeger)
- **GitHub Actions**

## 🚀 Como Executar

### Pré-requisitos

- Python 3.12+
- Ferramentas específicas conforme a aula (pytest, coverage, etc.)

### Executando Testes

```bash
# Instalar dependências (exemplo para pytest)
pip install -r requirements.txt

# Executar testes
pytest --cov=./

# Visualizar cobertura
pytest --cov-report html
```

## 📖 Conteúdos em Destaque

- **Fundamentos de Teste de Software**
- **Qualidade de Software e ISO/IEC 25010**
- **Técnicas de Teste Funcional e Estrutural**
- **Desenvolvimento Orientado a Testes (TDD, BDD, ATDD)**
- **Gestão de Defeitos e Métricas de Qualidade**
- **Automação de Testes e Integração Contínua**
- **Testes em Microserviços e Observabilidade**
- **Ferramentas de Mercado para Teste e Gestão**
- **Projeto Integrador Final**

## 🔮 Trabalhos Futuros

- [ ] Finalizar exemplos práticos e estudos de caso por aula
- [ ] Documentar todas as aulas e exercícios
- [ ] Implementar projeto integrador completo

## 🤝 Reúso do Material

O conteúdo deste repositório pode ser reutilizado com devida referência. Pull Requests com melhorias e novos exemplos são bem-vindos!

Para dúvidas, comentários ou sugestões, abra uma **issue**.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
