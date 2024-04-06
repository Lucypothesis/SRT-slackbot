import requests
import json
from datetime import date

# 메시지를 보내는 부분. 함수 안 argument 순서 :
# token : Slack Bot의 토큰
# channel : 메시지를 보낼 채널 #stock_notice
# text : Slack Bot 이 보낼 텍스트 메시지. 마크다운 형식이 지원된다.
# attachments : 첨부파일. 텍스트 이외에 이미지등을 첨부할 수 있다.

def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text ,"attachments": attachments})

Token = 'xoxb-6916490630515-6934042010977-mJ8t8faSQtnAJD2FFfNlFcjH' # 자신의 Token 입력
today = date.today().strftime("%Y-%m-%d %a")
str2 = 'SRT 예매가 가능해요'
# attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력
attach_dict = {
    'color' : '#6c1e96',
    'author_name' : str(today),
    'title' : '예매 바로가기(srail.kr)',
    'title_link' : 'https://etk.srail.kr/hpg/hra/02/selectReservationList.do?pageId=TK0102010000',
    # 'text' : 예매가 가능해요,
    #'image_url' : 'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png?sidcode=1632301488333'
}

attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
notice_message(Token, "srt", str2, attach_list)