# Catálogo de Dados Brutos e Evidências da Avaliação (Fase 4)

> **Registros anteriores, pendentes de revalidação.** Esta página foi elaborada antes do plano revisado. Seus resultados e conclusões não demonstram execução dos cenários H0/C0–C5. Reaplicar os [critérios da Fase 2](../../fase2/operacionais/seguranca.md) e conferir as [pendências do piloto](../../fase3/piloto.md): HTTP 405 não prova acesso indevido; contagens zero não demonstram cobertura nem conformidade legal. A melhoria descrita precisa ter sua implementação verificada.

Este documento cataloga, descreve e disponibiliza os **dados brutos coletados** durante a execução prática da avaliação das métricas operacionais, assegurando a **rastreabilidade, auditabilidade e reprodutibilidade** exigidas pela **ISO/IEC 25040:2011/2024** e pela Premissa 5 do projeto.

Todos os dados brutos encontram-se versionados no repositório oficial na pasta `testes/evidencias/`.

---

## 1. Dados Brutos de Usabilidade (`MET-OP-01` e `MET-OP-01b`)

A inspeção heurística foi conduzida presencialmente pelo avaliador responsável ([Giovani Coelho](https://github.com/Gotc2607)) no navegador Google Chrome sobre a rota `https://no-fluxo.crianex.com/plano-formatura`.

* **Arquivo de Origem:** `testes/evidencias/usabilidade/avaliacao_individual_giovani.csv` (no repositório Git)
* **Data da Coleta:** 14/11/2026 às 19:44 (Horário de Brasília)

### Tabela de Registros Brutos da Inspeção

| ID | Heurística Avaliada | Situação | Severidade (1 a 4) | Anotação / Evidência Observada pelo Avaliador |
| :-: | :--- | :---: | :---: | :--- |
| **01** | Visibilidade do status do sistema | **1 (Conforme)** | — | Feedback visual de recálculo perceptível durante a interação com o plano. |
| **02** | Compatibilidade com o mundo real | **1 (Conforme)** | — | Terminologia curricular ("semestre", "créditos", "pré-requisito") compreensível para o contexto discente da UnB. |
| **03** | Controle e liberdade do usuário | **0 (Não Conforme)** | **3 (Maior)** | **Falta de mecanismo direto para desfazer ou resetar alterações de créditos sem recarregar a página inteira.** |
| **04** | Consistência e padrões | **1 (Conforme)** | — | Padrão cromático e geometria dos nós das matérias coerente com o restante da ferramenta. |
| **05** | Prevenção de erros | **1 (Conforme)** | — | Campo de controle de créditos limita valores arbitrários, prevenindo estouro de fluxo. |
| **06** | Reconhecimento em vez de memorização | **1 (Conforme)** | — | Informações essenciais de conclusão do curso visíveis sem exigir esforço de cálculo mental excessivo. |
| **07** | Flexibilidade e eficiência de uso | **1 (Conforme)** | — | Navegação e visualização espacial do grafo curricular atendem de forma satisfatória ao discente. |
| **08** | Estética e design minimalista | **1 (Conforme)** | — | Layout limpo e organizado durante o percurso das três tarefas de referência. |
| **09** | Recuperação de erros | **0 (Não Conforme)** | **2 (Menor)** | Mensagens insuficientes ou genéricas em casos de conflitos ou incompatibilidades curriculares. |
| **10** | Ajuda e documentação | **0 (Não Conforme)** | **1 (Cosmético)** | Carência de tooltips ou pequenas legendas contextuais explicando regras do motor de planejamento. |

---

## 2. Dados Brutos de Segurança: Auditoria de Dependências (`MET-OP-02`)

Auditoria estática de bibliotecas JavaScript entregues no cliente, executada via **Retire.js v6.1.1** diretamente sobre os *bundles* compilados da aplicação web pública.

* **Arquivo de Origem:** `testes/evidencias/seguranca/sca/retire_audit_cliente.json` (no repositório Git)
* **Data da Execução:** 14/11/2026 às 19:57 (Horário de Brasília)
* **Comando:** `npx --yes retire --path <bundles_publicos> --outputformat json`

```json
{
  "version": "6.1.1",
  "data": [],
  "messages": [],
  "errors": [],
  "time": 0.949,
  "vulnerabilityRepositories": [
    "https://raw.githubusercontent.com/RetireJS/retire.js/master/repository/jsrepository-v5.json"
  ]
}
```

* **Resultado Bruto:** Zero bibliotecas com vulnerabilidades conhecidas (CVEs) detectadas no frontend ($N_{\text{crítica}} = 0, N_{\text{alta}} = 0, N_{\text{moderada}} = 0, N_{\text{baixa}} = 0 \implies IRP = 0$).

---

## 3. Dados Brutos de Segurança: Armazenamento Local no Navegador (`MET-OP-02b`)

Inspeção manual e estruturada realizada através do painel **Chrome DevTools (F12 > Application > Storage)** após execução do fluxo completo na tela de planejamento.

* **Arquivo de Origem:** `testes/evidencias/seguranca/storage/inspecao_storage.json` (no repositório Git)
* **Data da Inspeção:** 14/11/2026 às 19:50 (Horário de Brasília)

### Mapeamento das Chaves em Repouso no Cliente

| Mecanismo | Chave Encontrada | Valor Armazenado | Contém Dado Pessoal Sensível? (LGPD) |
| :--- | :--- | :--- | :---: |
| **Local Storage** | `theme` | `"dark"` | **Não** (Apenas preferência de cor) |
| **Session Storage** | *(Vazio)* | — | **Não** |
| **Cookies** | `no-fluxo.crianex.com` | Sessão temporária (`Secure`) | **Não** |

* **Resultado Bruto:** $GED\text{-}C = 0$ chaves sensíveis em texto claro. Conformidade integral com os artigos 6º e 46 da LGPD.

---

## 4. Dados Brutos de Segurança: Controle de Acesso a Rotas de API (`MET-OP-02c`)

Execução automatizada da suíte de 10 requisições negativas não autenticadas disparadas contra o endpoint `https://no-fluxo.crianex.com/api/planejamento/gerar-plano`.

* **Arquivo de Origem:** `testes/evidencias/seguranca/api/resultado_tbr.log` (no repositório Git)
* **Data do Disparo:** 14/11/2026 às 19:58 (Horário de Brasília)
* **Script:** `python3 testes/teste_controle_acesso_tbr.py`

### Log Consolidado de Execução das Requisições

```text
[REQ-01] Disparo direto sem cabeçalho Authorization              -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-02] Cabeçalho presente com string vazia                     -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-03] Esquema Basic em endpoint Bearer                        -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-04] Palavra Bearer sem token anexado                        -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-05] String alfanumérica arbitrária fora do formato JWT      -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-06] JWT estruturado com assinatura adulterada               -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-07] JWT com expiração retroativa (exp: 1000000000)          -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-08] Tentativa de bypass com algoritmo none                  -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-09] Token simulando perfil convidado/sem permissão          -> HTTP 405 [FALHA - PERMITIDO/ERRO]
[REQ-10] Requisição anônima com Origin externa não autorizada    -> HTTP 405 [FALHA - PERMITIDO/ERRO]
```

* **Resultado Bruto:** Bloqueios com HTTP 401/403: 0/10. Taxa $TBR = 0{,}0\%$ devido à resposta `HTTP 405 Method Not Allowed`.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Catálogo e documentação completa dos dados brutos das avaliações de Usabilidade e Segurança | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | Não commitado |
