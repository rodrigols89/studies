from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() # Select the browser driver (Chrome).
driver.get('https://www.google.com/') # Open the browser with Google page.

# Maximize the window.
driver.maximize_window()

# Find element with attribute NAME="q" and pass "temperature now" for him.
driver.find_element(By.NAME, "q").send_keys("temperature now")

#driver.implicitly_wait(10)

# Find element with attribute NAME="btnK" and use the click() method him.
#button_element = driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

driver.quit() # Closed the browser.
