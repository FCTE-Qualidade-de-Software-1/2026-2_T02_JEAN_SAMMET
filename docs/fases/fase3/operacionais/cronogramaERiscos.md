# Cronograma e riscos

## 1. Cronograma da entrega

O prazo da E2 é **22/11**, conforme alteração da professora informada por Gustavo. O burndown já utiliza essa data. O vencimento do Milestone no GitHub deve acompanhar o mesmo prazo.

As datas intermediárias abaixo são metas de execução propostas. As horas são estimativas; não representam esforço realizado.

| Data-alvo | Atividade | Dependência | Responsável | Estimativa |
|---|---|---|---|---|
| 15/11 | Conferir fontes, H0 e cenários | — | Gustavo | 2h |
| 15/11 | Piloto de viabilidade concluído e roteiro ajustado | Conferência da entrada | Gustavo; Giovani nos instrumentos de segurança | 2h |
| 16–18/11 | Executar CT-01 a CT-07 nos casos liberados | Piloto e fontes de cada CT | Gabriel | 4h |
| 16–18/11 | Duas inspeções heurísticas e consenso | Piloto; dupla identificada | Gustavo e Gabriel | 4h |
| 16–18/11 | SCA, storage e API | Pré-condições de cada método | Giovani | 4h |
| 19/11 | Consolidar dados e responder GQM | Coletas válidas | Gustavo, com revisão dos responsáveis | 3h |
| 20–21/11 | Executar/verificar melhoria e atualizar artigo | Análise dos resultados | Equipe; consolidação por Gustavo | 4h |
| 22/11 | Revisar e entregar | Evidências, análise e artigo revisados | Equipe | Incluída nas atividades anteriores |
| **Total** | | | | **23h** |

Gustavo informou aproximadamente **7h já realizadas** na preparação da Fase 3. O apontamento parcial está no [PSM — Recursos e Custos](../../../gestaoProjeto/painel.md#esforco-adicional-fase-3-em-andamento), separado das estimativas e dos registros anteriores. Não somar essas 7h às 23h para obter uma previsão: as grandezas descrevem esforço realizado e planejado, respectivamente.

Gabriel nos testes funcionais, Giovani na segurança e Gustavo na revisão/consolidação foram confirmados pelo responsável pelo planejamento. A dupla de usabilidade será Gustavo e Gabriel, em inspeções independentes antes do consenso. As coletas, o julgamento e a melhoria pertencem à Fase 4; registrar horas reais e decisões no PSM/CID durante sua execução.

## 2. Riscos e contingências

| Risco | Tratamento |
|---|---|
| Site indisponível ou automação interrompida | Registrar a interrupção, tentar novamente depois e manter o caso inconclusivo. Não trocar por build local sem identificar a nova versão e o ambiente. |
| Regra curricular ausente | Manter o caso pendente; não usar o comportamento do produto como única referência do resultado correto. |
| Mudança na produção | Separar execuções por data/versão verificável; preservar a evidência observada. |
| Perfil não aceito pelo importador | Usar histórico oficial autorizado; só variar disciplinas por edição suportada pelo site, se confirmada. Declarar os casos sem entrada viável. |
| Divergência de severidade | Comparar evidências e justificar consenso; não descartar folhas individuais. |
| Scanner ou script sem dados válidos | Corrigir instrumento ou apurar manualmente com conferência. Ausência não equivale a zero. |
| Dados pessoais em evidência | Sanitizar antes de versionar; não publicar histórico pessoal nem credenciais. |

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração do cronograma em 5 etapas, cálculo de esforço, grafo de precedências e matriz de riscos operacionais | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Revisão da sequência, esforço e contingências sem pressupor execução | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento do prazo de 22/11, responsáveis e metas de execução | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
