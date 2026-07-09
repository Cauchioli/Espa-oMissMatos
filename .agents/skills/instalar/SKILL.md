---
name: instalar
description: >
  Instala o Vértice OS no negócio do usuário. Conduz uma entrevista de descoberta,
  configura a memória do negócio, cria o Segundo Cérebro (vault Obsidian estruturado),
  instala e indexa o RAG local, e garante que todos os sistemas estão operacionais
  antes de encerrar. Use quando o usuário acabou de clonar o repositório e quer instalar
  o sistema, ou quando pedir "rodar /instalar", "instalar o Vértice OS", "primeiro setup".
---

# /instalar — Setup Completo do Vértice OS

O `/instalar` é a única vez que o sistema precisa ser configurado do zero. O objetivo é o usuário sair daqui com tudo funcionando: memória preenchida, Segundo Cérebro estruturado, RAG indexado e servidor ativo. Não pode falhar, não pode soar burocrático.

**Trate como conversa de descoberta** — uma pergunta por vez, escuta de verdade. O sistema sai daqui sabendo quem é o negócio, como ele fala, e o Segundo Cérebro já pronto para uso.

---

## Pré-checagem

### 1. Nome da pasta
Conferir o nome da pasta atual. Se for `VerticeOS`, `vertice-os`, `MazyOS` ou variação genérica:
> "Notei que a pasta ainda tem nome genérico. O ideal é ter o nome do seu negócio. Quando terminarmos o setup, te lembro de renomear — é rápido. Bora seguir?"

### 2. Dossiê DFY (Done-For-You)
Verificar se o arquivo `dossie_diagnostico.md` existe na raiz:
- **Existe:** Ler o dossiê, pular a Fase 2 (Entrevista), preencher tudo silenciosamente e ir direto para a Fase 3.
- **Não existe:** Seguir com a entrevista normal.

### 3. Memória já preenchida
Verificar se `_memoria/empresa.md` já tem conteúdo real (não placeholder):
- **Sim:** "Já tem contexto preenchido aqui. Quer que eu sobrescreva ou complemente o que falta?"
- **Não:** Seguir direto.

---

## Fase 1 — Entrevista de Descoberta

Fazer em ordem, esperando a resposta antes de avançar. Se a resposta for vaga, pedir concretude uma vez — não insistir.

**Sobre o negócio:**
1. "Como você chama o que você faz? (nome da empresa ou seu nome se for marca pessoal)"
2. "O que sua empresa entrega, em uma frase do jeito que você falaria pro vizinho?"
3. "Quem te paga? Descreve o perfil do cliente real em uma ou duas frases."
4. "Você toca sozinho ou tem equipe? Se tem, quantos e fazendo o quê?"

**Sobre voz:**
5. "Me cola um exemplo da tua escrita — uma legenda, um email, qualquer coisa real e recente. Assim eu calibro sem adivinhar."
6. "O que te dá ranço quando alguém escreve assim? (ex: 'vamos juntos!', emoji em email formal, jargão de guru)"

**Sobre foco:**
7. "Qual o gargalo do teu negócio hoje? O que está travando o crescimento?"
8. "Se eu pudesse tirar UMA tarefa que você repete toda semana das tuas costas, qual seria?"

**Sobre identidade visual:**
9. "Tem identidade visual definida? Se sim, me passa as cores principais e a fonte. Tem logo? Joga o arquivo em `identidade/logo.png` e me confirma."

---

## Fase 2 — Perfil do Sistema

Perguntar qual perfil mais combina com o negócio:

1. **Solopreneur / criador solo** — uma pessoa só, mistura de marca pessoal e negócio
2. **Freelancer / consultor** — atende clientes, organiza por projeto
3. **Agência / consultoria** — equipe pequena entregando pra vários clientes
4. **Empresa** — empresa estabelecida com setores distintos

A resposta determina qual template de `CLAUDE.md` aplicar (ver `templates/perfis/`).

---

## Fase 3 — Preenchimento da Memória

### `_memoria/empresa.md`
Preencher com base nas perguntas 1-4: nome, o que faz, perfil de cliente, equipe.

### `_memoria/preferencias.md`
- **Tom de voz:** derivar do exemplo real (pergunta 5) — descrever em 2-3 frases o jeito de escrever
- **O que evitar:** lista direta da resposta 6
- **Estilo geral:** síntese do que combina e o que destoa

### `_memoria/estrategia.md`
- **Gargalo atual:** resposta da 7
- **Pra tirar das costas:** resposta da 8 — registrar como candidata a virar skill via `/mapear-rotinas`
- **Próximas prioridades:** derivar do gargalo

### `identidade/design-guide.md`
Se forneceu cores/fontes/logo (pergunta 9): preencher. Se não: deixar como está e avisar.

### `CLAUDE.md` / `AGENTS.md`
Pegar o template do perfil escolhido (`templates/perfis/claude-md-<perfil>.md`), adaptar com o nome do negócio e sobrescrever.

---

## Fase 4 — Setup do Segundo Cérebro (Obsidian)

> Explicar ao usuário antes de agir:
> "Agora vamos criar o seu Segundo Cérebro — o vault Obsidian onde você vai organizar o conhecimento do negócio, decisões, metodologias e histórico de sessões. Pense nele como a memória de longo prazo que a IA vai consultar toda vez que você perguntar algo sobre o seu negócio."

Perguntar:

> "Você já usa o Obsidian com um Vault existente?
> - Se **sim**: me informe o caminho absoluto da pasta do seu Vault.
> - Se **não**: me informe onde quer criar a pasta do Segundo Cérebro (ex: `C:\Documentos\MeuNegocio-Cerebro`). Eu estruturo tudo por você."

**Se vault existente (caminho fornecido):**
1. Verificar se a pasta existe. Se não, criar.
2. Copiar apenas os arquivos de regras para não bagunçar: `00-ENTRADA.md`, `01-REGRAS.md`, `02-PROTOCOLO.md`, `03-SCHEMA.md`.
3. Criar as subpastas ausentes: `10-frentes/`, `20-entidades/`, `30-metodologia/`, `40-manuais/`, `50-referencia/`, `60-estado/`, `80-arquivo/`, `90-historico/`.

**Se vault do zero (caminho fornecido):**
1. Criar a pasta no caminho informado.
2. Copiar recursivamente todo o conteúdo de `templates/segundo-cerebro/` para a pasta.
3. Confirmar ao usuário que pode abrir essa pasta no Obsidian agora.

**Atualizar `rag/rag_config.json`** com o caminho do vault:
```json
{
  "obsidian_vault_path": "[caminho informado]",
  "additional_index_paths": [
    "./_memoria",
    "./identidade",
    "./dados"
  ]
}
```

> Confirmar:
> "Segundo Cérebro criado em [caminho]. Pode abrir essa pasta no Obsidian agora — as pastas e os arquivos de regras já estão lá."

---

## Fase 5 — Instalação e Indexação do RAG

> Explicar ao usuário antes de agir:
> "Agora vamos instalar o RAG — o motor de busca semântica que indexa tudo o que você tem no Segundo Cérebro, nos arquivos do sistema e nos documentos que você jogar na pasta `dados/`. Com ele ativo, a IA não precisa que você repita nada — ela busca sozinha no seu acervo antes de responder."

### Passo 5.1 — Instalar dependências
```bash
python install_rag.py
```
> "Instalando dependências do RAG. Isso acontece uma única vez. Pode levar alguns minutos na primeira execução."

### Passo 5.2 — Indexar o Segundo Cérebro primeiro
```bash
python rag/rag_acervo.py index "[caminho do vault]" "./_memoria" "./identidade"
```
> "Indexando o Segundo Cérebro e a memória do sistema. Essa é a base do seu acervo."

### Passo 5.3 — Perguntar por pastas adicionais
> "A pasta `dados/` dentro do Vértice OS já está configurada para indexação — é o lugar padrão para você jogar PDFs, DOCX, planilhas e outros arquivos soltos que quer que a IA conheça.
>
> Você tem outras pastas no computador com documentos relevantes para o seu negócio? (ex: pasta com PDFs de cursos, contratos, playbooks, transcrições)
>
> Se sim, me informe os caminhos separados por vírgula. Se não, seguimos com o que já temos."

**Se informou caminhos extras:**
1. Adicionar cada caminho ao `rag_config.json` em `additional_index_paths`.
2. Rodar indexação dos caminhos extras:
   ```bash
   python rag/rag_acervo.py index "[caminho1]" "[caminho2]"
   ```
   > "Indexando [N] pastas adicionais. A IA vai consultar esses documentos quando for relevante."

**Nota sobre organização** (apenas se o usuário tiver muitos documentos espalhados):
> "Dica: documentos organizados em pastas temáticas são indexados com mais precisão. Se você tiver arquivos muito espalhados em pastas diferentes, considere consolidar os mais importantes em `dados/` — isso melhora a velocidade e a relevância das buscas."

### Passo 5.4 — Subir o servidor do RAG
```bash
python rag/rag_server.py
```
> "Servidor do RAG ativo na porta 8799. A partir de agora, toda vez que a IA for responder algo sobre o seu negócio, ela vai buscar contexto no seu acervo antes de gerar a resposta."

> "**Importante:** o servidor do RAG precisa estar rodando em segundo plano para funcionar. Quando reiniciar o computador, rode `python rag/rag_server.py` antes de começar a trabalhar — ou use o atalho `rag/iniciar_rag.bat` (Windows)."

---

## Fase 6 — Verificação Final (Sistema Completo)

Executar checklist silencioso e mostrar o resultado:

```
VÉRTICE OS — INSTALAÇÃO CONCLUÍDA

✓ Memória do negócio:  _memoria/ preenchida
✓ Identidade visual:   identidade/design-guide.md [preenchida | em branco]
✓ Perfil aplicado:     [perfil]
✓ Segundo Cérebro:     [caminho do vault] — [N] pastas estruturadas
✓ RAG instalado:       dependências OK
✓ RAG indexado:        [N] documentos indexados
✓ RAG servidor:        http://127.0.0.1:8799 — ONLINE
✓ Pasta de dados:      dados/ pronta para receber arquivos
```

Se algum item falhou, indicar exatamente o que falhou e como corrigir.

---

## Fase 7 — Próximos passos

> "Pronto. O Vértice OS já te conhece.
>
> Roda `/abrir` no começo de cada sessão — eu carrego todo o contexto antes da primeira frase.
>
> A ordem natural de uso do sistema:
>
> 1. `/messaging-engine` — constrói sua mensagem, tese e vocabulário proprietário
> 2. `/content-os` — monta o calendário do mês conectado à sua oferta
> 3. `/sales-engine` — cria o roteiro de call, SPIN e follow-up
> 4. `/client-success` — estrutura a entrega e o plano de 90 dias
> 5. `/authority-engine` — expande uma ideia em palestra, artigo e livro
> 6. `/growth-engine` — diagnóstico de gargalos e prioridades de escala
> 7. `/research-engine` — transforma comentários e reviews em inteligência de copy
>
> Para conteúdo visual: `/carrossel`, `/publicar-tema`, `/aprovar-post`
> Para vendas: `/proposta-comercial` + `/sales-engine`
> Para SEO e tráfego: `/seo`, `/anuncio-google`, `/relatorio-ads`
>
> Você mencionou que repete '[resposta da pergunta 8]' toda semana.
> Roda `/mapear-rotinas` quando quiser transformar isso em skill automática.
>
> Para renomear a pasta com o nome do seu negócio: feche o editor, renomeie a pasta no Explorer/Finder, abra novamente."

---

## Fase 8 — Renomear pasta (se necessário)

Se a pasta ainda tem nome genérico, gerar o slug do nome da empresa:
- Minúsculas, sem acentos, espaços viram hífen, caracteres especiais removidos
- Ex: "Acme Consultoria" → `acme-consultoria`

Mostrar as instruções de renomeação ao final da mensagem da Fase 7.

---

## Regras Absolutas

- Não inventar dados — registrar o que veio, mesmo que vago
- Não bloquear o setup por falta de qualquer etapa — cada fase pode ser pulada e feita depois
- **A única exceção:** se o RAG falhar na instalação, informar o erro exato e sugerir o comando de diagnóstico (`python install_rag.py --verbose`)
- O setup completo deve durar entre 8 e 12 minutos — mais que isso indica fricção que precisa ser resolvida
- Não fazer perguntas fora do roteiro sem motivo explícito
- Ao final da instalação, confirmar que o `/abrir` está pronto para uso
