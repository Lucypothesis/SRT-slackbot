from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 로그인 페이지 => 로그인
browser = webdriver.Chrome()
url = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
browser.get(url)
browser.find_element(By.ID, 'srchDvCd3').click()
browser.find_element(By.ID, 'srchDvNm03').click()
browser.find_element(By.ID, 'srchDvNm03').send_keys('01051233632')
browser.find_element(By.ID, 'hmpgPwdCphd03').click()
browser.find_element(By.ID, 'hmpgPwdCphd03').send_keys('!eonsign27srt')
browser.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[4]/div/div[2]/input').click()


# 예약 페이지 => 출발과 도착 도시 선택 => 조회 버튼 클릭
reserve_url = 'https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
browser.get(reserve_url)
# 도착역 입력
browser.find_element(By.ID, 'dptRsStnCdNm').clear()
browser.find_element(By.ID, 'dptRsStnCdNm').send_keys('오송')
browser.find_element(By.ID, 'arvRsStnCdNm').clear()
browser.find_element(By.ID, 'arvRsStnCdNm').send_keys('수서')
# 출발일 선택
browser.find_element(By.XPATH, '//*[@id="dptDt"]/option[6]').click()
# 출발 시간 선택
browser.find_element(By.XPATH, '//*[@id="dptTm"]/option[11]').click()
# 기차표 조회
browser.find_element(By.XPATH, '//*[@id="search_top_tag"]/input').click()

import subprocess

def run_slackbot():
    command = ["python", "slackbot.py"]
    subprocess.run(command)

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="result-form"]/fieldset/div[6]/table/tbody/tr[2]/td[7]/a')))
is_soldout = element.text

for i in range(1,51):
    print(f'{i}번째 시도 중입니다.')
    if is_soldout == '매진':
        browser.refresh()
        time.sleep(1)
    else:
        element.click()
        print('예매성공!')
        run_slackbot()
        break