# Portal de Entrada — Segundo Cérebro do Negócio

> **Atenção Agente:** Esta é a porta de entrada de cada sessão.
> Leia este arquivo antes de qualquer resposta. Ele define onde está cada coisa e como operar.

---

## O que é este sistema

Este workspace é o **Vértice OS** — o sistema operacional do seu negócio.
Ele é composto de três camadas que trabalham juntas:

```
📁 [esta pasta]          ← Vértice OS: engines, agentes e skills
📓 Obsidian Vault        ← Segundo Cérebro: notas, metodologia, histórico
🔍 RAG (porta 8799)      ← Motor de busca semântica: indexa tudo e conecta
```

O RAG lê o Obsidian + todos os documentos configurados e os disponibiliza
para os engines em tempo real. Quando ativo, os engines sabem tudo o que
você já escreveu, decidiu ou aprendeu — sem você precisar repetir nada.

---

## Mapa do Workspace

- **`_memoria/`** — Contexto vivo do negócio (empresa, estratégia, preferências)
- **`_memoria/SCHEMA.md`** — Padrão de notas para o Obsidian do cliente
- **`identidade/`** — Design system (cores, fontes, logo)
- **`.agents/skills/`** — Os engines e automações do sistema
- **`.agents/AGENTS.md`** — Leis de operação do agente
- **`.agents/PROTOCOLO.md`** — Ciclo de início, execução e encerramento de sessão
- **`rag/`** — Motor RAG local (indexador + servidor)
- **`app/`** — Painel visual (Kanban, CRM, métricas do Instagram)
- **`templates/`** — Templates de proposta, carrossel e dossiê

---

## Checklist de Início de Sessão

Antes de responder qualquer tarefa, o agente deve:

- [ ] Carregar `_memoria/empresa.md`
- [ ] Carregar `_memoria/preferencias.md`
- [ ] Carregar `_memoria/estrategia.md`
- [ ] Carregar `identidade/design-guide.md`
- [ ] Verificar se o RAG está ativo: `GET http://127.0.0.1:8799/health`
  - Se ativo: consultar contexto relevante antes de responder
  - Se offline: prosseguir com `_memoria/` e avisar o usuário em 1 linha
- [ ] Identificar a tarefa. Se for complexa ou irreversível: escrever um plano curto e obter aprovação antes de agir

---

## Guias de Operação

- **`AGENTS.md`** — Leis invioláveis de comportamento, design e anti-alucinação
- **`PROTOCOLO.md`** — O ciclo de início, execução e encerramento de sessão
- **`SCHEMA.md`** — Padrão de metadados para notas do Obsidian

---

> *"Linhas de dados dispersas que colapsam em um único ponto. Isso é a Vértice."*
