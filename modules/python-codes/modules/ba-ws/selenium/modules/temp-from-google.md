# Getting the temperature from Google

## Contents

 - [Planning](#planning)
 - [Opening the browser and access the Google](#open)
 - [Typing search text in the browser](#typing-text)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)
 - [](#)

---

<div id="planning"></div>

## Planning

To get a temperature from Google first we need planning the steps:

 - Open the Browser;
 - Access the Google;
 - Enter the search (temperature);
 - Click to find;
 - Found the temperature;
 - Finally, save the temperature.

---

<div id="open"></div>

## Opening the browser and access the Google page

Let's start by opening the browser and access the Google page:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\WebDriver\chromedriver")

driver = webdriver.Chrome(service=service) # Select the browser (Chrome).
driver.get('https://www.google.com/') # Open the browser with Google page.

driver.quit() # Closed the browser.
```

---

<div id="typing-text"></div>

## Typing search text in the browser

> Now, let's typing search text in the browser.

**NOTE:**  
But, before typing search text in the browser first we need to know what element will receive that text.

To know what element represents the search field first, let's inspect it:

![img](images/inspect-01.png)  

Click in top left arrow to find elements passing the mouse:

![img](images/inspect-02.gif)  

Ok, see that this element has many attributes:

```html
<input
    class="gLFyf gsfi"
    jsaction="paste:puy29d;"
    maxlength="2048"
    name="q"
    type="text"
    aria-autocomplete="both"
    aria-haspopup="false"
    autocapitalize="off"
    autocomplete="off"
    autocorrect="off"
    autofocus=""
    role="combobox"
    spellcheck="false"
    title="Search"
    value=""
    aria-label="Search"
    data-ved="0ahUKEwjXiuDqhfb5AhUhFbkGHbzeAk0Q39UDCAQ">
```

> **NOTE:**  
> Now, let's use **name="q"** attribute to find this element with Selenium and pass text search for him.

To Apply this we use:

 - **find_element()** method from webdriver:
   - To find element in the page.
 - **By class**:
   - To find a specific element with "x" attribute (NAME) and "y" value ("q").
 - **send_keys()** method to send text to the specific element.

```python
//

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

//

# Find element with attribute NAME="q" and pass "temperature now" for him.
elem = driver.find_element(By.NAME, "q").send_keys("temperature now")

//
```

Ok, now we need do our script (program) press enter in the browser. Let's inspect button element to find a specific attribute to works with:

![img](images/inspect-03.gif)  

```html
<input
    class="gNO89b"
    value="Google Search"
    aria-label="Google Search"
    name="btnK"
    role="button"
    tabindex="0"
    type="submit"
    data-ved="0ahUKEwji5YrXkvb5AhUtK7kGHWKEBiYQ4dUDCA0">
```

> **NOTE:**  
> Let's use **name="btnK"** attribute to find this element with Selenium and work with.

```python
# Find element with attribute NAME="btnK" and use the click() method him.
driver.find_element(By.NAME, "btnK").click()
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
[Aprenda Automação WEB em 10 minutos! (Selenium com Python)](https://www.youtube.com/watch?v=myQIZElpXTU)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
