from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\WebDriver\chromedriver")

driver = webdriver.Chrome(service=service)
driver.get('http://www.python.org/')
driver.save_screenshot('../images/python-page-screenshot.png')
driver.quit()
