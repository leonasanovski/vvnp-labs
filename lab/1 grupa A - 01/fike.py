from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
driver.get('https://finance.yahoo.com/crypto')
crypto_names = driver.find_elements(By.CSS_SELECTOR,"tr .yf-paf8n5 td:nth-of-type(1) span")
print()
for name in crypto_names:
    print(name.text)
driver.quit()

print()