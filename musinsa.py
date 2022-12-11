import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sutils import get_selenium_driver

driver = get_selenium_driver(False)

def musinsaLogin():
    print('페이지 로딩 중..')
    driver.get('https://www.musinsa.com/app/')

    id = 'ilitech0720'
    pw = 'Ldhfame0902!'

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'black-index__home')))
        elem_btn = driver.find_element(By.CLASS_NAME, 'black-index__home')
        elem_btn.click()  # 버튼 클릭

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-member__login')))
        elem_btn = driver.find_element(By.CLASS_NAME, 'header-member__login')
        elem_btn.click()  # 버튼 클릭

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'id')))
        elem_id = driver.find_element(By.NAME, 'id')
        elem_id.send_keys(id)  # id 입력

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'pw')))
        elem_pw = driver.find_element(By.NAME, 'pw')
        elem_pw.send_keys(pw)

        login_btn = driver.find_element(By.XPATH, '//button[@class="login-button__item login-button__item--black"]')
        login_btn.click()

        print('로그인 성공')
    except:  # 이미 로그인이 되어있는 경우
        pass

def musinsaChooseitem():
    while True:
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_buy')))
        buy_btn = driver.find_element(By.CLASS_NAME, 'btn_buy')

        if buy_btn.text == '품절':
            driver.refresh()
            print("품절 처리... 새로고침 진행")
            del buy_btn
            time.sleep(2)
        elif buy_btn.text == '바로구매\n(회원전용)':
            break
        elif buy_btn.text == '바로구매':
            break
        else:
            break

    select_option1 = Select(driver.find_element(By.CLASS_NAME, 'option1'))
    size_choose1 = select_option1.select_by_index(1)
    print('옵션 선택 중..')

    buy_btn = driver.find_element(By.CSS_SELECTOR, '#buy_option_area > div.box-btn-buy.wrap-btn-buy > div.btn_buy')
    buy_btn.click()

    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        if alert.text == '옵션을 선택해 주세요.':
            alert.accept()
            select_option2 = Select(driver.find_element(By.CLASS_NAME, 'option2'))
            size_choose2 = select_option2.select_by_index(1)
            buy_btn.click()
    except:
        pass

def musinsaPayment():
    print('결제 페이지 진입..')

    # 무신사 페이 선택
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[1]/div/div[1]/ul[1]/li[2]/ul/li[1]/label')))
    musinsa_pay_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[1]/div/div[1]/ul[1]/li[2]/ul/li[1]/label')
    musinsa_pay_btn.click()
    print('무신사 페이 선택..')

    # 카드 선택
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[1]/div/div[1]/div[3]/ul/li[2]/div[3]/div/div[2]/i')))
    musinsa_pay_next_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[1]/div/div[1]/div[3]/ul/li[2]/div[3]/div/div[2]/i')
    musinsa_pay_next_btn.click()
    print('카드 넘기는 중..')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[2]/a')))
    pay_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/form/div[7]/div[2]/a')
    pay_btn.click()
    print('최종 결제 진행...')

    driver.implicitly_wait(10)

    print('보안 키패드 입력..')
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame('__tosspayments_connectpay_iframe__')

    keypad_5 = driver.find_element(By.LINK_TEXT, '5')
    keypad_5.click()
    keypad_2 = driver.find_element(By.LINK_TEXT, '2')
    keypad_2.click()
    keypad_8 = driver.find_element(By.LINK_TEXT, '8')
    keypad_8.click()
    keypad_4 = driver.find_element(By.LINK_TEXT, '4')
    keypad_4.click()
    keypad_9 = driver.find_element(By.LINK_TEXT, '9')
    keypad_9.click()
    keypad_1 = driver.find_element(By.LINK_TEXT, '1')
    keypad_1.click()

    print('결제 완료')
