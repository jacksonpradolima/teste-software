# Exercício 1.3 - Formulário de Contato 📧

## 📋 Informações do Exercício

**Nível**: 🔵 Básico  
**Tempo Estimado**: 25 minutos  
**Modalidade**: Individual  
**Competências**: Definição de critérios de teste, aplicação de thresholds, análise de qualidade

## 🎯 Objetivo

Desenvolver e aplicar critérios de entrada, cobertura e saída para um projeto de teste de formulário web, compreendendo como esses critérios orientam decisões de qualidade e conclusão de fases de teste.

## 📋 Cenário

Você é o testador responsável pelo formulário de contato do site corporativo de uma empresa de consultoria. O formulário será lançado na próxima semana e precisa de critérios claros para determinar quando está pronto para produção.

### Especificações do Formulário

**Campos Obrigatórios:**
- Nome completo (mín: 2 palavras, máx: 100 caracteres)
- Email (formato válido obrigatório)
- Empresa (máx: 80 caracteres)
- Assunto (seleção: "Orçamento", "Suporte", "Parceria", "Outros")
- Mensagem (mín: 10 caracteres, máx: 500 caracteres)

**Campos Opcionais:**
- Telefone (formato: (XX) XXXXX-XXXX)
- Website da empresa

**Funcionalidades:**
- Validação em tempo real (enquanto digita)
- Botão "Limpar" que zera todos os campos
- Botão "Enviar" que submete e exibe confirmação
- Proteção anti-spam (captcha)

### Requisitos de Qualidade

**Performance:**
- Página deve carregar em menos de 3 segundos
- Validação em tempo real deve responder em menos de 500ms
- Envio do formulário deve ser processado em menos de 5 segundos

**Usabilidade:**
- Mensagens de erro claras e específicas
- Campos obrigatórios claramente marcados
- Compatibilidade com Chrome, Firefox, Safari, Edge
- Responsivo para tablets e smartphones

**Segurança:**
- Proteção contra XSS (Cross-Site Scripting)
- Sanitização de entradas
- Rate limiting (máx 3 envios por minuto por IP)

## 📝 Sua Tarefa

### Etapa 1: Definir Critérios de Entrada (8 minutos)

Estabeleça as condições mínimas que devem estar satisfeitas antes de iniciar os testes:

**Critérios de Produto:**
- [Liste 4-5 critérios relacionados ao produto]

**Critérios de Ambiente:**
- [Liste 3-4 critérios relacionados ao ambiente de teste]

**Critérios de Documentação:**
- [Liste 2-3 critérios relacionados à documentação]

### Etapa 2: Definir Critérios de Cobertura (10 minutos)

Estabeleça o que deve ser testado e em que extensão:

**Cobertura Funcional:**
- [Defina percentuais e métricas específicas]

**Cobertura de Compatibilidade:**
- [Defina navegadores, dispositivos, sistemas]

**Cobertura de Cenários:**
- [Defina tipos de cenários que devem ser cobertos]

### Etapa 3: Definir Critérios de Saída (7 minutos)

Estabeleça quando os testes podem ser considerados suficientes:

**Critérios Quantitativos:**
- [Defina percentuais específicos e limiares numéricos]

**Critérios Qualitativos:**
- [Defina condições de qualidade não-numéricas]

**Critérios de Negócio:**
- [Defina condições relacionadas a prazos e recursos]

## 📄 Template para Entrega

```markdown
# Exercício 1.3 - Formulário de Contato
**Estudante**: [Seu Nome]
**Data**: [Data de Realização]

## Critérios de Entrada

### Critérios de Produto
- [ ] [Critério 1 - seja específico]
- [ ] [Critério 2 - seja específico]
- [ ] [Critério 3 - seja específico]
- [ ] [Critério 4 - seja específico]
- [ ] [Critério 5 - seja específico]

### Critérios de Ambiente
- [ ] [Critério 1 - seja específico]
- [ ] [Critério 2 - seja específico]
- [ ] [Critério 3 - seja específico]
- [ ] [Critério 4 - seja específico]

### Critérios de Documentação
- [ ] [Critério 1 - seja específico]
- [ ] [Critério 2 - seja específico]
- [ ] [Critério 3 - seja específico]

## Critérios de Cobertura

### Cobertura Funcional
- **Campos obrigatórios**: [X]% dos cenários de validação testados
- **Campos opcionais**: [Y]% dos cenários de validação testados
- **Funcionalidades principais**: [Z]% das funcionalidades cobertas
- **Regras de negócio**: [W]% das regras validadas

**Justificativa dos percentuais**: [Explique por que escolheu estes números]

### Cobertura de Compatibilidade
**Navegadores Desktop**:
- [ ] Chrome (versões [X] e [Y])
- [ ] Firefox (versões [X] e [Y])
- [ ] Safari (versões [X] e [Y])
- [ ] Edge (versões [X] e [Y])

**Dispositivos Móveis**:
- [ ] [Especifique dispositivos/resoluções]
- [ ] [Especifique dispositivos/resoluções]

### Cobertura de Cenários
- **Cenários positivos**: Mínimo [X] casos por funcionalidade principal
- **Cenários negativos**: Mínimo [Y] casos por tipo de validação
- **Cenários de boundary**: [Z] casos para cada campo com limites
- **Cenários de performance**: [W] casos para diferentes cargas

## Critérios de Saída

### Critérios Quantitativos
- **Taxa de execução**: [X]% dos casos de teste planejados executados
- **Taxa de aprovação**: [Y]% dos casos executados devem passar
- **Cobertura de código**: [Z]% (se aplicável)
- **Defeitos críticos**: Máximo [W] defeitos críticos em aberto
- **Defeitos altos**: Máximo [V] defeitos de prioridade alta em aberto

### Critérios Qualitativos
- [ ] [Critério qualitativo específico]
- [ ] [Critério qualitativo específico]
- [ ] [Critério qualitativo específico]
- [ ] [Critério qualitativo específico]

### Critérios de Negócio
- [ ] [Critério relacionado a prazo]
- [ ] [Critério relacionado a orçamento]
- [ ] [Critério relacionado a aprovações]

## Análise de Riscos dos Critérios

### Riscos se Critérios Forem Muito Rígidos
- [Risco 1 e impacto]
- [Risco 2 e impacto]

### Riscos se Critérios Forem Muito Flexíveis
- [Risco 1 e impacto]
- [Risco 2 e impacto]

## Plano de Contingência

**Se critérios de saída não puderem ser atendidos no prazo:**
1. [Ação 1]
2. [Ação 2]
3. [Ação 3]

## Reflexão
[1-2 parágrafos sobre a importância dos critérios e desafios na definição]
```

## 🔍 Critérios de Avaliação

### Completude dos Critérios (35 pontos)
- **Excelente (32-35)**: Todos os tipos de critérios bem definidos e específicos
- **Bom (28-31)**: Critérios adequados com pequenas lacunas
- **Satisfatório (24-27)**: Critérios básicos presentes
- **Insatisfatório (0-23)**: Critérios ausentes ou inadequados

### Especificidade e Mensurabilidade (30 pontos)
- **Excelente (27-30)**: Critérios específicos, mensuráveis e verificáveis
- **Bom (24-26)**: Critérios majoritariamente específicos
- **Satisfatório (21-23)**: Critérios moderadamente específicos
- **Insatisfatório (0-20)**: Critérios vagos ou não mensuráveis

### Realismo e Praticabilidade (25 pontos)
- **Excelente (23-25)**: Critérios realistas e aplicáveis ao contexto
- **Bom (20-22)**: Critérios majoritariamente realistas
- **Satisfatório (18-19)**: Critérios básicos adequados
- **Insatisfatório (0-17)**: Critérios irrealistas ou inaplicáveis

### Análise Crítica (10 pontos)
- **Excelente (9-10)**: Análise profunda de riscos e trade-offs
- **Bom (8)**: Boa análise com insights úteis
- **Satisfatório (6-7)**: Análise básica adequada
- **Insatisfatório (0-5)**: Análise superficial ou ausente

## 💡 Dicas para Sucesso

### ✅ Boas Práticas
- **Seja específico**: "90% dos casos" em vez de "maioria dos casos"
- **Considere o contexto**: Formulário simples não precisa critérios de sistema crítico
- **Balance rigor e praticidade**: Critérios muito rígidos podem ser contraproducentes
- **Use dados históricos**: Se disponíveis, baseie percentuais em projetos similares
- **Documente justificativas**: Explique por que escolheu determinados valores

### ❌ Armadilhas Comuns
- Critérios genéricos ("sistema deve funcionar bem")
- Percentuais irrealistas (100% de cobertura para tudo)
- Ignorar restrições de tempo e orçamento
- Critérios não verificáveis objetivamente
- Foco apenas em aspectos técnicos, ignorando negócio

### 📊 Referências de Percentuais Típicos

**Cobertura de Casos de Teste:**
- Projetos críticos: 95-100%
- Projetos comerciais: 85-95%
- Projetos internos: 70-85%

**Taxa de Aprovação:**
- Sistemas críticos: 98-100%
- Aplicações web: 90-95%
- Protótipos: 80-90%

**Defeitos Residuais:**
- Críticos: 0 para produção
- Altos: 0-2 para sistemas críticos, 0-5 para outros
- Médios/Baixos: Conforme tolerância do negócio

## ❓ Perguntas Frequentes

**P: Como definir percentuais se é meu primeiro projeto?**
R: Use benchmarks da indústria e seja conservador. É melhor começar com critérios atingíveis e ajustar depois.

**P: E se o prazo for muito apertado para atender os critérios?**
R: Documente os riscos, negocie prioridades com stakeholders e implemente controles compensatórios.

**P: Critérios podem mudar durante o projeto?**
R: Sim, mas mudanças devem ser controladas, documentadas e aprovadas. Mudanças frequentes indicam planejamento inadequado.

**P: Como lidar com critérios conflitantes?**
R: Priorize baseado em risco do negócio, documente trade-offs e obtenha aprovação dos stakeholders.

---

**Tempo extra?** Considere criar uma matriz de riscos vs. critérios ou um plano de comunicação para reportar status dos critérios aos stakeholders.
