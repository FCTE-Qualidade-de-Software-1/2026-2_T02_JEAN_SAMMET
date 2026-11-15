# Cronograma e riscos

## 1. Sequência proposta

As horas abaixo são estimativas de planejamento, não esforço já realizado. As datas serão associadas ao prazo oficial confirmado da E2; há divergência anterior entre Milestone e burndown que precisa ser resolvida.

| Ordem | Atividade | Dependência | Responsável | Esforço estimado |
|---|---|---|---|---|
| 1 | Conferir fontes, perfis e entrada no site | — | Gustavo, proposta a confirmar | 2h |
| 2 | Concluir piloto sintético e ajustar roteiro | 1 | Gustavo, proposta a confirmar | 2h |
| 3 | Executar CT-01 a CT-07 nos casos liberados | 2 e fontes de cada CT | Frente funcional, nomes a definir | 4h |
| 4 | Duas inspeções heurísticas e consenso | 2 | Dois avaliadores a definir; mediação proposta: Giovani | 4h |
| 5 | SCA, storage e API válida | 2 e pré-condições por método | Giovani, conforme plano anterior; confirmar | 4h |
| 6 | Consolidar dados e responder GQM | 3–5 | Equipe | 3h |
| 7 | Executar e verificar melhoria; atualizar artigo | 6 | Equipe | 4h |
| **Total** | | | | **23h** |

As atividades 3–7 são da Fase 4. Registrar horas reais e decisões no PSM/CID durante a execução. Atribuições propostas não significam que os integrantes já aceitaram as tarefas.

## 2. Riscos e contingências

| Risco | Tratamento |
|---|---|
| Site indisponível ou automação interrompida | Registrar a interrupção, tentar novamente depois e manter o caso inconclusivo. Não trocar por build local sem identificar a nova versão e o ambiente. |
| Regra curricular ausente | Manter o caso pendente; não usar o comportamento do produto como única referência do resultado correto. |
| Mudança na produção | Separar execuções por data/versão verificável; preservar a evidência observada. |
| Perfil não aceito pelo importador | Validar preenchimento manual ou preparar PDF totalmente sintético; não renomear JSON como PDF. |
| Divergência de severidade | Comparar evidências e justificar consenso; não descartar folhas individuais. |
| Scanner ou script sem dados válidos | Corrigir instrumento ou apurar manualmente com conferência. Ausência não equivale a zero. |
| Dados pessoais em evidência | Sanitizar antes de versionar; não publicar histórico pessoal nem credenciais. |

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração do cronograma em 5 etapas, cálculo de esforço, grafo de precedências e matriz de riscos operacionais | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Revisão da sequência, esforço e contingências sem pressupor execução | 15/11 | Não commitado |
