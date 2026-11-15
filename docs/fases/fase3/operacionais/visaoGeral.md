# Visão geral da avaliação operacional

## 1. Escopo

A avaliação observa a interface `/plano-formatura`, os componentes cliente reconhecidos pelo scanner, o armazenamento do navegador e as operações protegidas identificadas no fluxo. Manifestos públicos podem complementar a SCA quando disponíveis. Não se presume acesso ao backend nem equivalência entre o código público e a produção.

## 2. Critérios de entrada

1. Conta de teste e ambiente registrados; autorização para os testes de API informada pelo usuário.
2. Histórico oficial autorizado carregado e conferido, com dados e forma de entrada registrados sem exposição pública.
3. Dois avaliadores de usabilidade identificados e alinhados quanto ao checklist e à severidade.
4. Ferramentas e evidências previstas por métrica. Para API, requisito, rota e chamada positiva validados.

Critérios específicos podem liberar uma frente sem liberar as demais. A exploração inicial e as pendências constam no [piloto](../piloto.md).

## 3. Critérios de conclusão

Cada medida tem coleta válida, evidência e cálculo ou uma pendência justificada. Usabilidade exige folhas individuais e consenso. Segurança exige cobertura e limitações explícitas; arquivo ausente e HTTP 405 não são resultados favoráveis nem prova de vulnerabilidade.

O julgamento conjunto segue a [Fase 2](../../fase2/operacionais/visaoGeral.md#22-regra-de-julgamento-conjunto). Na Fase 3, concluir os procedimentos e verificar sua viabilidade no piloto. Julgar resultados e executar/verificar uma melhoria pertencem à Fase 4; não confundir proposta com implementação comprovada.

## 4. Preservação

Os modelos de registro estão em `testes/modelos_coleta/`. Na coleta definitiva, criar pastas por execução em `testes/evidencias/`, com identificador, entrada/cenário e data. Não publicar dados pessoais, cookies de sessão ou tokens. Guardar registros do piloto separados da coleta formal.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Criação da visão geral do plano de avaliação operacional, critérios de entrada/saída e governança | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Revisão do escopo e dos critérios operacionais de entrada e saída | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
