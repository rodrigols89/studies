# Django

## Contents

 - **Basics:**
   - [Django Architecture ( Model-Template-View | MTV )](#django-architecture)
   - [Projects vs. apps](#project-x-app)
   - [Django Structure](#django-structure)
 - **Commands:**
   - `django-admin startproject ProjectName`
   - `python manage.py runserver`
   - `python manage.py startapp polls`
 - **Code Snippet:**
   - **Model:**
   - **Template:**
   - **View:**
   - **Tests:**
 - [Settings](#settings)
 - [References](#ref)












<!--- ( Basics ) --->

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

The basic structure of **Django** is:

![img](images/django-structure-01.jpg)















































<!--- ( Code Snippet/Model ) --->

---

<!--- ( Code Snippet/Template ) --->
<!--- ( Code Snippet/View ) --->
<!--- ( Code Snippet/Tests ) --->
















































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

**Now, Be Happy!!!** 😬







































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [x](#)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
