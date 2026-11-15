# Evidências brutas — Adequação Funcional (Fase 4)

Este diretório reúne H0 sanitizado, dados normalizados e registros da execução funcional informada para 15/11/2026.

## Estado da coleta

- H0 é usado apenas em forma sanitizada/normalizada. O histórico original e seus identificadores pessoais permanecem fora do repositório.
- `execucoes.csv` mantém o registro histórico de pré-checagem DNS e adiciona o resumo das observações de CT-01 a CT-07 comunicadas pelo avaliador.
- `verificacoes_funcionais.csv` contém 74 linhas de verificação. A execução não deve ser confundida com a pré-checagem DNS anterior, que não alcançou o produto.
- As capturas de CT-01 a CT-06 estão no subdiretório `execucao-2026-11-15/`, bem como as imagens CT-07 de 240h e 360h.
- A captura `CT-07-06-480h.png` não foi anexada. O arquivo `execucao-2026-11-15/LEMBRETE-CT-07-06-480h.md` documenta o local e o resultado relatado (540h), sem fingir que a imagem existe.

## Resultados principais

- CT-01: duas sequências observadas em ordem válida; a fonte oficial da relação FGA0009→FGA0011 ainda precisa ser anexada.
- CT-02: co-requisito FGA0072/FGA0074 violado (semestres 7 e 8).
- CT-03: 13/14 obrigatórias presentes; FGA0206 omitida.
- CT-04: importação concluída; resumo 39 obrigatórias, 25 concluídas, 14 pendentes e 7 optativas; dados considerados compatíveis pelo avaliador.
- CT-05: as sete relações de H0 foram contabilizadas como corretas (TAE=0/7=0%). A captura mostra diretamente FGA0147 e FGA0172; as outras cinco classificações seguem a decisão expressa do avaliador, registrada em `execucao-2026-11-15/CT-05-criterio-7de7.md`.
- CT-06: três variantes de carga não conformes; C3/C4 inconclusivos por ausência de mudança visual identificável.
- CT-07: os três alvos de carga foram excedidos no semestre 9; a captura de 480h continua pendente.

## Como reprocessar

Na raiz do repositório:

```bash
python3 scripts/metricas_funcionais.py
python3 scripts/metricas_funcionais.py --json
python3 -m unittest testes.teste_metricas_funcionais testes.teste_h0_sanitizado
```

O processador calcula MET-FUN-05 com cobertura 7/7: `NEI=0`, `NRE=7` e `TAE=0%`. Cinco das classificações conformes não têm captura individual e foram lançadas conforme decisão do avaliador; consultar a nota CT-05. Para 240h/360h, a divergência registrada é em relação ao alvo configurado; 300h/390h ainda estão dentro da faixa global da matriz (240–480h). A carga informada de 540h excede também o máximo global.

## Privacidade

Não adicionar PDF original, nome, matrícula, CPF, nascimento, documento, credenciais, cookies ou tokens. Revisar/sanitizar capturas antes de versioná-las.
