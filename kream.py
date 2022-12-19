import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sutils import get_selenium_driver

driver = get_selenium_driver(False)

def kream_login():
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

def shoe_inventory_check():
    driver.get("https://www.kream.co.kr/inventory/28029")

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[9]/div[2]/div/button[2]')))
    choose_size = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[9]/div[2]/div/button[2]')
    choose_size.click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[4]')))
    continue_btn = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div/div[4]')
    continue_btn.click()

def cloth_inventory_check():
    driver.get("https://www.kream.co.kr/inventory/50900")

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/input')))
    choose_size = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/input')
    choose_size.send_keys("1")

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]')))
    continue_btn = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[4]')
    continue_btn.click()

    if EC.alert_is_present():
        print("불가")
    else:
        print("붸ㅔㅔ")


