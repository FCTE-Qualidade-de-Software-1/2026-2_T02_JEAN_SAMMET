# Modelo de Qualidade

<!-- Critério 4. Nível máximo: adaptações justificadas por contexto e stakeholders + diagrama ligado às subcaracterísticas. -->

## 1. Modelo base

O modelo adotado como referência é o **Modelo de Qualidade de Produto da norma ISO/IEC 25010:2011 (SQuaRE)**, complementado pelas definições métricas da **ISO/IEC 25023:2016**. A norma estrutura a qualidade interna e externa em características e subcaracterísticas mensuráveis.

## 2. Adaptações ao software

Para a avaliação da funcionalidade **Planejar formatura** do No Fluxo UnB, o modelo geral foi adaptado com base no propósito da ferramenta, nos perfis de estudantes e nas necessidades dos mantenedores:

| Elemento do modelo | Adaptação | Justificativa (contexto / stakeholder) |
| :--- | :--- | :--- |
| **Adequação funcional** | Mantida com foco em **Completude funcional** e **Correção funcional** | O núcleo do software é gerar um plano academicamente válido. Incorreções em pré-requisitos, co-requisitos ou disciplinas faltantes inviabilizam a utilidade para o estudante. |
| **Usabilidade** | Mantida com foco em **Apreensibilidade (Learnability)** e **Operabilidade (Operability)** | A interface apresenta grafos interativos de alta densidade cognitiva. O estudante precisa conseguir localizar sua previsão de formatura e entender as matérias críticas sem suporte humano. |
| **Segurança** | Mantida com foco em **Confidencialidade** e **Autenticidade / Controle de Acesso** | O software manipula dados acadêmicos sensíveis (histórico oficial, matrícula, notas e reprovações) extraídos no navegador e persistidos no Supabase. É crítico avaliar a proteção contra vazamentos no cliente e vulnerabilidades em dependências. |
| **Eficiência de desempenho** | Removida do escopo prioritário | O planejamento curricular é uma atividade analítica e assíncrona; variações normais de latência de rede não inviabilizam o propósito do software. |
| **Manutenibilidade** | Removida do escopo prioritário | Priorizou-se a experiência do usuário final e o resguardo legal da privacidade sobre a análise interna do código. |
| **Confiabilidade** | Removida do escopo prioritário | Falhas lógicas de geração de planos são tratadas diretamente como não conformidades funcionais (adequação funcional). |
| **Compatibilidade e Portabilidade** | Removidas do escopo prioritário | Foco estabelecido na versão desktop (navegadores modernos) devido a restrições de prazo e relevância. |

## 3. Representação gráfica

```mermaid
graph TD
    M["Modelo de Qualidade do Produto (ISO/IEC 25010 adaptado)"] --> C1["Adequação Funcional"]
    M --> C2["Usabilidade"]
    M --> C3["Segurança"]
    
    C1 --> S11["Completude Funcional<br/>(Disciplinas obrigatórias contempladas)"]
    C1 --> S12["Correção Funcional<br/>(Conformidade com pré/co-requisitos)"]
    
    C2 --> S21["Apreensibilidade<br/>(Interpretação da previsão e matérias críticas)"]
    C2 --> S22["Operabilidade<br/>(Taxa de sucesso na execução de tarefas)"]
    
    C3 --> S31["Confidencialidade<br/>(Proteção contra vazamento de dados no cliente)"]
    C3 --> S32["Autenticidade e Controle de Acesso<br/>(Validação de rotas protegidas e vulnerabilidades)"]
```

*Figura 6 - Modelo de qualidade adaptado para a funcionalidade Planejar formatura. Fonte: elaboração da equipe, com base na ISO/IEC 25010.*

A seleção e a priorização detalhada das características estão em [Características de Qualidade](caracteristicasDeQualidade.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Definição das adaptações do modelo, subcaracterísticas e diagrama | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do modelo adaptado para Adequação Funcional, Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |