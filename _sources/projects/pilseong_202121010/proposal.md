# 공감형 대화 생성

_Prepared by: [Group Name]_

1. [양필성 202121010]



## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [1. Executive Summary](#1-executive-summary)
  - [2. Background](#2-background)
  - [3. Objectives](#3-objectives)
  - [4. Scope](#4-scope)
  - [5. Software Process Model](#5-software-process-model)
  - [6. Budget](#6-budget)
  - [7. System Architecture](#7-system-architecture)
  - [8. Risks Assessment](#8-risks-assessment)
  - [9. Resources](#9-resources)
  - [10. Technical Specifications](#10-technical-specifications)
  - [11. Timeline and Deliverables](#11-timeline-and-deliverables)
  - [12. Conclusion](#12-conclusion)


## 1. Executive Summary

- 대화의 문맥을 파악하여 상황에 알맞는 공감형 문장을 결과로 도출하는 것을 주요 목표로 한다. 문맥을 이해해 한가지의 문장이 아닌 여러 가지의 문장을 도출하는 것이 가장 이상적인 결과이다.

## 2. Background

- 현재 사회에서는 공감을 많이 요구하는 대화가 많아지는 추세이다. 다른 사람과 대화할 때 상대방에 감정까지 생각하며 대답을 해야 좋은 대인관계가 형성되는 것이 당연하긴 하나 이런 대화를 많이 안해본 사람들은 어색하거나 어려워하는 경향이 있어 고민인 사람들이 있다.
- 이번 프로젝트를 통해서 공감형 대화가 익숙하지 않거나 어려워하는 사람들도 어떤 공감형 대화를 해야하지는 추천을 해줌으로써 보다 원할한 대화를 이어나가 좋은 대인관계를 갖게한다.
- 이 주제를 택한 이유는 주변 사람들과 얘기를 하다보면 이런 문제로 고민을 애기해주는 사람들이 많다. 연인사이에서도 이러한 대화로 다투는 모습까지 보았기 때문에 평소에 고민이 많았는데 이번 프로젝트로 이러한 상황을 해결을 해보려고 해 이 주제를 선택했다.

## 3. Objectives

- Specific(구체적): 공감형 대화 생성 프로그램은 상대방에 말에 어떻게 대답을 해야될지 모르는거나 자신의 답변의 확신이 없는 상황에 프로그램을 활용해 여러가지의 답변을 보며 참고를 해서 보다 더 좋은 대화를 이끌어가게 해줄 것이다. 
- Measruable(측정 가능한): aihub 와 모두의 말뭉치 웹사이트는  공적 데이터 포털이다. 이 웹사이트들에서 공감형 대화 데이터와 온라인 대화 데이터를 통해 모델을 훈련시킬 것이다.
- Achievable(달성 가능한): 이번 프로젝트는 결과의 만족도가 높아야된다. 따라서 결과에 대한 설문조사나 사용자들이 많이 선택한 답변에 가중치를 주는 단계가 목표에 달성하기위해 필요한 단계로 보인다.
- Realistic 그리고 Relevant(현실적이고 관련된): 최근에 MBTI라는 심리검사가 생겨 많은 사람들이 이검사를 진행했다. MBTI 검사는 4가지의 이진요소들로 에너지 방향, 인식 방식, 판단, 생활방식으로 나뉜다. 판단요소는 F와 T로 나뉜다. 공감형 대화는 판단 요소에 포함이 된다. T는 현실적인 성향으로 공감을 못하면 T라는 인식이 있다. 과거에는 이러한 심리검사가 많이 생기지않아 공감형 대화의 중요성이 크지 않았는데 현재에는 공감을 못하면 T라고 말하며 중요성이 커지기 시작하며 또한 서로 잘 맞는 MBTI까지 생기기 시작하며 공감에 대한 중요성은 더욱 커지고 있다.
- Time-bound(기한이 있는): 이번 프로젝트는 LLM을 활용하여 소프트웨어를 만드는 것이 목표이다. 모델을 훈련시키고 결과를 보며 이번 학기가 끝나기전에 결과를 바탕으로 수정을 해야되는 과정이 중요하다. 따라서 기한까지 완벽한 결과물을 도출시키는 것은 불확실할 것 같다.


## 4. Scope

- 공감형 대화 생성 프로젝트는 문맥에 맞는 공감형 대화를 생성하는 기능을 한다. 공감형 대화는 공적인 대화보다 사적인 대화가 많다. 따라서 대화체가 많이 사용될 것으로 예상을 한다. 이로 인해 온라인 대화체를 사용하는 것이 특징이다. 한국어 데이터가 필요하지만 데이터를 수집하는 것에 제한이 있을 것으로 예상된다.

## 5. Software Process Model

- State the chosen software process model (e.g., Agile, Waterfall, Scrum).
- Justify your model choice and illustrate its application to your project.
- Detail the activities and roles in each phase, possibly via a Gantt chart.
- Discuss testing methodologies, quality assurance, and project management strategies.

## 6. Budget

- Provide a financial plan covering hardware, software, labor, and other costs.
- Include a contingency plan for unexpected expenses.

## 7. System Architecture

- Detail the system architecture, mentioning tools, technologies, and data flows.
- Explain data storage, management strategies, and both hardware and software requirements.
- Discuss data visualization and analytical tools you plan to use.
- Incorporate flowcharts or diagrams to visually represent the system architecture.

## 8. Risks Assessment

- Identify potential risks such as technical issues or resource limitations.
- Provide mitigation strategies for each risk.

## 9. Resources

- Enumerate required resources, including staff roles, equipment, and software.

## 10. Technical Specifications

- Dive deep into technical aspects like data sources, data transformations, and algorithms.
- Discuss the technology stack, including programming languages, frameworks, and libraries.
- Outline data security measures.

## 11. Timeline and Deliverables

- Establish a project timeline with milestones and deadlines.
- Specify what will be delivered at each milestone and the quality assurance measures in place.

## 12. Conclusion

- Summarize key points, reiterate the project’s importance, and present a call to action.
- Address potential challenges and limitations.
