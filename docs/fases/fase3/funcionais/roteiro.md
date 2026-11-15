# Roteiro de avaliação funcional

O roteiro aplica as [métricas da Fase 2](../../fase2/funcionais/GQM.md) usando **H0**, o histórico oficial SIGAA/UnB já autorizado, mantido fora do repositório. A definição dos cenários fica em `testes/cenarios_avaliacao.json`; as regras de referência, em `testes/referencias/estrutura_6360_1.json`.

## 1. Entrada e cenários

Os cenários usam o mesmo histórico. Alteram somente controles oferecidos pelo produto, sem fabricar novas aprovações, reprovações ou equivalências.

| Cenário | Configuração | Finalidade |
|---|---|---|
| C0 — Base | H0, 24 créditos/360h; registrar trabalho, objetivo e período selecionados | Conferir histórico, regras e plano inicial |
| C1 — Carga menor | H0, 20 créditos/300h; demais escolhas iguais a C0 | Conferir carga e recálculo |
| C2 — Carga maior | H0, 32 créditos/480h; demais escolhas iguais a C0 | Conferir carga e limite curricular |
| C3 — Trabalho/estágio | H0; alternar somente essa resposta em relação a C0 | Conferir representação da preferência e efeito especificado |
| C4 — Objetivo | H0; alternar velocidade/equilíbrio em relação a C0 | Conferir representação da preferência e efeito especificado |
| C5 — Quantidade de matérias | H0; comparar 4, 6 e 8 matérias, mantendo trabalho e objetivo fixos | Conferir as cargas sugeridas exibidas no onboarding |

C1/C2 dependem de o campo aceitar esses valores; essa pré-condição será confirmada no piloto. C3–C5 não pressupõem um efeito algorítmico ainda não documentado. Esses são cenários planejados, não execuções concluídas. As cinco métricas operacionais também podem usar H0.

## 2. Preparação comum

1. Registrar ambiente, matriz, data/hora e identificador da execução. Conferir os códigos e status reconhecidos a partir de H0, preservando evidências sanitizadas.
2. Antes de gerar o plano, montar a lista esperada para cada caso com as regras oficiais aplicáveis. O comportamento do site não define sozinho o resultado correto.
3. Executar C0 e registrar todos os semestres, disciplinas, avisos e não alocadas. Nas variações, mudar um controle por vez e restaurar C0 antes da próxima comparação.
4. Registrar numerador, denominador e cobertura. Condições ausentes em H0 não serão inventadas nem contadas como atendidas. Não publicar o PDF, notas, matrícula ou credenciais.

## 3. Casos

### CT-01 — Pré-requisitos (`MET-FUN-01`)

- **Entrada:** C0; relações de disciplinas efetivamente presentes no histórico e no plano.
- **Referência:** verificar cada relação nas [fontes](fontes.md). FGA0170/FGA0211 e a expressão `MAT0025 OU MAT0024` de MAT0026 são exemplos já consultados; selecionar apenas relações pertinentes à entrada real.
- **Passos:** registrar o estado dos pré-requisitos e os semestres das dependentes; verificar cumprimento prévio. Disciplina em andamento só satisfaz projeção futura conforme política documentada, sem presumir aprovação real.
- **Esperado:** nenhuma dependente antecede o cumprimento válido da expressão de pré-requisito. Não confundir relação já satisfeita no histórico com relação verificada na sequência futura.
- **Registro:** `TVP = violações / relações verificadas × 100`. Informar quais situações foram cobertas; não afirmar teste com reprovação se esse cenário não foi executado. Sem relações verificáveis, não calcular.

### CT-02 — Co-requisitos (`MET-FUN-02`)

- **Entrada:** C0, quando houver um par aplicável na entrada e na saída; nenhuma aprovação será fabricada para preparar o caso.
- **Referência:** FGA0072/FGA0074 são optativas da matriz, com co-requisitos recíprocos e pré-requisito `ENE0277 OU (FGA0073 E FGA0071)`, ativos desde 01/08/2019.
- **Passos:** verificar se o par faz parte das disciplinas selecionadas e se os pré-requisitos estão satisfeitos. Conferir status e semestres. Seleção manual de optativas só será usada se o recurso existir e for validado no piloto.
- **Esperado:** ambas pendentes e selecionadas no mesmo semestre; uma já aprovada permite planejar a outra depois, conforme a regra. Reserva genérica de horas não demonstra alocação do par.
- **Registro:** `TVC = violações / relações verificadas × 100`, por relação dirigida. Se H0 não fornecer um par verificável e não houver seleção suportada, declarar **sem cobertura para CT-02**, sem valor numérico; isso não aprova a métrica.

### CT-03 — Obrigatórias pendentes (`MET-FUN-03`)

- **Entrada:** C0 e a lista oficial das 39 obrigatórias da matriz 6360/1.
- **Passos:** identificar as obrigatórias já satisfeitas por aprovação ou equivalência válida; calcular `P = obrigatórias − satisfeitas`. Registrar à parte disciplinas em andamento e aplicar sua política somente se documentada. Comparar P com as disciplinas identificadas no plano completo, considerando o semestre em curso quando fizer parte da projeção avaliada.
- **Esperado:** todas as pendências de P são contempladas, sem duplicatas. Omissões, exceções e não alocadas precisam de justificativa verificável; reserva genérica não conta como disciplina.
- **Registro:** `CDO = pendentes contempladas / quantidade de pendentes em P × 100`. O denominador vem de H0, sem quantidade fixa. Se P estiver vazio, justificar Não aplicável; se depender de política ausente, não emitir julgamento completo. O recorte não demonstra integralização de optativas ou cadeias de seletividade.

### CT-04 — Status do histórico (`MET-FUN-04`)

- **Entrada:** registros efetivamente existentes em H0.
- **Passos:** comparar cada status do documento com o reconhecido pelo site e com seu tratamento no plano. Separar aprovações, reprovações e matrículas; verificar apenas as categorias presentes.
- **Esperado:** os status são preservados e tratados de acordo com a política especificada. Matrícula não equivale a aprovação acadêmica; o planejamento pode projetar sua conclusão se isso estiver documentado.
- **Registro:** `TDH = divergências / verificações válidas × 100`. Informar quantidade por categoria e categorias ausentes. Não apresentar como comparação da mesma disciplina com três status. Política não conhecida gera pendência na parte afetada.

### CT-05 — Equivalências (`MET-FUN-05`; apoio a `MET-FUN-03`)

- **Entrada:** equivalências efetivamente presentes em H0; conferir as regras oficiais antes de julgar cada uma.
- **Referência:** MAT0138/MAT0026 é um exemplo confirmado no SIGAA, não uma ocorrência presumida no histórico. Outras equivalências exigem fonte e vigência próprias.
- **Passos:** para cada equivalência disponível, verificar reconhecimento, satisfação da obrigação e ausência de duplicação da pendência. Não exigir planos idênticos sem regra para isso.
- **Esperado:** a disciplina equivalente satisfaz a obrigação conforme a expressão aplicável à matriz e à vigência.
- **Registro:** `TAE` por equivalência válida examinada. Sem ocorrência verificável, declarar **sem cobertura para CT-05**, sem taxa. Não criar uma aprovação equivalente apenas para executar o teste nem presumir transitividade.

### CT-06 — Opções do onboarding (`MET-FUN-06`)

- **Entrada:** C0 e C3–C5, sempre com H0 fixo.
- **Passos:** percorrer trabalho → quantidade de matérias → objetivo. Alterar uma opção por comparação, registrar seleção, carga sugerida, plano e avisos; conferir as opções de 4/6/8 matérias, exibidas como aproximadamente 240/360/480h. Manter interesses opcionais vazios. Restaurar as escolhas iniciais.
- **Esperado:** seleção e carga são representadas coerentemente. Trabalho e objetivo só geram verificação de correção algorítmica quando houver efeito prometido identificável; ausência de mudança, isoladamente, não demonstra erro.
- **Registro:** `COO = expectativas atendidas / expectativas válidas × 100`, com a expectativa definida antes de cada comparação. Sem expectativa especificada, não calcular essa parte.

### CT-07 — Restrições semestrais (`MET-FUN-07`)

- **Entrada:** C0–C2, com H0 fixo e as mesmas demais preferências.
- **Referência:** máximo curricular de 480h. Conferir a conversão exibida e o limite configurado. Oferta e semestre inicial exigem calendário e fonte próprios.
- **Passos:** somar as cargas de cada semestre futuro, incluindo reservas identificadas; comparar com o limite configurado e o curricular. Separar semestre em curso de futuro. Conferir oferta apenas onde houver referência disponível.
- **Esperado:** respeitar máximo curricular e limite prometido para cada cenário. Interpretar exceções e carga inferior ao mínimo, especialmente no último semestre, antes de classificar como falha.
- **Registro:** `TVS` por tipo de restrição, com denominadores próprios. Calendário/oferta sem fonte ficam pendentes. Registrar o retorno a C0.

## 4. Encerramento e cobertura

Manter uma execução inicial por cenário e preservar repetições com motivo. Separar piloto e coleta definitiva. A avaliação usa um histórico autorizado e configurações distintas: não representa uma amostra de estudantes nem dois perfis acadêmicos independentes. Resultados parciais não comprovam correção para condições ausentes. Os critérios de julgamento permanecem na Fase 2.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Detalhamento dos sete casos funcionais e das evidências de coleta | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Substituição dos perfis fictícios por histórico autorizado e cenários de uso | 15/11 | Não commitado |
