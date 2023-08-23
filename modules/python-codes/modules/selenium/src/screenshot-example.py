from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import keyboard

service = Service()

print("Press 'Insert' to start the script...")
keyboard.wait("insert")

driver = webdriver.Chrome(service=service)
driver.get("http://www.python.org/")
driver.save_screenshot("../images/python-page-screenshot.png")
driver.quit()
