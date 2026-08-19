# Prática 03 — HTML: Formulários e Multimídia

## Formulário de Inscrição em Evento

Você vai construir a página de inscrição de um evento (real ou inventado: semana de tecnologia, maratona de programação, show, campeonato...), usando **apenas HTML** — o CSS básico já está no esqueleto.

O arquivo `index.html` já tem o esqueleto pronto. Complete o `<body>`.

---

## Requisitos mínimos

| Requisito | Descrição |
|---|---|
| `<form>` | Com `action="#"` e `method="post"` |
| Dados pessoais | Nome, email e telefone — cada um com o `type` correto |
| Data de nascimento | `input type="date"` |
| Tipo de ingresso | Radio buttons agrupados em `fieldset` + `legend` |
| Quantidade | `input type="number"` com `min` e `max` |
| Interesses | Pelo menos 3 checkboxes |
| Comentários | `textarea` |
| `<label>` | Associado a **todos** os campos (via `for`/`id` ou envolvendo o campo) |
| Validação HTML5 | `required` nos campos obrigatórios; `minlength`/`pattern` onde fizer sentido |
| Vídeo de divulgação | Um `<video>` ou um `<iframe>` do YouTube, com `title` descritivo, antes do formulário |
| Botões | `submit` e `reset`, com `type` explícito |

---

## Desafios extras

- Adicione `autocomplete` (`name`, `email`, `tel`) e `inputmode="numeric"` no telefone
- Adicione um `select` de estado (UF) com pelo menos 5 opções
- Adicione um `datalist` com sugestões de "como conheceu o evento"
- Adicione um `<audio>` com o jingle do evento (pode usar o áudio de exemplo da aula)
- Upload de comprovante: `input type="file"` com `accept` (lembre do `enctype` no form!)

---

## Checklist (antes de entregar)

- [ ] Ao enviar vazio, o navegador bloqueia e aponta os campos obrigatórios?
- [ ] Só é possível marcar **um** tipo de ingresso (radios com o mesmo `name`)?
- [ ] Clicar no texto de cada label ativa o campo correspondente?
- [ ] O vídeo/iframe tem `title` ou fallback?
- [ ] O HTML passa no [W3C Validator](https://validator.w3.org/) sem erros?

---

## Dicas

- Consulte os exemplos da aula: `../../exemplos/05-formulario-inputs.html`, `06-formulario-selecao.html` e `07-video-audio.html`.
- Teste o formulário também no celular (ou no modo responsivo do DevTools) e repare nos teclados diferentes por tipo de campo.

---

## Entrega

- Arquivo `index.html` completo, na pasta `pratica/ex2-formulario-inscricao/`.

A solução de referência está disponível em `pratica/ex2-formulario-inscricao/solucao/` para consulta após a tentativa.
