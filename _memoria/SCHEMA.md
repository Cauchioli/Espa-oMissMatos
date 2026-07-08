# SCHEMA — Padrão de Notas do Segundo Cérebro

> Use este padrão em **todas as notas do seu Obsidian** para que o RAG indexe
> corretamente e o grafo de conhecimento se mantenha conexo e sem notas órfãs.

---

## Estrutura Padrão de Frontmatter

```yaml
---
id: nome-da-nota-em-kebab-case
tipo-no: frente | entidade | metodologia | manual | referencia | estado | sessao
tipo: caso | cliente | principio | procedimento | indice | template | aprendizado
dominio: comercial | marketing | juridico | operacional | pessoal | financeiro
status: ativo | encerrado | prospect | rascunho
relaciona:
  - "[[outra-nota]]"
  - "[[outra-nota-2]]"
fontes:
  - "[FONTE: link ou caminho do arquivo original]"
---
```

---

## Vocabulário Fechado de Tags

Use apenas estas tags para manter consistência no Dataview:

```
#tipo/ideia
#tipo/decisao
#tipo/aprendizado
#tipo/procedimento
#tipo/caso
#status/ativo
#status/concluido
#status/rascunho
#verificar
#cliente
#oferta
#conteudo
```

---

## Estrutura de Pastas Recomendada para o Obsidian

```
📓 Vault/
├── 00-inbox/          ← Notas brutas, rascunhos, capturas rápidas
├── 10-frentes/        ← Projetos e frentes ativas do negócio
├── 20-entidades/      ← Clientes, parceiros, mentores, personas
├── 30-metodologia/    ← Frameworks, princípios, teses (Hormozi, etc.)
├── 40-manuais/        ← SOPs, guias passo a passo, scripts
├── 50-referencia/     ← Material permanente, templates, MOCs
├── 60-estado/         ← Estado atual do sistema (verdade presente)
├── 80-arquivo/        ← Notas e projetos encerrados (nunca deletar)
└── 90-historico/      ← Logs de sessão, registros de reuniões
```

---

## Regras de Ouro

1. **Todo wikilink por basename** — `[[nome-da-nota]]` sem especificar pasta
2. **Nunca deletar notas** — mover para `80-arquivo/` quando encerrar
3. **Fontes sempre verificáveis** — afirmações sem fonte marcadas com `[VERIFICAR]`
4. **Dados de clientes finais** — nunca no vault; salvar em pasta separada de entregáveis
5. **Após criar notas importantes** — rodar indexação incremental do RAG:
   ```bash
   python rag/rag_acervo.py index
   ```

---

## Exemplo de Nota Completa

```markdown
---
id: playbook-qualificacao-leads
tipo-no: manual
tipo: procedimento
dominio: comercial
status: ativo
relaciona:
  - "[[sales-engine]]"
  - "[[funil-dm]]"
fontes:
  - "[FONTE: Playbook Diagnóstico Comercial v2 - 2026-06]"
---

# Playbook de Qualificação de Leads

Procedimento para conduzir a chamada de diagnóstico de 30 minutos...

## Etapa 1 — Abertura
...

## Etapa 2 — SPIN
...
```
