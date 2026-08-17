---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('images/background.png')
footer: 'Introdução à Web e Estrutura do HTML'
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

# 1. Introdução à Web e Estrutura do HTML
## Programação Web I (2026.2)

### Prof. Diego Pessoa / Prof. Wallennon Dunga

---

# Roteiro

- Como os sites são criados?
- Como funciona a Web?
- Estrutura de uma página web
- Anatomia de uma tag HTML
- Elementos semânticos HTML5
- Acessibilidade web básica
- Ferramentas modernas de desenvolvimento
- Boas práticas

---

<!-- _header: 'Introdução' -->

# Como os sites são criados?

- Todos os sites são construídos com **HTML** e **CSS**.
- Sistemas como blogs, e-commerce e CMS utilizam tecnologias adicionais
- Ao acessar um site, o navegador geralmente está recebendo HTML, CSS e JavaScript de um **servidor web**

### **Tecnologias Fundamentais**

- **HTML**: Estrutura e conteúdo (esqueleto)
- **CSS**: Aparência e layout (pele)
- **JavaScript**: Interatividade e dinamicidade (movimento)
- **Python/Flask**: Lógica de backend e geração dinâmica de páginas

---

*Uma página web é como uma casa: HTML é a estrutura, CSS a decoração, JavaScript as portas automáticas, e o backend é o encanamento/infraestrutura que faz tudo funcionar!*

---

# História da Web

<div class="columns">
<div>

### **Marcos importantes**

- **1989**: Tim Berners-Lee cria a WWW
- **1993**: Primeiro navegador gráfico (Mosaic)
- **1995**: JavaScript nasce
- **2008**: HTML5 começa a ser desenvolvido

</div>
<div>

### **Evolução dos navegadores**

- Internet Explorer (1995-2022)
- Firefox (2004-presente)
- Chrome (2008-presente)
- Edge (2015-presente)
- Safari (2003-presente)

</div>
</div>

---

*A primeira página web ainda está online!*
*[info.cern.ch/hypertext/WWW/TheProject.html](http://info.cern.ch/hypertext/WWW/TheProject.html)*
<br>

[![A Guerra dos Navegadores](https://img.youtube.com/vi/gb2btn2skFU/maxresdefault.jpg)](https://www.youtube.com/watch?v=gb2btn2skFU)

**[▶️ Assistir vídeo: A Guerra dos Navegadores](https://www.youtube.com/watch?v=gb2btn2skFU)**

---

<!-- _header: 'Como funciona a Web?' -->

# Como funciona a Web?

### **O processo completo**

1. **Usuário** digita URL no navegador
2. **DNS** converte domínio em endereço IP
3. **Navegador** conecta com o servidor web
4. **Servidor** envia arquivos HTML/CSS/JS
5. **Navegador** renderiza e exibe a página

---

<div class="columns">
<div>

### **Protocolos importantes**

- **HTTP/HTTPS** - Transferência
- **TCP/IP** - Comunicação
- **DNS** - Resolução de nomes

</div>
<div>

### **Exemplo prático**

- Você digita: `google.com`
- DNS resolve: `172.217.0.142`
- Servidor do Google responde
- Navegador exibe a página

</div>
</div>

---

# Resolução DNS e Comunicação
<!-- _footer: '' -->

![width:750px](aula-01/images/dns_global_communication.png)

---

# Cliente vs Servidor

<div class="columns">
<div>

### **Cliente (Frontend)**

- **Navegador** web
- Executa **HTML, CSS, JavaScript**
- Interface do usuário
- Responsivo e interativo

*HTML5, CSS3, JavaScript, React, Vue, Angular*

</div>
<div>

### **Servidor (Backend)**

- **Servidor** web
- Processa **lógica de negócio**
- Banco de dados
- APIs e serviços

*Python, Java, Node.js, PHP, C#, Ruby*

</div>
</div>

*Cliente e servidor se comunicam via **HTTP/HTTPS** usando requisições GET, POST, PUT, DELETE*

---

# Cliente, Servidor e HTTP
<!-- _footer: '' -->

![width:850px](aula-01/images/client_server_http.png)

**Figura:** Comunicação entre navegador (cliente) e servidor web via protocolo HTTP.

---

# Ferramentas para Entender a Web

<div class="columns">
<div>

### **Ferramentas de rede**

- **ping** - Testa conectividade
- **nslookup** - Consulta DNS
- **traceroute** - Rastreia caminho
- **curl** - Faz requisições HTTP

**Exemplos:** `ping google.com`, `nslookup ifpb.edu.br`, `traceroute github.com`

</div>
<div>

### **Análise de sites**

- **[PageSpeed Insights](https://pagespeed.web.dev/)** - Performance
- **[GTmetrix](https://gtmetrix.com/)** - Otimização
- **[Lighthouse](https://developer.chrome.com/docs/lighthouse/)** - Auditoria completa
- **[Web.dev](https://web.dev/)** - Boas práticas

*Use sempre **HTTPS** em produção! Segurança é fundamental.*

</div>
</div>

---

<!-- _header: 'Estrutura de uma página web' -->

# Estrutura de uma página web

- Toda página HTML é composta por **elementos estruturais** chamados de **tags**

```html
<p>Lorem ipsum dolor.</p>
```

- Tag de abertura: `<p>`
- Conteúdo: `Lorem ipsum dolor.`
- Tag de fechamento: `</p>`

---

<div class="columns">
<div>

### **Tags de conteúdo**

- `<h1>` a `<h6>` - Títulos
- `<p>` - Parágrafos
- `<a>` - Links
- `<img>` - Imagens
- `<ul>`, `<ol>`, `<li>` - Listas

</div>
<div>

### **Tags de formatação**

- `<strong>` - Texto importante
- `<em>` - Ênfase
- `<span>` - Inline genérico
- `<div>` - Block genérico
- `<br>` - Quebra de linha

</div>
</div>

*Use `<strong>` em vez de `<b>` e `<em>` em vez de `<i>` para melhor semântica!*

---

# Exemplo de estrutura básica

<div class="columns">
<div>

### **Estrutura HTML básica**

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content=
        "width=device-width, initial-scale=1.0">
    <title>Minha primeira página</title>
</head>
<body>
    <h1>Olá Mundo!</h1>
    <p>Esta é minha primeira página web.</p>
</body>
</html>
```

</div>
<div>

### **Elementos obrigatórios**

- `<!DOCTYPE html>`
- `<html lang="pt-br">`
- `<meta charset="UTF-8">`
- Meta viewport (responsivo)

*Essa estrutura cria uma página válida, acessível e responsiva!*

![width:250px](aula-01/images/ola_mundo.png)

</div>
</div>

---

# Detalhes sobre o DOCTYPE html

### **O que é o DOCTYPE?**

O `<!DOCTYPE html>` é uma declaração especial usada no início de um documento HTML para informar ao navegador qual versão do HTML está sendo usada.

### **Por que é importante?**

- **Compatibilidade**: Garante que o navegador renderize a página no modo padrão
- **HTML5**: A declaração mais simples comparada com versões anteriores
- **Evita modo quirks**: Previne renderização inconsistente

*Não diferencia maiúsculas de minúsculas, não gera conteúdo visível na página, e é essencial para o funcionamento correto do documento.*

---

<!-- _header: 'Anatomia de uma tag HTML' -->

# Anatomia de uma tag HTML

<div class="columns">
<div>

### **Tag de abertura**

```html
<p>
```

</div>
<div>

### **Tag de fechamento**

```html
</p>
```

</div>
</div>

### **Conceitos importantes**

- As **tags** delimitam o início e o fim de um **elemento HTML**
- Elementos podem conter texto, outros elementos, ou atributos
- A estrutura é hierárquica

---

<!-- _header: 'Atributos em HTML' -->

# Atributos em HTML

- Atributos fornecem **informações adicionais** sobre os elementos
- Sintaxe: `nome="valor"`

### **Exemplo**

```html
<p lang="en-us">Paragraph in English</p>
```

---

<div class="columns">
<div>

### **Atributos globais**

- `id` - Identificador único
- `class` - Classes CSS
- `style` - Estilos inline
- `title` - Tooltip

</div>
<div>

### **Atributos específicos**

- `href` - Links (`<a>`)
- `src` - Imagens (`<img>`)
- `alt` - Texto alternativo
- `target` - Destino do link

</div>
</div>

---

### **Exemplos práticos**

```html
<a href="https://ifpb.edu.br" target="_blank">IFPB</a>
```

```html
<img src="logo.png" alt="Logo do IFPB">
```

---

<!-- _header: 'Head, Body e Title' -->
<!-- _footer: '' -->

# Head, Body e Title

### **Estrutura principal do HTML**

- `<html>`: Contém toda a estrutura da página
- `<head>`: Define **metadados**, como o título da aba
- `<title>`: Título exibido na aba do navegador
- `<body>`: Todo o conteúdo visível na página

### **O que vai no Head?**

- Metadados (charset, viewport, description)
- Links para CSS, fontes, favicon

### **O que vai no Body?**

Todo o conteúdo visível: textos, imagens, links, formulários, etc.


---

<!-- _header: 'Elementos Semânticos HTML5' -->

# Elementos Semânticos HTML5

### **Por que usar elementos semânticos?**

- Melhor **acessibilidade** para leitores de tela
- **SEO** mais efetivo
- Código mais **legível** e **manutenível**

---

<div class="columns">
<div>

### **Estrutura da página**

- `<header>` - Cabeçalho
- `<nav>` - Navegação
- `<main>` - Conteúdo principal
- `<footer>` - Rodapé

</div>
<div>

### **Conteúdo**

- `<section>` - Seções
- `<article>` - Artigos
- `<aside>` - Conteúdo lateral
- `<figure>` - Figuras

</div>
</div>

---

# Exemplo com elementos semânticos
<!-- _footer: '' -->

### **Estrutura semântica**

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Meu Site</title>
</head>
<body>
  <header>
    <h1>Meu Blog</h1><nav><a href="#home">Home</a></nav>
  </header>
  <main><article><h2>Primeiro Post</h2><p>Conteúdo...</p></article>
  </main>
  <footer><p>&copy; 2025</p></footer>
</body>
</html>
```

---

<!-- _header: 'Acessibilidade Web' -->

# Acessibilidade Web Básica

### **Por que acessibilidade importa?**

- **15%** da população mundial tem alguma deficiência
- É **lei** em muitos países (incluindo Brasil)
- Melhora a **experiência** para todos

---

<div class="columns">
<div>

### **Boas práticas básicas**

- Texto alternativo em imagens
- Estrutura de cabeçalhos lógica
- Contraste adequado de cores
- Navegação por teclado

</div>
<div>

### **Exemplos práticos**

- `<img alt="Descrição">`
- `<button>` vs `<div>`
- `<label for="nome">`
- `<h1>`, `<h2>`, `<h3>`...

</div>
</div>

---

<!-- _header: 'Boas Práticas' -->

# Boas Práticas em HTML

<div class="columns">
<div>

### **Estrutura e organização**

- Sempre usar `<!DOCTYPE html>`
- Definir `lang="pt-br"`
- Meta charset UTF-8
- Viewport para mobile
- Estrutura semântica

</div>
<div>

### **Qualidade do código**

- Indentação consistente
- Tags em minúsculas
- Atributos entre aspas
- Fechar todas as tags
- Validar o HTML

</div>
</div>

---

### **Performance**

- Otimizar imagens (WebP, tamanhos apropriados)
- Minificar HTML em produção
- Usar CDNs para recursos externos
- Lazy loading para imagens

---

# Validação e Testes

### **Por que validar HTML?**

- Garante compatibilidade entre navegadores
- Melhora acessibilidade e SEO (Search Engine Optimization)
- Evita erros de renderização e facilita manutenção do código

---

<div class="columns">
<div>

### **Ferramentas de validação**

- **[W3C Markup Validator](https://validator.w3.org/)**
- **[HTML5 Validator](https://html5.validator.nu/)**
- [VS Code extensions](https://marketplace.visualstudio.com/items?itemName=mkaufman.HTMLHint)
- [Browser DevTools](https://developer.chrome.com/docs/devtools/)

</div>
<div>

### **Testes essenciais**

- Testar em diferentes navegadores
- Verificar responsividade
- Testar com leitor de tela
- Validar performance

</div>
</div>

### **Processo recomendado**

Escrever HTML → Validar → Testar → Corrigir → Repetir

---

<!-- _header: 'Ferramentas Modernas' -->

# Ferramentas Modernas de Desenvolvimento

<div class="columns">
<div>

### **Editores recomendados**

- **[VS Code](https://code.visualstudio.com/)** - Editor mais popular
- [Sublime Text](https://www.sublimetext.com/) - Rápido e leve
- [WebStorm](https://www.jetbrains.com/webstorm/) - IDE completa

### **Extensões úteis (VS Code)**

- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) - Servidor local
- [HTML CSS Support](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - Formatação
- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)

</div>
<div>

### **Ferramentas de validação**

- **[W3C Validator](https://validator.w3.org/)** - Validar HTML
- [WAVE](https://wave.webaim.org/) - Acessibilidade
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - Performance

### **Controle de versão**

- **[Git](https://git-scm.com/)** - Essencial!
- [GitHub](https://github.com/) - Repositórios
- Commits frequentes
- Branches para features

</div>
</div>

---

# Chrome DevTools

### **Ferramenta essencial**

Use **"Inspecionar Elemento"** (botão direito na página)

<div class="columns">
<div>

### **Funcionalidades principais**

- Inspecionar HTML/CSS
- Testar modificações
- Debugar JavaScript
- Analisar performance
- Simular dispositivos

</div>
<div>

### **Atalhos úteis**

- **F12** - Abrir DevTools
- **Ctrl+Shift+I** - Inspecionar
- **Ctrl+U** - Ver código fonte
- **Ctrl+Shift+M** - Modo mobile

</div>
</div>

---

<!-- _header: 'Conclusão' -->

# Resumo da Aula

### **O que aprendemos?**

- Como os sites funcionam
- Estrutura básica do HTML
- Tags e elementos
- Atributos

---

### **Lição importante:**
### **A prática leva à perfeição!**

---

# Recursos para Estudo

### **Documentação e referências**

- **[MDN Web Docs](https://developer.mozilla.org/pt-BR/)** - Referência completa
- **[W3Schools](https://www.w3schools.com/)** - Tutoriais práticos
- **[HTML5 Validator](https://validator.w3.org/)** - Validação online
- **[Can I Use](https://caniuse.com/)** - Compatibilidade de browsers

### **Prática**

- **[CodePen](https://codepen.io/)** - Testes rápidos
- **[freeCodeCamp](https://www.freecodecamp.org/)** - Exercícios guiados
- **[GitHub Pages](https://pages.github.com/)** - Hospedar projetos

---

<!-- _class: lead -->

# Obrigado!

## **Perguntas?**

*"O conhecimento se constrói passo a passo!"*
