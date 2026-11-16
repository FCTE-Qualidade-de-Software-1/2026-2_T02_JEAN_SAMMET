# Dados brutos — Avaliação funcional de H0

## 1. Entrada e coleta

H0 é o histórico oficial autorizado da matriz **6360/1 — 2017.1**. A referência contém **44 registros** (37 APR e 7 MATR), **15 obrigatórias pendentes** e **8 equivalências** (6 concluídas e 2 em andamento). Código e período identificam cada ocorrência; DSC0172/FGA0413 em períodos diferentes foram preservadas.

A coleta utiliza a conta de teste e o histórico autorizados e fica disponível para revisão da equipe. Foram executados C0–C5 e o caso de seleção explícita do par de CT-02, mantendo os registros acadêmicos de H0. Os planos foram observados na interface e nas respostas reais do serviço; os dados importados foram comparados por unidade. PDF, identificadores, notas, tokens e payload acadêmico completo não foram publicados.

## 2. Arquivos da execução

Pasta: `testes/evidencias/funcionais/execucao-h0-2026-11-15/`.

| Registro | Conteúdo |
|---|---|
| `c0-plano.json` a `c5-8-plano.json` | Respostas sanitizadas por cenário; códigos, cargas, reservas e semestres |
| `ct02-plano-interface.json` e `ct02-grafo.txt` | Par selecionado pelo recurso de optativas; posição real dos cartões |
| `h0-importado.json` | Registros reconhecidos e relações de equivalência, sem identificação |
| `fluxograma-status.txt` | Estados exibidos pelos cartões das disciplinas |
| `politica-projecao.txt` | Distinção entre curso atual e projeção condicionada à aprovação |
| `ambiente-coleta.json` | Condições observadas; servidor sem versão identificada |
| `resultado-metricas.json` | Saída do processador, sem preencher ausências com zero |

Em `testes/evidencias/funcionais/`, os arquivos `execucoes.csv` e `verificacoes_funcionais.csv` registram contexto e **102 comparações**: 1 pré-requisito, 2 co-requisitos, 15 pendências, 44 registros, 8 equivalências, 7 expectativas de onboarding e 25 verificações/restrições. Destas, duas expectativas e dois tipos de restrição permanecem pendentes de especificação/fonte.

## 3. Como as evidências sustentam a avaliação

| Caso | Conferência realizada | Evidência principal | Meta | Resultado observado |
|---|---|---|---|---|
| CT-01 | Ordem de FGA0170 e FGA0211, distinguindo matrícula e projeção | `c0-plano.json` e `politica-projecao.txt` | TVP = 0%: nenhuma relação violada | Dependente em 2027.1 após o semestre em curso 2026.2 |
| CT-02 | Posição das duas optativas selecionadas no grafo | `ct02-plano-interface.json`, `ct02-grafo.txt` e captura na análise | TVC = 0%: nenhuma relação violada | FGA0072 e FGA0074 em 2027.1 |
| CT-03 | Cruzamento das 15 pendências esperadas com o plano completo | Referência sanitizada de H0, `c0-plano.json` e CSV de verificações | CDO = 100%: 15/15 obrigatórias contempladas | 14 contempladas; FGA0206 ausente |
| CT-04 | Comparação individual de código/período/status | `h0-importado.json`, `fluxograma-status.txt` e CSV de verificações | TDH = 0%: nenhuma divergência nos 44 registros | 44 registros sem divergência confirmada |
| CT-05 | Conferência de destino, status e efeito das equivalências | Referência de H0, dados importados e estados da interface | TAE = 0%: nenhuma aplicação incorreta nas oito relações | Seis concluídas e duas em andamento tratadas corretamente |
| CT-06 | Comparação de configurações mantendo H0 fixo | Planos C1, C2, C3, C4 e variantes C5 | COO = 100% das expectativas previamente especificadas | Cinco expectativas de carga atendidas; duas sem efeito obrigatório especificado |
| CT-07 | Soma das cargas por semestre, incluindo reservas | Planos C0–C5 e CSV de verificações | TVS = 0% por tipo; máximo curricular ≤ 480h por semestre | Nenhum excesso de 480h nas 23 unidades; demais tipos pendentes |

As evidências têm funções complementares: a referência define o esperado, as respostas e a interface registram o observado, e o CSV identifica a comparação que entra no cálculo. As capturas facilitam a leitura, mas não substituem a conferência individual. Não há uma captura exclusiva para cada uma das 102 linhas.

## 4. Regras de comparação

- **CT-03:** o semestre em curso integra o plano observado, mantendo MATR. Cadeias e ENADE ficam fora das 15 disciplinas. FGA0206 está ausente do plano-base e de `materiasNaoAlocadas`.
- **CT-04:** equivalentes podem ser representados pelo código de destino oficial. Essa normalização é aplicada antes da comparação de período/status; a unidade de referência continua sendo o registro original. Não confundir representação válida com perda de ocorrência.
- **CT-05:** conferidos estado do destino, relação oficial, efeito nas pendências e ausência de duplicação; as duas equivalentes matriculadas não aparecem como aprovadas.
- **CT-06/07:** carga sugerida não foi presumida como teto rígido. As reservas explícitas de optativas entram na soma de carga futura.

Os registros de [Execução anterior](execucaoAnterior.md) continuam preservados, sem substituir a coleta de H0.

## 5. Reprocessamento

```bash
python3 scripts/metricas_funcionais.py
python3 scripts/metricas_funcionais.py --json
python3 -m unittest discover -s testes -t . -p 'teste_*.py'
```

O processador exige uma comparação válida para cada unidade de CT-03/04/05. Os percentuais de CT-06/07 devem ser lidos junto da cobertura, conforme a [análise](analiseResultados.md).

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação dos dados brutos e evidências da avaliação funcional | 15/11 | [dcfdb1a](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/dcfdb1a07e1511a2ac831844012889753ad837d4)  |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | Não commitado |
