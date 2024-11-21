from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import OrderedDict
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import openpyxl
from openpyxl import workbook

driver = webdriver.Chrome(executable_path=r"C:\Users\Public\AppData\chromedriver.exe")
site =r'https://tt.amazon.com/540960835'
driver.get(site)
driver.maximize_window()

try:
    driver.find_element(By.ID, "action_bar").click()
    resolu = driver.find_element(By.ID, "resolution").text
except NoSuchElementException:
    pass
else:
    pass
resolution = resolu.strip()
ex_resol = resolution.lower()
