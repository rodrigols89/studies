# Django

## Conteúdo

 - **Formulários:**
   - [`Como enviar dados do formulário para uma view (backend)`](#htsdtv)
   - [`Como pegar dados de um formulário (de cadastro ou login)`](#htgd)
 - **ORM:**
   - [`Como modelar uma tabela com Django models`](#hmdt)
   - [`Como registrar uma tabela no Django Admin`](#register-table-django-admin)
   - [`Como instanciar uma classe (tabela) e salvar no Banco de Dados`](#instance-table-and-save-on-db)
 - **Eventos:**
   - [`Criando um signal (gatilho) para determinados eventos`](#create-signals)
<!---
[WHITESPACE RULES]
- 20
--->




















---

<div id="htsdtv"></div>

## `Como enviar dados do formulário para uma view (backend)`

Para enviar dados de um formulário para uma view (backend) o caminho mais fácil é utilizar a tag `url` do Django no formulários:

```html
<form method="post" action="{% url 'cadastro' %}">
    {% csrf_token %}

</form>
```

Vejam que nós:

 - Utilizamos o método `POST`
   - Ou seja, estamos enviando dados para o servidor
 - E a ação (action) vai ser chamar a URL `cadastro`

> **⚠️ NOTE:**  
> Agora lá dentro da view ela vai ser capaz de receber os dados do formulário





















---

<div id="htgd"></div>

## `Como pegar dados de um formulário (de cadastro ou login)`

Para pegar os dados os dados de um formulário com views do Django, primeiro nós precisamos identificar os `name` dos campos no formulário:

```html
<input id="username"
        name="username"
        type="text"
        placeholder="seu.usuario"
        autocomplete="username"
        required>

<input id="password"
        name="senha"
        type="password"
        placeholder="**********"
        autocomplete="new-password"
        required>

<input id="confirm_password"
        name="confirmar_senha"
        type="password"
        placeholder="**********"
        autocomplete="new-password"
        required>
```

Vejam que nós temos os `name`:

 - username
 - senha
 - confirmar_senha

Agora é só pegar esses dados do formulário com o método `request.POST.get()`:

```python
username = request.POST.get('username')
senha = request.POST.get('senha')
confirmar_senha = request.POST.get('confirmar_senha')
```

Agora, você poderá pegar esses dados e fazer validações. Por exemplo:

**VALIDAÇÕES DE CADASTRO:**
```python
# Verifica se as senhas coincidem
if senha != confirmar_senha:
    messages.add_message(request, constants.ERROR, 'Senha e confirmar senha não conferem')
    return redirect('cadastro')

# Verifica se a senha tem menos de 6 caracteres
if len(senha) < 6:
    messages.add_message(request, constants.ERROR, 'Sua senha deve ter pelo menos 6 caracteres.')
    return redirect('cadastro')

# Faz uma consulta no banco de dados usando a ORM do Django para buscar usuários
# cujo campo username seja igual ao valor armazenado na variável username.
users = User.objects.filter(username=username)

# Se o usuário já existir retornar uma mensagem de erro dizendo que o usuário já existe
if users.exists():
    messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username.')
    return redirect('cadastro')

# Se o usuário não existe ainda, cria o mesmo no Banco de Dados.
User.objects.create_user(username=username, password=senha)
```

**VALIDAÇÕES DE LOGIN:**
```python
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('clientes')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('login')
```





















---

<div id="hmdt"></div>

## `Como modelar uma tabela com Django models`

Para criar (ou modelar) uma tabela para o nosso Banco de Dados com Django basta criar uma classe em `models.py` e fazer ela herdar de models a classe `Model`:

```python
from email.policy import default
from django.db import models

class Cliente(models.Model):
    especie_choices = [
        ('C', 'Cachorro'),
        ('G', 'Gato'),
    ]
    raca_choices = [
        ('SRD', 'SRD'),
        ('Labrador', 'Labrador'),
    ]
    triagem_choices = [
        ('verde', 'Verde'),
        ('amarelo', 'Amarelo'),
        ('laranja', 'Laranja'),
        ('vermelho', 'Vermelho'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    especie = models.CharField(max_length=1, choices=especie_choices, default='C')
    nome_animal = models.CharField(max_length=100, null=True, blank=True)
    raca = models.CharField(max_length=100, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    triagem = models.CharField(max_length=10, choices=triagem_choices, null=True, blank=True)

    def __str__(self):
        return self.nome
```

> **É só isso?**

**Não!**  
Primeiro, nós precisamos rodar as migrações:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Agora, se você olhar no Banco de Dados (não no Django Admin) verá que essa tabela foi criada.





















---

<div id="register-table-django-admin"></div>

## `Como registrar uma tabela no Django Admin`

Se você criou (modelou) uma tabela no Banco de Dados e ela não está aparecendo no Django Admin é porque você ainda não registrou a mesma no arquivo `admin.py`.

Para fazer isso é só fazer o seguinte:

`admin.py`
```python
from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)
```

> **NOTE:**  
> Agora é só reiniciar o servidor e abrir o Django Admin que você verá uma tabela `Cliente`.





















---

<div id="instance-table-and-save-on-db"></div>

## `Como instanciar uma classe (tabela) e salvar no Banco de Dados`

Sabendo-se que com o método `request.POST.get()` nós podemos pegar dados de um formulário a partir do atributo `name`, vamos ver como:

 - Instanciar uma classe (tabela)
 - Passar os dados recebidos com `request.POST.get()` para essa instância
 - Salvar no Banco de Dados

```python
def clientes(request):
    if request.method == 'GET':
        # GET codes.
    elif request.method == 'POST':

        # Pega os dados (enviados) do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        especie = request.POST.get('especie')
        nome_animal = request.POST.get('nome_animal')
        raca = request.POST.get('raca')
        idade = request.POST.get('idade')
        peso = request.POST.get('peso')

        # Passa os dados pelo construtor da classe
        # durante a instância
        cliente = Cliente(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            especie=especie,
            nome_animal=nome_animal,
            raca=raca,
            idade=idade,
            peso=peso
        )
        cliente.save()  # Salva esse registro no Banco de Dados
        messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado com sucesso.')
        return redirect('clientes')
```




















---

<div id="create-signals"></div>

## `Criando um signal (gatilho) para determinados eventos`

> A finalidade de uma `signal` no Django é permitir que o sistema execute ações automaticamente quando algum evento acontece na aplicação.

Ela funciona como um “gatilho”, por exemplo:

 - usuário foi criado
 - objeto foi salvo
 - objeto foi deletado
 - usuário fez login
 - requisição começou
 - requisição terminou

> **⚠️ NOTE:**  
> Quando um desses eventos acontece, o Django “dispara” uma signal, e funções registradas podem reagir automaticamente.

### `Registrando o signal (ready)`

Vamos começar criando um método `ready()` que será executado quando o Django carregar/inicializar a aplicação.

`apps.py`
```python
from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    name = 'usuarios'

    def ready(self):
        import usuarios.signals
```

> **Por que usar ready()?**

 - Porque as `signals` precisam ser registradas.
 - O Django só conhece a `signal` depois que o módulo é importado.
 - Isso força o carregamento do arquivo:
   - `usuarios/signals.py`

### `Criando um signal`

Para criar um signal nós temos que ficar atentos aos seguintes parâmetros:

 - `signal` → O QUE está acontecendo
   - `post_save` → Depois de salvar
   - `pre_save` → Antes de salvar
   - `post_delete` → Depois de deletar
   - `pre_delete` → Antes de deletar
   - `m2m_changed` → Quando relacionamento ManyToMany muda
 - `sender` → QUEM está fazendo
 - `dispatch_uid` → IDENTIDADE única da função
 - `weak` → detalhe interno (quase nunca importa)

**EXEMPLO:**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(
    signal=post_save,
    sender=User,
    dispatch_uid="user_create_profile"
)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        print("Criando perfil automaticamente")
```

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
