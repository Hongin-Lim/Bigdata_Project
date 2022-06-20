import urllib.request
import xmltodict
from datetime import date, timedelta
import json
from json import dumps
from kafka import KafkaProducer
import schedule
import time



def price_api():
    # p_ymd
    today = date.today()
    today = str(today).split('-')
    today = ''.join(today)
    print(today)

    # p_jymd
    yesterday = date.today() - timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    yesterday = str(yesterday).split('-')
    yesterday = ''.join(yesterday)
    print(yesterday)


    # p_jjymd
    lastyear = date.today() - timedelta(366)
    lastyear = lastyear.strftime('%Y-%m-%d')
    lastyear = str(lastyear).split('-')
    lastyear = ''.join(lastyear)
    print(lastyear)

    # 딕셔너리 날짜 변수 ( 오늘 )
    today2 = date.today()
    today2 = str(today2)
    print(today2)

    # 딕셔너리 날짜 변수 ( 어제 )
    yesterday2 = date.today() - timedelta(1)
    yesterday2 = str(yesterday2)
    print(yesterday2)

    # 딕셔너리 날짜 변수 ( 작년 어제 )
    lastyear2 = date.today() - timedelta(366)
    lastyear2 = str(lastyear2)
    print(lastyear2)

    # 전체 페이지 리스트 출력
    json_f = open("./price.json", 'w', encoding="UTF-8")
    URL = 'http://www.garak.co.kr/publicdata/dataOpen.do?id=3179&passwd=gmlgml3502!!&dataid=data4&pagesize=1&pageidx=1&portal.templet=false&p_ymd='+today+'&p_jymd='+yesterday+'&d_cd=2&p_jjymd='+lastyear+'&p_pos_gubun=1&pum_nm='
    json_page = urllib.request.urlopen(URL)
    json_data = json_page.read().decode("UTF-8")
    dic = xmltodict.parse(json_data)
    list_count = dic.get('lists').get('list_total_count')
    list_count = int(list_count)
    # print(list_count)


    # json 파일로 만들기
    for i in range(1,list_count+1):
        URL = 'http://www.garak.co.kr/publicdata/dataOpen.do?id=3179&passwd=gmlgml3502!!&dataid=data4&pagesize=1&pageidx='+str(i)+'&portal.templet=false&p_ymd='+today+'&p_jymd='+yesterday+'&d_cd=2&p_jjymd='+lastyear+'&p_pos_gubun=1&pum_nm='
        json_page = urllib.request.urlopen(URL)
        # print(json_page)
        json_data = json_page.read().decode("UTF-8")
        # print(json_data)
        dic = xmltodict.parse(json_data)
        alist = dic.get('lists').get('list')
        data = alist
        data["today"] = today2
        data["yesterday"] = yesterday2
        data["lastyear"] = lastyear2
        # print(data)
        json_f.write(json.dumps(data, ensure_ascii=False) + "\n")

    json_f.close()

    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['172.30.1.222:31256'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    start = time.time()

    with open("./price.json", 'r', encoding='utf-8') as f:
        for i in f:
            data = i
            producer.send('test_price', value=json.loads(data))
            producer.flush()

# schedule.every(10).seconds.do(price_api) # 3초마다 job 실행

# # 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
schedule.every().day.at("11:00").do(price_api)
# schedule.every().day.at("10:30:42").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
