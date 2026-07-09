---
name: instalar
description: >
  Instala o MazyOS no negócio do usuário. Entrevista sobre empresa, tom de voz,
  foco atual e identidade visual, e preenche `_memoria/empresa.md`, `_memoria/preferencias.md`,
  `_memoria/estrategia.md`, `identidade/design-guide.md` e adapta o `CLAUDE.md` conforme o perfil.
  Use quando o usuário acabou de clonar o repositório e quer instalar o sistema, ou quando
  pedir explicitamente "rodar /instalar", "instalar o MazyOS", "primeiro setup".
---

# /instalar — Instalação inicial do MazyOS

Esse é o primeiro comando que o usuário roda depois de clonar o repositório. Não pode falhar e não pode soar burocrático. Trata como conversa de descoberta — pergunta uma coisa por vez, escuta de verdade, não enfileira tudo. O objetivo é o sistema sair daqui sabendo quem é a empresa, como ela fala, e onde tá o atrito do dia a dia.

## Pré-checagem

### 1. Nome da pasta

Conferir o nome da pasta atual (`basename "$(pwd)"`). Se for `mazyos`, `MazyOS`, `MazyOS-main`, `mazyos-main` ou variação genérica:

> "Notei que a pasta atual ainda tem nome genérico ('<nome-atual>'). O ideal é a pasta ter o nome do seu negócio, não 'MazyOS'. Quando terminarmos o setup, te lembro de renomear (é rápido — fechar VS Code, renomear a pasta no Finder/Explorer, abrir de novo). Bora seguir?"

Registrar mentalmente o nome atual pra usar na Fase 5.

### 2. Arquivos de contexto

Conferir se algum arquivo de memória já está preenchido (não é placeholder):
- `_memoria/empresa.md`
- `_memoria/preferencias.md`
- `_memoria/estrategia.md`
- `identidade/design-guide.md`

Se algum já tiver conteúdo real, perguntar:
> "Já tem algum contexto preenchido aqui. Quer que eu sobrescreva (recomeçar do zero) ou complemente o que falta?"

Se for setup limpo, seguir direto.

---

## Fase 1 — Escolha do perfil

### 🌟 Verificação do Dossiê Done-For-You (DFY)
Antes de fazer perguntas ao usuário no chat, verifique se o arquivo `dossie_diagnostico.md` existe na raiz do workspace.
* **Se o arquivo `dossie_diagnostico.md` EXISTIR:** 
  1. A I.A. deve pular toda a **Fase 2 (Entrevista)**.
  2. Ler e processar os dados contidos no dossiê de diagnóstico.
  3. Preencher silenciosamente todos os arquivos de memória na **Fase 3 (Preenchimento)** com o maior nível de riqueza e profundidade estratégica possível.
  4. Gerar o arquivo `rag/rag_config.json` e aplicar o perfil escolhido de `CLAUDE.md`.
  5. Pular direto para a **Fase 4 (Resumo)** e apresentar o resultado configurado.
* **Se o arquivo NÃO existir:** Seguir com o fluxo normal fazendo a escolha do perfil e a entrevista manual por perguntas no chat.

Perguntar qual perfil mais combina com o negócio:

1. **Solopreneur / criador solo** — uma pessoa só, mistura de marca pessoal e negócio
2. **Freelancer** — atende clientes, organiza por projeto/cliente
3. **Agência / consultoria** — equipe pequena entregando pra vários clientes
4. **Empresa** — empresa estabelecida com setores (marketing, comercial, financeiro, etc.)

A resposta determina qual template de `CLAUDE.md` aplicar (ver `templates/perfis/`).

---

## Fase 2 — Entrevista

Fazer essas perguntas em ordem, esperando a resposta de cada uma antes de seguir. Se vier resposta vaga, repetir uma vez pedindo concretude. Não insistir mais que isso — registrar o que vier.


**Sobre o negócio:**
1. "Como você chama o que você faz? (nome da empresa, ou seu nome se for marca pessoal)"
2. "O que sua empresa entrega, em uma frase do jeito que você falaria pro vizinho?"
3. "Quem te paga? (perfil de cliente real — descreve em uma ou duas frases, sem persona genérica)"
4. "Você toca sozinho ou tem equipe? Se tem, quantos e cada um fazendo o quê?"

**Sobre voz:**
5. "Me cola um exemplo da tua escrita — uma legenda do Insta, um email pra cliente, qualquer coisa real e recente. Assim eu calibro o jeito de escrever sem precisar adivinhar."
6. "O que te dá ranço quando alguém escreve assim? (ex: 'vamos juntos!', emoji em email formal, 'caro cliente', jargão de guru, 'alavancar', 'sinergia')"

**Sobre foco:**
7. "Qual o gargalo do teu negócio hoje? O que tá segurando ele de crescer?"
8. "Se eu pudesse tirar UMA coisa que você repete toda semana das tuas costas, qual seria?"

**Sobre identidade visual:**
9. "Tem identidade visual definida ou tá no zero? Se tem, me passa as cores principais e a fonte."
**Sobre RAG e Segundo Cérebro (Diferenciais Vértice OS):**
11. "Você já usa o Obsidian como Segundo Cérebro? Se sim, me informe o caminho absoluto do seu Vault atual. Se não usa e deseja que eu crie um Vault modelo estruturado do zero na sua máquina, me informe o caminho absoluto da pasta onde quer criá-lo."
12. "Eu criei uma pasta chamada 'dados' na raiz do Vértice OS para você jogar seus documentos soltos (PDFs, DOCX, planilhas). Deseja indexar alguma outra pasta de documentos do seu computador além desta? Se sim, me informe os caminhos absolutos separados por vírgula."

---

## Fase 3 — Preenchimento dos arquivos

### `_memoria/empresa.md`
Preencher com base nas perguntas 1-4. Manter formato simples — nome, o que faz, perfil de cliente, equipe.

### `_memoria/preferencias.md`
Preencher com base nas perguntas 5-6. Estrutura:
- **Tom de voz:** derivar do exemplo de escrita real da pergunta 5 (descrever em 2-3 frases o jeito de escrever, com referência ao exemplo)
- **O que evitar:** lista direta da resposta 6
- **Estilo geral:** síntese do que combina e o que destoa

### `_memoria/estrategia.md`
Preencher com base nas perguntas 7-8. Estrutura:
- **Gargalo atual:** [resposta da 7]
- **Pra tirar das costas:** [resposta da 8] — registrar como candidata a virar skill via `/mapear-rotinas`
- **Próximas prioridades:** derivar do gargalo (o que ataca o gargalo direto)

### `identidade/design-guide.md`
Se o usuário forneceu cores/fontes/logo (perguntas 9-10), preencher os campos correspondentes. Se não, deixar como está e avisar.

### Cópia e Setup do Segundo Cérebro (Obsidian)
Se o usuário informou um caminho na pergunta 11:
1. Certifique-se de que a pasta de destino existe. Se não existir, crie-a.
2. Copie recursivamente todo o conteúdo de `templates/segundo-cerebro/` para a pasta indicada (incluindo subpastas e arquivos `.gitkeep`).
3. Se a pasta já continha um Vault Obsidian existente, copie apenas os arquivos de regras (`00-ENTRADA.md`, `SCHEMA.md`, `PROTOCOLO.md` e `fechar-sessao/SKILL.md` como atalho) para a raiz do Vault do usuário para não bagunçar a organização dele.

### `rag/rag_config.json`
Criar ou atualizar o arquivo de configuração `rag/rag_config.json` com a seguinte estrutura:
```json
{
  "obsidian_vault_path": "[resposta da 11]",
  "additional_index_paths": [
    "./_memoria",
    "./identidade",
    "./dados"[se a resposta 12 tiver caminhos extras, adicione-os aqui como caminhos absolutos]
  ]
}
```

### `CLAUDE.md` (ou `AGENTS.md`)
Pegar o template correspondente ao perfil escolhido na Fase 1 (`templates/perfis/claude-md-<perfil>.md`), adaptar com o nome do negócio e estrutura de pastas mencionada nas respostas, e sobrescrever o `CLAUDE.md` da raiz.

---

## Fase 4 — Resumo

Mostrar pro usuário o que foi configurado:

```
✓ Perfil aplicado: [perfil]
✓ Contexto do negócio: _memoria/empresa.md
✓ Tom de voz: _memoria/preferencias.md
✓ Foco atual: _memoria/estrategia.md
✓ Marca: identidade/design-guide.md  [preenchida | em branco]
✓ Segundo Cérebro (Obsidian): Configurado e estruturado no caminho [caminho]
✓ RAG local: rag/rag_config.json configurado
✓ CLAUDE.md adaptado pro perfil [perfil]
```

Se o RAG estiver configurado, instruir:
> "Para ativar a memória de longo prazo, execute no terminal:
> `python install_rag.py`   ← instala dependências
> `python rag/rag_acervo.py index`   ← indexa seu acervo
> `python rag/rag_server.py`   ← sobe o servidor (manter aberto em segundo plano)
>
> Com o servidor ativo, todos os engines do Vértice OS vão buscar contexto
> no seu segundo cérebro automaticamente antes de criar qualquer coisa."

Se o usuário disser que NÃO quer usar RAG (ex: computador sem recursos ou setup inicial básico):
> "Tudo bem — o Vértice OS funciona sem o RAG. Os engines vão usar apenas
> os arquivos de _memoria/ como contexto. Quando quiser ativar a memória
> completa, é só rodar `python install_rag.py` no futuro."

---

## Fase 5 — Renomear pasta (se necessário)

Se a pasta atual ainda tem nome genérico (detectado na Pré-checagem), gerar slug do nome da empresa (resposta da pergunta 1):
- minúsculas
- sem acentos
- espaços viram hífen
- caracteres especiais removidos

Ex: "Acme Empresa Ltda" → `acme-empresa-ltda`

Mostrar:

> "Última coisa: a pasta ainda tá com nome genérico ('<nome-atual>').
> Pra ter cara do seu negócio, recomendo renomear pra '<slug>'.
>
> Como fazer:
> 1. Fecha o VS Code
> 2. Renomeia a pasta no Finder (Mac) ou Explorer (Windows) — ou no
>    terminal fora dela: `mv <nome-atual> <slug>`
> 3. Abre o VS Code de novo na pasta renomeada
>
> Se preferir outro nome, me fala que eu ajusto a sugestão."

Se a pasta já tem nome próprio (não genérico), pular essa fase.

---

## Fase 6 — Próximos passos

> "Pronto. O Vértice OS já te conhece.
>
> Roda `/abrir` no começo de cada sessão — eu carrego todo o contexto
> antes da primeira frase.
>
> A ordem natural de uso do sistema é:
>
> 1. `/messaging-engine` — constrói sua mensagem, tese e vocabulário proprietário
>    (tudo o mais fica mais fácil depois disso)
>
> 2. `/content-os` — monta o calendário do mês conectado à sua oferta
>
> 3. `/sales-engine` — cria o roteiro de call, SPIN e follow-up
>
> 4. `/client-success` — estrutura a entrega e o plano de 90 dias
>
> 5. `/authority-engine` — expande uma ideia sua em palestra, artigo e livro
>
> 6. `/growth-engine` — diagnóstico de gargalos e prioridades de escala
>
> 7. `/research-engine` — transforma comentários e reviews em inteligência de copy
>
> Para criar conteúdo visual: `/carrossel`, `/publicar-tema`, `/aprovar-post`
> Para SEO e tráfego pago: `/seo`, `/anuncio-google`, `/relatorio-ads`
> Para vendas: `/proposta-comercial` + `/sales-engine`
>
> Você mencionou que repete '<resposta da pergunta 8>' toda semana.
> Roda `/mapear-rotinas` quando quiser transformar isso em skill automática."

Se o usuário quiser salvar e versionar no GitHub, mencionar `/salvar`.

---

## Regras

- Não inventar dados — se a resposta for vaga, registrar do jeito que veio (ou deixar placeholder claro)
- Não escrever "este arquivo será preenchido pelo /instalar" nos arquivos finais
- O setup deve durar 5-7 minutos no máximo — registrar o que veio e seguir
- Não fazer perguntas extras além das listadas acima sem motivo claro
- O RAG é OPCIONAL: se o usuário não quiser ou não tiver recursos, o sistema funciona sem ele
- Nunca bloquear o setup por falta do RAG — é um bônus, não um requisito
