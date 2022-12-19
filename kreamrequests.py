import time
import requests

from kream import kream_login
from kream import driver

session = requests.session()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

cookie = {'name'}

data = {
    "email": "ilitech0720@naver.com",
    "password": "Ldhfame0902!"
}

def kream_request_login():

    #셀레니움으로 로그인 이후 쿠키를 얻어 request로 데이터 추출

    kream_login()

    session.headers.update(headers)
    allCookies = driver.get_cookies()

    driver.quit()

    for cookie in allCookies:
        cook = {cookie['name']: cookie['value']}
        session.cookies.update(cook)

    # response = session.get('https://www.kream.co.kr/my/inventory')
    # soup = BeautifulSoup(response.text, 'html.parser')
    # title = soup.select_one('class.my_inventory')
