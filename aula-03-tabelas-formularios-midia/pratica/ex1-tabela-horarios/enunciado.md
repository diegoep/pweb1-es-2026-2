# Prática 03 — HTML: Tabelas

## Tabela de Horários

Você vai construir a tabela de horários da sua turma neste semestre, usando **apenas HTML** (o CSS já está pronto no esqueleto — não é preciso mexer nele).

O arquivo `index.html` já tem o esqueleto (`<!DOCTYPE>`, `<head>` completo e um `<style>` básico para a tabela ficar legível). Complete o `<body>`.

---

## Requisitos mínimos

| Requisito | Descrição |
|---|---|
| `<caption>` | Descreve a tabela (ex.: "Horários da turma de ES — 2026.2") |
| `<thead>` | Linha de cabeçalho com os dias da semana (segunda a sexta) |
| `<tbody>` | Pelo menos 4 linhas de horários |
| `scope` | `scope="col"` nos dias, `scope="row"` nos horários |
| `colspan` | Uma linha de "Intervalo" atravessando todas as colunas |
| Dados reais | Use as disciplinas do seu horário real neste semestre |

---

## Desafios extras

- Use `rowspan` para agrupar disciplinas que ocupam dois horários seguidos
- Adicione um `<tfoot>` com a carga horária semanal total
- Envolva a tabela em um `<div class="tabela-wrapper">` com `overflow-x: auto` no CSS e teste em uma janela estreita (a tabela deve ganhar scroll horizontal, sem estourar a página)

---

## Checklist (antes de entregar)

- [ ] A tabela tem `caption`, `thead` e `tbody`?
- [ ] Todos os cabeçalhos usam `<th>` com `scope`?
- [ ] O `colspan` do intervalo cobre exatamente o número de colunas da tabela?
- [ ] O HTML passa no [W3C Validator](https://validator.w3.org/) sem erros?

---

## Dicas

- Desenhe a grade no papel antes de escrever o HTML — `colspan` e `rowspan` ficam muito mais fáceis de acertar.
- Consulte os exemplos da aula: `../../exemplos/02-tabela-semantica.html`, `03-tabela-colspan.html` e `04-tabela-rowspan.html`.

---

## Entrega

- Arquivo `index.html` completo, na pasta `pratica/ex1-tabela-horarios/`.

A solução de referência está disponível em `pratica/ex1-tabela-horarios/solucao/` para consulta após a tentativa.
