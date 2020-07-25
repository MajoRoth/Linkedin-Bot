import os
from selenium import webdriver



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver')


driver = webdriver.Chrome(DRIVER_PATH)

driver.get("https://www.linkedin.com/feed/")
