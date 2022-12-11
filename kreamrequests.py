import time
import requests

session = requests.session()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

cookie = {'name'}

data = {
    "email": "ilitech0720@naver.com",
    "password": "Ldhfame0902!"
}

def kreamRequestsLogin():

    url = "https://www.kream.co.kr/api/auth/login?request_key=bf3c5411-e906-4485-ba24-2c87b7ee4cb3"


    response = session.post(url, data=data, headers=headers)
    response.raise_for_status()

    print(response.raise_for_status())


