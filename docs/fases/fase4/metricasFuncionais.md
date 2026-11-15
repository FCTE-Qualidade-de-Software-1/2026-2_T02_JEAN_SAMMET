# Execução e Conclusão da Avaliação — Métricas Funcionais (Fase 4)

Esta página centraliza a avaliação de **Adequação Funcional** de *Planejar formatura* do No Fluxo UnB, conforme o [GQM da Fase 2](../fase2/funcionais/GQM.md) e o [roteiro da Fase 3](../fase3/funcionais/roteiro.md).

## 1. Documentação da Fase 4

| Página | Conteúdo |
|---|---|
| [Dados brutos e evidências](funcionais/dadosBrutos.md) | H0 sanitizado, capturas, CSVs e limitações da coleta. |
| [Análise dos resultados e julgamento](funcionais/analiseResultados.md) | Cálculos, critérios, respostas GQM e julgamento das hipóteses. |

## 2. Resultado das métricas funcionais

| Métrica | Fórmula aplicada | Resultado | Meta | Julgamento |
|---|---|---:|---:|---|
| `MET-FUN-01` — TVP | 0/2 | **0,00%** | 0% | Conforme, com ressalva de fonte para a relação FGA0009→FGA0011 |
| `MET-FUN-02` — TVC | 2/2 | **100,00%** | 0% | Não conforme |
| `MET-FUN-03` — CDO | 13/14 | **92,86%** | 100% | Não conforme; FGA0206 omitida |
| `MET-FUN-04` — TDH | 0/41 | **0,00%** | 0% | Conforme |
| `MET-FUN-05` — TAE | 7/7 | **100,00%** | 0% | Conforme |
| `MET-FUN-06` — COO | 0/3 | **0,00%** | 100% | Não conforme; C3/C4 inconclusivos |
| `MET-FUN-07` — TVS | 3/3 | **100,00%** | 0% por tipo | Não conforme para o alvo de carga do cenário |

## 3. Pontos de atenção

- CT-02: FGA0074 (semestre 7) e FGA0072 (semestre 8) violam o co-requisito recíproco.
- CT-03: 13 das 14 obrigatórias pendentes foram contempladas; FGA0206 ficou de fora.
- CT-06/CT-07: as variantes de 240h, 360h e 480h divergiram dos alvos. As cargas reportadas no semestre 9 foram 300h, 390h e 540h. A captura de 480h está pendente.
- C3 (trabalho/estágio) e C4 (velocidade/equilíbrio) permanecem inconclusivos porque não houve mudança visual identificável e não há efeito algorítmico suficientemente especificado.

## 4. Processamento reproduzível

```bash
python3 scripts/metricas_funcionais.py
python3 scripts/metricas_funcionais.py --json
python3 -m unittest testes.teste_metricas_funcionais testes.teste_h0_sanitizado
```

## 5. Conclusão

A execução funcional foi reportada para CT-01 a CT-07. Há resultados conformes em pré-requisitos (nos pares observados) e tratamento do histórico, e não conformidades em co-requisitos, cobertura de obrigatórias e cargas-alvo do planejamento. As opções de trabalho/estágio e velocidade/equilíbrio não puderam ser julgadas.

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação dos resultados de CT-01 a CT-07 | 15/11/2026 | [f469332](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f4693325fd9642696269942bb29aed671f0d8778) |
