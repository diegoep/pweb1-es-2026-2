---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('images/background.png')
footer: 'HTML Detalhado: Elementos Semânticos, Listas, Imagens e Acessibilidade'
style: |
  section {
    font-size: 28px;
    background-size: cover;
    background-position: center;
  }
  section.capa {
    position: relative;
  }
  section.capa p {
    margin: 0;
    padding: 0;
  }
  h1 {
    color: #186fad;
  }
  h2 {
    color: #186fad;
  }
  h3 {
    color: #22acd5;
  }
  strong {
    color: #186fad;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
  footer {
    background-color: #186fad;
    color: white;
  }
  code {
    background-color: #f0f0f0;
    padding: 2px 6px;
    border-radius: 3px;
  }
---

<!-- _class: capa -->
<!-- _paginate: false -->
<!-- _footer: '' -->
<!-- _backgroundImage: url('images/capa.png') -->

# 2. HTML Detalhado: Elementos Semânticos, <br>Listas, Imagens e Acessibilidade
## Programação Web I (2026.2)

### Prof. Diego Pessoa / Prof. Wallennon Dunga

---

# Roteiro

- Elementos semânticos na prática (recapitulando a aula 1)
- Elementos textuais e formatação
- Trabalhando com listas
- Links e navegação
- Imagens e elementos multimídia
- Entidades HTML e caracteres especiais
- Acessibilidade básica, na prática
- Exemplo prático completo
- Boas práticas, validação e auditoria de acessibilidade
- Exercícios práticos

---

<!-- _header: 'Elementos Semânticos' -->

# Relembrando: Elementos Semânticos

### **Na aula 1 vimos o "porquê". Hoje vamos ao "como".**

<div class="columns">
<div>

### **Estrutura da página**

- `<header>` `<nav>` `<main>` `<footer>`

### **Conteúdo**

- `<section>` `<article>` `<aside>` `<figure>`

</div>
<div>

### **Ganhos**

- Acessibilidade (leitores de tela)
- SEO
- Código legível e manutenível

</div>
</div>

---

# "Div Soup" vs HTML Semântico

<div class="columns">
<div>

### **❌ Antes (só div)**

```html
<div class="topo">
  <div class="titulo">Meu Blog</div>
  <div class="menu">...</div>
</div>
<div class="conteudo">
  <div class="post">...</div>
</div>
<div class="rodape">...</div>
```

</div>
<div>

### **✅ Depois (semântico)**

```html
<header>
  <h1>Meu Blog</h1>
  <nav>...</nav>
</header>
<main>
  <article>...</article>
</main>
<footer>...</footer>
```

</div>
</div>

*O navegador (e o leitor de tela) não entende `class="menu"`, mas entende `<nav>`!*

---

# Quando usar cada elemento?

<div class="columns">
<div>

### **Estrutura (uma vez por página)**

- `<header>` - topo da página ou de uma seção
- `<nav>` - blocos de links de navegação
- `<main>` - conteúdo principal (só um por página)
- `<footer>` - rodapé da página ou de uma seção

</div>
<div>

### **Conteúdo (podem se repetir)**

- `<section>` - agrupamento temático com título
- `<article>` - conteúdo independente e reutilizável
- `<aside>` - conteúdo relacionado, mas secundário
- `<figure>`/`<figcaption>` - mídia com legenda

</div>
</div>

---

# `<section>` vs `<article>` vs `<div>`

### **A regra prática**

<div class="columns">
<div>

- **`<article>`** — faria sentido sozinho fora da página? (um post de blog, uma notícia, um card de produto)
- **`<section>`** — é um bloco temático da página, geralmente com um `<h2>`/`<h3>` de título

</div>
<div>

- **`<div>`** — só quando não há nenhum significado semântico (ex.: um wrapper só para aplicar CSS/Grid)

</div>
</div>

*Na dúvida: primeiro pense em `article`/`section`, e use `div` só como último recurso.*

---

<!-- _header: 'Elementos Textuais' -->

# Títulos (Headings)

### **Estrutura hierárquica dos títulos**

<div class="columns">
<div>

```html
<h1>Título Principal</h1>
<h2>Seção</h2>
<h3>Subseção</h3>
<h4>Sub-subseção</h4>
```

</div>
<div>

### **Boas práticas**

- Usar apenas um `<h1>` por página
- Manter hierarquia lógica
- Não pular níveis (h1 → h3)
- Usar para estrutura, não tamanho

</div>
</div>

*Os títulos formam o "sumário" que leitores de tela usam para navegar pela página!*

---

# Parágrafos e Formatação de Texto

### **Elementos básicos para textos**

<div class="columns">
<div>

```html
<p>Este é um parágrafo normal.</p>

<p>Texto com <strong>ênfase forte</strong>
   e <em>ênfase simples</em>.</p>

<p>Para quebrar<br>linha usamos br.</p>
```

</div>
<div>

### **Elementos semânticos**

- `<p>` - Parágrafo
- `<strong>` - Importância
- `<em>` - Ênfase
- `<mark>` - Destaque
- `<small>` - Texto pequeno
- `<br>` - Quebra de linha

</div>
</div>

*Prefira elementos semânticos como `<strong>` e `<em>` em vez de `<b>` e `<i>`!*

---

# Mais Elementos Textuais

### **Elementos especiais para diferentes tipos de conteúdo**

<div class="columns">
<div>

```html
<blockquote>
  Esta é uma citação longa
  de um texto importante.
</blockquote>

<code>var x = 10;</code>

<pre>
  Texto pré-formatado
  mantém espaços
</pre>

<del>Texto removido</del>
<ins>Texto inserido</ins>
```

</div>
<div>

### **Elementos especiais**

- `<blockquote>` - Citações
- `<code>` - Código inline
- `<pre>` - Texto pré-formatado
- `<del>` / `<ins>` - Remoção/inserção
- `<sup>` / `<sub>` - Sobre/subscrito

</div>
</div>

---

<!-- _header: 'Listas' -->

# Listas Não Ordenadas

### **Listas com marcadores (bullets)**

<div class="columns">
<div>

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3
    <ul>
      <li>Subitem 1</li>
      <li>Subitem 2</li>
    </ul>
  </li>
</ul>
```

</div>
<div>

### **Características**

- `<ul>` - Lista não ordenada
- `<li>` - Item da lista
- Pode ser aninhada

### **Quando usar?**

- Menus de navegação
- Itens sem ordem específica

</div>
</div>

---

# Listas Ordenadas

### **Listas numeradas e sequenciais**

<div class="columns">
<div>

```html
<ol>
  <li>Primeiro passo</li>
  <li>Segundo passo</li>
</ol>

<ol type="A">
  <li>Item A</li>
</ol>

<ol start="5">
  <li>Item 5</li>
</ol>
```

</div>
<div>

### **Atributos especiais**

- `type="1|A|a|I|i"` - Estilo
- `start="5"` - Inicia no número 5

### **Quando usar?**

- Passos de um tutorial
- Instruções sequenciais

</div>
</div>

---

# Listas de Definição

### **Listas para termos e definições**

<div class="columns">
<div>

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>

  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

</div>
<div>

### **Elementos**

- `<dl>` - Lista de definição
- `<dt>` - Termo
- `<dd>` - Definição

### **Quando usar?**

- Glossários, FAQ, dicionários

</div>
</div>

---

<!-- _header: 'Links e Navegação' -->

# Links Básicos

### **Conectando páginas e recursos**

<div class="columns">
<div>

```html
<a href="https://ifpb.edu.br">Site do IFPB</a>

<a href="sobre.html">Página Sobre</a>

<a href="https://google.com" target="_blank">
  Google (nova aba)
</a>

<a href="mailto:contato@ifpb.edu.br">
  Enviar email
</a>
```

</div>
<div>

### **Tipos de links**

- **Externos** / **Internos** / **Âncoras**
- **Email** (`mailto:`) / **Telefone** (`tel:`)

### **Atributo target**

- `_blank` - Nova aba
- `_self` - Mesma aba (padrão)

</div>
</div>

---

# Âncoras e Navegação Interna

### **Links dentro da mesma página**

<div class="columns">
<div>

```html
<nav>
  <ul>
    <li><a href="#introducao">Introdução</a></li>
    <li><a href="#conteudo">Conteúdo</a></li>
  </ul>
</nav>

<section id="introducao">
  <h2>Introdução</h2>
  <p>Texto da introdução...</p>
</section>
```

</div>
<div>

### **Como funciona**

- Use `id` nos elementos de destino
- Links com `href="#id"`
- Ótimo para páginas longas e para
  "pular para o conteúdo" (acessibilidade!)

</div>
</div>

---

<!-- _header: 'Elementos Multimídia' -->

# Imagens

### **Incorporando imagens nas páginas**

<div class="columns">
<div>

```html
<img src="foto.jpg" alt="Desc. da imagem">

<img src="logo.png" alt="Logo da empresa"
     width="200" height="100">

<figure>
  <img src="grafico.png" alt="Gráfico de vendas">
  <figcaption>Vendas do 1º trimestre
  </figcaption>
</figure>
```

</div>
<div>

### **Atributos essenciais**

- `src` - Caminho da imagem
- `alt` - Texto alternativo (essencial!)
- `width`/`height` - Dimensões

### **Formatos comuns**

- **JPEG/PNG/WebP/SVG**

</div>
</div>

---

<!-- _header: 'Entidades HTML' -->

# Entidades HTML e Caracteres Especiais

### **Representando caracteres especiais**

<div class="columns">
<div>

```html
&lt; &gt; &amp; &quot; &#039;

&copy; &reg; &trade;

&nbsp; &mdash; &ndash;

&ccedil; &atilde; &aacute;
```

</div>
<div>

### **Resultado**

- `&lt;` → < &nbsp; `&gt;` → >
- `&amp;` → &  &nbsp; `&copy;` → ©
- `&nbsp;` → espaço
- `&ccedil;` → ç &nbsp; `&atilde;` → ã

</div>
</div>

---

<!-- _header: 'Acessibilidade Básica' -->

# Acessibilidade na Prática: Texto Alternativo

<div class="columns">
<div>

### **Imagem informativa**

```html
<img src="grafico-vendas.png"
     alt="Gráfico mostrando aumento de
          30% nas vendas em 2026">
```

### **Imagem decorativa**

```html
<img src="linha-decorativa.png" alt="">
```

</div>
<div>

### **Regra prática**

- Se a imagem **transmite informação**,
  descreva o que ela mostra
- Se é **só decoração**, use `alt=""`
  (nunca omita o atributo!)
- Evite "imagem de..." — vá direto ao ponto

</div>
</div>

---

# Acessibilidade na Prática: Hierarquia e Landmarks

<div class="columns">
<div>

### **Hierarquia de headings**

- Um leitor de tela lista os headings
  como um sumário
- Pular de `<h1>` pra `<h4>` quebra
  essa navegação

</div>
<div>

### **Landmarks (elementos semânticos)**

- `<nav>`, `<main>`, `<aside>`, `<footer>`
  viram **atalhos de navegação**
- Usuário pode "pular direto para
  o conteúdo principal"

</div>
</div>

*É por isso que elementos semânticos e acessibilidade andam juntos!*

---

# Acessibilidade na Prática: Contraste e Teclado

<div class="columns">
<div>

### **Contraste de cores**

- Mínimo recomendado (WCAG AA): **4,5:1**
  entre texto e fundo
- Texto cinza claro em fundo branco
  costuma falhar

</div>
<div>

### **Navegação por teclado**

- Todo link/botão precisa ser
  alcançável com **Tab**
- O foco (contorno ao navegar) não
  deve ser removido no CSS

</div>
</div>

---

# Auditoria Automática de Acessibilidade

### **Ferramentas para testar o que você construiu**

<div class="columns">
<div>

### **Lighthouse (Chrome DevTools)**

- `F12` → aba **Lighthouse** → categoria
  *Accessibility* → **Analyze page load**
- Gera nota + lista de problemas com
  explicação de cada um

</div>
<div>

### **Outras opções**

- **[axe DevTools](https://www.deque.com/axe/devtools/)** - extensão de navegador
- **[WAVE](https://wave.webaim.org/)** - avaliação visual direto na página

</div>
</div>

*Rode antes de entregar qualquer exercício — é rápido e pega erros bobos (alt faltando, contraste, heading fora de ordem).*

---

<!-- _header: 'Exemplo Prático Completo' -->

# Exemplo Prático: Integrando Todos os Conceitos
<!-- _footer: '' -->

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Página Completa</title>
</head>
<body>
    <header>
        <h1>Meu Site Pessoal</h1>
        <nav>
            <ul>
                <li><a href="#sobre">Sobre</a></li>
                <li><a href="#projetos">Projetos</a></li>
                <li><a href="#contato">Contato</a></li>
            </ul>
        </nav>
    </header>
```

*`<header>` + `<nav>` no topo: landmark que leitores de tela reconhecem de cara.*

---

# Exemplo Prático: Integrando Todos os Conceitos

### **Seções de conteúdo**
<!-- _footer: '' -->
```html
    <main>
        <section id="sobre">
            <h2>Sobre Mim</h2>
            <p>Sou um <strong>desenvolvedor web</strong> apaixonado
               por <em>tecnologia</em>.</p>
            <img src="perfil.jpg" alt="Foto de perfil sorrindo, fundo azul" width="200">
        </section>

        <section id="projetos">
            <h2>Projetos</h2>
            <ol>
                <li>Site de Portfólio</li>
                <li>Sistema de Gestão</li>
            </ol>
        </section>
    </main>
```

*`<main>` só aparece uma vez: é "pule direto pro conteúdo" para quem usa leitor de tela.*

---

# Exemplo Prático: Integrando Todos os Conceitos

### **Contato e rodapé**

```html
        <section id="contato">
            <h2>Contato</h2>
            <p>Email:
               <a href="mailto:contato@exemplo.com">contato@exemplo.com</a>
            </p>
        </section>

    <footer>
        <p>&copy; 2026 - Todos os direitos reservados</p>
    </footer>
</body>
</html>
```

*Uma página inteira sem nenhum `<div>` — e mais fácil de navegar por isso.*

---

<!-- _header: 'Validação e Boas Práticas' -->

# Boas Práticas em HTML

### **Princípios para código de qualidade**

<div class="columns">
<div>

### **Estrutura e semântica**

- Elementos semânticos apropriados
- Hierarquia lógica de títulos
- `alt` em toda imagem

</div>
<div>

### **Qualidade do código**

- Indentação consistente
- Atributos sempre entre aspas
- Fechar todas as tags corretamente

</div>
</div>

---

# Ferramentas de Validação e Acessibilidade
<!-- _footer: '' -->

<div class="columns">
<div>

### **Validação de código**

- **[W3C Markup Validator](https://validator.w3.org/)**
- **[HTML5 Validator](https://html5.validator.nu/)**

</div>
<div>

### **Auditoria de acessibilidade**

- **Lighthouse** (já vem no Chrome)
- **[axe DevTools](https://www.deque.com/axe/devtools/)**
- **[WAVE](https://wave.webaim.org/)**

</div>
</div>

### **Processo de desenvolvimento**

1. Escrever HTML semântico → 2. Validar → 3. Rodar auditoria de acessibilidade → 4. Testar navegação por teclado

---

<!-- _header: 'Exercícios Práticos' -->
<!-- _footer: '' -->
# Exercício 1: Página Pessoal

### **Crie sua página pessoal**

### **Requisitos mínimos:**

<div class="columns">
<div>

- Estrutura HTML5 completa com `<!DOCTYPE html>`
- `<header>`, `<main>` e `<footer>` (elementos semânticos, não `<div>`)
- Seção "Sobre mim" com parágrafo de apresentação
- Lista de seus hobbies ou interesses
- Link para seu email

</div>
<div>

### **Desafios extras:**

- Adicione uma imagem sua com `alt` bem escrito
- Crie um menu de navegação interno (`<nav>` + âncoras)
- Rode o **Lighthouse (Accessibility)** e corrija os problemas apontados
- Valide seu HTML no W3C Validator

</div>
</div>

---

# Exercício 2: Blog Simples
<!-- _footer: '' -->
<div class="columns">
<div>

- **Cabeçalho com título do blog**
  Use `<header>` e `<h1>` para o título principal.

- **Menu de navegação com 3-4 links**
  Utilize `<nav>` com uma lista `<ul>` de links `<a>`.

- **Pelo menos 2 artigos**
  Cada artigo em `<article>`, com `<h2>`, `<time>`, `<p>` e listas.
</div>
<div>

- **Barra lateral com informações adicionais**
  Use `<aside>` para categorias ou links úteis.

- **Rodapé com informações de contato**
  Utilize `<footer>`.

- **Checklist de acessibilidade:** headings em ordem, `alt` em toda imagem, e o resultado do Lighthouse anexado à entrega.
</div>
</div>

---

<!-- _header: 'Conclusão' -->

# Resumo da Aula

### **O que aprendemos hoje?**

<div class="columns">
<div>

### **Conceitos fundamentais**

- Elementos semânticos na prática
- `section` vs `article` vs `div`
- Elementos textuais, listas e links
- Imagens e entidades HTML

</div>
<div>

### **Acessibilidade aplicada**

- `alt` informativo vs decorativo
- Hierarquia de headings e landmarks
- Contraste e navegação por teclado
- Auditoria com Lighthouse/axe/WAVE

</div>
</div>

---

# Recursos para Continuar Aprendendo

<div class="columns">
<div>

### **Documentação essencial**

- **[MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/HTML)** - Referência completa
- **[HTML Living Standard](https://html.spec.whatwg.org/)** - Especificação oficial

### **Ferramentas**

- **[W3C Validator](https://validator.w3.org/)**
- **[CodePen](https://codepen.io/)** - Testes online

</div>
<div>

### **Acessibilidade**

- **[The A11y Project](https://www.a11yproject.com/)** - checklist prática
- **[WebAIM](https://webaim.org/)** - artigos e ferramentas

### **Prática**

- **[Frontend Mentor](https://frontendmentor.io/)** - Desafios reais

</div>
</div>

---

<!-- _class: lead -->

# Obrigado!

## **Perguntas?**

*"Elementos semânticos e acessibilidade não são 'extra' — são a diferença entre uma página que só parece certa e uma que funciona para todo mundo."*
