# Escopo da Avaliação

A avaliação se concentrará no fluxo de planejamento de formatura do No Fluxo UnB, composto por três etapas:

1. **Enviar o histórico (Figura 1):** o estudante envia o PDF do histórico oficial da UnB ou preenche os dados manualmente.
2. **Visualizar o fluxograma (Figura 2):** o sistema apresenta a matriz curricular e indica a situação das disciplinas já cursadas e das que faltam.
3. **Planejar formatura (Figura 3):** ao clicar em **“Planejar formatura”**, o sistema gera uma sequência de disciplinas prevista até a formatura. **Esta tela é o objeto central da avaliação.**

![Tela de importação do histórico, com área para enviar o PDF, botão para selecionar arquivo e opção de preenchimento manual](img/noFluxo_importar.png)

*Figura 1 — Tela de importação do histórico. Fonte: captura de tela do No Fluxo UnB, outubro de 2026.*

![Fluxograma do curso de Engenharia de Software, com a matriz curricular por semestre e disciplinas identificadas por situação](img/noFluxo_fluxograma.png)

*Figura 2 — Fluxograma da matriz curricular com a situação das disciplinas. Fonte: captura de tela do No Fluxo UnB, outubro de 2026.*

![Tela Planejar formatura, com previsão de formatura, semestres restantes, matérias críticas, créditos por semestre, aviso de optativas e grafo de disciplinas](img/noFluxo_planejarFormatura.png)

*Figura 3 — Tela “Planejar formatura”. Fonte: captura de tela do No Fluxo UnB, outubro de 2026.*

## Foco da avaliação

| Característica | O que será avaliado |
|---|---|
| **Adequação Funcional** | Com históricos sintéticos e uma matriz curricular de referência, verificar se o plano gerado inclui as disciplinas esperadas e respeita as regras curriculares consideradas no teste. |
| **Usabilidade** | Observar se estudantes conseguem gerar o plano e compreender a previsão de formatura, os semestres restantes, as matérias críticas e a distribuição das disciplinas. Registrar sucesso nas tarefas, erros e necessidade de ajuda. |
| **Segurança** | Verificar de forma não invasiva o acesso ao fluxo e o tratamento observável do histórico enviado. Usar dados sintéticos, sem tentar invadir o sistema nem acessar dados de terceiros. |

## Fora do escopo e limites

Não serão realizados testes de penetração nem testes de carga na aplicação em produção. Também não será avaliada exaustivamente a matriz de todos os cursos, a experiência em todos os dispositivos ou a qualidade das respostas de ferramentas de IA.

Os resultados funcionais valerão para os cenários e a matriz curricular testados. Os resultados de usabilidade descreverão apenas os participantes envolvidos. Verificações não invasivas de segurança não comprovam que o sistema esteja livre de vulnerabilidades.

**Premissas:** serão usados históricos sintéticos; a equipe registrará a versão/data e o ambiente dos testes; e as verificações serão realizadas somente em funcionalidades e ambientes aos quais tenha acesso autorizado.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Detalhamento inicial do escopo operacional, exclusões, limites e premissas | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |
