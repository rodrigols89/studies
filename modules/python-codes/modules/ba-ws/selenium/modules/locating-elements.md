# Locating Elements

## Contents

 - [Introduction](#intro)
 - [Locating by Id](#by-id)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)

---

<div id="intro"></div>

## Introduction

There are various strategies to locate elements in a page. You can use the most appropriate one for your case. Selenium provides the following method to locate elements in a page:

 - **find_element**
 - **find_elements:**
   - To find multiple elements (these methods will return a list):

Example usage:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

The attributes available for the By class are used to locate elements on a page. These are the attributes available for By class:

```python
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

The **‘By’ class** is used to specify which attribute is used to locate elements on a page. These are the various ways the attributes are used to locate elements on a page:

```python
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```

**NOTE:**  
If you want to locate several elements with the same attribute replace **find_element** with **find_elements**.

---

<div id="by-id"></div>

## Locating by Id

> Use this when you know the id attribute of an element.

 - With this strategy, the first element with a matching id attribute will be returned.
 - If no element has a matching id attribute, a **NoSuchElementException** will be *raised*.

For instance, consider this page source:

[by-id.html](src/by-id.html)
```html
<html>
    <body>
        <form id="loginForm">
            <input name="username" type="text" />
            <input name="password" type="password" />
            <input name="continue" type="submit" value="Login" />
        </form>
    </body>
</html>
```

The form element can be located like this:

```python

```






```python

```

















































---

<div id=""></div>

## x

x


```python

```



---

**REFERENCES:**  
[4. Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
