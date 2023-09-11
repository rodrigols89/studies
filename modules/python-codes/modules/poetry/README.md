# Poetry

## Contents

 - [Introduction to Poetry](#intro)
 - [Creating a project with poetry](#create-a-project)
 - [Initialising a pre-existing project](#pre-existing)
 - [Managing virtual environments with Poetry](#ve)
 - [Using activated virtual environment with "poetry shell"](#poetry-shell)
 - [Creating requirements.txt with poetry](#requirements)
 - [poetry install](#install)
 - [poetry add](#poetry-add)
 - [poetry update](#update)
 - [poetry show](#poetry-show)
 - [poetry search](#poetry-search)

---

<div id="intro"></div>

## Introduction to Poetry

> **Poetry** is a **Python Package Manager** that follows the **PEP** specifications [517](https://peps.python.org/pep-0517/) and [518](https://peps.python.org/pep-0518/).

**NOTE:**  
Poetry changes de follows files and commands:

![poetry-changes](images/poetry-changes.png)  

**NOTE:**  
When use the **Poetry?** **In dev environment!**

![dev-env](images/dev-env.png)  

**NOTE:**  
**pyproject.toml** is a Python format defined by PEP [517](https://peps.python.org/pep-0517/) and [518](https://peps.python.org/pep-0518/), don't Poetry format. 

---

<div id="create-a-project"></div>

## Creating a project with poetry

To create a project with poetry is very easy:

**CONSOLE:**  
```python
poetry new poetry-demo
```

**OUTPUT:**  
```python
Created package poetry_demo in poetry-demo
```

**NOTE:**  
This will create the **poetry-demo** directory with the following content:

```python
poetry-demo
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

**NOTE:**  
The **pyproject.toml** file is what is the most important here. This will orchestrate your project and its dependencies. For now, it looks like this:

```python
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"
```

---

<div id="pre-existing"></div>

## Initialising a pre-existing project

Instead of creating a new project, Poetry can be used to **‘initialise’** a pre-populated directory. To interactively create a **pyproject.toml** file in directory **pre-existing-project**:

**CONSOLE:**  
```python
mkdir pre-existing-project && cd pre-existing-project
```

**CONSOLE:**  
```python
poetry init
```

**OUTPUT:**  
```python
This command will guide you through creating your pyproject.toml config.

Package name [pre-existing-project]:  my_package
Version [0.1.0]:
Description []:  My first example
Author [drigols <drigols.creative@gmail.com>, n to skip]:
License []:  MIT
Compatible Python versions [^3.8]:

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
You can specify a package in the following forms:
  - A single name (requests)
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Search for package to add (or leave blank to continue):

Would you like to define your development dependencies interactively? (yes/no) [yes]
Search for package to add (or leave blank to continue):

Generated file

[tool.poetry]
name = "my_package"
version = "0.1.0"
description = "My first example"
authors = ["drigols <drigols.creative@gmail.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```

**NOTE:**  
See that we are setting the project <u>interactively</u>.

---

<div id="ve"></div>

## Managing virtual environments with Poetry

To create a **virtual environment** with **Poetry** is very easy. For example, for create a **virtual environment** with Python=3.8 use the follows poetry commands (Windows example):

**CONSOLE:**  
```python
where python
```

**OUTPUT:**  
```python
$ where python
C:\Users\Drigo\AppData\Local\Programs\Python\Python38\python.exe
C:\Users\Drigo\anaconda3\python.exe
C:\Users\Drigo\AppData\Local\Programs\Python\Python37\python.exe
```

**CONSOLE:**  
```python
poetry env use "C:\Users\Drigo\AppData\Local\Programs\Python\Python38\python.exe"
```

**OUTPUT:**  
```python
Creating virtualenv poetry-demo-GAZ1sPsk-py3.8 in C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs
Using virtualenv: C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.8
```

**NOTE:**  
We can have many **virtual environments** for the same project. For example, let's create another **virtual environment** with **python=3.7**.

**CONSOLE:**  
```python
poetry env use "C:\Users\Drigo\AppData\Local\Programs\Python\Python37\python.exe"
```

**OUTPUT:**  
```python
NoCompatiblePythonVersionFound

The specified Python version (3.7.0) is not supported by the project (^3.8).
Please choose a compatible version or loosen the python constraint specified in the pyproject.toml file.
```

**NOTE:**  
The problem here is that [pyproject.toml](poetry-demo/pyproject.toml) was specifying **python=^3.8**:

[pyproject.toml](poetry-demo/pyproject.toml)
```python
[tool.poetry.dependencies]
python = "^3.8"
```

Let's change to python=3.7 and try again:

[pyproject.toml](poetry-demo/pyproject.toml)
```python
[tool.poetry.dependencies]
python = "^3.7"
```

**CONSOLE:**  
```python
poetry env use "C:\Users\Drigo\AppData\Local\Programs\Python\Python37\python.exe"
```

**OUTPUT:**  
```python
Creating virtualenv poetry-demo-GAZ1sPsk-py3.7 in C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs
Using virtualenv: C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.7
```

**NOTE:**  
Now we have two virtual enviroments. To see just use the **poetry env list** command

**CONSOLE:**  
```python
poetry env list
```

**OUTPUT:**  
```python
poetry-demo-GAZ1sPsk-py3.7 (Activated)
poetry-demo-GAZ1sPsk-py3.8
```

**NOTE:**  
The activated virtual environment is Python=3.7. To change to the python=3.8 just use the command

**CONSOLE:**  
```python
poetry env use "C:\Users\Drigo\AppData\Local\Programs\Python\Python38\python.exe"
```

**OUTPUT:**  
```python
Using virtualenv: C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.8
```

**CONSOLE:**  
```python
poetry env list
```

**OUTPUT:**  
```python
poetry-demo-GAZ1sPsk-py3.7
poetry-demo-GAZ1sPsk-py3.8 (Activated)
```

**NOTE:**  
Now our virtual environment is using **python=3.8**.

You can also see information about your activated virtual environment using the command **poetry env info**:

**CONSOLE:**  
```python
poetry env info
```

**OUTPUT:**  
```python
Virtualenv
Python:         3.8.10
Implementation: CPython
Path:           C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.8
Valid:          True

System
Platform: win32
OS:       nt
Python:   c:\users\drigo\appdata\local\programs\python\python38
```

**NOTE:**  
Ok, but how a delete a specific virtual environment? Using **"poetry env remove /full/path/to/python"**:

**CONSOLE:**  
```python
poetry env remove "C:\Users\Drigo\AppData\Local\Programs\Python\Python38\python.exe"
```

**OUTPUT:**  
```python
Deleted virtualenv: C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.8
```

**CONSOLE:**  
```python
poetry env list
```

**OUTPUT:**  
```python
poetry-demo-GAZ1sPsk-py3.7
```

**CONSOLE:**  
```python
poetry env remove "C:\Users\Drigo\AppData\Local\Programs\Python\Python37\python.exe"
```

**OUTPUT:**  
```python
Deleted virtualenv: C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.7
```

**CONSOLE:**  
```python
$ poetry env list
```

**OUTPUT:**  
```python

```

**NOTE:**  
Ok, now we have not virtual environment for our project.

---

<div id="poetry-shell"></div>

## Using activated virtual environment with "poetry shell"

> Ok, now we know how manages virtual environment with poetry, let's go learn how use it.

To use virtual environment with poetry is easy, just use the command **"poetry shell"** to use activated virtual environment:

**CONSOLE:**  
```python
poetry shell
```

**OUTPUT:**  
```python
Spawning shell within C:\Users\Drigo\AppData\Local\pypoetry\Cache\virtualenvs\poetry-demo-GAZ1sPsk-py3.7
```

**CONSOLE:**  
```python
python
```

**OUTPUT:**  
```python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**NOTES:**  
 - See that we are using **poetry virtual environment** with **python=3.7**.
 - To exit of the virtual environment just use the **"exit"** command on the console.

---

<div id="requirements"></div>

## Creating requirements.txt with poetry

To create your **requirements.txt** with poetry is very easy:

**CONSOLE:**  
```python
poetry export -f requirements.txt -o requirements.txt
```

**NOTE:**  
To install **requirements.txt** in production with **"pip"** you need to use the follows command.

**CONSOLE:**  
```python
pip install --require-hashes --upgrade -r requirements.txt
or
pip install --require-hashes -r requirements.txt
```

---

<div id="install"></div>

## poetry install

 - The install command reads the **pyproject.toml** file from the current project;
 - Resolves the dependencies;
 - And installs them.

**CONSOLE:**  
```python
poetry install
```

**NOTE:**  
You can specify to the command that you do not want the development dependencies installed by passing the **--no-dev** option:

**CONSOLE:**  
```python
poetry install --no-dev
```

**Poetry install have the follows Options:**
 - **--no-dev:** Do not install dev dependencies.
 - **--no-root:** Do not install the root package (your project).
 - **--extras (-E):** Features to install (multiple values allowed).

---

<div id="poetry-add"></div>

## poetry add

> The add command adds required packages to your pyproject.toml and installs them.

**NOTE:**  
If you do not specify a version constraint, poetry will choose a suitable one based on the available package versions.

**CONSOLE:**  
```python
poetry add requests pendulum
```

You also can specify a constraint when adding a package, like so:

**CONSOLE:**  
```python
poetry add pendulum@^2.0.5
poetry add "pendulum>=2.0.5"
```

If you try to add a package that is already present, you will get an error. However, if you specify a constraint, like above, the dependency will be updated by using the specified constraint. If you want to get the latest version of an already present dependency you can use the special latest constraint:

**CONSOLE:**  
```python
poetry add pendulum@latest
```

You can also add git dependencies:

**CONSOLE:**  
```python
poetry add git+https://github.com/sdispater/pendulum.git
```

or use ssh instead of https:

**CONSOLE:**  
```python
poetry add git+ssh://git@github.com/sdispater/pendulum.git
```

If you need to checkout a specific branch, tag or revision, you can specify it when using **add**:

**CONSOLE:**  
```python
poetry add git+https://github.com/sdispater/pendulum.git#develop
poetry add git+https://github.com/sdispater/pendulum.git#2.0.5
```

or make them point to a local directory or file:

**CONSOLE:**  
```python
poetry add ./my-package/
poetry add ../my-package/dist/my-package-0.1.0.tar.gz
poetry add ../my-package/dist/my_package-0.1.0.whl
```

---

<div id="update"></div>

## poetry update

In order to get the latest versions of the dependencies and to update the **poetry.lock** file, you should use the **poetry update** command:

**CONSOLE:**  
```python
poetry update
```

**NOTE:**  
This will resolve all dependencies of the project and write the exact versions into **poetry.lock**.

**NOTE:**  
If you just want to update a few packages and not all, you can list them as such:

**CONSOLE:**  
```python
poetry update requests toml
```

---

<div id="poetry-show"></div>

## poetry show

To list all of the available packages, you can use the **poetry show** command:

**CONSOLE:**  
```python
poetry show
```

If you want to see the details of a certain package, you can pass the package name:

**CONSOLE:** 
```python
poetry show pendulum
```

**OUTPUT:** 
```python
name        : pendulum
version     : 1.4.2
description : Python datetimes made easy

dependencies:
 - python-dateutil >=2.6.1
 - tzlocal >=1.4
 - pytzdata >=2017.2.2
```

---

<div id="poetry-search"></div>

## poetry search

> This command searches for packages on a remote index.

**CONSOLE:**  
```python
poetry search tensorflow
```

**OUTPUT:**  
```python
tensorflow (2.9.1)
 TensorFlow is an open source machine learning framework for everyone.

tensorflow-tflex (1.13.1rc3)
 TensorFlow is an open source machine learning framework for everyone.

tensorflow-aarch64 (2.9.0)
 TensorFlow is an open source machine learning framework for everyone.

tensorflow-radam (0.15.0)
 RAdam implemented in Keras & TensorFlow

tensorflow-model (0.1.1)
 Command-line tool to inspect TensorFlow models

tensorflow-consciousness (0.1)
 Supports a variety of biological learning algorithms.

essentia-tensorflow (2.1b6.dev778)
 Library for audio and music analysis, description and synthesis, with TensorFlow support

tensorflow-plot (0.3.2)
 TensorFlow Plot

tensorflow-gan (2.1.0)
 TF-GAN: A Generative Adversarial Networks library for TensorFlow.

tensorflow-ascend (1.15.0)
 TensorFlow is an open source machine learning framework for everyone.

tensorflow-scientific (0.2.0.dev0)
 Scientific modeling in TensorFlow

tensorflow-directml (1.15.7)
 TensorFlow is an open source machine learning framework for everyone.

neuraxle-tensorflow (0.1.2)
 TensorFlow steps, savers, and utilities for Neuraxle. Neuraxle is a Machine Learning (ML) library for building neat pipelines, providing the right abstractions to both ease research, development, and deployment of your ML applications.

tensorflow-play (0.0.1)
 The lightweight engineering TensorFlow wrapper for AI engineer. Write less, Reuse more, Scale easily.

tensorflow-fedora28 (1.9.0rc0)
 TensorFlow is an open source machine learning framework for everyone.

tensorflow-datasets (4.5.2)
 tensorflow/datasets is a library of datasets ready to use with TensorFlow.

tensorflow-similarity (0.16.0)
 Metric Learning for Humans

condor-tensorflow (1.0.1)
 A tensorflow implementation of Conditionals for Ordinal Regression

tensorflow-modules (0.0.8)
 tensorflow layers, models

dask-tensorflow (0.0.2)
 Interactions between Dask and Tensorflow
```

---

**Rodrigo Leite -** *drigols*
