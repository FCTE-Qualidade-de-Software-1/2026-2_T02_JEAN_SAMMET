# Encaminhamento de melhoria

Os achados atuais orientam as prioridades abaixo. **Nenhuma alteração no produto foi implementada ou verificada nesta etapa.** Os passos realizados foram coleta e apuração; executar e comparar uma melhoria exige uma versão identificada do produto.

| Prioridade proposta | Achado | Verificação necessária após alteração |
|---|---|---|
| Revisar persistência de dados no cliente | GED-C=3, com campos pessoais em localStorage e cookies codificados | Repetir os três estados, verificar chaves/conteúdo e efeitos funcionais sem publicar valores |
| Corrigir completude do planejamento | FGA0206 omitida em H0; CDO=14/15 | Repetir CT-03 e casos de pré-requisitos, garantindo cobertura sem regressões |
| Melhorar explicações de termos e validação de créditos | Itens 2 e 9 confirmados no consenso da equipe | Repetir T2/T3 e comparar TCH/ISVH após a alteração |

## Critérios para verificar as melhorias

**Persistência de dados:** identificar quais informações precisam permanecer no cliente e por quanto tempo. Depois da alteração, repetir os mesmos três estados e apurar GED-C, verificando também se importação, sessão e geração do plano continuam operáveis. A redução da contagem só demonstra melhoria se mantiver a funcionalidade e respeitar o critério de dados legíveis definido na Fase 2.

**Completude curricular:** confrontar novamente as 15 obrigatórias de H0 com o plano completo. A meta é CDO=100%, com FGA0206 contemplada conforme a regra aplicável e sem retirar outras obrigatórias ou gerar duplicações. Uma nova restrição identificada deve ser documentada e julgada, não usada para excluir a disciplina sem justificativa.

**Clareza da interface:** acrescentar explicação acessível dos termos críticas/estratégicas e informar a faixa permitida ao ajustar créditos inválidos. Gustavo e Gabriel devem repetir T2/T3 e consolidar o checklist, comparando TCH/ISVH antes e depois. Uma melhora é demonstrada pela nova inspeção; ainda não há resultado posterior à alteração.

## Situação da proposta

As evidências atuais definem a linha de base. A próxima execução deve identificar a versão alterada, preservar o mesmo histórico e registrar o que mudou. Até isso ocorrer, não se afirma que as propostas foram implementadas nem que elevaram os indicadores.

A proposta anterior de botão de reversão fica no [histórico](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/blob/7a74d9e0809e91d60a36a88559b357bfe171f37e/docs/fases/fase4/operacionais/acaoMelhoria.md). Na inspeção atual foi possível restaurar a carga sem recarregar; a prioridade deve seguir os resultados consolidados da equipe.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da ação de melhoria de usabilidade, prototipação em SvelteKit e projeção de impacto nas métricas | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Detalhamento dos critérios de verificação das melhorias propostas | 15/11 | Não commitado |
