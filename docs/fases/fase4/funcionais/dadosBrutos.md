# Dados Brutos e Evidências — Métricas Funcionais (Fase 4)

## 1. Origem e proteção da entrada H0

H0 é o histórico SIGAA/UnB fornecido e autorizado pelo usuário, emitido em 15/11/2026 e associado à matriz 6360/1 — 2017.1. O PDF original permanece fora do repositório. A cópia `testes/evidencias/funcionais/H0_sanitizado.pdf` contém redaction dos identificadores pessoais; os dados normalizados estão em `testes/referencias/h0_sanitizado.json` e `testes/evidencias/funcionais/h0_*.csv`.

A linha de base usada é de 41 componentes com status (33 aprovados, 7 matriculados e 1 trancado), cinco equivalências concluídas, duas em andamento e 14 disciplinas obrigatórias pendentes (1.050h). Duas cadeias de seletividade e ENADE permanecem separados do denominador de CDO.

## 2. Evidências da execução de 15/11/2026

As capturas disponíveis estão em `testes/evidencias/funcionais/execucao-2026-11-15/`:

| Caso | Evidência(s) | Observação registrada |
|---|---|---|
| CT-01 | `CT-01-FGA0170.png`, `CT-01-TCC1e2.png` | FGA0170 antecede FGA0211; FGA0009 (semestre 9) antecede FGA0011 (semestre 10). |
| CT-02 | `CT-02-TED2-PED2.png` | FGA0074 no semestre 7 e FGA0072 no semestre 8: co-requisito violado. |
| CT-03 | `CT-03-FGA0206.png` | 13/14 obrigatórias; FGA0206 omitida. |
| CT-04 | `CT-04-C0-01-importacao.png` | Processamento concluído; 39 obrigatórias, 25 concluídas, 14 pendentes e 7 optativas. |
| CT-05 | `CT-05-Equivalencias.png` | FGA0147 e FGA0172 exibidas como equivalentes/concluídas; |
| CT-06 | `CT-06-Antes.png`, `CT-06-Depois.png`, e capturas de carga CT-07 | 240h, 360h e 480h foram relatadas como não conformes; C3/C4 inconclusivos por ausência de mudança visual identificável. |
| CT-07 | `CT-07-06-240h.png`, `CT-07-06-360h.png` | 300h no semestre 9 para alvo 240h; 390h para alvo 360h. |

**Captura pendente:** `CT-07-06-480h.png` não foi fornecida. A composição de 540h no semestre 9 (210h + 90h + quatro componentes de 60h) foi registrada somente como observação relatada pelo avaliador em `testes/evidencias/funcionais/execucao-2026-11-15/LEMBRETE-CT-07-06-480h.md`. Essa nota não é uma captura de tela e deve ser substituída/complementada pela imagem quando ela for adicionada.

## 3. Arquivos de dados brutos

| Arquivo | Conteúdo |
|---|---|
| `testes/evidencias/funcionais/execucoes.csv` | Tentativa de pré-condição antiga e resumo das execuções CT-01 a CT-07 de 15/11/2026. |
| `testes/evidencias/funcionais/verificacoes_funcionais.csv` | 68 verificações atômicas: pré-requisitos, co-requisitos, 14 obrigatórias, 41 status, duas equivalências visualmente confirmadas, opções do onboarding e cargas semestrais. |
| `testes/evidencias/funcionais/h0_registros.csv` | 41 componentes acadêmicos da entrada H0. |
| `testes/evidencias/funcionais/h0_obrigacoes_pendentes.csv` | 14 disciplinas obrigatórias, duas cadeias de seletividade e ENADE. |
| `testes/evidencias/funcionais/h0_equivalencias.csv` | Cinco equivalências concluídas e duas em andamento. |
| `testes/referencias/h0_sanitizado.json` | Inventário normalizado de H0 usado pelo processador. |
| `testes/referencias/estrutura_6360_1.json` | Estrutura curricular de referência 6360/1 restaurada do histórico Git incluído no pacote. |

Os campos de ambiente que não foram informados (hora/fuso, navegador, sistema, viewport, zoom e versão do produto) ficaram sem preenchimento. O dia 15/11/2026 vem do diretório da execução; não foi inventado horário.

## 4. Reprocessamento

Na raiz do repositório:

```bash
python3 scripts/metricas_funcionais.py
python3 scripts/metricas_funcionais.py --json
python3 -m unittest testes.teste_metricas_funcionais testes.teste_h0_sanitizado
```

O processador emite percentuais somente com cobertura suficiente. Para CT-03, CT-04 e CT-05, os universos de referência continuam sendo 14, 41 e 7; por isso, CT-05 permanece sem percentual final enquanto houver somente 2/7 relações verificadas.

## 5. Limitações e rastreabilidade

- A execução atual foi informada pelo avaliador; o registro de falha DNS em `tentativa_acesso_aplicacao.log` corresponde a uma tentativa anterior do ambiente de apoio e deve ser mantido apenas como histórico, não como conclusão sobre a execução do usuário.
- A relação FGA0009→FGA0011 foi observada na interface e relatada como respeitada, mas a fonte curricular oficial e a vigência ainda precisam ser anexadas.
- A falta de `CT-07-06-480h.png` está explícita no lembrete e nas linhas correspondentes dos CSVs.
- Para 240h/360h, a não conformidade registrada é em relação ao alvo do cenário; as cargas de 300h/390h ficam dentro da faixa global da matriz (240–480h). Para 480h, 540h supera também o máximo global.
- Oferta/calendário por período letivo não foi verificada.

## 6. Privacidade

Não versionar o PDF original, nome, matrícula, CPF, nascimento, documento, índices acadêmicos, credenciais, cookies ou tokens. As capturas devem permanecer restritas aos elementos necessários e ser sanitizadas caso revelem novos identificadores.

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação dos dados brutos e evidências da avaliação funcional | 15/11/2026 | [dcfdb1a](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/dcfdb1a07e1511a2ac831844012889753ad837d4)  |
