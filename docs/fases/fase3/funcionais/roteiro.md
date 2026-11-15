# Roteiro de avaliação funcional

O roteiro aplica as [métricas funcionais da Fase 2](../../fase2/funcionais/GQM.md). Usar os perfis de `testes/massa_dados_sintetica.json`, a referência de `testes/referencias/estrutura_6360_1.json` e os modelos de registro em `testes/modelos_coleta/`.

## 1. Preparação comum

1. Registrar ambiente, matriz e data/hora. Confirmar o modo de entrada sintética antes de substituir os dados da conta.
2. Carregar o perfil, conferir cada código e status e salvar evidência da entrada. O JSON organiza os cenários; não é um formato de importação já validado pelo site.
3. Selecionar 24 créditos como base e registrar trabalho, objetivo e período de início. Gerar o plano e registrar todos os semestres, disciplinas e avisos, inclusive não alocadas e reservas de optativas.
4. Comparar esperado e observado por relação/disciplina. Salvar evidência sanitizada e calcular a métrica com numerador e denominador explícitos.

## 2. Casos

### CT-01 — Pré-requisitos (`MET-FUN-01`)

- **Entrada:** P1 com MAT0025 aprovada e P2 com MAT0025 reprovada; MAT0024 e MAT0026 não aprovadas em ambos.
- **Referência:** regra de MAT0026 nas [fontes](fontes.md).
- **Passos:** gerar um plano por perfil; localizar MAT0025/MAT0026 e verificar a satisfação de MAT0025 **ou** MAT0024 antes de MAT0026. Repetir para FGA0170/FGA0211 quando o histórico sintético pertinente estiver definido.
- **Esperado:** P1 já satisfaz a condição; em P2, MAT0026 não deve anteceder nem ser simultânea ao cumprimento válido do pré-requisito.
- **Registro:** uma linha por relação em `verificacoes_funcionais.csv`; `TVP = violações / relações verificadas × 100`. Relação sem dados suficientes fica inconclusiva.

### CT-02 — Co-requisitos (`MET-FUN-02`)

- **Entrada:** par de disciplinas pendentes com co-requisito oficial aplicável, a definir.
- **Referência:** localizar expressão e vigência; Física 1 Experimental não será usada como par presumido.
- **Passos:** após identificar o par, executar cenários com ambas pendentes e com uma concluída; comparar a alocação à regra.
- **Esperado:** satisfação simultânea ou prévia, conforme a fonte.
- **Registro:** relações atendidas/violadas e `TVC`. Até definir o par, **Pendente de especificação**, sem valor numérico.

### CT-03 — Obrigatórias pendentes (`MET-FUN-03`)

- **Entrada:** P1; quatro das 39 obrigatórias estão aprovadas e não há equivalências ou disciplinas em andamento nesse perfil.
- **Referência:** relação das 39 obrigatórias da matriz, totalizando 2.580h.
- **Passos:** calcular a diferença entre a lista de obrigatórias e as aprovações; a lista esperada tem **35 disciplinas**. Comparar com a união de todos os semestres futuros do plano. Registrar separadamente omissões, repetições, não alocadas e justificativas.
- **Esperado:** as 35 pendentes aparecem no plano; eventual exclusão depende de regra e política registradas antes da execução. Reserva genérica de horas não conta como disciplina identificada.
- **Registro:** `CDO = pendentes contempladas / 35 × 100`. Esse recorte não demonstra integralização completa das optativas e cadeias de seletividade.

### CT-04 — Status do histórico (`MET-FUN-04`)

- **Entrada:** usar MAT0025 em cenários pareados como aprovada, reprovada e matriculada, sem alterar os demais campos.
- **Referência:** regra curricular e política documentada para disciplinas em andamento.
- **Passos:** conferir o status após a entrada, a inclusão da disciplina nos semestres e o efeito em MAT0026. Guardar os três planos.
- **Esperado:** aprovação e reprovação permanecem distinguíveis. O efeito de disciplina em andamento no planejamento futuro só será julgado após confirmar a política adotada; não presumir aprovação real.
- **Registro:** `TDH = divergências / verificações válidas × 100`; marcar a parte sem política como pendente.

### CT-05 — Equivalências (`MET-FUN-05`; apoio a `MET-FUN-03`)

- **Entrada:** cópia de P1 com MAT0138 aprovada; compará-la a outra com MAT0026 aprovada, mantendo os demais dados iguais.
- **Referência:** equivalência de MAT0026 e vigência, com aplicação à matriz confirmada antes do teste. Carga e cadastro de MAT0138 ainda devem ser conferidos; esse cenário não integra os perfis prontos.
- **Passos:** conferir pendências e efeitos da aprovação em ambos os planos. Não exigir igualdade da ordenação se não houver regra para isso.
- **Esperado:** MAT0138 satisfaz MAT0026 quando a equivalência for aplicável, sem duplicar a pendência.
- **Registro:** resultado por equivalência e `TAE`; sem confirmação de aplicabilidade, manter pendente. Não testar cadeia transitiva sem fonte.

### CT-06 — Opções do onboarding (`MET-FUN-06`)

- **Entrada:** P1 fixo; variar uma opção por vez: trabalho/estágio, carga e objetivo.
- **Passos:** em **Preferências**, percorrer trabalho → quantidade de matérias → objetivo. Comparar 4/6/8 matérias, exibidas como aproximadamente 240/360/480h. Registrar seleção, valores resultantes e planos. O campo opcional de interesses pode ficar vazio.
- **Esperado:** as seleções e a carga são representadas de forma coerente. Trabalho e objetivo só geram verificação de correção algorítmica quando o efeito prometido estiver especificado.
- **Registro:** uma linha por expectativa previamente definida; `COO = expectativas atendidas / expectativas válidas × 100`. Se nenhuma estiver especificada, não calcular.

### CT-07 — Restrições semestrais (`MET-FUN-07`)

- **Entrada:** P1, com limite de 24 créditos; repetir com outro valor permitido, registrando a conversão exibida.
- **Referência:** máximo curricular de 480h; a interface observada mostra 24 créditos = 360h. Oferta e semestre inicial exigem calendário e fonte próprios.
- **Passos:** somar a carga de cada semestre futuro, incluindo reservas identificadas; comparar ao limite configurado e ao curricular. Conferir oferta e período apenas onde houver fonte. Não comparar o limite futuro ao semestre já em curso como se fosse a mesma condição.
- **Esperado:** não ultrapassar o máximo curricular nem o limite prometido para o cenário. Exceções ou carga abaixo do mínimo precisam de interpretação documentada; não presumir erro no último semestre.
- **Registro:** `TVS` separado por tipo de restrição, com denominadores próprios. Oferta e calendário sem fonte ficam pendentes.

## 3. Encerramento

Manter uma execução inicial por cenário controlado. Repetir se houver erro externo ou divergência a investigar, preservando ambas as tentativas. Não misturar o piloto com a coleta definitiva. Responder as sete questões somente a partir das verificações válidas e da cobertura declarada.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Detalhamento dos sete casos funcionais e das evidências de coleta | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
