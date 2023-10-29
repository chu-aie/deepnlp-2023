# HLU ( Hand Location Upload )

_Prepared by: [Group Name]_

1. 202332012 양권우
2. [Name and Student ID]

## Table of Contents

- [Project Title](#project-title)
  - [목차](#table-of-contents)
  - [1. 요약](#1-executive-summary)
  - [2. 배경](#2-background)
  - [3. 목표](#3-objectives)
  - [4. 범위](#4-scope)
  - [5. 소프트웨어 프로세스 모델](#5-software-process-model)
  - [6. 예산](#6-budget)
  - [7. 시스템 구조](#7-system-architecture)
  - [8. 위험요소](#8-risks-assessment)
  - [9. 자원](#9-resources)
  - [10. 기술사양](#10-technical-specifications)
  - [11. 타임라인 및 결과물](#11-timeline-and-deliverables)
  - [12. 결론](#12-conclusion)


## 1. 요약

- Summarize the project's primary goals, intended outcomes, and problem it aims to solve. Keep it concise, ideally under 200 words.
-  인공지능의 자연어처리를 드론에 적용하여 명령된 장소에 따라 이동할수 있도록하는 프로그램을 만드려고함.    

## 2. 배경
- 2023년 1월쯤부터 초경량비행장치중에서 멀티콥터 종목의 자격증을 따기위해서, 그리고 멀티콥터에 대한 지식을 습득하기위해 전문교육기관으로가서 비행시간 24시간 이상을 채우던 중이였음.  그러던중 2022년에 만들어진 chatGPT에 대한 정보를 듣고 인공지능에 대해서 조사해본 결과
  ChatGPT가 LLM에 근거하여 만들어졌고 그 LLM이 NLP라는 자연어처리를 위한 목적을 위한 데이터베이스라는걸 알게됨.  향후 수십년뒤 NLP가 영향을 미칠수 있는 다양한 변수중 드론과 관련된 가능성을 고민하던 결과,  NLP를 통해 드론의 이동 및 수행명령을 내릴수 있다는 사실을 알게됨.
  그 명령이란 조난자나 사건 현장이 발생했을경우에  구두 명령을 수행한것을 인식하여 해당 좌표로 이동하여 도와줄수 있는 것임.

## 3. 목표

- Detail your project’s SMART objectives.
- Describe how the software will meet these objectives and solve the outlined problem.
- 구체적 -  구두명령을 내렸을때 드론이 필요한 위치로 이동할수 있는가를 알아본다.
- 측정가능 - 장기적인 프로젝트이기때문에 프로그래밍, 명령의 가짓수?, 실전 비행 테스트 등으로 세부 목표를 나뉘며 혹여나 일정으로 인해  드론 비행 테스트가 안될경우  답변의 출력을 확인함 (예 -> 구두명령으로 왼쪽 5m 이동명령을 내렸다면 xy축으로 생각했을시 출력 결과에 x5로 나옴) 
- 행동중심 - 해당 과제물에서 중요한것은 임베딩임. 드론은 결국 기계이므로 기계가 동작하기위한 프로그래밍이 절대조건으로 필요하게됨 따라서 임베딩을 위한 준비가 필요함. 
- 현실적 -  임베딩을 위한 파이썬의 기본적인 문법 입력은 가능하지만 문제는 수행명령이 내려질수 있는 경우의 수가 많으므로 시간이 걸리기때문에 확실한 이동명령(예:왼쪽으로 고도를 유지한채 5m이동.)정도를 인식할수 있도록함.   
- 제한적인 - 기말까지 7주 정도 시간이 남아있음. 그시간안에 기말고사 과목들에 대한 준비가 이루어지기때문에 기말 준비시간 1주를 빼면 6주가 남음.   따라서 11월 28일까지 초기버전 완성해야함.
  
## 4. 범위

- Define the scope of the project, outlining its features and functionalities.
- Mention any limitations or constraints such as resources, time, or technologies.
- 3단계에 걸친 목표 (텍스트변환 시스템 완성 -> 좌표 비행 완성-> 화물 운송)이 주어졌으며, 각 작은목표중 지연되는 경우에는 최소한 텍스트변환 시스템, 좌표변환 시스템등의 작은 목표를 최소 큰 목표로 잡음.
- 임베딩에 대해 아는 사람과 방과후 활동을 하면서 임베딩에 대한 기초지식을 습득하여 준비함.
- 
## 5. 소프트웨어 프로세스 모델

- State the chosen software process model (e.g., Agile, Waterfall, Scrum).
- Justify your model choice and illustrate its application to your project.
- Detail the activities and roles in each phase, possibly via a Gantt chart.
- Discuss testing methodologies, quality assurance, and project management strategies.
- 제안서의 경우 그때그때 수정이 들어가는 agile이지만, 실제 작업시 프로그램을 만들어보고 시험용 드론에 적용하여 잘 돌아갈수있을지 확인하고, 실패하게될시 피드백 과정을 거쳐서 프로그램을 좀더 보강하고자 나선형 모델을 택함.
## 6. 예산

- Provide a financial plan covering hardware, software, labor, and other costs.
- Include a contingency plan for unexpected expenses.
-  학교서버를 빌려 프로그램을 제작하고자함.  

## 7. 시스템 구조

- Detail the system architecture, mentioning tools, technologies, and data flows.
- Explain data storage, management strategies, and both hardware and software requirements.
- Discuss data visualization and analytical tools you plan to use.
- Incorporate flowcharts or diagrams to visually represent the system architecture.
- https://github.com/thiagoalessio/tesseract-ocr-for-php (tesseract ocr for php)의 코드를 인용하여 임베딩을 함. 
## 8. 위험요소

- Identify potential risks such as technical issues or resource limitations.
- Provide mitigation strategies for each risk.
- 데이터 부족
- 비행중 오작동 가능성
- 좌표 특정불가
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
- 임베딩 준비 시간 1주
- 명령어 수집 프로그래밍 4주
## 12. 결론

- Summarize key points, reiterate the project’s importance, and present a call to action.
- Address potential challenges and limitations.
- 
