import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import shutil
import subprocess
import os


def get_selenium_driver(headless=True):
    chromedriver_autoinstaller.install()  # chromedriver 자동 다운로드
    #os.system("taskkill /IM chrome.exe /F")  # 열려 있는 chrome.exe 모두 종료

    chrome_options = webdriver.ChromeOptions()

    if headless:
        chrome_options.add_argument('headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('lang=en')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("disable-agpu")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    """
    try:
        shutil.rmtree(r"c:\chrometemp")  # 쿠키 / 캐쉬파일 삭제
    except FileNotFoundError:
        pass

    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    if headless:
        option.add_argument('--headless')

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.implicitly_wait(10)
    """
    driver.maximize_window()

    return driver
