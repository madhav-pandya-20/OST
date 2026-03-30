from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

time.sleep(2)

driver.maximize_window()

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("open source software")

search_button = driver.find_element(By.ID, "search-icon-legacy")
search_button.click()

time.sleep(5)

driver.quit()