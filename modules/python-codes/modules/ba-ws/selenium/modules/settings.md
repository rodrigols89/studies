# Settings

## Contents

 - [Installing Selenium](#install)
 - [Drivers](#drivers)
 - [Using Drivers for Windows](#drivers-for-windows)

---

<div id="install"></div>

## Installing Selenium

To install Selenium library is very easy:

```
pip install selenium
```

---

<div id="drivers"></div>

## Drivers

> Selenium requires a driver to interface with the chosen browser.

For example, **Firefox** requires [geckodriver](https://github.com/mozilla/geckodriver/releases), which needs to be installed.

Supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow:

| Driver       | Link                                                                  |
|--------------|-----------------------------------------------------------------------|
| **Chrome:**  | https://sites.google.com/chromium.org/driver/                         |
| **Edge:**    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| **Firefox:** | https://github.com/mozilla/geckodriver/releases                       |
| **Safari:**  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |

**NOTE:**  
Make sure it’s in your **PATH**, e. g., place it in *(for example, <u>chromedriver binary</u>)* **/usr/bin** or **/usr/local/bin**.

For more information about driver installation, please refer the [official documentation (Install browser drivers)](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).

---

<div id="drivers-for-windows"></div>

## Using Drivers for Windows

> To use a specific driver for Windows you need specific the ***.exe PATH***.

For example:

 1. Download a specific driver;
 2. Create a folder *C:\WebDriver*;
 3. Put you **.exe** (for example, chromedriver.exe) in *C:\WebDriver*;

Ok, now you have an ***.exe*** to set in your code.

**Deprecated approach:**
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\WebDriver\chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

**Service approach:**
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\WebDriver\chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

---

**REFERENCES:**  
[1. Installation](https://selenium-python.readthedocs.io/installation.html)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
