# 프로젝트 제안서

**Text summarizer**

_Prepared by: [Group Name]_

1. 202332012 양권우
2. [Name and Student ID]

## Table of Contents

- [프로젝트 제안서](#프로젝트-제안서)
  - [Table of Contents](#table-of-contents)
  - [1. 요약](#1-요약)
  - [2. 배경](#2-배경)
  - [3. 목표](#3-목표)
  - [4. 범위](#4-범위)
  - [5. 소프트웨어 프로세스 모델](#5-소프트웨어-프로세스-모델)
  - [6. 예산](#6-예산)
  - [7. 시스템 구조](#7-시스템-구조)
  - [8. 위험요소](#8-위험요소)
  - [9. 자원](#9-자원)
  - [10. 기술 사양](#10-기술-사양)
  - [11. 타임라인 및 결과물](#11-타임라인-및-결과물)
  - [12. 결론](#12-결론)


## 1. 요약

- Summarize the project's primary goals, intended outcomes, and problem it aims to solve. Keep it concise, ideally under 200 words.
-  NLP관련 문제중 인공지능의 코드를 알고자 제일먼저 텍스트를 요약하는 알고리즘을 쓰려했음 

## 2. 배경
- 2023년 1월쯤부터 초경량비행장치중에서 멀티콥터 종목의 자격증을 따기위해서, 그리고 멀티콥터에 대한 지식을 습득하기위해 전문교육기관으로가서 비행시간 24시간 이상을 채우던 중이였음.  그러던중 2022년에 만들어진 chatGPT에 대한 정보를 듣고 인공지능에 대해서 조사해본 결과
  ChatGPT가 LLM에 근거하여 만들어졌고 그 LLM이 NLP라는 자연어처리를 위한 목적을 위한 데이터베이스라는걸 알게됨.  향후 수십년뒤 NLP가 영향을 미칠수 있는 다양한 변수중 드론과 관련된 가능성을 고민하던 결과,  NLP를 통해 드론의 이동 및 수행명령을 내릴수 있다는 사실을 알게됨.
하지만 본인에게는 아직 드론까지 코딩할수 있는 능력이 있지는 않으므로 적절한 타협선을 보아 문장요약부터 차근차근 실행해보도록하게됨

## 3. 목표

- Detail your project’s SMART objectives.
- Describe how the software will meet these objectives and solve the outlined problem.
- 구체적 -  어떤 텍스트가 주어졌을시 코드가 그것을 어떻게 추론하는지 봄.
- 측정가능 - 텍스트를 번역할시 어떤 오류가 벌어지는지 체크하고, 알고리즘에 어떤 해결이 필요할지 알아냄
- 행동중심 - 주변에서 응용할수 있는 코드들을 참고함.  
- 현실적 - 파이썬문법까지는 가능함. 그러나 복잡한 데이터베이스 구현에는 어려움이 있으므로, 최소한 텍스트 데이터를 해석하는 함수까지는 적을수 있도록함.
- 제한적인 - 기말까지 7주 정도 시간이 남아있음. 그시간안에 기말고사 과목들에 대한 준비가 이루어지기때문에 기말 준비시간 1주를 빼면 6주가 남음.   따라서 11월 28일까지 초기버전 완성해야함.
  
## 4. 범위

- Define the scope of the project, outlining its features and functionalities.
- Mention any limitations or constraints such as resources, time, or technologies.
- 간단한 텍스트 요약 알고리즘이기에 시간은 적게걸릴것으로 예상된다. 
- 
## 5. 소프트웨어 프로세스 모델

- State the chosen software process model (e.g., Agile, Waterfall, Scrum).
- Justify your model choice and illustrate its application to your project.
- Detail the activities and roles in each phase, possibly via a Gantt chart.
- Discuss testing methodologies, quality assurance, and project management strategies.
- 제안서의 경우 그때그때 수정이 들어가는 agile이지만, 실제 작업시 프로그램을 만들어보고 실패하게될시 피드백 과정을 거쳐서 프로그램을 좀더 보강하고자 나선형 모델을 택함.
## 6. 예산

- Provide a financial plan covering hardware, software, labor, and other costs.
- Include a contingency plan for unexpected expenses.
-  학교서버를 빌려 프로그램을 제작하고자함.  

## 7. 시스템 구조

- Detail the system architecture, mentioning tools, technologies, and data flows.
- Explain data storage, management strategies, and both hardware and software requirements.
- Discuss data visualization and analytical tools you plan to use.
- Incorporate flowcharts or diagrams to visually represent the system architecture.
-https://velog.io/@sjb2010/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%9A%94%EC%95%BD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98에 나온 텍스트랭크 기법을 참고하여 만듬.
## 8. 위험요소

- Identify potential risks such as technical issues or resource limitations.
- Provide mitigation strategies for each risk.
- 데이터 부족 : 자신의 한글파일로 해결함
- 퀄리티 부족 : 기존의 코드에 한국어를 지원할수 있도록 변경함
- 이미 흔히 사용되고 있는 코드 : 본인의 코딩 역량 및 인공지능 관련 역량을 만들기위한 교육역량의 과정이므로 실패하든 성공하든 그것을 경험으로 받아들여 차후 더 나은 코딩을 할수 있도록 함.
## 9. 자원

- Enumerate required resources, including staff roles, equipment, and software.
서버, 파이썬 
## 10. 기술 사양 

- Dive deep into technical aspects like data sources, data transformations, and algorithms.
- Discuss the technology stack, including programming languages, frameworks, and libraries.
- Outline data security measures.

## 11. 타임라인 및 결과물

- Establish a project timeline with milestones and deadlines.
- Specify what will be delivered at each milestone and the quality assurance measures in place.
- 자료조사 2주
- 프로그래밍 2주
## 12. 결론

- Summarize key points, reiterate the project’s importance, and present a call to action.
- Address potential challenges and limitations.
- 실용적인 목적보다도 교육의 목적을 둔 첫 코딩 프로젝트인 만큼 부족한점은 한없이 많다. 그러나, 하여 그렇기에 이런 단계들이 있어 내가 알고리즘을 만들어 방식을 이해하고, 그것을 실천에 옮길수만 있다면 그것만으로 본인의 역량을 느리지만 높이 쌓아올릴수 있을것이라 본다.
- 
