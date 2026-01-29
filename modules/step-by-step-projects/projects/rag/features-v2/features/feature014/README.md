# `Criando a landing page da aplicação (base.html + index.html)`

Aqui nós vamos implementar a `landing page` da nossa aplicação, mas antes disso vamos criar o nosso `HTML base` que é responsável por aplicar configurações globais aos nossos templates:

[base.html](../../../templates/base.html)
```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <!-- ================================================================== -->
        <!-- METADADOS E CONFIGURAÇÕES BÁSICAS                                -->
        <!-- ================================================================== -->
        
        <!-- Codificação de caracteres UTF-8 -->
        <meta charset="UTF-8">
        
        <!-- Viewport para responsividade em dispositivos móveis -->
        <meta name="viewport" 
              content="width=device-width, initial-scale=1.0">
        
        <!-- Título da página (pode ser sobrescrito por templates filhos) -->
        <title>
            {% block title %}RAG Project{% endblock title %}
        </title>
        
        <!-- ================================================================== -->
        <!-- FRAMEWORKS E BIBLIOTECAS EXTERNAS                                -->
        <!-- ================================================================== -->
        
        <!-- Tailwind CSS via CDN (versão browser) -->
        <!-- Fornece utilitários de CSS para estilização rápida -->
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4">
        </script>
        
        <!-- ================================================================== -->
        <!-- BLOCOS CUSTOMIZÁVEIS                                             -->
        <!-- ================================================================== -->
        
        <!-- Bloco para adicionar elementos no <head> (CSS, meta tags, etc) -->
        {% block head %}{% endblock head %}
    </head>
    <body class="min-h-screen bg-[#343541]">
        <!-- ================================================================== -->
        <!-- CONTEÚDO PRINCIPAL                                                -->
        <!-- ================================================================== -->
        
        <!-- Bloco principal de conteúdo da página -->
        <!-- Deve ser preenchido pelos templates filhos -->
        {% block content %}{% endblock content %}
        
        <!-- ================================================================== -->
        <!-- SCRIPTS JAVASCRIPT                                                -->
        <!-- ================================================================== -->
        
        <!-- Bloco para adicionar scripts JavaScript no final do body -->
        <!-- Colocar scripts no final melhora o tempo de carregamento -->
        {% block scripts %}{% endblock scripts %}
    </body>
</html>
```

Agora sim, vamos partir para a criação da nossa `landing page`...

> **Mas, afinal, o que é um "landing page"?**

Uma `landing page` pública geralmente contem:

 - Apresentação do produto/serviço.
 - Botões de “Entrar” e “Cadastrar”.
 - Sessões com informações sobre a empresa.
 - Depoimentos, preços, etc.

Vamos começar configurando a rota/url que vai ser nosso `/`:

[users/urls.py](../../../users/urls.py)
```python
from django.urls import path

from .views import login_view

urlpatterns = [
    path(route="", view=login_view, name="index"),
]
```

 - Essa rota/url `/` vai ser tratada dentro do App `users` porque futuramente nós vamos criar condições para verificar se o usuário está logado ou não no sistema.
 - Desta maneira, é interessante que essa rota/url `/` seja tratada dentro do App `users`.

Continuando, agora vamos criar uma view (ação) para essa `landing page`:

[users/views.py](../../../users/views.py)
```python
from django.shortcuts import render


def login_view(request):
    if request.method == "GET":
        return render(request, "pages/index.html")
```

> **NOTE:**  
> O nome desta view (ação) é `login_view()` porque futuramente nós vamos atualizar ela para tratar logins de usuários.

Por fim, vamos criar o HTML para essa `landing page`:

[templates/icons/github.svg.html](../../../templates/icons/github.svg.html)
```html
<!--
    Ícone SVG do GitHub.

    Este ícone é usado nos botões de login social com GitHub.
    Utiliza SVG inline para melhor performance e customização.
    O ícone é estilizado com classes Tailwind CSS.
-->
<svg class="h-5 w-5 mr-2"
     viewBox="0 0 24 24"
     fill="currentColor"
     aria-hidden="true">
    <!-- Path do logo do GitHub (gato Octocat) -->
    <path fill-rule="evenodd" 
          d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.385.6.11.82-.26.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.385-1.333-1.754-1.333-1.754-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.236 1.84 1.236 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.304.762-1.603-2.665-.303-5.467-1.333-5.467-5.93 0-1.31.468-2.38 1.235-3.22-.124-.303-.535-1.523.117-3.176 0 0 1.008-.322 3.3 1.23a11.5 11.5 0 013.003-.404c1.02.005 2.045.138 3.003.404 2.29-1.552 3.297-1.23 3.297-1.23.653 1.653.243 2.873.12 3.176.77.84 1.234 1.91 1.234 3.22 0 4.61-2.807 5.624-5.48 5.92.43.372.823 1.102.823 2.222 0 1.604-.014 2.896-.014 3.29 0 .32.217.694.825.576C20.565 21.796 24 17.297 24 12c0-6.63-5.37-12-12-12z"/>
</svg>
```

[templates/icons/google.svg.html](../../../templates/icons/google.svg.html)
```html
<!--
    Ícone SVG do Google.

    Este ícone é usado nos botões de login social com Google.
    Utiliza SVG inline para melhor performance e customização.
    O ícone mantém as cores oficiais do Google (azul, verde, 
    amarelo e vermelho) e é estilizado com classes Tailwind CSS.
-->
<svg class="h-5 w-5 mr-2"
     viewBox="0 0 533.5 544.3"
     xmlns="http://www.w3.org/2000/svg"
     aria-hidden="true">
    <!-- Parte azul do logo (canto superior esquerdo) -->
    <path d="M533.5 278.4c0-18.2-1.6-36-4.7-53.2H272v100.8h147.4c-6.4 34.9-26 64.5-55.5 84.3v69.9h89.6c52.5-48.3 82-119.7 82-201.8z" 
          fill="#4285F4"/>
    <!-- Parte verde do logo (canto inferior esquerdo) -->
    <path d="M272 544.3c73.5 0 135.3-24.5 180.4-66.7l-89.6-69.9c-24.9 16.7-56.9 26.6-90.8 26.6-69.7 0-128.7-47.1-149.8-110.4H31.6v69.5C76.3 494.7 169 544.3 272 544.3z" 
          fill="#34A853"/>
    <!-- Parte amarela do logo (canto inferior direito) -->
    <path d="M122.2 327.1c-11.7-34.6-11.7-72 0-106.6V150.9H31.6c-39.6 77-39.6 168.5 0 245.5l90.6-69.3z" 
          fill="#FBBC05"/>
    <!-- Parte vermelha do logo (canto superior direito) -->
    <path d="M272 107.7c39.9 0 75.7 13.7 104 40.6l78-78C403.3 24.7 337.2 0 272 0 169 0 76.3 49.6 31.6 150.9l90.6 69.5C143.3 154.8 202.3 107.7 272 107.7z" 
          fill="#EA4335"/>
</svg>
```

[templates/pages/index.html](../../../templates/pages/index.html)
```html
<!--
    Template da página inicial (login).

    Esta página exibe um formulário de login com suporte a:
    - Login tradicional (username/password)
    - Login social via Google e GitHub
    - Link para criação de nova conta

    Utiliza Tailwind CSS para estilização e django-allauth
    para autenticação social.
-->
{% extends "base.html" %}

{% block content %}

    <!-- ==================================================================== -->
    <!-- CONTEÚDO PRINCIPAL - ÁREA DE LOGIN                                  -->
    <!-- ==================================================================== -->
    
    <main class="min-h-screen flex items-center justify-center py-12 
                 px-4 sm:px-6 lg:px-8">
        
        <!-- ================================================================ -->
        <!-- CARD DE LOGIN                                                  -->
        <!-- ================================================================ -->
        
        <div class="max-w-md w-full space-y-8 bg-white py-8 px-6 shadow 
                    rounded-lg">
            
            <!-- ============================================================ -->
            <!-- CABEÇALHO - LOGO E TÍTULO                                   -->
            <!-- ============================================================ -->
            
            <div class="mb-6 text-center">
                <h2 class="mt-4 text-2xl font-semibold text-gray-900">
                    RAG Project
                </h2>
                <p class="mt-1 text-sm text-gray-500">
                    Faça login para acessar seu painel
                </p>
            </div>

            <!-- ============================================================ -->
            <!-- MENSAGENS DO SISTEMA                                        -->
            <!-- ============================================================ -->
            
            <!-- Exibe mensagens de erro ou sucesso do Django -->
            {% if messages %}
                <div class="mb-4">
                    {% for message in messages %}
                        <div class="text-red-600 bg-red-100 
                                    border border-red-200 rounded-md 
                                    px-4 py-2 text-sm">
                            {{ message }}
                        </div>
                    {% endfor %}
                </div>
            {% endif %}

            <!-- ============================================================ -->
            <!-- FORMULÁRIO DE LOGIN TRADICIONAL                             -->
            <!-- ============================================================ -->
            
            <form method="post" action="" class="space-y-6">
                <!-- Token CSRF para proteção contra ataques -->
                {% csrf_token %}

                <!-- Campo de Username -->
                <div>
                    <label for="username" 
                           class="block text-sm font-medium 
                                  text-gray-700">
                        Usuário
                    </label>
                    <div class="mt-1">
                        <input
                            id="username"
                            name="username"
                            type="text"
                            autocomplete="username"
                            required
                            class="appearance-none block w-full px-3 
                                   py-2 border border-gray-300 
                                   rounded-md shadow-sm 
                                   placeholder-gray-400 
                                   focus:outline-none focus:ring-2 
                                   focus:ring-blue-500 
                                   focus:border-blue-500 sm:text-sm">
                    </div>
                </div>

                <!-- Campo de Senha -->
                <div>
                    <label for="password" 
                           class="block text-sm font-medium 
                                  text-gray-700">
                        Senha
                    </label>
                    <div class="mt-1">
                        <input
                            id="password"
                            name="password"
                            type="password"
                            autocomplete="current-password"
                            required
                            class="appearance-none block w-full px-3 
                                   py-2 border border-gray-300 
                                   rounded-md shadow-sm 
                                   placeholder-gray-400 
                                   focus:outline-none focus:ring-2 
                                   focus:ring-blue-500 
                                   focus:border-blue-500 sm:text-sm">
                    </div>
                </div>

                <!-- Botão de Submit -->
                <div>
                    <button type="submit"
                            class="w-full flex justify-center py-2 px-4 
                                   border border-transparent 
                                   rounded-md shadow-sm 
                                   text-sm font-medium 
                                   text-white bg-blue-600 
                                   hover:bg-blue-700 
                                   focus:outline-none focus:ring-2 
                                   focus:ring-offset-2 
                                   focus:ring-blue-500">
                        Entrar
                    </button>
                </div>
            </form>

            <!-- ============================================================ -->
            <!-- DIVISOR - SEPARADOR ENTRE LOGIN TRADICIONAL E SOCIAL        -->
            <!-- ============================================================ -->
            
            <div class="mt-6 relative">
                <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-gray-200"></div>
                </div>
                <div class="relative flex justify-center text-sm">
                    <span class="bg-white px-2 text-gray-500">
                        ou continuar com
                    </span>
                </div>
            </div>

            <!-- ============================================================ -->
            <!-- BOTÕES DE LOGIN SOCIAL                                       -->
            <!-- ============================================================ -->
            
            <!-- Grid com dois botões lado a lado (Google e GitHub) -->
            <div class="mt-6 grid grid-cols-2 gap-3">
                
                <!-- Botão de Login com Google -->
                <div>
                    <a href=""
                       class="w-full inline-flex justify-center 
                              items-center py-2 px-4 border 
                              border-gray-300 rounded-md 
                              shadow-sm bg-white hover:bg-gray-50">
                        <!-- Ícone do Google -->
                        {% include "icons/google.svg.html" %}
                        <span class="text-sm font-medium 
                                     text-gray-700">
                            Google
                        </span>
                    </a>
                </div>

                <!-- Botão de Login com GitHub -->
                <div>
                    <a href=""
                       class="w-full inline-flex justify-center 
                              items-center py-2 px-4 border 
                              border-gray-300 rounded-md 
                              shadow-sm bg-white hover:bg-gray-50">
                        <!-- Ícone do GitHub -->
                        {% include "icons/github.svg.html" %}
                        <span class="text-sm font-medium 
                                     text-gray-700">
                            GitHub
                        </span>
                    </a>
                </div>
            </div>

            <!-- ============================================================ -->
            <!-- RODAPÉ - LINK PARA CADASTRO                                 -->
            <!-- ============================================================ -->
            
            <p class="mt-6 text-center text-sm text-gray-600">
                Não tem conta?
                <a href="" 
                   class="font-medium text-blue-600 
                          hover:text-blue-700">
                    Cadastrar
                </a>
            </p>

        </div>

    </main>
{% endblock %}
```

> **NOTE:**  
> Não vou comentar sobre os *CSS/TailwindCSS* utilizados porque não é o foco desse tutorial.

Finalmente, se você abrir o projeto (site) na rota/url principal vai aparecer essa `landing page`.

 - [http://localhost/](http://localhost/)

![landing page](images/index-landing-01.png)  

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
