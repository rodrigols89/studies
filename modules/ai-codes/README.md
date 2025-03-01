> **NOTE:**  
> I have old studies on [Artificial Intelligence (Clicking here)](docs/old-studies/README.md) that you might like to see.

# Artificial Intelligence (Theory & Practice)

## Contents

 - [**Project Structure**](#project-structure)
 - [**Settings**](#settings)
 - [**References**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Project Structure ) --->

---

<div id="project-structure"></div>

## Project Structure

 - **ai-codes/**
   - Main package directory containing the source code.
    - **algorithms/**
      - Contains implementations of machine learning and deep learning algorithms.
      - **`__init__.py`**
        - Marks the directory as a Python package, enabling direct module imports.
      - **`dl.py`**
        - Implementations of deep learning algorithms.
      - **`ml.py`**
        - Functions and classes for traditional machine learning algorithms.
      - **`utils.py`**
        - Utility functions that support the algorithms.
    - **datasets/**
      - Holds scripts for loading and preprocessing datasets.
      - **`__init__.py`**
        - Marks the datasets directory as a package.
      - **`loader.py`**
        - Functions for loading and managing datasets.
   - **docs/**
     - Contains the detailed documentation of the project, such as usage guides, API references, and technical notes that help developers and users understand how the project works.
     - **`__init__.py`**
       - Marks the datasets directory as a package.
   - **examples/**
     - Holds practical examples and notebooks (e.g., Jupyter Notebooks) demonstrating how to use the algorithms and models provided by the project.
     - **`__init__.py`**
       - Marks the examples directory as a package.
   - **models/**
     - Defines models and neural network structures for training and evaluation.
     - **`__init__.py`**
       - Initializes the models module.
   - **tests/**
     - Contains automated unit and integration tests to ensure code quality and stability.
     - **`__init__.py`**
       - Marks the tests directory as a package.
   - **`__init__.py`**
     - Marks the root (top-level) directory as a Python package, enabling direct module imports.
   - **`main.py`** (Optional)
      - Serves as the entry point for running demonstrations or integrated tests of the project.
   - **`README.md`**
     - Provides an overview of the project, including basic installation instructions, usage examples, and information for contributions or contact.





















































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

> **NOTE:**  
> *Python==3.12.7* is required for TensorFlow.

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source environment/Scripts/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**UPDATE DEPENDENCIES:**
```bash
pip freeze > requirements.txt --require-virtualenv
```

**Now, Be Happy!!!** 😬










<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - **General:**
   - [Neural Networks from Scratch in Python Book](https://nnfs.io/)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
