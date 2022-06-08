![header](https://capsule-render.vercel.app/api?type=soft&color=auto&height=300&section=header&text=Hello%20VeryMarket!&fontColor=f7f5f5&fontSize=50)

# 읽어주세요!

▶ Data PipeLine 전체 흐름도

![image](https://user-images.githubusercontent.com/97893538/172515060-2a27c33b-c3fa-4612-aa6f-7828448db96d.png)

- dd
- 소비자의 로그 데이터 분석(초록색 화살표)
- 판매자가 OPEN API 데이터를 볼 수 있게 시각화(노란색 화살표)

---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

▶ Data PipeLine - OPEN API 데이터 흐름도

![image](https://user-images.githubusercontent.com/97893538/172515131-29dfcf88-301f-45bc-9513-25111233d2b9.png)

- OPEN API 데이터 -> Kafka -> Logstash -> ElasticSearch -> Kibana -> Django2(BigVeryMarket)

---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

▶ Data PipeLine - Log 데이터 흐름도

![image](https://user-images.githubusercontent.com/97893538/172515188-46240698-a0e4-441a-8051-674e07057a8d.png)

- 소비자의 Log 데이터(Django1, VeryMarket) -> Kafka -> Spark

---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

▶ CI /CD 흐름도

![image](https://user-images.githubusercontent.com/97893538/172520682-74059816-e844-4023-ad86-a262588d3814.png)

- 개발자(dev)가 어쩌구 저쩌구..

---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

![footer](https://capsule-render.vercel.app/api?type=soft&color=auto&height=300&section=footer&text=See%20you%20again%20VeryMarket!&fontColor=f7f5f5&fontSize=50)
