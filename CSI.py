import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import OrderedDict
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os, os.path
import time
import pandas as pd
import re
import openpyxl
from openpyxl import workbook
import getpass
import traceback
from webdriver_manager.chrome import ChromeDriverManager


username = getpass.getuser()

# For webdriver
profile_name = 'WWCRAutomation'
profile_path = rf'{os.path.expanduser("~")}\Chrome Profiles\{profile_name}'
driver_path = rf'{os.path.expanduser("~")}\Chrome Profiles\chromedriver.exe'

try:
    # First, let's get the chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'user-data-dir={profile_path}')
    chrome_options.add_argument(f'--profile-directory={profile_name}')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("https://csi.amazon.com/view?view=blame_o&item_id=B00IF7RAP8&marketplace_id=3&customer_id=&merchant_id=&sku=&fn_sku=&gcid=&fulfillment_channel_code=&listing_type=purchasable&submission_id=&order_id=&external_id=&search_string=bullet_point&realm=USAmazon&stage=prod&domain_id=&keyword=&submit=Show")
    time.sleep(10)
except:
    print(traceback.format_exc())

time.sleep(5)

value_box = driver.find_element(By.XPATH, """/html/body/table/tbody/tr[1]/td[4]/div""").get_attribute("innerHTML")
print(value_box)
time.sleep(2)
