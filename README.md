# Vértice OS — Sistema Operacional de Negócios por I.A.

O **Vértice OS** é um ecossistema integrado que transforma IAs generativas em assistentes executivos focados no contexto real de um negócio. Ao contrário de soluções que usam apenas prompts estáticos, o Vértice OS combina o **Segundo Cérebro** (Obsidian) com **RAG Local de Acervo**, **Métricas de Performance** (Facebook/Instagram Graph API) e um **Dashboard Web interativo** em circuito fechado.

---

## 🗺️ Estrutura do Repositório

O repositório é organizado de forma modular para facilitar a implantação na máquina do cliente final:

```
├── .agents/                 # Regras do Agente & Motores de Habilidades (Skills)
│   ├── AGENTS.md            # Leis operacionais e regras de design
│   └── skills/              # As 15 skills operacionais (SEO, Ads, Posts, E-mails...)
├── _memoria/                # Contexto estratégico do negócio (populado pelo Obsidian)
│   ├── empresa.md           # Fatos, serviços, ferramentas e equipe
│   ├── estrategia.md        # Gargalos atuais, metas e prioridades
│   └── preferencias.md      # Tom de voz, escrita e diretrizes de estilo
├── identidade/              # Design System do Cliente
│   └── design-guide.md      # Cores hexadecimais, fontes e caminhos de logo
├── app/                     # Painel Visual de Controle
│   ├── app_backend.py       # Servidor local Flask/FastAPI (Porta 5000)
│   ├── index.html           # SPA Dashboard (Kanban de ideias, leads e métricas)
│   ├── crm_database.json    # Banco de dados leve dos Leads capturados
│   └── instagram_cache.json # Cache de performance de posts e engajamento
├── rag/                     # Módulo RAG Local
│   └── rag_acervo.py        # Script Python para indexar notas e playbooks do Obsidian
└── README.md                # Este guia
```

---

## 🧠 1. Configurando o Segundo Cérebro (Obsidian)

O Obsidian funciona como a interface de texto do cliente. É onde ele descarrega playbooks, roteiros, anotações de reuniões e relatórios.

1. Baixe e instale o [Obsidian](https://obsidian.md/).
2. Crie um novo Vault (Cofre) chamado `Memorias-Pessoal` ou aponte para a pasta de notas estratégicas da empresa.
3. Copie o arquivo [.agents/AGENTS.md](file:///.agents/AGENTS.md) para a raiz do vault Obsidian. Ele instruirá qualquer agente de IA (como Claude Code, Gemini ou ChatGPT integrado) sobre as regras de comportamento corporativas da marca.

---

## 🔍 2. Configurando o RAG Local (Acervo Seguro)

Para que a IA tenha acesso semântico inteligente a todas as notas do cliente sem vazar dados para a internet, configuramos o RAG local.

1. Vá para a pasta `/rag` do repositório:
   ```bash
   cd rag
   ```
2. Instale o ambiente virtual Python e as dependências:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # No Windows
   pip install -r requirements.txt
   ```
3. Para indexar as notas do Obsidian na primeira vez ou atualizar o banco semântico local, execute:
   ```bash
   python rag_acervo.py index
   ```

---

## 🖥️ 3. Iniciando o Painel de Controle (Vértice App)

O painel centraliza as métricas de redes sociais, funil de conversão (CRM) e o pipeline de produção de conteúdo.

1. Vá para a pasta `/app` e inicie o backend Python (Porta 5000):
   ```bash
   python app_backend.py
   ```
2. Abra o arquivo `index.html` em seu navegador para acessar a central de comando visual.
3. No painel, configure o token da Graph API do Meta (Facebook/Instagram) clicando em **Configurar Token** na aba de métricas para obter dados dinâmicos de engajamento ao vivo.
