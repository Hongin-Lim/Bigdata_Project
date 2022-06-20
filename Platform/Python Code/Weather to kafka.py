```import json
import requests
from datetime import date, timedelta
from kafka import KafkaProducer
from json import dumps
import time
import schedule


def weather_api():
    # 날짜변수
    today = date.today()
    yesterday = date.today() - timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    yesterday = str(yesterday).split('-')
    yesterday = ''.join(yesterday)
    print(yesterday)

    # api 데이터 불러오기
    url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'

    params = {'serviceKey': 'BdvqtMGP6rQV3O0RUGZeT98nIq+hTusTrxlgAe0vBdxUxasmhGOFPqTPYoCKb5pxrY3h0hyWqqMGHzlEoLTqdQ==',
              'pageNo': '1',
              'numOfRows': '999',
              'dataType': 'JSON',
              'dataCd': 'ASOS',
              'dateCd': 'HR',
              'startDt': yesterday,
              'startHh': '00',
              'endDt': yesterday,
              'endHh': '23',
              'stnIds': '108'
              }

    # api 데이터 전처리
    response = requests.get(url, params=params)
    res = json.loads(response.content)
    data = res.get('response').get('body').get('items').get('item')

    # json 파일 만들기
    json_f = open("./weather.json", 'w', encoding="UTF-8")

    for i in data:
        data = i
        tm = data.get('tm')
        tm1 = tm.split(' ')[0]
        tm2 = tm.split(' ')[1]
        tm = tm1 + "T" + tm2 + ":00Z"
        data['tm'] = tm
        # print(data)

        json_f.write(json.dumps(data, ensure_ascii=False) + "\n")

    json_f.close()


    # 카프카로 보내는 코드
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['172.30.1.222:31256'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    start = time.time()

    with open("./weather.json", 'r', encoding='utf-8') as f:
        for i in f:
            data = i
            producer.send('final_weather', value=json.loads(data))
            producer.flush()



# schedule.every(10).seconds.do(weather_api) # 3초마다 job 실행

# # 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
schedule.every().day.at("09:00").do(weather_api)
# schedule.every().day.at("10:30:42").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)```
