# Django

## Contents

 - **Django Basics:**
   - [Django Architecture ( Model-Template-View | MTV )](#django-architecture)
   - [Projects vs. apps](#project-x-app)
   - [Django Structure](#django-structure)
 - **Django Admin:**
   - `python manage.py createsuperuser` (http://localhost:8000/admin)
   - [Add your models to the Django Admin](#add-your-models-to-the-django-admin)
 - **Migrations (Allows Django to "Manage" and "Version Control" database schemas):**
   - [Specifying the Databases](#specifying-the-databases)
   - [`python manage.py migrate (Send migrations to the database)`](#migrate)
   - [`python manage.py makemigrations (Create/Version the changes in the model using migrations files)`](#makemigrations)
 - **Model-View-Template (MVT):**
   - [**Model:**](#intro-to-models)
     - [Separating models by files](#separating-models-by-files)
   - [**View:**](#intro-to-views)
   - [**Template:**](#intro-to-templates)
 - **Project & App Settings:**
   - [How add an App to the Project](#how-add-an-app-to-the-project)
   - [Creating React and Django Projects](#react-django-projects)
 - **Commands:**
   - `django-admin startproject <ProjectName>`
   - `django-admin startapp <AppName>`
   - `python manage.py runserver (You can specify a port number here)`
 - **Code Snippet:**
   - **Model:**
   - **Template:**
   - **View:**
   - **Tests:**
   - **Database:**
   - **API:**
 - **Projects:**
   - [Pythonando (PSW 11)](projects/psw11)
 - [**Settings**](#settings)
 - [**References**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "5" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Django Basics ) --->

---

<div id="django-architecture"></div>

## Django Architecture ( Model-Template-View | MTV )

> **Django** is a Web Framework that is built on the **Model-Template-View (MTV)** pattern.

For example, see the examples below to understand more easily:

**Example-01:**
![img](images/django-architecture-01.png)  

 - **Model:**
   - The *model* is responsible for `storing` and `retrieving` data from a database.
   - It also contains the business logic for the application, such as validation and relationships between data.
   - **When to use:** The model is used to manage and manipulate data. It is responsible for handling the data-related tasks, such as fetching data from a database, processing it, and updating it.
 - **Template:**
   - The *template* is `responsible for rendering the user interface of the application`.
   - It uses *HTML*, *CSS*, and *JavaScript* to create the pages that users see.
   - **When to use:** Templates are used for rendering and displaying information to the user. They take the data provided by the model and format it in a way that is suitable for presentation.
 - **View:**
   - The *view* is `responsible for handling user requests` and `rendering the appropriate template`.
   - It also communicates with the model to retrieve data.
   - **When to use:** Views are used to present the user interface and handle user input. They interact with the model to fetch and display data, and they also capture user actions and pass them to the controller for further processing.





---

<div id="project-x-app"></div>

## Projects vs. apps

The difference between **a project** and **an app** is:

 - **A project** is a `collection of configuration` and `apps` for a particular website:
   - `A project can contain multiple apps.`
 - **An app** is a web application that *"does something"*:
   - A blog system;
   - A database of public records;
   - A small poll app...
   - `An app can be in multiple projects.`





---

<div id="django-structure"></div>

## Django Structure

After you create a Django project you will have the following structure:

```bash
django-admin startproject <ProjectName>
```

```bash
├─── .<ProjectName>
│    ├── <ProjectName>
│    |      ├── __init__.py
│    |      ├── asgi.py
│    |      ├── settings.py
│    |      ├── urls.py
│    |      ├── wsgi.py
│    ├── manage.py
│    ├── <AppName>
│    |      ├── /migrations
│    |      |      ├── __init__.py
│    |      ├── __init__.py
│    |      ├── admin.py
│    |      ├── apps.py
│    |      ├── models.py
│    |      ├── tests.py
│    |      ├── views.py
```

Where:

 - `.<ProjectName>` Root folder.
   - `<ProjectName>` Project setting files.
     - `__init__.py`
     - `asgi.py` ASGI server settings.
     - `settings.py` All settings for the project:
       - Define templates sources.
       - Apps installed.
       - Project secret key.
     - `urls.py` Project URLs:
       - www.example.com/blog
       - www.example.com/admin
     - `wsgi.py` WSGI server settings.
   - `manage.py` File to manage the project.
     - `python manage.py runserver`.
   - `<AppName>` Project apps (E.g. /site, /store, etc).
     - `/migrations` Manage changes to the Database.
       - `__init__.py`
     - `/templates` Project/App frontend files.
       - `__init__.py`
       - HTML, CSS, and JavaScript files.
     - `__init__.py`
     - `admin.py`
     - `apps.py`
     - `models.py` Here you will create things that you will store in your Database:
       - For example, database tables.
     - `tests.py`
     - `views.py` Represents your App's logic:
       - When the use click on the `/blog` URL what happens?
       - When the user clicks on the `/admin` URL what happens?
       - Link the views to the templates.




















































<!--- ( Django Admin ) --->

---

<div id="add-your-models-to-the-django-admin"></div>

## Add your models to the Django Admin

For your models to appear in the Django Admin, first imagine we have the following models (classes):

```python
# your-app/models.py

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
```

Now, for your models to appear in the Django Admin, we need to add them to the `admin.py` file:

```python
# your-app/admin.py

from django.contrib import admin
from blog.models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass
```

Now, let's register a `user` to login on the Django Admin:

```bash
python manage.py makemigrations <app_name>
```

```bash
python manage.py migrate <app_name>
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

> **NOTE:**
> If we look better, we don't have our models in the Django Admin.

To solva that we need to register our models in the `admin.py` file:

```python
# your-app/admin.py

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
```

 - Now, if you reload the Django Admin page, you should see your models listed.
 - If you click on *Posts*, you can add new posts for the blog manually.




















































<!--- ( Migrations ) --->

---

<div id="specifying-the-databases"></div>

## Specifying the Databases

To specify the database we need to open the `settings.py` file in the project folder and find the **"DATABASES key"**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

> ***NOTE:**  
> By default, Django uses the **"sqlite3"** database.

Now, let's see how to add other databases:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mysql_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': 'localhost',
        'PORT': '3310',
    },
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'toor',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

See that:

 - We have a default database: **sqlite3**.
 - Setting to use another databases: **"mysql_db"** and **"postgresql_db"**.

**NOTE:**  
To apply migrations to a specific database you need to run the following command:

```bash
# MySQL.
python manage.py migrate --database=mysql_db

# PostgreSQL.
python manage.py migrate --database=postgresql_db
```





---

<div id="migrate"></div>

## `python manage.py migrate (Send migrations to the database)`

```bash
python manage.py migrate
```

> The command above is used to *"send migrations to the database"*.

For example:

 - The command `migrate` prepares the Django Database:
   - Commonly used to initialize the database.
 - When we *create/modify a model*, we need to run the `migrate` command to send the changes to the database.





---

<div id="makemigrations"></div>

## `python manage.py makemigrations (Create/Version the changes in the model using migrations files)`

To understand the command `makemigrations`, let's imagine we have an App `employees_management` with the following models.

```python
# employees_management/models.py

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=250)
```

> **NOTE:**  
> Before run the `makemigrations` command, we need to:
> - Add the App to the `INSTALLED_APPS` list in `settings.py` file.
> - Run the command `python manage.py migrate`.

```bash
python manage.py makemigrations
```

**OUTPUT:**  
```bash
 employee_management/migrations/0001_initial.py
    + Create model Employee
```

See that:

 - The django created a folder `/migrations`.
 - With the file `0001_initial.py`:
   - Represents the first migration or model version.
   - If we change the model, we need to run the `makemigrations` command again:
     - **NOTE:** In other words, as we improve our models (a medida que nós vamos incrementando nossos modelos), we will run the `makemigrations` command and version the changes in the model.

```python
# migrations/0001_initial.py

# Generated by Django 5.1 on 2024-08-11 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
```

 - `Generated by Django 5.1 on 2024-08-11 04:30`
   - Date and hour of the migration.
 - `initial = True`
   - Says that this is the first migration.
 - `dependencies = []`
   - Dependencies for this migration.
 - `migrations.CreateModel()`
   - Class to create a model's table.
 - `name='Employee'`
   - Name of the model (table).
 - `fields=[id, name]`
   - Fields of the model (table).
   - **NOTE:** Since I didn't define a *"Primary Key"*, django automatically created the `id` field to be the *primary key*.

Briefly:

> The command `makemigrations` create/version the changes in the model using the migrations files.




















































<!--- ( Model-View-Template (MVT)/Model ) --->

---

<div id="intro-to-models"></div>

## Model

> Everything related to Databases.

 - **Definition:**
   - Models are Python classes that define the structure of your database.
 - **Purpose:**
   - Define database schema.
   - Define relationships between different data entities.
   - Provide an abstraction layer for database operations.

**EXAMPLE:**
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name
```

In this example:

 - Author is a model with three fields:
   - *"name"*, *"birth_date"*, and *"email"*.
 - Each field is represented by a field class (e.g., CharField, DateField, EmailField) that specifies the type of data it holds.

---

<div id="separating-models-by-files"></div>

## Separating models by files

 - It is common at the beginning of our application to create our models in the `models.py` file.
 - However, as our application scales, we will have many models in the same file.
 - So, the interesting thing here would be to divide our models by files:
   - **NOTE:** This ensures/helps the modularization of the system.

For example, imagine we have the following models:

```python
# employees_management/models.py

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=250)


class Department(models.Model):
    name = models.CharField(max_length=250)
```

To separate them first, let's create the following structure: 

```bash
├── <employees_management>
|      ├── /models
|      |      ├── __init__.py
|      |      ├── employee.py
|      |      ├── department.py
```

```python
# employees_management/models/employee.py

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=250)
```

```python
# employees_management/models/department.py

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=250)
```

**NOTE:**  

 - **EN -** Now we need to import the modules `(employee.py and department.py)` in the `__init__.py` file so that Django can work with these models that are in separate files.
 - **PT -** Agora nós precisamos importar os módulos `(employee.py e department.py)` no arquivo `__init__.py `para o django conseguir trabalhar com esses models que estão em arquivos separados.

```python
# employees_management/models/__init__.py

from .employee import Employee
from .department import Department
```

Finally, run the Django migration commands:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```





<!--- ( Model-View-Template (MVT)/View ) --->

---

<div id="intro-to-views"></div>

## View

 - Views are where the logic of our Application is located.
 - For example, these are the Python functions that will receive a *"request"* and return a *"response"*.





<!--- ( Model-View-Template (MVT)/Template ) --->

---

<div id="intro-to-templates"></div>

## Template

> Templates are our HTML files that will be displayed to the user.




















































<!--- ( Project & App Settings ) --->

---

<div id="how-add-an-app-to-the-project"></div>

## How add an App to the Project

> After install (create) an App we need to install (register) this App in our project. To do this, we need to add it in our `settings.py` file.

For example, imagine we create the `blog` App:

```bash
django-admin startapp blog
```

Now, let's add the new app to the project:

```python
# personal_blog/settings.py

# ...

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig", # <--- App added here.
]

# ...
```

You can check the app settings on the `apps.py` file inside the app folder:

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```





---

<div id="react-django-projects"></div>

## Creating React and Django Projects

A common approach to create Django and React Project is:

 - Create a project with django-admin (This will be the Root/Backend of the project):
   - django-admin startproject `<project_name>`
 - Initialize `pyproject.toml` inside the root:
   - poetry init
 - Create the frontend with create-react-app:
   - npx create-react-app frontend




















































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv django-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source django-environment/Scripts/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source django-environment/bin/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**VSCode - Tip:**  
If your VSCode doesn't recognize your Python interpreter you can add it manually:

 - View:
   - Comand Palette:
     - Python: Select Interpreter:
       - Enter interpreter path...
         - Find...
           - Select your "environment":
             - environment/bin/your-python-interpreter-version.

**Now, Be Happy!!!** 😬





<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - **General:**
   - [Python Documentation](https://docs.djangoproject.com/)
   - [Google Gemini](https://gemini.google.com/app)
   - [ChatGPT](https://chatgpt.com/)
   - [Estrutura Básica de um Projeto em Django](https://www.youtube.com/watch?v=4u0aI-90KnU)
 - **Tutorials:**
   - [How To Build a To-Do application Using Django and React](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
   - [Build a Blog From Scratch With Django](https://realpython.com/build-a-blog-from-scratch-django/)
   - [Dev Fullstack Cloud](https://www.youtube.com/playlist?list=PLsA_kcShOU63R5AWqD4Apn78ePPbpncv4)

---

**Rodrigo** **L**eite da **S**ilva
