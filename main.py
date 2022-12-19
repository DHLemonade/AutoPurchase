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

from kream import kream_login, shoe_inventory_check, cloth_inventory_check
from kreamrequests import kream_request_login, session

if __name__ == "__main__":
    kream_login()
    cloth_inventory_check()

    time.sleep(10)
