# Protegendo rotas (páginas) do frontend

## Conteúdo

 - [`Introdução e problema`](#ntro-and-problem)
 - [`Criando e registrando (ROTA/URL) o endpoint de sessão autenticada`](#session-endpoint)
 - [`Criando um mecanismo (no frontend) para verificar se o usuário está logado`](#check-login)
 - [`Bloqueando (no frontend) as páginas que necessitam de autenticação`](#block-not-autenticated-pages)
 - [`Interceptando requisições antes de chegar nas páginas (frontend/middleware.ts)`](#intercep-front-pages)
 - [`Interceptando requisições antes de chegar nas páginas (backend/core/middleware.py)`](#intercep-backend-pages)
<!---
[WHITESPACE] = 50
--->









































---

<div id="intro-and-problem"></div>

## `Introdução e problema`

Neste projeto, o frontend roda em **Next.js** (`localhost:3000`) e o backend em **Django** (`localhost:8000`).

> Por isso, apenas proteger no Django não bloqueia sozinho a navegação direta no frontend.  

Para resolver isso nós vamos criar uma implementação em **camadas**, seguido a seguinte ordem:

1. Criar no Django um endpoint que informa se a sessão está autenticada.
2. Criar no Next um helper que consulta esse endpoint e redireciona para login.
3. Aplicar esse helper nas páginas protegidas.
4. (Camada extra) manter middleware no Next e no Django para reforço.









































---

<div id="session-endpoint"></div>

## `Criando e registrando (ROTA/URL) o endpoint de sessão autenticada`

Vamos começar criando um endpoint no backend para verificar se o usuário está autenticado:

### `Código Completo`

**backend/users/views.py:**
```python
def session_status_api(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    return JsonResponse(
        {"authenticated": request.user.is_authenticated},
        status=200,
    )
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar criando uma função que:

 - Vai receber uma requisição (do tipo HttpRequest)
 - Retornar um `JsonResponse`

```python
def session_status_api(request: HttpRequest) -> JsonResponse:
    ...
```

Continuando, agora nós vamos criar uma verificação para quando a requisição for do tipo `GET`, seja exibida uma mensagem dizendo que esse endpoint não aceita esse método:

```python
def session_status_api(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )
```

Ótimo, agora sabendo que esse endpoint não vai aceitar requisição do tipo `GET`, vamos retornar um `JsonResponse` com:

 - Uma chave chamada `authenticated`
 - E o valor de `request.user.is_authenticated`
   - É um atributo booleano (`True` ou `False`)
   - Indica se o usuário está logado

```python
def session_status_api(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    return JsonResponse(
        {"authenticated": request.user.is_authenticated},
        status=200,
    )
```

**drive.py:**
```python
import os
import sys
from pathlib import Path
import django

# Ensure `backend/` is in sys.path when running this file directly.
BACKEND_DIR = Path(__file__).resolve().parents[1]
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

# 🔹 1. Configurar o ambiente do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# 🔹 2. Imports depois do setup
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User

# Import through the app package so relative imports in views.py work.
from users.views import session_status_api


def test_session_status_authenticated():
    print("\n🔐 Teste: Usuário autenticado")

    factory = RequestFactory()
    request = factory.get("/fake-url/")

    # 🔹 Simulando usuário autenticado
    user = User(username="teste")
    user.set_password("123")
    user.save()

    request.user = user

    response = session_status_api(request)

    print("Status:", response.status_code)
    print("Body:", response.content.decode())


def test_session_status_unauthenticated():
    print("\n🚫 Teste: Usuário NÃO autenticado")

    factory = RequestFactory()
    request = factory.get("/fake-url/")

    # 🔹 Usuário anônimo
    request.user = AnonymousUser()

    response = session_status_api(request)

    print("Status:", response.status_code)
    print("Body:", response.content.decode())


def test_wrong_method():
    print("\n⚠️ Teste: Método errado (POST)")

    factory = RequestFactory()
    request = factory.post("/fake-url/")

    request.user = AnonymousUser()

    response = session_status_api(request)

    print("Status:", response.status_code)
    print("Body:", response.content.decode())


if __name__ == "__main__":
    test_session_status_authenticated()
    test_session_status_unauthenticated()
    test_wrong_method()
```

**OUTPUT:**
```python
python driver.py

🔐 Teste: Usuário autenticado
Status: 200
Body: {"authenticated": true}

🚫 Teste: Usuário NÃO autenticado
Status: 200
Body: {"authenticated": false}

⚠️ Teste: Método errado (POST)
Status: 405
Body: {"error": "Method not allowed"
```

Por fim, nós vamos registrar esse endpoint nas nossas ROTAS/URLs para quem precisar utilizar a mesma:

**backend/users/urls.py**
```python
from django.urls import path

from . import views

urlpatterns = [
    path(
        route="auth/session/",
        view=views.session_status_api,
        name="session_status"
    ),

    ...

]
```









































---

<div id="check-login"></div>

## `Criando um mecanismo (no frontend) para verificar se o usuário está logado`

> Agora, nós vamos criar um mecanismo (no frontend) para verifica se o usuário está logado e, se não estiver, redireciona para `/login`.

### `Código Completo`

**frontend/src/lib/require-auth.ts**
```ts
import { headers } from "next/headers"
import { redirect } from "next/navigation"

const DEFAULT_BACKEND_URL = "http://127.0.0.1:8000"

export async function requireAuth(pathname: string): Promise<void> {
  const backendUrl = process.env.BACKEND_URL ?? DEFAULT_BACKEND_URL
  const requestHeaders = await headers()
  const cookieHeader = requestHeaders.get("cookie") ?? ""

  if (!cookieHeader.includes("sessionid=")) {
    redirect(`/login?next=${encodeURIComponent(pathname)}`)
  }

  try {
    const response = await fetch(`${backendUrl}/auth/session/`, {
      method: "GET",
      headers: {
        cookie: cookieHeader,
      },
      cache: "no-store",
    })

    if (!response.ok) {
      redirect(`/login?next=${encodeURIComponent(pathname)}`)
    }

    const data = (await response.json()) as { authenticated?: boolean }
    if (!data.authenticated) {
      redirect(`/login?next=${encodeURIComponent(pathname)}`)
    }
  } catch {
    redirect(`/login?next=${encodeURIComponent(pathname)}`)
  }
}
```

### `Explicação`

Agora criamos o bloco que **consome** o endpoint do `session_status_api`.

- `headers()`  
  - pega headers da request atual no server-side do Next.
- `cookieHeader.includes("sessionid=")`  
  - filtro rápido: se nem cookie de sessão existe, já redireciona.
- `fetch(.../auth/session/)`  
  - consulta o Django para confirmar se a sessão é válida.
- `redirect("/login?next=...")`  
  - manda para login e guarda para qual rota voltar após autenticar.
- `cache: "no-store"`  
  - evita usar cache antigo de autenticação.

> **⚠️ NOTE:**  
> Esse helper foi feito para ser reutilizado por qualquer página protegida que necessita de autenticação para ser utilizada.









































---

<div id="block-not-autenticated-pages"></div>

## `Bloqueando (no frontend) as páginas que necessitam de autenticação`

Agora, ós vamos utilizar a função `requireAuth` do módulo `frontend/src/lib/require-auth.ts` para bloquear as páginas que necessitam de autenticação para serem acessadas:

**frontend/src/app/home/page.tsx**
```tsx
import type { Metadata } from "next"

import { Chat } from "@/components/chat"
import { AppShell } from "@/components/layout/app-shell"
import { requireAuth } from "@/lib/require-auth"

export const metadata: Metadata = {
  title: "Chat · Easy RAG",
  description: "Converse com o assistente e visualize respostas em Markdown.",
}

export default async function HomePage() {
  await requireAuth("/home")

  return (
    <AppShell>
      <Chat />
    </AppShell>
  )
}
```

**frontend/src/app/workspace/page.tsx**
```tsx
import type { Metadata } from "next"

import {
  NewButton,
  RemoveButton,
  RenameButton,
  UploadButton,
} from "@/components/buttons"
import { WorkspaceBreadcrumb } from "@/components/breadcrumb"
import { AppShell } from "@/components/layout/app-shell"
import { requireAuth } from "@/lib/require-auth"

export const metadata: Metadata = {
  title: "Workspace · Easy RAG",
}

export default async function WorkspacePage() {
  await requireAuth("/workspace")

  return (
    <AppShell>
      <div className="flex flex-1 flex-col gap-4 p-6">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <h1 className="text-lg font-semibold tracking-tight">Workspace</h1>
            <WorkspaceBreadcrumb className="mt-2" />
          </div>
          <div className="flex flex-wrap items-center gap-2">
            <NewButton />
            <UploadButton />
            <RemoveButton itemName={null} />
            <RenameButton currentName={null} />
          </div>
        </div>
      </div>
    </AppShell>
  )
}
```

**frontend/src/app/treinamento/page.tsx**
```tsx
import type { Metadata } from "next"

import { AppShell } from "@/components/layout/app-shell"
import { requireAuth } from "@/lib/require-auth"

export const metadata: Metadata = {
  title: "Treinamento · Easy RAG",
}

export default async function TreinamentoPage() {
  await requireAuth("/treinamento")

  return (
    <AppShell>
      <div className="flex flex-1 flex-col p-6">
        <h1 className="text-lg font-semibold tracking-tight">Treinamento</h1>
        <p className="mt-2 max-w-prose text-sm text-muted-foreground">
          Conteúdo de treinamento virá aqui.
        </p>
      </div>
    </AppShell>
  )
}
```

**frontend/src/app/lixeira/page.tsx**
```tsx
import type { Metadata } from "next"

import { AppShell } from "@/components/layout/app-shell"
import { requireAuth } from "@/lib/require-auth"

export const metadata: Metadata = {
  title: "Lixeira · Easy RAG",
}

export default async function LixeiraPage() {
  await requireAuth("/lixeira")

  return (
    <AppShell>
      <div className="flex flex-1 flex-col p-6">
        <h1 className="text-lg font-semibold tracking-tight">Lixeira</h1>
        <p className="mt-2 max-w-prose text-sm text-muted-foreground">
          Itens removidos aparecerão aqui.
        </p>
      </div>
    </AppShell>
  )
}
```

### `Explicação`

Com isso, aplicamos nas páginas que precisam login.

- Cada página virou `async function`.
- A primeira linha útil da página é `await requireAuth("...")`.
- Se usuário não está autenticado:
  - o `requireAuth` interrompe o fluxo e redireciona para `/login`.
- Se autenticado:
  - o restante da página renderiza normalmente.

> **⚠️ NOTE:**  
> Essa etapa é a que efetivamente impede renderização das páginas protegidas.









































---

<div id="intercep-front-pages"></div>

## `Interceptando requisições antes de chegar nas páginas (frontend/middleware.ts)`

Aqui nós vamos implementar um `middleware.ts` que vai:

 - 👉 interceptra requisições antes de chegar na página
 - 👉 Verifica se o usuário está autenticado (consultando o backend Django)
 - 👉 Decidir se:
   - deixa acessar a página
   - ou redireciona para login

### `🧠 Qual o problema que esse código resolve?`

Sem esse middleware:

> ❌ Qualquer usuário poderia acessar URLs protegidas digitando direto no navegador

**Ex:**
```url
/workspace
/home
```

Com esse middleware:

 - ✅ Só acessa quem está autenticado
 - ✅ Integra com seu backend Django
 - ✅ Evita vazamento de dados e acesso indevido

### `Código Completo`

**frontend/middleware.ts**
```ts
import { NextRequest, NextResponse } from "next/server"

const PROTECTED_PATHS = ["/home", "/workspace", "/treinamento", "/lixeira"]
const DEFAULT_BACKEND_URL = "http://127.0.0.1:8000"

function isProtectedPath(pathname: string): boolean {
  return PROTECTED_PATHS.some(
    (path) => pathname === path || pathname.startsWith(`${path}/`)
  )
}

function redirectToLogin(request: NextRequest): NextResponse {
  const loginUrl = new URL("/login", request.url)
  loginUrl.searchParams.set("next", request.nextUrl.pathname + request.nextUrl.search)
  return NextResponse.redirect(loginUrl)
}

export async function middleware(request: NextRequest) {
  if (!isProtectedPath(request.nextUrl.pathname)) {
    return NextResponse.next()
  }

  const backendUrl = process.env.BACKEND_URL ?? DEFAULT_BACKEND_URL
  const cookieHeader = request.headers.get("cookie") ?? ""

  if (!cookieHeader.includes("sessionid=")) {
    return redirectToLogin(request)
  }

  try {
    const response = await fetch(`${backendUrl}/auth/session/`, {
      method: "GET",
      headers: {
        cookie: cookieHeader,
      },
      cache: "no-store",
    })

    if (!response.ok) {
      return redirectToLogin(request)
    }

    const data = (await response.json()) as { authenticated?: boolean }
    if (!data.authenticated) {
      return redirectToLogin(request)
    }

    return NextResponse.next()
  } catch {
    return redirectToLogin(request)
  }
}

export const config = {
  matcher: ["/home/:path*", "/workspace/:path*", "/treinamento/:path*", "/lixeira/:path*"],
}
```









































---

<div id="intercep-backend-pages"></div>

## `Interceptando requisições antes de chegar nas páginas (backend/core/middleware.py)`

Até, então nós estavamos bloqueando as requisições antes de chegar nas páginas no frontend, mas agora nós vamos fazer o mesmo processo *no backend*.

> **🧠 Qual a necessidade disso?**

Mesmo que você já tenha proteção no frontend (como no `middleware` do `Next.js`):

> **👉 isso NÃO é suficiente para segurança**  
> Por quê?

 - O frontend pode ser burlado (ex: curl, Postman)
 - Usuário pode acessar direto o backend
 - JavaScript pode ser desativado

👉 Então o backend precisa garantir:

 - ✅ Segurança real
 - ✅ Bloqueio definitivo de acesso
 - ✅ Proteção contra requisições diretas

**backend/core/middleware.py**
```python
from django.contrib.auth.views import redirect_to_login


class ProtectedFrontendRoutesMiddleware:
    """
    Blocks unauthenticated access to selected frontend routes.
    """

    PROTECTED_PREFIXES = (
        "/home",
        "/workspace",
        "/treinamento",
        "/lixeira",
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if self._is_protected_path(path) and not request.user.is_authenticated:
            return redirect_to_login(
                next=request.get_full_path(),
                login_url=None,
                redirect_field_name="next",
            )

        return self.get_response(request)

    def _is_protected_path(self, path: str) -> bool:
        for prefix in self.PROTECTED_PREFIXES:
            if path == prefix or path.startswith(f"{prefix}/"):
                return True
        return False
```

Agora, nós precisamos configurar esse `middleware` nas configurações do Django:

**backend/core/settings.py**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'core.middleware.ProtectedFrontendRoutesMiddleware', # <--- Page protection
]
LOGIN_URL = os.getenv("DJANGO_LOGIN_URL", "/login")
```

### `Explicação`

Esses blocos são reforços adicionais:

- `frontend/middleware.ts`  
  - intercepta cedo as rotas protegidas e já redireciona se necessário.
- `backend/core/middleware.py` + `settings.py`  
  - mantém uma regra no Django para cenários onde essas URLs possam chegar ao backend.
- `LOGIN_URL`  
  - centraliza destino de login e permite configurar via variável de ambiente.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
