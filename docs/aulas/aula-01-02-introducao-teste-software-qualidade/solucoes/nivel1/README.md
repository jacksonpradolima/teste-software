# Soluções - Nível 1 (Conceitual)

## Questão 1: Verificação vs. Validação

a) **Verificação.** Justificativa: A atividade não executa o código; ela analisa um artefato (o código-fonte) para garantir conformidade com um padrão predefinido.

b) **Validação.** Justificativa: A atividade envolve a execução do software por usuários finais para determinar se ele atende às suas necessidades reais de negócio.

c) **Verificação.** Justificativa: É uma análise estática de um artefato (o diagrama de arquitetura) para checar se ele está em conformidade com os requisitos especificados.

d) **Validação.** Justificativa: O teste beta é uma forma de validação com usuários reais em um ambiente real, focando em como o software atende às suas expectativas.

e) **Verificação.** Justificativa: Embora o código esteja sendo executado, o teste unitário, neste contexto, é uma forma de verificação técnica para garantir que a classe está sendo construída corretamente de acordo com a especificação do desenvolvedor, não se ela atende a uma necessidade do usuário final. (Nota: Testes unitários podem servir a ambos os propósitos, mas seu foco principal é a correção técnica da unidade).

## Questão 2: Objetivos do Teste

"Prezado CEO, além de encontrar bugs, o teste de software é crucial para o nosso sucesso de outras formas. Primeiro, ele **garante que nosso aplicativo cumpre todos os requisitos**, o que significa que estamos entregando o valor prometido aos nossos clientes. Segundo, ao testar desde o início, **reduzimos significativamente os custos de desenvolvimento**, pois corrigir um problema em produção é muito mais caro do que na fase de design. Por fim, um software bem testado **melhora a reputação da nossa marca**, pois um aplicativo confiável e fácil de usar gera clientes satisfeitos e leais, que são a base para nosso crescimento sustentável."

## Questão 3: ISO/IEC 25010

1.  **Manutenibilidade:** A facilidade de modificar o código reflete diretamente sua manutenibilidade.
2.  **Segurança:** A proteção contra acesso não autorizado é um pilar da segurança.
3.  **Usabilidade:** A facilidade de aprendizado e operação para um novo usuário é a definição de usabilidade.
4.  **Eficiência de Desempenho:** A capacidade de lidar com uma carga de usuários sem degradação do tempo de resposta é uma medida de desempenho.
5.  **Adequação Funcional:** O sistema executa sua função de cálculo corretamente, conforme especificado.
6.  **Confiabilidade:** A alta disponibilidade (pouco tempo fora do ar) é uma medida chave de confiabilidade.

## Questão 4: Curva de Boehm

a) **Fase de Requisitos:** Custo mínimo (1x). O impacto é apenas a correção do texto no documento de requisitos. A correção é rápida e barata.

b) **Fase de Codificação:** Custo moderado (10x). O desenvolvedor pode ter que descartar o código XML já escrito e começar a implementação do JSON. Envolve retrabalho, mas ainda está contido na equipe de desenvolvimento.

c) **Fase de Testes de Aceitação:** Custo alto (30-70x). A funcionalidade já foi projetada, codificada e testada unitariamente. A correção envolve voltar à fase de codificação, refazer os testes unitários, testes de integração e, finalmente, o teste de aceitação. O cronograma do projeto provavelmente será impactado.

d) **Em Produção:** Custo altíssimo (40-1000x). Além de todo o custo de correção técnica (codificar, testar, etc.), há custos adicionais: impacto nos clientes que já podem estar usando a exportação XML, custo de migração de dados, dano à reputação da empresa, comunicação com os clientes sobre a mudança e um novo ciclo de lançamento de emergência (*hotfix*).
