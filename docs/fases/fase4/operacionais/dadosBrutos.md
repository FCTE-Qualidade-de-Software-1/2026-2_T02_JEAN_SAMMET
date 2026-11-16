# Dados brutos — Avaliação operacional

## 1. Origem e identificação

Coleta com H0 na conta de teste autorizada. Os arquivos sanitizados ficam em `testes/evidencias/seguranca/execucao-h0-2026-11-15/`, com horário UTC por estado/chamada. A leitura de data local usa America/Sao_Paulo. Não foram publicados tokens, valores pessoais, payload acadêmico ou credenciais.

| Frente | Evidência | Cobertura |
|---|---|---|
| SCA | `sca/retire-cliente.json`, inventário e `sca.json` | 100 scripts observados; nenhum componente/versão reconhecido pelo scanner |
| Storage | Três JSONs em `storage/` e `resultado-ged.json` | localStorage, sessionStorage e cookies; união por chave |
| API | `api/plano.json`, controle positivo, sete JSONs de chamadas e `tbr.json` | Dez casos previstos; sete executados com condição validada |
| Usabilidade | [Avaliação da equipe](avaliacaoUsabilidade.md), três CSVs e registro de origem | Dez itens por avaliador e consenso; resultados confirmados por Gustavo |

## 2. Armazenamento

E0 é a sessão inicial **já contendo H0**, antes de reimportar o mesmo documento. E1 foi registrado após a importação; E2, após gerar o plano. Não houve limpeza de storage para fabricar um estado vazio.

| Mecanismo / chave | Conteúdo identificado, sem valores | Presença |
|---|---|---|
| localStorage / `nofluxo_user` | Campos de nome, email e dados do fluxograma em JSON legível | E0, E1 e E2 |
| Cookies / `sb-auth-token.0` | Campos pessoais legíveis após decodificação base64 alinhada | E0, E1 e E2 |
| Cookies / `sb-auth-token.1` | Campos pessoais legíveis após decodificação base64 alinhada | E0, E1 e E2 |

A união tem **três chaves**, contadas uma vez entre os estados. Os cookies são fragmentos físicos distintos e ambos apresentaram campos pessoais legíveis. Secure=true, HttpOnly=false e SameSite=Lax foram registrados separadamente; flags de cookie não demonstram cifragem. Verificadores de fluxo e chaves de navegação sem dado pessoal identificado ficaram fora do numerador.

## 3. Acesso à API

Alvo real: `POST https://api-nofluxo.crianex.com/planejamento/gerar-plano`. Controle positivo: **200**, com plano confirmado. Método, corpo e User-ID foram preservados nos testes; somente a condição de Authorization foi alterada. O hash do payload consta nas evidências.

| Caso | Condição | Meta de resposta | HTTP observado |
|---|---|---|---|
| REQ-01 | Authorization ausente | 401 ou 403 — bloquear a chamada | 401 |
| REQ-02 | Authorization vazio | 401 ou 403 — bloquear a chamada | 401 |
| REQ-03 | Basic sem JWT | 401 ou 403 — bloquear a chamada | 401 |
| REQ-04 | Bearer sem token | 401 ou 403 — bloquear a chamada | 401 |
| REQ-05 | Token malformado | 401 ou 403 — bloquear a chamada | 401 |
| REQ-06 | JWT com assinatura adulterada | 401 ou 403 — bloquear a chamada | 401 |
| REQ-08 | JWT sem assinatura, alg none | 401 ou 403 — bloquear a chamada | 401 |

REQ-07 (expirado com assinatura válida), REQ-09 (papel insuficiente) e REQ-10 (revogado) não foram executados: faltam credenciais que isolem essas condições. Não foram substituídos por assinaturas falsas e apresentados como testes equivalentes.

## 4. Usabilidade e registros anteriores

Gustavo e Gabriel registraram oito itens conformes e dois problemas menores, nos itens 2 e 9, sem divergências no consenso. Os resultados individuais e consolidados estão em `testes/evidencias/usabilidade/h0-2026-11-15/`, com identificação da origem em `origem.md`. A [avaliação de usabilidade](avaliacaoUsabilidade.md) reúne a tabela completa e o cálculo de TCH e ISVH.

Os registros de 14/11 permanecem nos diretórios anteriores e no [histórico Git](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/tree/7a74d9e0809e91d60a36a88559b357bfe171f37e/testes/evidencias). Não foram reaproveitados como medições de H0.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Catálogo e documentação completa dos dados brutos das avaliações de Usabilidade e Segurança | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento dos registros à avaliação consolidada da equipe | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | Não commitado |
