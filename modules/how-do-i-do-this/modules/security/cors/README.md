# O que significa CORS?

## Conteúdo

 - [`Cross-Origin Resource Sharing (CORS)`](#intro-to-cors)
 - [`Aplicando CORS na prática`](#apply-cors)
<!---
[WHITESPACE] = 50
--->









































---

<div id="intro-to-cors"></div>

## `Cross-Origin Resource Sharing (CORS)`

CORS significa:

> **Cross-Origin Resource Sharing**

Em português:

> **“Compartilhamento de recursos entre origens diferentes”**

### `🔐 Same-Origin Policy (SOP)`

O `CORS` existe por causa de uma regra do navegador chamada:

> **🔐 Same-Origin Policy (SOP)**

Ela diz:

> “Um site só pode acessar dados de outro site se o servidor permitir explicitamente.”

### `O que é “origem”?`

Uma `origem` é a combinação de:

```
protocolo (HTTP/HTTPS) + domínio (easyrag.com) + porta (800 ou 800)
```

Exemplo:

| URL                                            | Origem   |
| ---------------------------------------------- | -------- |
| [http://localhost:3000](http://localhost:3000) | frontend |
| [http://localhost:8000](http://localhost:8000) | backend  |

> **⚠️ NOTE:**  
> São origens diferentes → precisa de CORS.

Por exemplo (bem simples), imagine isso que você está no Next.js:

```ts
fetch("http://localhost:8000/api/register/")
```

O browser pensa:

> **“Hmm… esse site (3000) está tentando acessar outro (8000). Vou verificar segurança.”**

**❌ Sem CORS**  
O backend NÃO responde permissões:

```http
Access-Control-Allow-Origin: (não existe)
```

Resultado no browser:

```
❌ Blocked by CORS policy
```

Mesmo que:

 - Django esteja funcionando
 - Banco esteja OK
 - API esteja perfeita

**✅ Com CORS correto**  
Django responde:

```http
Access-Control-Allow-Origin: http://localhost:3000
```

Resultado:

 - ✔ requisição liberada
 - ✔ dados chegam no frontend

### `Como isso se aplica no nosso projeto?`

Nós temos a seguinte *arquitetura*:

```
Next.js (3000)
        ↓
Browser (CORS check)
        ↓
Django API (8000)
        ↓
PostgreSQL
```

> **💥 Onde o problema acontece?**

Aqui:

```
Next.js → Django
```

Porque:

| Origem         | Destino        |
| -------------- | -------------- |
| localhost:3000 | localhost:8000 |

> **⚠️ NOTE:**  
> Ou seja, **Cross-origin request**.

### `💡 Exemplo importante`

Mesmo com CORS ativo:

 - Postman consegue acessar sua API
 - curl consegue acessar sua API
 - ➔ só o browser bloqueia sem permissão

### `🧭 Exemplo visual completo`

```
┌────────────────────────────┐
│        Next.js             │
│   (localhost:3000)         │
└─────────────┬──────────────┘
              │ fetch("/api/register")
              ▼
┌────────────────────────────┐
│          Browser           │
│  🔐 Same-Origin Policy    │
│  🔍 CORS CHECK            │
│                            │
│  ORIGEM: 3000              │
│  DESTINO: 8000             │
│                            │
│  ❌ bloqueia OU           │
│  ✅ libera                │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│           Django           │
│  API (register endpoint)   │
└─────────────┬──────────────┘
              ▼
┌────────────────────────────┐
│        PostgreSQL          │
│   users table INSERT       │
└────────────────────────────┘
```

### `🧠 Resumo final (bem direto)`

 - **👉 O que é CORS?**
   - Um mecanismo do navegador que controla quais sites podem acessar sua API.
 - **👉 Por que ele existe?**
   - Para evitar que sites maliciosos façam requisições escondidas em nome do usuário.
 - **👉 No nosso projeto ele serve para?**
   - Permitir Next.js (3000) acessar Django (8000)
   - Evitar bloqueio do browser
 - **👉 Onde ele atua?**
   - ✔ No browser
   - ❌ Não no backend
   - ❌ Não no banco
  - ❌ Não em proxy reverso









































---

<div id="apply-cors"></div>

## `Aplicando CORS na prática`

Sabendo-se que:

> “Um site (uma origem) só pode acessar dados de outro site (outra origem) se o servidor permitir explicitamente.”

Por exemplos, imagine que nós temos a seguinte *resposta (POST)* de um formulário/input, de uma origem:

```js
export function RegisterCard() {

  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {

    e.preventDefault()
    setError(null)
    setSuccess(null)

    // Captura os valores dos campos do formulário (username, email, senha e confirmação)
    const form = e.currentTarget
    const username = (form.elements.namedItem("username") as HTMLInputElement).value
    const email = (form.elements.namedItem("email") as HTMLInputElement).value
    const password = (form.elements.namedItem("password") as HTMLInputElement).value
    const confirm = (form.elements.namedItem("confirmPassword") as HTMLInputElement).value

    // Validação: verifica se as senhas digitadas são iguais
    if (password !== confirm) {
      setError("As senhas não coincidem.")
      return
    }

    // Ativa o estado de envio (pode ser usado para desabilitar botão ou mostrar loading)
    setIsSubmitting(true)

    // Tenta enviar os dados para o backend
    try {
      /**
       * fetch() é uma função nativa do JavaScript usada para fazer requisições HTTP.
       * Nesse contexto, ela está enviando dados do formulário para o backend (Django)
       * através de uma requisição para a URL "http://localhost:8000/register/".
       *
       * Ela retorna uma Promise, por isso usamos "await" para esperar a resposta.
       */
      const response = await fetch("http://localhost:8000/register/", {

        /**
         * method define o tipo da requisição HTTP.
         * "POST" é usado quando queremos ENVIAR dados para o servidor (ex: criar usuário).
         * - Outros exemplos: "GET" (buscar dados), "PUT" (atualizar), "DELETE" (remover).
         */
        method: "POST",

        /**
         * headers são metadados da requisição (informações extras).
         * Aqui estamos dizendo ao backend como os dados estão sendo enviados.
         * - "application/json" indica que o corpo da requisição está no formato JSON.
         */
        headers: {
          "Content-Type": "application/json",
        },

        /**
         * body é o conteúdo da requisição (os dados que estamos enviando).
         * JSON.stringify() converte um objeto JavaScript em uma string JSON.
         * Exemplo:
         * { username: "rodrigo" } -> '{"username":"rodrigo"}'
         * - Isso é necessário porque o HTTP só envia texto, não objetos JS diretamente.
         */
        body: JSON.stringify({
          username,
          email,
          password1: password,
          password2: confirm,
        }),
      })

      // Converte a resposta da API para JSON
      const data = await response.json()

      // Trata erros retornados pela API
      if (!response.ok) {
        if (data?.errors) {
          const firstError = Object.values(data.errors)[0]
          const message = Array.isArray(firstError) ? firstError[0] : "Erro ao criar conta."
          setError(String(message))
        } else {
          setError("Não foi possível criar a conta.")
        }
        return
      }

      // Se deu tudo certo, mostra mensagem de sucesso e limpa o formulário
      setSuccess("Conta criada com sucesso.")
      form.reset() // Limpa todos os campos do formulário

    } catch {
      // Caso ocorra erro de conexão (backend offline, por exemplo)
      setError("Falha de conexão com o backend.")
    } finally {
      // Finaliza o estado de envio, independentemente de sucesso ou erro
      setIsSubmitting(false)
    }
  }
}
```

> **Como eu faço para a outra ponta (outra origem) acessar os dados desse formulário/input?**

Para resolver isso, primeiro nós precisamos liberar *explicitamente* o acesso do lado do servidor:

```bash
uv add django-cors-headers
```

**settings.py**
```python
INSTALLED_APPS = [
    ...
    "corsheaders",
]
```

**settings.py**
```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]
```

**settings.py**
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_ALL_ORIGINS = True
```

> **O que isso faz na prática?**

Aqui nós estamos dizendo:

> **“Django, permita que o frontend (Next.js) acesse nossa API.”**

Ótimo, agora o nosso frontoend (uma origem) conseguirá enviar dados (com fetch() por exemplo) para o nosso servidor (outra origem).

> **Como receber esses dados?**

### `Código Completo`

```python
import json
from typing import Any, cast

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm


@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    try:
        data = cast(dict[str, Any], json.loads(request.body))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    form = CustomUserCreationForm(data)

    if form.is_valid():
        user = form.save()
        return JsonResponse(
            {
                "message": "User created successfully",
                "user_id": user.id,
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors},
        status=400
    )
```

### `Explicação passo a passo (Step-by-Step)`

Vamos começar criando uma função que vai receber uma requisição (do tipo HttpRequest) e retornar uma resposta (do tipo JsonResonde) que será ...

```python
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:
    ...
```

 - Essa resposta (JsonResponse) sempre vai retornar o `corpo da resposta {}` e o `status code`.
 - `@csrf_exempt`
   - `csrf_exempt` é um decorador do Django que desativa a proteção CSRF para uma view específica.
   - **🧠 Mas o que é CSRF?**
     - **CSRF (Cross-Site Request Forgery)** é um ataque onde um site malicioso tenta fazer requisições em nome do usuário autenticado.
     - 👉 O Django protege contra isso exigindo um CSRF token em requisições como `POST`, `PUT`, `DELETE`.

Agora, se a requisição não for do tipo `POST` nós vamos retornar:

 - Uma resposta do tipo `JsonResponse` (como definido)
 - Uma mensagem `json` dizendo que esse método não é permitido
 - E o status_code 405, ou seja, *navegador web enviou uma solicitação usando um método HTTP válido, mas o servidor considerou esse método inadequado para o recurso que você está tentando acessar*.

```python
@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )
```

> **⚠️ NOTE:**  
> Veja que estamos retornando `corpo da resposta {}` e o `status code`.

**drive.py:**
```python
import os
import sys
from pathlib import Path

import django
from django.test import RequestFactory

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from users.views import register_api

def test_register_api():

    factory = RequestFactory()

    # Simulando uma requisição GET (errada)
    request = factory.get("/register/")

    response = register_api(request)

    print(response.status_code)  # 405
    print(response.content)      # {"error": "Method not allowed"}


if __name__ == "__main__":
    test_register_api()
```

**OUTPUT:**
```python
405
b'{"error": "Method not allowed"}'
```

> **Lembra que no frontend (uma das origem) foi enviado dados com a função fetch()?**

```js
const response = await fetch("http://localhost:8000/register/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    username,
    email,
    password1: password,
    password2: confirm,
  }),
})
```

Então, nós precisamos pegar esses dados e para isso vamos utilizar o `request.body`:

```python
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    data = request.body
```

> **⚠️ NOTE:**  
> O problema é que o `request.body` retornaria bytes e não seria bom trabalhar com isso.

Para resolver isso vamos:

 - Aplicar `cast` no `request.body` para converter em um dicionário
 - E dar um load com `json.loads(request.body)`:

```python
import json
from typing import cast


@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    try:
        data = cast(dict[str, Any], json.loads(request.body))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    return JsonResponse(data)
```

> **⚠️ NOTE:**  
> Não vamos retornar o `corpo da resposta {}` e o `status code` porque ainda é uma fase de teste.

**drive.py:**
```python
import json
import os
import sys
from pathlib import Path

import django
from django.test import RequestFactory

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from users.views import register_api


def test_register_api():

    factory = RequestFactory()

    payload = {
        "username": "rodrigo",
        "email": "rodrigo@email.com",
        "password1": "123456",
        "password2": "123456",
    }

    request = factory.post(
        "/register/",
        data=json.dumps(payload),          # JSON igual ao fetch
        content_type="application/json",   # MUITO IMPORTANTE
    )

    # Simula requisição POST
    response = register_api(request)

    print("Status:", response.status_code)
    print("Body:", response.content.decode())


if __name__ == "__main__":
    test_register_api()
```

**OUTPUT:**
```python
Status: 200
Body: {"username": "rodrigo", "email": "rodrigo@email.com", "password1": "123456", "password2": "123456"}
```

> **⚠️ NOTE:**   
> O código HTTP 200 OK é a resposta de status de sucesso que indica que a requisição foi bem sucedida

Ótimo, nós já entendemos o processo de como os dados são recebidos e convertidos em um dicionário, agora nós vamos transformar esses dados em um objeto (que foi modelado em forms.py):

```python
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    try:
        data = cast(dict[str, Any], json.loads(request.body))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    form = CustomUserCreationForm(data)

    ...
```

> **Ótimo, só isso?**  
> Não!

Agora, nós precisamos salvar esses dados no Banco de Dados, que vai seguir o seguinte processo:

 - Verificar se o formulário está válido:
   - `if form.is_valid():`
 - Aplicar `user = form.save()`, isso faz basicamente 3 coisas:
   - Valida os dados já limpos (cleaned_data)
   - Cria um objeto do modelo (User)
   - Salva no banco de dados
   - O que isso retorna?
     - 👉 Ele retorna a instância do usuário criado
     - `print(user)      # <User: rodrigo>`
     - `print(user.id)   # 1 `
 - Por fim, retornar um o `corpo da resposta {}` e o `status code`.

```python
@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    try:
        data = cast(dict[str, Any], json.loads(request.body))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    form = CustomUserCreationForm(data)

    if form.is_valid():  # ✅ corrigido
        user = form.save()  # ✅ salva no banco
        return JsonResponse(
            {
                "message": "User created successfully",
                "user_id": user.id,
            },
            status=201,
        )
    
    ...
```

Vocês concordam que:

 - Se o método for `get()` nós vamos retornar uma mensagem de erro
 - E se der um erro durante o processo de `user = form.save()`?

Bem, nesse caso vamos precisar retornar esse erro (no corpo da requisição) + status code de erro:

```python
import json
from typing import Any, cast

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm


@csrf_exempt
def register_api(request: HttpRequest) -> JsonResponse:

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    try:
        data = cast(dict[str, Any], json.loads(request.body))
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    form = CustomUserCreationForm(data)

    if form.is_valid():
        user = form.save()
        return JsonResponse(
            {
                "message": "User created successfully",
                "user_id": user.id,
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors},
        status=400
    )
```

**drive.py:**
```python
import json
import os
import sys
from pathlib import Path

import django
from django.test import RequestFactory

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from users.views import register_api
from django.contrib.auth import get_user_model


def test_register_api():
    factory = RequestFactory()

    User = get_user_model()

    # 🔥 Evita erro de usuário duplicado
    User.objects.filter(username="rodrigo").delete()

    payload = {
        "username": "rodrigo",
        "email": "rodrigo@email.com",
        "password1": "@SenhaQuePass98",
        "password2": "@SenhaQuePass98",
    }

    request = factory.post(
        "/register/",
        data=json.dumps(payload),
        content_type="application/json",
    )

    response = register_api(request)

    print("Status:", response.status_code)
    print("Body:", response.content.decode())

    # 🔍 Verificando se salvou no banco
    user_exists = User.objects.filter(username="rodrigo").exists()
    print("User criado no banco?", user_exists)


if __name__ == "__main__":
    test_register_api()
```

**OUTPUT:**
```python
Status: 201
Body: {"message": "User created successfully", "user_id": 5}
User criado no banco? True
```

> **⚠️ NOTE:**  
> Agora, se você olhar no Banco de Dados verá que esse usuário foi salvo.

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
