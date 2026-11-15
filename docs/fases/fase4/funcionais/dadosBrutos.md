# Dados Brutos e Evidências — Métricas Funcionais

As capturas recuperadas estão em [Execução anterior](execucaoAnterior.md), com entrada e limites identificados. Não preenchem os resultados de H0 automaticamente.

## 1. Entrada H0

O histórico oficial autorizado foi normalizado em `testes/referencias/h0_sanitizado.json`, sem nome, matrícula, notas, índices ou credenciais. O PDF original fica fora do repositório.

H0 contém **44 registros acadêmicos: 37 aprovados e 7 matriculados**, correspondentes a 42 códigos distintos. DSC0172 e FGA0413 aparecem em dois períodos diferentes e são preservadas como ocorrências separadas. Não há registro atual com status Trancado na tabela de componentes cursados/cursando.

São **seis equivalências concluídas** (FGA0302→FGA0161, FGA0146→FGA0147, FGA0307→FGA0184, FGA0312→FGA0138, FGA0313→FGA0172 e FGA0314→FGA0238) e **duas em andamento** (FGA0303→FGA0150 e FGA0315→FGA0278).

## 2. Arquivos em `testes/evidencias/funcionais/`

| Arquivo | Finalidade |
|---|---|
| `h0_registros.csv` | 44 registros com código, período e status |
| `h0_obrigacoes_pendentes.csv` | 15 obrigatórias e três exigências separadas: duas cadeias e ENADE |
| `h0_equivalencias.csv` | Seis relações concluídas e duas em andamento |
| `unidades_esperadas_h0.csv` | Checklist de 15 disciplinas, 44 registros e oito relações; não contém resultado do produto |
| `execucoes.csv` | Ambiente, entrada, configuração e resultado de cada execução |
| `verificacoes_funcionais.csv` | Comparações efetivas que sustentam os cálculos |

## 3. Estado da coleta

Os arquivos de execução e verificação estão preparados, sem medições definitivas para H0. A transcrição do histórico não representa aprovação de métricas nem prova de importação correta. Percentuais dependem de observar o produto.

Guardar capturas por execução, sem dados pessoais, com caso, entrada, cenário e regra. Totais da importação não substituem conferência individual.

## 4. Processamento

```bash
python3 scripts/metricas_funcionais.py
python3 scripts/metricas_funcionais.py --json
```

Os universos de CT-03/04/05 são 15/44/8. Sem comparação observada, numeradores e percentuais permanecem desconhecidos.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação dos dados brutos e evidências da avaliação funcional | 15/11 | [dcfdb1a](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/dcfdb1a07e1511a2ac831844012889753ad837d4)  |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
