# Prática 02 — HTML: Elementos Semânticos, Listas e Acessibilidade

## Página Pessoal

Você vai construir uma página de apresentação pessoal, usando **apenas HTML** (sem CSS — isso vem na próxima unidade).

O arquivo `index.html` já tem o esqueleto (`<!DOCTYPE>`, `<head>` com `meta charset`/`viewport`/`title`, `<body>` vazio). Complete o `<body>`.

---

## Requisitos mínimos

| Requisito | Descrição |
|---|---|
| `<header>` | Seu nome em `<h1>` |
| `<nav>` | Menu interno (âncoras `#`) para as seções da página |
| `<main>` | Envolve todo o conteúdo principal |
| Seção "Sobre mim" | `<section>` com `<h2>` e um parágrafo de apresentação |
| Lista de hobbies/interesses | `<ul>` ou `<ol>`, dentro de uma seção |
| Link de contato | `<a href="mailto:...">` |
| `<footer>` | Rodapé com copyright |

---

## Desafios extras

- Adicione uma imagem sua (pode ser um placeholder) com `alt` bem escrito
- Adicione uma segunda seção, por exemplo "Projetos", com uma lista ordenada
- Valide seu HTML no [W3C Validator](https://validator.w3.org/)

---

## Checklist de acessibilidade (antes de entregar)

1. Abra a página no Chrome, `F12` → aba **Lighthouse** → categoria *Accessibility* → **Analyze page load**.
2. Corrija os problemas apontados (nota esperada: acima de 90).
3. Confira manualmente:
   - [ ] Um único `<h1>` na página, headings depois em ordem lógica?
   - [ ] Toda imagem tem `alt`?
   - [ ] Os links do `<nav>` levam para as seções certas?

---

## Dicas

- Use o exemplo `../../exemplos/02-pagina-completa.html` da aula como ponto de partida.
- Sem `<div>` — se sentir necessidade de um, veja se não é um `<section>`.

---

## Entrega

- Arquivo `index.html` completo, na pasta `pratica/ex1-pagina-pessoal/`.
- Print ou nota do resultado do Lighthouse (Accessibility).

A solução de referência está disponível em `pratica/ex1-pagina-pessoal/solucao/` para consulta após a tentativa.
