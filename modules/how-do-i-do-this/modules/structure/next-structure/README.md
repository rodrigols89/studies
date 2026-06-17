# Qual a 📁 estrutura de um projeto Next.js?

## Conteúdo

 - [`Qual a estrutura de um projeto Next.js`](#public)
 - [`📁 front/src/app`](#src-app)
 - [`📁 Estrutura do diretório`](#structure)
<!---
[WHITESPACE] = 50
--->









































---

<div id="public"></div>

## `📁 frontend/public`

> **Para que serve a pasta `public`?**

A pasta `public` é onde nós vamos colocar arquivos estáticos que serão servidos diretamente pelo navegador.

> **⚠️ NOTE:**  
> Tudo que estiver lá fica acessível pela URL raiz do nosso projeto.

Por exemplo, se tivermos:

```bash
/public
  ├── logo.png
  ├── favicon.ico
  └── images/
        └── banner.jpg
```

Podemos acessar assim no navegador:

 - http://localhost:3000/logo.png
 - http://localhost:3000/images/banner.jpg

> **Como usar isso no código?**

**Exemplo com `<img>`:**
```ts
<img src="/logo.png" alt="Logo" />
```

**Exemplo com next/image (melhor prática):**
```ts
import Image from "next/image";

<Image 
  src="/images/banner.jpg"
  alt="Banner"
  width={800}
  height={400}
/>
```

> **✔️ Resumindo:**  
> - Serve para imagens, ícones, fontes, arquivos estáticos
> - Não precisa importar — usa direto pelo caminho `/`









































---

<div id="src-app"></div>

## `📁 frontend/src/app`

> Isso faz parte do `App Router` do **Next.js** (versão moderna).

### `🎨 global.css`

 - É o CSS global da aplicação.
 - 👉 Tudo que nós colocarmos aqui afetará o projeto inteiro.

**Exemplo:**
```css
body {
  background-color: #0f172a;
  color: white;
  font-family: sans-serif;
}
```

Se você usa shadcn + Tailwind, normalmente tem algo assim:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

// Ou na versão mais recente
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
```

✔️ Serve para:

 - Reset de CSS
 - Variáveis globais
 - Estilos padrão

### `🧱 layout.tsx`

 - É o layout base da aplicação (estrutura padrão de todas as páginas).
 - 👉 Tudo que estiver aqui aparecerá em TODAS as páginas.

**Exemplo:**
```ts
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body>
        <header>Meu Header</header>

        {children}

        <footer>Meu Footer</footer>
      </body>
    </html>
  );
}
```

✔️ Serve para:

 - Header
 - Footer
 - Providers (tema, auth, etc.)
 - Estrutura global

> 👉 `{children}` = onde as páginas vão ser renderizadas

### `📄 page.tsx`

 - Esse arquivo representa a rota `/`
 - 👉 O `page.tsx` pode ser considerado o equivalente ao home.html (ou index.html de uma página específica).

**Exemplo:**
```ts
export default function Home() {
  return (
    <main>
      <h1>Bem-vindo ao meu projeto</h1>
    </main>
  );
}
```









































---

</div id="structure"></div>

## `📁 Estrutura do diretório`

Aqui nós temos uma breve introdução da estrutura desse diretório:

```
/                                         # Raiz do projeto
└─ frontend/                              # Frontend do projeto
      ├── public/                         # Arquivos estáticos
      ├── src/                            # Código fonte principal
      │    ├── app/                       # App Router (rotas, layouts e páginas)
      │    │    ├── globals.css           # CSS global da aplicação
      │    │    ├── layout.tsx            # Layout base da aplicação
      │    │    └── page.tsx              # Representa a rota /
      │    ├── components/                # Componentes reutilizáveis da aplicação
      │    │     └── ui/                  # shadcn: Button, Input, Card, Dialog, etc.
      │    │       └── button.tsx         # Componente de botão reutilizável
      │    └── lib/                       # Funções utilitárias e helpers
      │          └── utils.ts             # Utilitários (ex: cn para classes)
      ├── .gitignore                      # Arquivos/pastas ignorados pelo Git
      ├── components.json                 # Configuração do shadcn/ui
      ├── eslint.config.mjs               # Configuração do ESLint
      ├── next-env.d.ts                   # Tipagens automáticas do Next.js
      ├── next.config.ts                  # Configuração do Next.js
      ├── package-lock.json               # Lock de dependências (npm)
      ├── package.json                    # Dependências e scripts do projeto
      ├── postcss.config.mjs              # Configuração do PostCSS (Tailwind, etc.)
      └── tsconfig.json                   # Configuração do TypeScript
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<!---
**drive.py:**
```python

```

**OUTPUT:**
```python

```
--->
