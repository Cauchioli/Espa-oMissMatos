---
name: site-cliente
description: Cria sites e landing pages premium para clientes da Vértice OS. Segue o fluxo wireframe → plano de design → código final com as diretrizes de estética frontend da Anthropic. Use quando o usuário pedir "criar site para [cliente]", "landing page para [nicho]", "página de vendas", "/site-cliente" ou descrever um projeto de site.
---

# Skill: /site-cliente

## Objetivo
Criar sites e landing pages visualmente distintos, rápidos e de alta conversão para clientes do Vértice OS — sem cair no "AI slop aesthetic" (layouts genéricos, roxo em fundo branco, Inter em tudo, sem personalidade).

O fluxo tem 3 etapas obrigatórias antes de escrever uma linha de código.

---

## Etapa 0 — Carregar Contexto
Antes de começar, ler:
- `_memoria/empresa.md` — quem é o Leo e o negócio dele
- `identidade/design-guide.md` — paleta, tipografia e padrões visuais da Vértice

---

## Etapa 1 — Briefing Rápido (5 perguntas)

Fazer as perguntas abaixo em uma única mensagem, numeradas:

```
1. Qual é o nome do projeto/cliente e o nicho de atuação?
2. Qual é o objetivo principal da página? (capturar lead, vender produto, institucional, portfólio...)
3. Existe alguma referência visual que o cliente admira? (site, marca, estilo — pode ser concorrente ou de outro setor)
4. Qual é a paleta de cores da marca do cliente, se existir? (ou posso sugerir uma)
5. Qual é o CTA principal da página? (ex: "Agendar consulta", "Comprar agora", "Entrar em contato")
```

Aguardar as respostas antes de prosseguir.

---

## Etapa 2 — Wireframe Textual

Com base no briefing, gerar um **wireframe em texto puro** (sem código) descrevendo a estrutura de cada seção da página:

```
WIREFRAME — [Nome do Projeto]

[ HEADER ]
- Logo à esquerda | Nav links à direita
- CTA button no canto direito: "[texto do CTA]"

[ HERO ]
- Headline principal (máx. 8 palavras, em UPPERCASE)
- Subheadline (1 frase de suporte, max 15 palavras)
- CTA primário + prova social discreta abaixo (ex: "127 empresas atendidas")
- Elemento visual à direita: [descrever — foto, ilustração, mockup, abstrato]

[ SEÇÃO X ]
...
```

Apresentar o wireframe e perguntar: **"Quer ajustar alguma seção ou posso partir para o código?"**

Aguardar aprovação antes de prosseguir.

---

## Etapa 3 — Geração do HTML Premium

### Regras de Estética Obrigatórias (Anthropic Frontend Aesthetics Protocol)

> Fonte: https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb

Ao gerar o código HTML/CSS, aplicar **todas** as diretrizes abaixo sem exceção:

#### Tipografia
- **Proibido**: Arial, Roboto, Inter como fonte principal, system-ui genérico
- **Obrigatório**: escolher uma combinação distinta do Google Fonts que seja coerente com o nicho
  - Exemplos bons: `Syne + DM Sans`, `Cormorant Garamond + Epilogue`, `Playfair Display + Nunito`, `Bebas Neue + Lato`
  - Variar entre light e dark themes; não convergir sempre para os mesmos padrões
- Títulos em peso 700–800, corpo em 400–500, usar `letter-spacing` para headlines em uppercase

#### Cor e Tema
- **Proibido**: gradientes roxo/lavanda em fundo branco (o default genérico da IA)
- **Obrigatório**: definir variáveis CSS (`--color-primary`, `--color-accent`, `--color-bg`) antes de qualquer outra coisa
- Usar uma cor dominante forte com 1-2 acentos nítidos
- Inspirar-se em: temas de IDE (Dracula, Catppuccin, Tokyo Night), estéticas culturais (brutalismo editorial, japandi, art deco moderno)

#### Motion / Animações
- Priorizar CSS puro (sem bibliotecas externas, exceto se o cliente pedir)
- Foco em **1 animação de impacto no carregamento** com `animation-delay` escalonado (staggered reveal das seções)
- Micro-interações nos botões (`:hover`, `:active`), links e cards
- Evitar animações em todo lugar — menos é mais, mas o que tiver deve ser cirúrgico

#### Backgrounds
- **Proibido**: fundos sólidos brancos ou cinzas sem textura
- **Obrigatório**: criar atmosfera com uma das abordagens:
  - Gradiente radial sutil no hero
  - Padrão SVG de grid (cruzinhas ou pontos em opacidade baixa)
  - Noise texture via CSS `filter` ou SVG `feTurbulence`
  - Formas geométricas grandes com baixa opacidade no fundo

#### Estrutura do HTML
- Todo o código em **arquivo único** (`index.html`) com CSS no `<style>` e JS no `<script>`
- Responsivo desde a base: breakpoint principal em `768px`
- Sem frameworks externos CSS (Tailwind, Bootstrap) — vanilla CSS com variáveis
- Sempre incluir: `<meta name="description">`, `<title>` descritivo, `lang="pt-BR"`
- IDs únicos em todos os elementos interativos

---

## Etapa 4 — Entrega Final

Após gerar o código:

1. Indicar o **caminho onde salvar o arquivo** (sugerir criar uma pasta em `saidas/sites/[nome-cliente]/`)
2. Listar as **3 principais decisões de design** tomadas e por quê
3. Perguntar: **"Quer ajustar paleta, tipografia ou alguma seção específica?"**

---

## Quando NÃO usar esta skill
- Para carrosséis de Instagram → usar `/carrossel`
- Para propostas comerciais A4 → usar `/proposta-comercial`
- Para artigos de blog → usar `/publicar-tema`
