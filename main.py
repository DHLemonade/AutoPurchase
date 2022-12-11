import chromedriver_autoinstaller
import time
import shutil
import subprocess

from bs4 import BeautifulSoup

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from kream import driver
from kream import kreamLogin

from kreamrequests import session
from kreamrequests import headers

kreamLogin()

session.headers.update(headers)
allCookies = driver.get_cookies()

driver.quit()

for cookie in allCookies:
    cook = {cookie['name'] : cookie['value']}
    session.cookies.update(cook)

response = session.get('https://www.kream.co.kr/my/inventory')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.select_one('class.my_inventory')
print(title)
print()