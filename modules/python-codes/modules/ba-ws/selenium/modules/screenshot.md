# Screenshot

## Contents

 - [Taking a screenshot of the current window](#take-ss)

---

<div id="take-ss"></div>

## Taking a screenshot of the current window

To take a screenshot of the current window is very easy using the **save_screenshot()** method provided by the webdriver:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\WebDriver\chromedriver")

driver = webdriver.Chrome(service=service)
driver.get('http://www.python.org/')
driver.save_screenshot('../images/python-page-screenshot.png')
driver.quit()
```

**Saved screenshot:**  
![img](images/python-page-screenshot.png)  

---

**REFERENCES:**  
[8. Appendix: Frequently Asked Questions](https://selenium-python.readthedocs.io/faq.html)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
