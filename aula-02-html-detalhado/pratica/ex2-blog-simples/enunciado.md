# Prática 02 — HTML: Elementos Semânticos, Listas e Acessibilidade

## Blog Simples

Você vai construir a página inicial de um blog fictício, usando **apenas HTML** (sem CSS — isso vem na próxima unidade). O foco é usar os elementos semânticos e as boas práticas de acessibilidade vistas na aula.

O arquivo `index.html` já tem o esqueleto (`<!DOCTYPE>`, `<head>` com `meta charset`/`viewport`/`title`, `<body>` vazio). Complete o `<body>`.

---

## O que a página precisa ter

| Elemento | Descrição |
|---|---|
| `<header>` | Título do blog em `<h1>` |
| `<nav>` | Lista (`<ul>`) com 3 a 4 links de navegação (podem ser âncoras `#`) |
| `<main>` | Contém os artigos |
| 2 ou mais `<article>` | Cada um com `<h2>` (título do post), `<time>` (data) e `<p>` (texto) |
| Pelo menos 1 lista | `<ul>` ou `<ol>` dentro de algum artigo (ex: tópicos do post) |
| `<aside>` | Barra lateral com uma lista de categorias ou links úteis |
| `<footer>` | Informações de contato (link `mailto:`) |

---

## Requisitos mínimos

| Requisito | Descrição |
|---|---|
| Sem `<div>` | Toda a estrutura deve usar elementos semânticos — se você sentir necessidade de um `<div>`, pare e pense se não é um `<section>` ou `<article>` |
| Hierarquia de headings | Um único `<h1>`, depois `<h2>` em cada artigo — sem pular níveis |
| `alt` em imagens | Se adicionar alguma imagem, toda `<img>` precisa de `alt` (descritivo ou `alt=""` se for decorativa) |
| Links de navegação funcionando | Os `href="#id"` do `<nav>` devem apontar para `id`s que existem na página |
| `<time datetime="...">` | Pelo menos uma data marcada com o atributo `datetime` |

---

## Checklist de acessibilidade (antes de entregar)

1. Abra a página no Chrome, `F12` → aba **Lighthouse** → categoria *Accessibility* → **Analyze page load**.
2. Corrija os problemas apontados (nota esperada: acima de 90).
3. Confira manualmente:
   - [ ] Os headings estão em ordem lógica (sem pular de h1 para h3)?
   - [ ] Toda imagem tem `alt`?
   - [ ] Dá pra navegar pelos links só usando `Tab` no teclado?

---

## Dicas

- Comece pelo `<header>` e pelo `<nav>`, depois vá preenchendo os `<article>` um de cada vez.
- Use o exemplo `../../exemplos/01b-semantico.html` da aula como referência de estrutura.
- Não se preocupe com aparência — sem CSS a página vai ficar "feia", e está tudo bem, isso é assunto da próxima unidade.

---

## Entrega

- Arquivo `index.html` completo, na pasta `pratica/ex2-blog-simples/`.
- Print ou nota do resultado do Lighthouse (Accessibility).

A solução de referência está disponível em `pratica/ex2-blog-simples/solucao/` para consulta após a tentativa.
