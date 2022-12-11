import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sutils import get_selenium_driver

driver = get_selenium_driver(False)

def kreamLogin():
    print('크림 로그인 페이지 로딩 중..')
    driver.get('https://www.kream.co.kr/login')

    id = 'ilitech0720@naver.com'
    pw = 'Ldhfame0902!'

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')))
        elem_id = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')
        elem_id.send_keys(id)  # id 입력

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')))
        elem_pw = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')
        elem_pw.send_keys(pw)

        login_btn = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[3]/a')
        login_btn.click()

        print('로그인 성공')
    except:  # 이미 로그인이 되어있는 경우
        pass