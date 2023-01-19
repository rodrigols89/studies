from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\WebDriver\chromedriver")

driver = webdriver.Chrome(service=service) # Select the browser (Chrome).
driver.get('https://www.google.com/') # Open the browser with Google page.

# Maximize the window.
driver.maximize_window()

# Find element with attribute NAME="q" and pass "temperature now" for him.
driver.find_element(By.NAME, "q").send_keys("temperature now")

# Find element by XPATH attribute and use the click() method him.
driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"
).click()

# Find element by ID and return the result as a text.
temperature = driver.find_element(By.ID, "wob_tm").text

driver.quit() # Closed the browser.

# Print the result.
print("\nDaily Temperature:", temperature)
