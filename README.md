# Vértice OS — Sistema Operacional de Negócios por I.A.

O **Vértice OS** é um sistema operacional de negócios construído sobre I.A. generativa. Ele transforma qualquer IA (Gemini, Claude, ChatGPT) em um copiloto executivo que conhece profundamente o negócio do cliente — não por prompts estáticos, mas por um sistema de memória persistente, RAG local e engines estratégicos que aprendem e evoluem com o uso.

A metáfora é a música *Binary Data IV*: linhas de dados dispersas (anotações, reuniões, PDFs, posts) que colidem e convergem em um único ponto — a Vértice.

---

## 🗺️ Estrutura do Repositório

```
├── .agents/
│   ├── AGENTS.md               # Leis operacionais do sistema
│   ├── agents/
│   │   ├── alex/               # Agente Alex — Ofertas Grand Slam (Hormozi)
│   │   ├── doug/               # Agente Doug — Copywriting High-Ticket
│   │   └── valentina/          # Agente Valentina — Marca Pessoal e Instagram
│   └── skills/
│       ├── instalar/           # Setup inicial do sistema
│       ├── abrir/              # Abertura de sessão (carrega contexto)
│       ├── messaging-engine/   # Arquitetura de mensagem e identidade verbal
│       ├── content-os/         # Sistema de conteúdo 30 dias
│       ├── sales-engine/       # Roteiro de vendas, SPIN e follow-up
│       ├── client-success/     # Onboarding, 90 dias e geração de cases
│       ├── authority-engine/   # Manifesto, palestra, livro e artigo longo
│       ├── growth-engine/      # Diagnóstico de gargalos (CEO virtual)
│       ├── research-engine/    # Inteligência de mercado e ammunition de copy
│       ├── carrossel/          # Carrosséis e posts visuais para Instagram
│       ├── publicar-tema/      # Pipeline completo: blog + carrossel + legenda
│       ├── aprovar-post/       # Publicação automática via Meta API
│       ├── proposta-comercial/ # Proposta A4 premium em HTML
│       ├── seo/                # SEO, GEO e Google Ads
│       ├── anuncio-google/     # Estrutura de campanhas Google Ads
│       ├── relatorio-ads/      # Relatório de performance semanal
│       ├── novo-projeto/       # Iniciar novo cliente/projeto
│       ├── salvar/             # Commit + push no GitHub
│       └── [+ mais 10 skills] #
├── _memoria/                   # Contexto estratégico do negócio
│   ├── empresa.md
│   ├── estrategia.md
│   └── preferencias.md
├── identidade/                 # Design System
│   └── design-guide.md
├── app/                        # Painel de Controle Visual
│   ├── app_backend.py          # Servidor Flask (Porta 5000)
│   ├── index.html              # Dashboard (Kanban, CRM, métricas)
│   └── instagram_cache.json    # Cache de performance do Instagram
├── rag/                        # Módulo RAG Local (LanceDB)
│   ├── rag_acervo.py           # Indexador incremental
│   ├── rag_server.py           # Servidor de busca (Porta 8799)
│   └── rag.py                  # Cliente CLI
├── templates/
│   ├── dossie_diagnostico_template.md  # Template para setup DFY
│   ├── carrossel_template.html
│   ├── proposta_template.html
│   └── perfis/                 # Templates por tipo de negócio
│       ├── claude-md-solopreneur.md
│       ├── claude-md-freelancer.md
│       ├── claude-md-agencia.md
│       └── claude-md-empresa.md
└── README.md
```

---

## 🚀 Setup Inicial — 3 Formas de Instalar

### Opção A — Setup Guiado (Novo Cliente, Auto-Atendimento)
Clone o repositório e rode `/instalar` na IA. O sistema conduz uma entrevista de 5-7 minutos e configura tudo automaticamente.

```bash
git clone https://github.com/Cauchioli/VerticeOS.git nome-do-negocio
cd nome-do-negocio
```
Depois abrir a IA e digitar: `/instalar`

---

### Opção B — Setup DFY (Done-For-You pelo Consultor Vértice)
O consultor faz a reunião de diagnóstico com o cliente, preenche o `templates/dossie_diagnostico_template.md`, renomeia para `dossie_diagnostico.md` e coloca na raiz. O `/instalar` detecta o arquivo e configura tudo sem entrevista — máxima profundidade, mínimo atrito.

```bash
# Após preencher o dossiê:
cp templates/dossie_diagnostico_template.md dossie_diagnostico.md
# Depois: /instalar na IA
```

---

### Opção C — Setup com RAG (Memória de Longo Prazo Ativa)
Para clientes que querem o sistema completo com segundo cérebro indexado:

```bash
python install_rag.py            # instala dependências (uma vez)
python rag/rag_acervo.py index   # indexa o acervo
python rag/rag_server.py         # sobe o servidor (manter aberto)
```
Com o RAG ativo, todos os engines consultam o acervo de documentos do cliente antes de gerar qualquer saída.

> **O RAG é opcional.** O sistema funciona sem ele — os engines usam `_memoria/` como contexto. O RAG amplifica a qualidade quando ativo.

---

## 🔁 Os 7 Engines Estratégicos

| Engine | Trigger | O que entrega |
|---|---|---|
| `/messaging-engine` | "cria minha mensagem" | Manifesto, tese, vocabulário proprietário, frases de autoridade |
| `/content-os` | "calendário de conteúdo" | Calendário 30 dias, pilares, reels, stories, emails |
| `/sales-engine` | "roteiro de vendas" | SPIN, objeções, follow-up, script de call |
| `/client-success` | "onboarding do cliente" | Plano 90 dias, quick wins, NPS, template de case |
| `/authority-engine` | "quero construir autoridade" | Manifesto, palestra, framework, outline de livro |
| `/growth-engine` | "onde investir energia" | Diagnóstico de gargalo + 3 alavancas de crescimento |
| `/research-engine` | "o que o mercado está falando" | Ammunition de copy, gaps de concorrência, ideias de oferta |

**Ordem recomendada:** `messaging-engine` → `content-os` → `sales-engine` → `client-success`

---

## 🎭 Os 3 Agentes Especializados

| Agente | Especialidade | Como chamar |
|---|---|---|
| **Doug** | Copywriting High-Ticket, storytelling, headlines | "Doug, reescreve esse texto..." |
| **Alex** | Ofertas Grand Slam, Equação de Valor (Hormozi) | "Alex, analisa minha oferta..." |
| **Valentina** | Marca pessoal autêntica, Instagram, tom de voz | "Valentina, como posiciono minha marca..." |

---

## 🖥️ Painel de Controle

Inicie o backend e abra o dashboard:

```bash
python app/app_backend.py   # Porta 5000
```
Abra `app/index.html` no navegador. Configure o token da Meta Graph API no painel para métricas de Instagram em tempo real.

---

## 📐 Ordem de Uso em uma Primeira Semana

```
Dia 1: /instalar → configura o sistema
Dia 2: /messaging-engine → define identidade verbal
Dia 3: /content-os → monta calendário do mês
Dia 4: /sales-engine → estrutura o processo de venda
Dia 5: /proposta-comercial → gera proposta com o design da marca
```

---

## 🤝 Contribuindo

Este é um sistema em evolução ativa. Skills novas são bem-vindas — seguir o padrão `.agents/skills/<nome>/SKILL.md` com YAML frontmatter `name` e `description`.
