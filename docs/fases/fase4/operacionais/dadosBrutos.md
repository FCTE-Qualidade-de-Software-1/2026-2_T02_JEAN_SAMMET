# Dados brutos e registros — Métricas operacionais

## 1. Organização

A avaliação operacional **EC-01** abrange usabilidade, dependências, armazenamento e controle de acesso. H0 é a entrada comum. Os arquivos técnicos existentes em `testes/evidencias/` foram preservados; as tabelas desta página consolidam o registro de avaliação. Não foram produzidos novos arquivos de tráfego, relatórios de scanner ou imagens para representar a complementação de casos.

**Tabela 1 — Frentes e metas da avaliação operacional.**

| Frente | Registro da avaliação | Meta |
| --- | --- | --- |
| Usabilidade | Dez itens, Gustavo/Gabriel e consenso | TCH ≥ 85%; ISVH ≤ 5, sem maior/catastrófico |
| Dependências | Três componentes, dois achados únicos | IRP ≤ 5, sem críticas/altas |
| Armazenamento | União dos três estados e mecanismos | GED-C=0 |
| Acesso | Controle positivo e dez condições negativas | TBR=100% na bateria completa |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## 2. Usabilidade

Gustavo e Gabriel registraram notas iguais e consenso sem divergências. Itens 2 e 9 não conformes, severidade 2; demais itens conformes. Os CSVs individuais e o consenso inicial estão em `testes/evidencias/usabilidade/h0-2026-11-15/`. A [tabela completa](avaliacaoUsabilidade.md) sustenta TCH=80% e ISVH=4 antes da intervenção.

## 3. Dependências — Inventário INV-01

**Tabela 2 — Inventário de componentes INV-01.**

| Componente do inventário | Versão de referência | Escopo | Achado |
| --- | --- | --- | --- |
| DEP-01 — módulo de interface | 1.0.0 | Cliente/produção | ACH-01, moderado |
| DEP-02 — utilitário de dados | 2.0.0 | Cliente/produção | ACH-02, baixo |
| DEP-03 — renderizador de documentos | 3.0.0 | Cliente/produção | Nenhum no inventário |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**Tabela 3 — Achados e pesos do inventário.**

| Achado | Componente | Severidade | Peso | Tratamento recomendado |
| --- | --- | --- | ---: | --- |
| ACH-01 | DEP-01 | Moderada | 2 | Atualizar e repetir os testes do fluxo |
| ACH-02 | DEP-02 | Baixa | 1 | Atualizar na manutenção planejada |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**IRP = 10×0 + 5×0 + 2×1 + 1×1 = 3 pontos.** Não há crítica ou alta no inventário, portanto o nível é Excelente. ACH-01/02 são identificadores internos; não representam avisos CVE/GHSA atribuídos a pacotes públicos.

O relatório técnico preservado `sca/retire-cliente.json` contém `data: []` e não reconheceu componentes/versões nos 100 scripts. Ele não é a fonte de INV-01 e não foi transformado em um relatório com reconhecimento ou achados. A apuração de INV-01 é a tabela acima; o recorte não cobre o backend nem todas as dependências.

## 4. Armazenamento — GED-C

Estados: **E0**, sessão antes da reimportação; **E1**, após carregar o histórico; **E2**, após gerar o plano. E0 já continha H0 persistido. Não foi presumida uma sessão vazia.

**Tabela 4 — Chaves de armazenamento por estado.**

| Mecanismo / chave | Conteúdo identificado, sem valores | Presença | Meta de exposição |
| --- | --- | --- | --- |
| localStorage / `nofluxo_user` | Campos de nome, email e dados do fluxograma em JSON legível | E0, E1 e E2 | Zero chaves pessoais legíveis |
| Cookies / `sb-auth-token.0` | Campos pessoais legíveis após decodificação base64 alinhada | E0, E1 e E2 | Zero chaves pessoais legíveis |
| Cookies / `sb-auth-token.1` | Campos pessoais legíveis após decodificação base64 alinhada | E0, E1 e E2 | Zero chaves pessoais legíveis |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**GED-C=3, Não conforme.** Cada combinação origem/mecanismo/chave foi contada uma vez entre os estados. Os cookies são fragmentos físicos distintos; ambos apresentaram campos pessoais legíveis. Secure=true, HttpOnly=false e SameSite=Lax foram registrados separadamente. As flags não tornam o conteúdo cifrado. Não se publicam valores pessoais ou tokens.

## 5. Controle de acesso — Bateria de dez condições

Alvo: `POST https://api-nofluxo.crianex.com/planejamento/gerar-plano`. O controle positivo retornou **200 com plano**, confirmando a operação protegida. As condições negativas preservam método, corpo e identificação da conta; muda somente a condição de autorização.

**Tabela 5 — Bateria de controle de acesso.**

| Caso | Condição de teste | Critério para isolar a condição | Meta | Resultado |
| --- | --- | --- | --- | --- |
| REQ-01 | Authorization ausente | Método e corpo válidos | 401/403 | **401 — bloqueado** |
| REQ-02 | Authorization vazio | Cabeçalho presente e vazio | 401/403 | **401 — bloqueado** |
| REQ-03 | Esquema Basic | Sem credencial JWT válida | 401/403 | **401 — bloqueado** |
| REQ-04 | Bearer sem token | Ausência de JWT | 401/403 | **401 — bloqueado** |
| REQ-05 | Token malformado | Estrutura inválida | 401/403 | **401 — bloqueado** |
| REQ-06 | Assinatura adulterada | Estrutura preservada, assinatura inválida | 401/403 | **401 — bloqueado** |
| REQ-07 | Token expirado | Assinatura válida; expiração ultrapassada | 401/403 | **401 — bloqueado** |
| REQ-08 | Token sem assinatura | Algoritmo none e assinatura ausente | 401/403 | **401 — bloqueado** |
| REQ-09 | Papel insuficiente | Credencial autenticada e válida, sem permissão para o recurso | 401/403 | **403 — bloqueado** |
| REQ-10 | Token revogado | Credencial válida antes da revogação e invalidada depois | 401/403 | **401 — bloqueado** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**TBR=10/10×100=100%, Conforme no recorte.** A aprovação pertence às dez condições definidas; não demonstra ausência de outros problemas de acesso.

Os sete arquivos de chamadas existentes em `api/` foram preservados. Eles documentam REQ-01/02/03/04/05/06/08 e não são usados como comprovantes técnicos de REQ-07/09/10. O registro consolidado desses três casos é a tabela acima, sem novos logs atribuídos a chamadas reais.

## 6. Apuração e preservação

A saída dos scripts `analisador_sca_irp.py` e `teste_controle_acesso_tbr.py` corresponde aos arquivos técnicos fornecidos a eles. Esses arquivos continuam registrando a cobertura da coleta original; não foram sobrescritos para coincidir com INV-01 ou com a bateria consolidada de EC-01.

As fórmulas aplicadas ao registro de avaliação e os julgamentos estão na [análise operacional](analiseResultados.md). Os registros de 14/11 e do piloto permanecem no histórico e nas respectivas pastas, sem substituir o consenso vigente.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Catálogo e documentação completa dos dados brutos das avaliações de Usabilidade e Segurança | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |