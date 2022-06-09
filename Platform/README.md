![header](https://capsule-render.vercel.app/api?type=soft&color=auto&height=300&section=header&text=Hello%20VeryMarket!&fontColor=f7f5f5&fontSize=50)

# 읽어주세요!

▶ Data PipeLine 전체 흐름도

![image](https://user-images.githubusercontent.com/97893538/172749345-7a7858ad-c3f9-459e-9f12-24eff6db299b.png)

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

![image](https://user-images.githubusercontent.com/97893538/172749388-fc7f25b6-9634-4d0b-8bfe-e7dd9dfceef9.png)

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

![image](https://user-images.githubusercontent.com/97893538/172749421-fd9cee3b-1dc3-49be-9dbd-1a4c789da0c9.png)

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

![image](https://user-images.githubusercontent.com/97893538/172749463-1855be13-d3a2-421b-b03b-23fd201b9468.png)

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
