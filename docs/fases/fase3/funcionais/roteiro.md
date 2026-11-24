# Roteiro de avaliação funcional

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

Aplicar as [métricas da Fase 2](../../fase2/funcionais/GQM.md) ao histórico oficial autorizado **H0**. O original fica fora do repositório; os dados normalizados estão em `testes/referencias/h0_sanitizado.json`.

## 1. Entrada e cenários

H0 contém **44 registros acadêmicos: 37 aprovados e 7 matriculados**, correspondentes a 42 códigos distintos. DSC0172 e FGA0413 aparecem em dois períodos diferentes e são preservadas como ocorrências separadas. Não há registro atual com status Trancado na tabela de componentes cursados/cursando.

São **seis equivalências concluídas** (FGA0302→FGA0161, FGA0146→FGA0147, FGA0307→FGA0184, FGA0312→FGA0138, FGA0313→FGA0172 e FGA0314→FGA0238) e **duas em andamento** (FGA0303→FGA0150 e FGA0315→FGA0278).

As 15 obrigatórias pendentes somam 1.110h. Os universos de CT-03/04/05 são **15 disciplinas, 44 registros e 8 relações**. As unidades esperadas estão em `testes/evidencias/funcionais/unidades_esperadas_h0.csv`; esse arquivo prepara a conferência, sem resultado observado.

### 1.2 Cenários controlados

Todos os cenários mantêm H0 fixo. Somente a configuração da interface muda.

**Tabela 1 — Cenários controlados.**

| Cenário | Configuração | Finalidade |
| --- | --- | --- |
| C0 — Base | H0, alvo de 24 créditos/360h; registrar trabalho, objetivo e período selecionados | Conferir importação do histórico, regras e plano inicial |
| C1 — Carga menor | H0, alvo de 20 créditos/300h; demais escolhas iguais a C0 | Conferir a configuração de carga e o recálculo |
| C2 — Carga maior | H0, alvo de 32 créditos/480h; demais escolhas iguais a C0 | Conferir limite curricular e recálculo |
| C3 — Trabalho/estágio | H0; alternar somente essa resposta em relação a C0 | Conferir representação e efeito apenas se especificado |
| C4 — Objetivo | H0; alternar velocidade/equilíbrio em relação a C0 | Conferir representação e efeito apenas se especificado |
| C5 — Quantidade de matérias | H0; comparar 4, 6 e 8 matérias, mantendo trabalho e objetivo fixos | Conferir as cargas sugeridas exibidas no onboarding: 240/360/480h |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

C0–C2 usam cargas-alvo e não pressupõem que o valor esteja selecionado por padrão. C1/C2 tiveram os valores aceitos no piloto, com recálculo e restauração de C0; isso não julga a correção de todas as alocações. C3/C4 não pressupõem efeito algorítmico não documentado. C5 permite conferir a associação exibida no onboarding, mas o comportamento do plano exige saída observável.

## 2. Preparação comum

1. Carregar o histórico oficial e conferir a matriz, códigos, períodos e status. Não publicar o PDF ou identificadores pessoais.
2. Registrar data/hora com fuso, versão conhecida, navegador, viewport, zoom, entrada e cenário.
3. Definir esperado e fonte antes de executar. Usar `unidades_esperadas_h0.csv` como checklist e registrar a observação em `verificacoes_funcionais.csv`.
4. Gerar C0 e salvar todos os semestres, avisos e não alocadas. Nas variações, alterar um controle por vez e restaurar C0.
5. Classificar apenas com comparação efetiva. Ausência de dados não é zero nem aprovação.

## 3. Casos de teste

### CT-01 — Pré-requisitos (`MET-FUN-01`)

- **Entrada:** C0; FGA0170 está matriculada e FGA0211 pendente.
- **Regra:** FGA0211 exige FGA0170, desde 01/08/2019.
- **Passos:** conferir a representação de FGA0170 e o semestre de FGA0211. Confirmar a política de projeção de disciplinas em andamento antes de julgar.
- **Esperado:** a dependente não antecede o cumprimento válido do pré-requisito; matrícula não é aprovação acadêmica concluída. Projeção futura permitida precisa estar documentada.
- **Registro:** `TVP = violações / relações verificadas × 100`. TCC 1/2 só entram no denominador com fonte oficial/vigência. MAT0025/MAT0026 já aprovadas não demonstram ordenação futura.

### CT-02 — Co-requisitos (`MET-FUN-02`)

- **Entrada:** H0 tem FGA0071/FGA0073 aprovadas; FGA0072/FGA0074 não estão concluídas.
- **Regra:** FGA0072/FGA0074 são co-requisitadas reciprocamente e exigem `ENE0277 OU (FGA0073 E FGA0071)`.
- **Passos:** validar a seleção explícita das optativas, selecionar ambas sem alterar o histórico e conferir cada direção segundo a satisfação simultânea ou prévia aplicável.
- **Esperado:** atender a todas as relações aplicáveis. Reserva genérica de horas não demonstra seleção do par.
- **Registro:** `TVC = violações / relações dirigidas verificadas × 100`. Sem seleção viável, declarar falta de cobertura, sem aprovação.

### CT-03 — Obrigatórias pendentes (`MET-FUN-03`)

- **Entrada:** as 15 obrigatórias de `h0_obrigacoes_pendentes.csv`, incluindo FGA0170.
- **Passos:** cruzar a lista com o plano completo. As seis equivalências concluídas satisfazem suas obrigações; as duas matriculadas ainda não são aprovações. Tratar o semestre em curso conforme a política documentada.
- **Esperado:** contemplar as 15 pendências ou justificar exclusão previamente por regra. “Nenhuma não alocada” não comprova cobertura.
- **Registro:** `CDO = pendentes contempladas / 15 × 100`. Cadeias e ENADE ficam separados. Sem plano completo, não fechar o percentual.

### CT-04 — Tratamento do histórico (`MET-FUN-04`)

- **Entrada:** 44 registros: 37 aprovados e 7 matriculados.
- **Passos:** comparar cada registro com o reconhecido pelo sistema. Usar `registro_id = código@período`, preservando DSC0172/FGA0413 nos períodos diferentes.
- **Esperado:** preservar status e ocorrências. Matrícula não é aprovação real; projeção futura depende de política identificada.
- **Registro:** `TDH = divergências / 44 × 100`, após conferência completa. Totais agregados da importação não substituem a verificação individual.

### CT-05 — Equivalências (`MET-FUN-05`; apoio a `MET-FUN-03`)

- **Entrada:** seis relações concluídas e duas em andamento, conforme `h0_equivalencias.csv`.
- **Passos:** comparar reconhecimento, pendências e ausência de duplicação de cada relação.
- **Esperado:** seis relações satisfazem suas obrigatórias; os destinos das duas matriculadas permanecem não concluídos. ENGENHARIA E AMBIENTE é satisfeita por FGA0302→FGA0161.
- **Registro:** `TAE = aplicações incorretas / 8 × 100`, após conferir todas as relações no produto. O histórico define o esperado, não a taxa observada. MAT0138 não é ocorrência desta entrada.

### CT-06 — Onboarding (`MET-FUN-06`)

- **Entrada:** H0 fixo; C0 e variações C1–C5.
- **Passos:** variar um controle por vez e registrar seleção, texto da interface e plano. Conferir 4/6/8 matérias e as sugestões de 240/360/480h.
- **Esperado:** efeito correspondente ao comportamento prometido. Em EC-01, CA-C3 exige sugestão de 20 créditos ao ativar trabalho/estágio; CA-C4 exige horizonte de dois semestres para velocidade. Sugestão geral não é automaticamente teto rígido.
- **Registro:** `COO = expectativas atendidas / expectativas válidas × 100`. Sem efeito obrigatório especificado, manter essa parte pendente de especificação.

### CT-07 — Restrições semestrais (`MET-FUN-07`)

- **Entrada:** H0 fixo; C0/C1/C2 e variações C5 com configuração registrada.
- **Passos:** somar cargas futuras e comparar com o máximo curricular de 480h. Incluir reservas identificadas e separar semestre em curso de futuro. Conferir as dez alocações de OC-01 e as três condições de CAL-01.
- **Esperado:** atender às restrições verificáveis. Conferir oferta/calendário somente com fonte do período e interpretar exceções antes de julgar.
- **Registro:** `TVS = violações / verificações válidas × 100`, por tipo. Oferta, sugestão e máximo curricular não compartilham julgamento único.

## 4. Encerramento

A execução e o julgamento estão concluídos em [EC-01](../../fase4/conclusao.md). A configuração-base de 24 créditos foi restaurada conforme confirmação de Gustavo.

Os cenários usam o mesmo histórico e não representam estudantes independentes. Concluir cálculos somente com referências, evidências e cobertura suficientes. A [Fase 4](../../fase4/metricasFuncionais.md) registra os resultados do produto separadamente da preparação.

## 5. Referências

Referências usadas nesta página, conforme [Referências — Fase 3](../../../referencias/fase3.md).

- UNIVERSIDADE DE BRASÍLIA. **SIGAA — Estruturas curriculares de Engenharia de Software**, matriz 6360/1 — 2017.1. [Consulta pública](https://sigaa.unb.br/sigaa/public/curso/curriculo.jsf?id=414924&lc=pt_BR). Acesso em: 15 nov. 2026. Nos detalhes, consultar os componentes FGA0211, MAT0026 e IFD0173 e seus históricos de vigência.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Detalhamento dos sete casos funcionais e das evidências de coleta | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Substituição dos perfis fictícios por histórico autorizado e cenários de uso | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Normalização de H0, sanitização da evidência e adequação dos cenários à entrada real | 15/11 | [b07997f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b07997f34eb1a595571e3e5abd3cc4e15002949b) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |