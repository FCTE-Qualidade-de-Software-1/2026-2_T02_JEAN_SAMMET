# Referências para os testes funcionais

## 1. Matriz de referência

Foi conferida a estrutura **6360/1 — 2017.1**, no [SIGAA público](https://sigaa.unb.br/sigaa/public/curso/curriculo.jsf?id=414924&lc=pt_BR), em 15/11. Na lista, escolher 6360/1 e **Visualizar Estrutura Curricular**. A matriz estar inativa para novos ingressos não invalida seu uso como recorte da avaliação.

| Regra | Valor conferido |
|---|---|
| Carga total mínima | 3.480h |
| Obrigatórias | 2.580h, distribuídas em 39 componentes |
| Optativas mínimas | 900h |
| Limites por período | Mínimo de 240h e máximo de 480h |
| Componentes eletivos | Máximo de 360h |

A relação foi conferida com o relatório oficial fornecido pelo usuário, emitido em 15/11. A transcrição estruturada e o hash desse relatório ficam em `testes/referencias/estrutura_6360_1.json`. A lista de obrigatórias não inclui as exigências de cadeias de seletividade nem substitui as horas optativas: a CDO será julgada apenas no recorte declarado.

## 2. Regras consultadas no SIGAA

Nos detalhes da matriz, abrir o nível e selecionar **Visualizar Detalhes do Componente**. O endereço do resumo depende da sessão; usar o código abaixo para repetir a consulta.

| Componente | Regra observada | Uso no teste |
|---|---|---|
| FGA0211 — Redes | Exige FGA0170; pré-requisito ativo desde 01/08/2019. | CT-01 e comparação de status em CT-04 |
| MAT0026 — Cálculo 2 | Exige MAT0025 ou MAT0024; expressão ativa desde 07/11/2021. | CT-01, cobrindo uma relação alternativa |
| MAT0026 — Cálculo 2 | MAT0138 consta como equivalência ativa desde 07/11/2021. | CT-05: conferir aplicação à matriz e ao período antes da coleta |
| IFD0173 — Física 1 Experimental | Sem pré/co-requisito exibido; há equivalências cadastradas. | Não presumir que Física 1 seja seu co-requisito |

Essas consultas verificam exemplos, não todos os pré/co-requisitos do curso. Preservar captura ou transcrição dos campos e da vigência de cada regra usada na coleta formal. A posição da disciplina no fluxograma não substitui a regra oficial.

## 3. Lacunas

- **Co-requisitos:** identificar um par aplicável antes de executar CT-02. Ausência nos exemplos consultados não prova ausência em toda a matriz.
- **Equivalências:** conferir exceções específicas da matriz e vigência; não presumir equivalência transitiva.
- **Oferta e calendário:** registrar o período real da coleta e a oferta oficial. Sem isso, a parte correspondente de CT-07 fica pendente.
- **Onboarding:** a interface mostra carga sugerida e objetivo; o efeito algorítmico exato de trabalho e objetivo ainda precisa de requisito identificável.
- **Optativas:** conferir apenas as selecionadas para o cenário. As demais ficam fora da cobertura declarada.

O repositório de referência e o commit `87b5475` não puderam ser recuperados por consulta pública nesta preparação. Isso não comprova remoção definitiva; as conclusões atuais não dependem de suposta inspeção desse código.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das fontes curriculares e das pendências por regra | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
