import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.find_element(By.XPATH,'//*[@id = "twotabsearchtextbox"]').send_keys("iphone 16")
driver.find_element(By.XPATH,'//*[@id = "nav-search-submit-button"]').click()
driver.find_element(By.XPATH,'//*[@id = "a-autoid-1-announce"]').click()
time.sleep(10)

