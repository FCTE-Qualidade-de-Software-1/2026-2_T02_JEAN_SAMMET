# Métodos de avaliação operacional

## 1. Usabilidade — TCH e ISVH

Dois avaliadores da equipe percorrem T1–T3 independentemente, com a mesma massa e ambiente, e preenchem os dez itens do [checklist da Fase 2](../../fase2/operacionais/usabilidade.md). Para cada violação, registrar descrição, tarefa, severidade 1–4 e evidência. Depois, consolidar em consenso, preservando notas individuais e justificativas de divergência.

`TCH = itens conformes / 10 × 100`. `ISVH = 4 × Ncatastrofico + 3 × Nmaior + 2 × Nmenor + Ncosmetico`. Os limites são os da Fase 2; não atribuir uma nota final a partir de uma única exploração.

## 2. Dependências — IRP

Inspecionar os scripts efetivamente carregados no cliente, com Retire.js e inventário de arquivos/versões. Registrar achados únicos por componente, versão e aviso. Auditar manifestos públicos separadamente, quando disponíveis; não somar coberturas sobrepostas.

`IRP = 10 × Ncritica + 5 × Nalta + 2 × Nmoderada + Nbaixa`. Ausência de relatório, cobertura desconhecida ou erro do scanner gera Inconclusivo. O resultado do cliente não avalia o backend. Separar produção e desenvolvimento quando verificável.

## 3. Armazenamento — GED-C

Inspecionar `localStorage`, `sessionStorage` e cookies em três estados: sessão inicial, após carregar o perfil e após gerar o plano. Registrar origem, mecanismo, chave, conteúdo sintético e evidência. Contar cada chave com dado pessoal/acadêmico em claro uma vez. Verificar flags no painel de cookies, sem publicar seus valores de autenticação.

`GED-C = quantidade de chaves com dados em claro`. Uma coleta parcial não pode receber Conforme. As flags de cookie não demonstram criptografia do conteúdo nem conformidade legal.

## 4. Acesso — TBR

Primeiro observar no DevTools a chamada real usada ao gerar o plano. Confirmar a operação protegida, domínio, método, payload e chamada positiva autorizada. Somente depois executar os casos negativos, com conta e dados de teste.

| Caso | Condição | Cuidados para validar o teste |
|---|---|---|
| REQ-01 | Sem Authorization | Preservar método e payload válidos |
| REQ-02 | Authorization vazio | Diferenciar header vazio de ausente |
| REQ-03 | Esquema incorreto | Comparar ao esquema realmente exigido |
| REQ-04 | Bearer sem token | Aplicável apenas se o serviço usar Bearer |
| REQ-05 | Token malformado | Registrar resposta, sem reutilizar credencial pessoal |
| REQ-06 | Assinatura inválida | Token de teste com estrutura apropriada |
| REQ-07 | Token expirado | Credencial de teste cuja assinatura seja verificável; assinatura falsa não isola expiração |
| REQ-08 | Token sem assinatura | Aplicável somente ao mecanismo observado |
| REQ-09 | Papel insuficiente | Usuário de teste autenticado sem a permissão necessária |
| REQ-10 | Token revogado | Credencial de teste revogada; se o fluxo não existir, substituir por caso aplicável, antes da coleta |

Credenciais necessárias ainda devem ser preparadas. Não fabricar uma assinatura e apresentar o teste como validação de permissões. Enviar `Origin` em Python, por si só, não testa a aplicação de CORS pelo navegador.

`TBR = bloqueios 401/403 / chamadas negativas válidas × 100`. Informar bateria planejada, válida e inconclusiva. HTTP 404/405, falha de conexão ou HTTP 500 sem prova de acesso não demonstram falha de autenticação. Sem operação protegida no recorte, registrar Não aplicável com fonte. Aplicar os [critérios completos](../../fase2/operacionais/seguranca.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação detalhada dos métodos de Usabilidade (Nielsen) e Segurança (SCA, Storage e Matriz de 10 testes de API) | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento dos métodos aos critérios e à validade das coletas | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
