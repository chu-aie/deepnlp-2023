# Project Title

**다중 AI NPC(Non-Player Character) 상호작용 게임 프로그램**

_Prepared by: 김도현_202021009

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

본 프로젝트는 다중 AI NPC 상호작용 게임 프로그램의 개발을 목표로 하고 있습니다.
이 게임 프로그램은 플레이어가 다양한 상호작용 가능한 AI NPC들을 통해 자연스럽고 현실적인 게임세계를 경험할 기회를 제공하는 것이 목적입니다.

## 2. Background

최근 인공지능 관련 기술들이 수많은 발전을 이룸에 따라 게임 산업에도 매우 혁명적인 변화를 가져다 주고 있습니다.

그 중 특히, 관련 기술들을 적극 활용하여 게임 내 NPC들의 AI를 발전시키는 주제에 대해 많은 관심이 기울이고 있는 추세입니다.
(관련 자료 : Generative Agents, Replica Smart NPCs 등)

그 이유로는 관련 주제를 통해 개발자들은 게임 개발에 관해 더 많은 창의적인 가능성을 열어주고 그 뿐만이 아니라,
수많은 게임 플레이어들에게도 더욱 현실적이고, 풍부하며 흥미진진한 경험 할 수 있는 기회가 제공되기 때문입니다.

이에 대한 내용들을 통해 저 또한 관심과 흥미가 생겼기에 관련 프로젝트를 선택하게 되었습니다.

## 3. Objectives

**Specific(구체적인)** : 플레이어가 다양한 상황에서 각각의 AI NPC들과 자연스럽게 상호작용할 수 있는 게임 환경 제공.
**Measurable(측정 가능한)** : 상호작용 가능한 AI NPC들의 경험에 관련된 모든것들을 기록, 또한 플레이어의 선택이 게임 진행에 어떠한 영향을 미치는지에 대해서도 기록.
**Achievable(달성 가능한)** : 관련 기술과 리소스들을 적극 활용하여 시스템 개발 목표 달성 (generative agents)
**Relavant(관련성 있는)** : 게임 산업에서 AI 기술의 활용의 미래 게임의 핵심 요소가 될 것으로 예측된다. 따라서 이 프로젝트 또한 많은 측면에서 관련성이 높다고 볼 수 있다.
**Time-bound(기한이 정해진)** : 프로그램 개발 목표에 무사히 도달하고 기한까지 완벽한 결과물을 도출 시킬 수 있을지에 대해서는 미지수.

## 4. Scope

**AI NPC 특징 및 성격**
- 각 AI NPC는 고유의 특징, 성격, 뒷배경이 부여되며, 이를 바탕으로 상호작용

**다중 AI NPC 상호작용 시스템**
- 플레이어가 AI NPC들과 대화하고 상호작용할 수 있는 기능을 구현
- AI NPC들은 다양한 대화 주제에 대한 응답을 생성하며, 플레이어의 행동에 따라 반응

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

**Developer**
- ME(All)

**Hardware**
- Development Desktop & Labtop

**Software**
- OS : Windows (or Linux)
- Language : Python
- Development Tools : Visual Studio Code

- [Generative Agents](https://github.com/joonspk-research/generative_agents/)

## 10. Technical Specifications

### 10.1. data sources and transformations
- **data sources** : 게임 내 플레이어 및 AI NPC 상호작용, 진행 상황 등의 데이터는 클라이언트-서버 구조를 통해 수집.
- **data transformations** : 수집된 데이터는 클라이언트에서 서버로 전송되며, 서버에서는 데이터를 데이터베이스에 저장하고 필요한 경우에 따라 변환하여 활용.

### 10.2. technology stack
- **Programming Language** : Python
- ...
- **Web Server** : Django

### 10.3. data security
- 모든 사용자 데이터는 암호화 되여 저장되며 액세스 권한은 제한됨.
- 데이터 베이스는 주기적으로 백업을 수행하여 데이터 손실을 방지함.

## 11. Timeline and Deliverables

- Establish a project timeline with milestones and deadlines.
- Specify what will be delivered at each milestone and the quality assurance measures in place.

## 12. Conclusion

- Summarize key points, reiterate the project’s importance, and present a call to action.
- Address potential challenges and limitations.