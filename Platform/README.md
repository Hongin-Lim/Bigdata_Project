![rect](https://capsule-render.vercel.app/api?type=rect&color=gradient&text=Hello%20VeryMarket!&fontAlign=30&fontSize=30&descAlign=60&descAlignY=50)

# 읽어주세요!

![slice](https://capsule-render.vercel.app/api?type=slice&color=auto&height=200&text=CI/CD&fontAlign=70&rotate=13&fontAlignY=25&descAlign=70.&descAlignY=44)

![image](https://user-images.githubusercontent.com/97893538/172767725-3a4ef603-7782-4b88-abdd-276d927c81e9.png)

- Jenkins : 대표적인 CI /CD 도구
    - Jenkins와 GitHub를 연동하여 CI / CD 구현


- GitHub Push
    - 개발자가 소스를 추가 / 수정, GitHub에 Push

<br/>

- Webhook
    - GitHub에서 Webhook을 설정하면 변경사항이 발생할 때 Jenkins가 이를 포착

<br/>

- DockerHub Push
    - Jenkins가 변경된 GitHub 소스를 기반으로 Dockerfile을 사용하여 Docker Image를 생성
    - 변경된 Docker Image를 DockerHub에 Push

<br/>

- Deploy
    - DockerHub에 Push된 Docker Image를 기반으로 Pod를 생성(기존에 있던 파드는 삭제)

<br/>

---

![slice](https://capsule-render.vercel.app/api?type=slice&color=auto&height=200&text=Data%20PipeLine&fontAlign=70&rotate=13&fontAlignY=22&desc=ALL&descAlign=70.&descAlignY=44)

![image](https://user-images.githubusercontent.com/97893538/172749345-7a7858ad-c3f9-459e-9f12-24eff6db299b.png)

- Kubernetes 환경

<br/>

- 소비자의 로그 데이터(결제 정보) 분석하여 인기상품 TOP 10 출력 -> 초록색 화살표

<br/>

- 판매자가 OPEN API 데이터(기상, 과일 가격)를 볼 수 있게 시각화 -> 노란색 화살표

<br/>

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

![slice](https://capsule-render.vercel.app/api?type=slice&color=auto&height=200&text=Data%20PipeLine&fontAlign=70&rotate=13&fontAlignY=22&desc=OPEN%20API&descAlign=70.&descAlignY=44)

![image](https://user-images.githubusercontent.com/97893538/172749388-fc7f25b6-9634-4d0b-8bfe-e7dd9dfceef9.png)

- OPEN API 데이터 -> Kafka -> Logstash -> ElasticSearch -> Kibana -> Django2(BigVeryMarket)

<br/>

- OPEN API 데이터 : 공공데이터포털에서 가져온 기상 정보, 과일 가격 정보
    - 매일 오전 11시에 업데이트 되는 데이터

<br/>

- Kafka : 실시간 기록 스트림 게시, 구독, 저장, 처리하는 분산 데이터 스트리밍 플랫폼
    - 기상 / 가격 정보를 서로 다른 Topic에 수집, ELK로 보내기

<br/>

- Logstash : 데이터 수집
    - 원하는 Topic을 요청, Filter로 전처리

<br/>

- ElasticSearch : 데이터 저장
    - Index 생성, 숫자와 날짜 등을 Mapping

<br/>

- Kibana : 데이터 시각화
    - ElasticSearch에 저장된 데이터를 시각화

<br/>

- Django2(BigVeryMarket) : 웹서버
    - Kibana로 시각화한 데이터를 BigVeryMarket에 게시

<br/>

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

![slice](https://capsule-render.vercel.app/api?type=slice&color=auto&height=200&text=Data%20PipeLine&fontAlign=70&rotate=13&fontAlignY=22&desc=Log%20data&descAlign=70.&descAlignY=44)

![image](https://user-images.githubusercontent.com/97893538/172749421-fd9cee3b-1dc3-49be-9dbd-1a4c789da0c9.png)

- 소비자의 Log 데이터(Django1, VeryMarket) -> Kafka -> Spark

<br/>

- Django1(VeryMarket) : 웹서버
    - VeryMarket 소비자들의 Log 데이터(결제 정보)를 저장

<br/>

- Kafka : 실시간 기록 스트림 게시, 구독, 저장, 처리하는 분산 데이터 스트리밍 플랫폼
    - 결제 정보가 쌓일 때 마다 실시간으로 Topic에 저장

<br/>

- Spark : 대용량 데이터를 여러 대의 서버에 분산 처리하는 프레임 워크
    - Topic에서 불러온 데이터를 배치 처리 코드로 분석

<br/>

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

![rect](https://capsule-render.vercel.app/api?type=rect&color=gradient&text=See%20you%20again%20VeryMarket!&fontAlign=30&fontSize=30&descAlign=60&descAlignY=50)
