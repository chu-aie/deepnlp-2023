# DLUH (Drone Location Upload with Hand)

_Prepared by: [Group Name]_

1. 202332012 양권우
2. [Name and Student ID]

## Table of Contents

- [Project Title](#project-title)
  - [목차](#table-of-contents)
  - [1. 요약](#1-executive-summary)
  - [2. 배경](#2-background)
  - [3. 목표](#3-objectives)
  - [4. 목표범위](#4-scope)
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

## 2. 배경

- Introduce the context and problem your software aims to address.
- Discuss its relevance and potential impact.
- Briefly explain the rationale behind choosing this specific project.
  2023년 1월쯤부터 초경량비행장치중에서 멀티콥터 종목의 자격증을 따기위해서, 그리고 멀티콥터에 대한 지식을 습득하기위해 전문교육기관으로가서 비행시간 24시간 이상을 채우던 중이였음.  그러던중 2022년에 만들어진 chatGPT에 대한 정보를 듣고
  LLM언어모델과 프롬포트를 이용하여 새 문장을 만들수 있는 당시 시점에서 향후 몇십년뒤에 그 이전에 있던 인공지능 왓슨보다 자연어 습득능력이 향상될것이라는것뿐만 아니라 좌표또한 추적할수 있다는것을 간파하게됨
  그럼에 따라  s펜으로 적혀진 문장만으로 언제 어디로 무엇을 배달할수 있을지  요약한 다음 수치화하여 지도상의 좌표값, 물건값으로 변환하여 입력할수 있다는것을 알아보고자 프로젝트를 실행하게됨

## 3. 목표

- Detail your project’s SMART objectives.
- Describe how the software will meet these objectives and solve the outlined problem.
  s펜으로 입력한 이미지만으로 프로그램이 문장을 완성할수 있는지 확인하고, 완성한 값으로서 이동수단인 드론의 좌표 해석능력을 높여 운송효율 증대를 꾀하고자함.
  
## 4. 범위

- Define the scope of the project, outlining its features and functionalities.
- Mention any limitations or constraints such as resources, time, or technologies.

## 5. 소프트웨어 프로세스 모델

- State the chosen software process model (e.g., Agile, Waterfall, Scrum).
- Justify your model choice and illustrate its application to your project.
- Detail the activities and roles in each phase, possibly via a Gantt chart.
- Discuss testing methodologies, quality assurance, and project management strategies.
  프로그램을 만들어보고 시험용 드론에 적용하여 잘 돌아갈수있을지 확인하고, 실패하게될시 피드백 과정을 거쳐서 프로그램을 좀더 보강하고자 나선형 모델을 택함.
## 6. 예산

- Provide a financial plan covering hardware, software, labor, and other costs.
- Include a contingency plan for unexpected expenses.
  물건을 들기 이전에 프로그래밍값을 확인할수 있는 소형 드론 1대(십만원대), 실제 비행으로 물건이송이 가능한지 확인하는 대형드론 1대(백만원대)가 필요하다. 또한 지표면 감지 시스템이 있어야함.   총 130만원이 필요함.

## 7. 시스템 구조

- Detail the system architecture, mentioning tools, technologies, and data flows.
- Explain data storage, management strategies, and both hardware and software requirements.
- Discuss data visualization and analytical tools you plan to use.
- Incorporate flowcharts or diagrams to visually represent the system architecture.
s펜으로 입력된 글자를 이미지로 해석하여 이미지를 텍스트로 변환하여 텍스트로 좌표 요약본을 만들고 드론의 이동위치로 반영함. 필체 데이터를 통하여 패턴을 기계학습시켜서  좌표 요약을 한다. 이륙후부터  비행 순항시 지표면으로부터 150미터 미만, 140미터 이상을 유지하도록 한다. 
## 8. 위험요소

- Identify potential risks such as technical issues or resource limitations.
- Provide mitigation strategies for each risk.
-비행 전:프로그램 인식이 안됨, 업데이트가 이루어지지않음, 용량 한계, 프로펠러 파손, 드론 동력원인 리튬 전지에 문제 발생,  사전 비행허가를 받지않음, 안전구역 확보가 되지않음, 날씨가 비행하기 부적절함  
-비행 중: 날개 회전수에 불균형이 이뤄어짐, 주변에 사람이 있음, 정해진 코스를 이탈함, 너무 낮게남, 너무 높이남
-비행 후: 리튬전지 과열이 있었는가, 착륙 이후 고장이 있었는가, 입력된 값에 따른 착륙이 이루어졌는가
## 9. 필요 자원

- Enumerate required resources, including staff roles, equipment, and software.

## 10. 기술 사양 

- Dive deep into technical aspects like data sources, data transformations, and algorithms.
- Discuss the technology stack, including programming languages, frameworks, and libraries.
- Outline data security measures.

## 11. 타임라인 및 결과물

- Establish a project timeline with milestones and deadlines.
- Specify what will be delivered at each milestone and the quality assurance measures in place.
  드론을 띄울수 있는 시간에서 저녁시간이 금지되어있기에 오후 6시 30분 이후부터 오전 8시 29분까지 드론 비행이 안되고, 12시부터 1시까지를 점심시간으로 마찬가지로 빼면,  오전 8시 30분부터 11시 50분, 1시부터 6시 20분   전반부와 후반부로 나뉘어 비행할수 있다.  따라서 비행금지시간에는 프로그램 및 필체 데이터를 수집하고있다가, 실제 비행시간시에 그동안 만들었던 데이터를 입력하여 드론을 비행시켜서 비행안정성과 좌표 정확도를 확인한다.      
## 12. 결론

- Summarize key points, reiterate the project’s importance, and present a call to action.
- Address potential challenges and limitations.

