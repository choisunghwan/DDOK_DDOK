

# :droplet: 똑똑 (한 프로그램) 똑똑 (들여보내주세요) :droplet: 💻🥇
<!-- <img src="https://capsule-render.vercel.app/api?type=soft&color=33b9cc&height=300&section=header&text=DDOK DDOK&fontSize=90&animation=twinkling&fontAlign=48&desc=DCU Capstone Design Project.&descAlignY=65&descAlign=65" /> -->

![header](https://capsule-render.vercel.app/api?type=wave&color=B3ECFF&height=300&section=header&text=온라인부정행위방지%20시스템&fontSize=70)

- Team name: DDOK DDOK (똑똑)
- Project execution period : 2021. 08. 31 ~ 2022. 06
- APP ICON: ![image](https://user-images.githubusercontent.com/33335762/205942440-66c88136-e74e-4ce5-9ee7-a301ef06bd8e.png)



<p align= 'center'>
<a href="https://github.com/choisunghwan/ddokddok/labels/Idea">
    <img src="https://img.shields.io/badge/IDEA ISSUE-%23F7DF1E?&logoColor=black&style=for-the-badge&&logoColor=white"/>
  </a>
</p>

## 핵심

- 온라인 시험 부정행위 감지 프로그램
- 코로나19로 인하여 비대면 교육 형식이 보편화됨에 따라 온라인 학습 및 시험 형태가 교육기관에서 일반화되고 있다. 이러한 급격한 변화로 교육의 공정성 문제와 온라인 시험의 부정행위 문제가 대두되고 있다. 시험 응시자의 다양한 환경을 고려하여 정확하게 부정행위자를 판별하는 방법이 중요해지고 있다. 이를 위해 본 연구에서는 온라인 시험환경에서의 응시자의 행동 데이터와 영상데이터 분석을 진행하여 부정행위자를 감별하는 연구를 진행하였다. 분석 결과 긍정적인 반응을 얻었으며 앞으로 활용 가능성이 기대된다.

## 구현및 구현 환경
![image](https://user-images.githubusercontent.com/33335762/205472246-1abe58c4-0990-4693-a622-940675825984.png)

## 계획

- 부정행위 감지된 부분 사진 캡처
- 시험 종료시 부정행위 감지 로그 출력
- 특정 키 입력시 로그 기록
- 얼굴인식으로 대리시험 방지
- 특정 프로그램 차단
![image](https://user-images.githubusercontent.com/33335762/205472358-2341f37f-2233-46f4-8aba-f7d6cf071f20.png)


## 개발동기
![image](https://user-images.githubusercontent.com/33335762/205472187-aba1e5e2-a222-413d-b990-81a41f3acc54.png)

## 설계
![image](https://user-images.githubusercontent.com/33335762/205472212-aae6f2b1-d895-45d6-b490-f7cd85cd8db9.png)
![image](https://user-images.githubusercontent.com/33335762/205472230-2df607e8-54b9-4ce3-bf45-5733d3cbea2c.png)



## 핵심 기능
1. 얼굴 인식 방식

온라인 시험 전 응시자의 얼굴을 HOP 알고리즘을 통해 얼굴을 인식하며, 기존에 촬영하여 저장해둔 응시자의 얼굴과 일치하면, 시험 방에 접속할 수 있게 된다.
시험 응시 중에도 얼굴이 일치하지 않다고 판단 시, 로그에 기록이 남도록 한다.

2. 특수키 인식 방식

온라인 시험 도중 부정행위를 하는 응시자의 키보드 패턴을 파악하여 시험을 치르는 도중에 사용되어 지지 않는 입력 값들을 특수 키 입력으로 확인하고 부정행위를 잡아 낼 수 있다. Keyboard 모듈을 사용하여 응시자가 시험 도중 부정행위 오해의 소지를 발생시킬 수 있는 입력 값들을 감지할 수 있다. 시험 도중 응시자가 특수 키를 인풋하게 되면 본 프로그램의 로그에 기록이 남게 되며, 입력 값이 들어온 즉시 감독관이 파악할 수 있게 알람이 간다. 특정한 키의 입력을 탐지함으로써 응시자의 부정행위를 막아 낼 수 있다는 장점이 있다. 

3. 차단프로그램 관리

시험 감독관이 시험 방 생성과정에서 시험 중에 차단시킬 응용프로그램을 선택할 수 있다. (*차단프로그램: 크롬, 마이크로소프트 엣지, 사파리, 카카오톡, 메모장, 계산기) 프로세스 킬 명령어를 통하여 시험 도중 차단 프로그램 실행 시 강제종료 시킴으로써 해당 프로그램을 이용한 부정행위를 사전에 막을 수 있다.

## 수행과정
![image](https://user-images.githubusercontent.com/33335762/205472483-331ffa56-70bb-4ff8-8117-0716ce21e352.png)


## 시연영상 
https://drive.google.com/file/d/1ujD_6FtqBTP8ZRkiDpEBZTOg2Lcli9_j/view

https://user-images.githubusercontent.com/33335762/205472540-d9707a1e-f844-48bf-942a-e31c227d170b.mp4

## 논문
![image](https://user-images.githubusercontent.com/33335762/205943032-a1450861-6413-4cd2-a0e4-2353abe17eb6.png)
 
- http://kips.or.kr/bbs/confn/article/2484
