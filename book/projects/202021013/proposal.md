# 프로젝트 제안서

**Project Title**
- 소셜 미디어 언어 다변환 시스템: 싸이월드 vs. 인스타그램

_Prepared by: 김지연_

1. 김지연 202021013

## Table of Contents

- [프로젝트 제안서](#프로젝트-제안서)
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

- 2000년대의 싸이월드와 현재의 인스타그램이라는 두 소셜 미디어 플랫폼 사이의 언어와 콘텐츠 생성 양식의 차이를 탐구하고자합니다. 각 플랫폼에서 흔히 사용되는 유행어와 신조어를 비교하여, 두 플랫폼의 고유한 문화적 특성을 이해하고, 사용자의 입력에 맞는 콘텐츠를 싸이월드 버전과 인스타그램 버전으로 제공하여 재미를 주고자 합니다.

## 2. Background

- 21세기 초반에 등장한 싸이월드와 현재의 획기적인 변화를 겪고 있는 인스타그램은 두 가지 다른 소셜 미디어 플랫폼으로, 언어 및 콘텐츠 생성의 영역에서 중요한 차이점을 보여주고 있습니다. 이 프로젝트는 각 플랫폼의 고유한 특성을 탐구하고, 시대별 소셜 미디어 사용의 언어적 흐름을 연구하며 싸이월드와 인스타그램에서 가장 흔히 사용되는 유행어와 신조어를 비교하고, 사용자가 입력한 내용을 싸이월드 버전과 인스타그램 버전으로 변환하여, 어떻게 언어와 콘텐츠 생성 양식이 시대에 따라 변화하는지를 보여줄 것입니다. 이를 통해 우리는 소셜 미디어의 언어적 진화와 문화적 특성을 더 깊게 이해하고, 사용자들에게 재미있는 비교 경험을 제공하고자합니다.

## 3. Objectives

- 2023년 12월 10일 까지 LLM을 활용하여 사용자 입력을 싸이월드 버전과 인스타그램 버전으로 자동 변환하는 프로세스를 개발하고, 언어 및 스타일의 차이를 자세히 분석합니다. 또한 개발하기 위해 필요한 인력 및 컴퓨팅 자원을 확보해야합니다. 이 프로젝트를 통해 소셜 미디어의 언어적 진화를 자세히 분석하고, 미래의 소셜 미디어 플랫폼에 대한 지침을 제공하고자하며 딥러닝 자연어처리 과목과 밀접한 관련이 있어, 해당 과목의 학습과 실무 경험을 향상시키는데 기여할 것으로 예상됩니다.

## 4. Scope
**주요 특징 및 기능:**
1. 데이터 지원 소스 :2000년대 초반과 현재의 다양한 유행어와 신조어를 포함한 다양한 데이터 소스(예: 싸이월드, 인스타그램 댓글 등)에서 데이터 수집 및 분석 기능을 제공합니다.

2. LLM을 이용한 언어 분석: 
싸이월드와 인스타그램 플랫폼에서 사용되는 일반적인 속어, 유행어, 신조어를 자동으로 식별하고 문서화하기 위해 언어 모델(예: LLM이라고 하는 GPT-3.5)을 활용합니다. 각 플랫폼 고유의 언어 패턴과 추세를 분석하여 시간이 지남에 따라 소셜 미디어 언어가 어떻게 발전했는지에 대한 통찰력을 얻을 수 있습니다.

3. 유행어와 신조어 대응 : 
신조어와 유행어의 빠른 대응을 위해 새로운 데이터 수집 및 모델 업데이트 기능을 제공합니다.

**제약 및 제한:**
1. 프로젝트 일정: 12월 말까지 제한된 시간 내에 프로젝트를 완료하는 일정을 준수해야합니다.

2. 데이터 수집 제약: 
2000년대 초반 데이터의 한정적인 접근성 및 현재의 데이터는 실시간으로 크롤링되어야 해 정확하고 많은 데이터 수집이 어려울 수 있습니다.

3. 법적 제한: 
사용자 데이터 수집 및 가공에 관한 법적 제한과 규정을 준수해야 합니다.

## 5. Software Process Model
V 모델은 소프트웨어 개발 및 품질 관리 단계를 나타내는 대칭적인 모델로, 개발과 품질 보증 단계가 대칭되어 연결되어 있습니다.

**1. 요구사항 분석 (Requirements Analysis):**

- 프로젝트 목표: 2000년대의 대표적인 소셜 미디어 플랫폼인 싸이월드와 현재의 인스타그램 간의 언어와 콘텐츠 생성 양식의 차이를 조사하고, 양식 차이를 이해하여 사용자에게 각 플랫폼 버전에 맞는 콘텐츠를 제공하는 것을 목표로 합니다.

- 데이터 수집: 싸이월드와 인스타그램에서 사용된 텍스트 데이터를 크롤링으로 수집하고, 각 플랫폼의 특징을 파악하기 위한 콘텐츠를 저장합니다.

**2. 시스템 설계 (System Design):**

- 데이터 수집과 분석: 각 플랫폼에서 데이터를 수집하고, 자연어 처리 및 텍스트 분석 기술을 사용하여 언어 및 콘텐츠 생성 양식의 차이를 식별하고 비교합니다.

**3. 소프트웨어 개발 (Software Development):**

- 프로젝트 개발: 각 플랫폼 버전을 개발하여 사용자의 입력에 따라 싸이월드와 인스타그램 버전으로 적절한 콘텐츠를 생성합니다.

**4. 단위 테스트 (Unit Testing):**
- 각 플랫폼 버전을 단위 테스트하여 각각의 콘텐츠 생성 기능이 제대로 작동하는지 확인합니다.

**5. 통합 테스트 (Integration Testing):**
- 각 플랫폼 버전을 통합하여 전체 시스템이 예상대로 작동하는지 확인하고, 사용자의 입력에 따라 올바른 콘텐츠가 생성되는지 테스트합니다.

**6. 시스템 테스트 (System Testing):**
- 시스템 테스트를 통해 두 플랫폼 버전 간의 언어 및 콘텐츠 생성 차이를 검증하고 사용자 경험을 평가합니다.

**7. 인수 테스트 (Acceptance Testing):**
- 사용자나 이해관계자의 참여를 통한 인수 테스트로, 사용자 피드백을 수집하고 프로젝트의 최종 버전을 검증합니다.

**8. 유지보수 단계 (Maintenance):**
- V-모델의 유지보수 단계에서는 소셜 미디어 플랫폼의 변화에 대응하고, 새로운 언어 및 콘텐츠 트렌드를 반영하여 시스템을 지속적으로 유지합니다.

**간트 차트:**
- 데이터 수집: 4주
- 데이터 전처리 및 분석: 2주
- 모델 개발: 2주
- 시스템 구현: 2주
- 테스트 및 오류 수정: 6주
- 사용자 피드백 및 모델 업데이트 계획: 1주

## 6. Budget
- 학교 서버 활용 계획입니다.

## 7. System Architecture
**1. 데이터 수집 및 전처리:**

- 데이터 소스: 인터넷 컨텐츠, 유튜브 채널, 인스타그램 댓글
- 데이터 크롤링: 웹 크롤링 도구 (예: Scrapy)
- 데이터 전처리: 토큰화, 불용어 제거, 형태소 분석
- 수정된 데이터 저장: 수정된 데이터를 기존의 JSON 또는 CSV 파일에 업데이트하거나, 새로운 파일로 저장합니다.

**2. LLM 모델 훈련 (GPT-3 모델 훈련):**

- 데이터 준비: Scrapy로 수집한 데이터를 PyTorch 및 GPT-3 모델 학습을 위한 형식으로 변환합니다.
- 모델 학습: GPT-3 모델을 사용하여 언어 스타일과 특징을 학습시킵니다. 모델을 싸이월드와 인스타그램 버전 모두에 적용할 수 있도록 훈련합니다.

**3. 사용자 인터페이스 (User Interface):**

- 사용자가 입력한 텍스트를 받고, 어떤 버전(싸이월드 또는 인스타그램)으로 변환할지 선택할 수 있는 사용자 인터페이스를 제공합니다.

**4. 콘텐츠 생성 (Content Generation):**

- 사용자 입력 처리: 사용자가 입력한 텍스트를 받아 GPT-3 모델에 전달합니다.
콘텐츠 생성 엔진 (Content Generation Engine): GPT-3 모델을 사용하여 어떤 버전(싸이월드 또는 인스타그램)으로 변환할지 결정하고, 해당 플랫폼에 맞는 말투,언어, 유행어, 해시태그 등을 사용하여 결과 콘텐츠를 생성합니다.

## 8. Risks Assessment
**1. 데이터 부족:** 2000년대 초의 데이터 양이 한정적일 수 있음

- 완화 전략: 데이터 증식 및 데이터 강화 기술을 사용하여 학습 데이터를 보강합니다.

**2. 유행어와 신조어 변화:** 현재 유행어와 신조어가 빠르게 변하므로 시스템이 이에 대응하기 어려울 수 있음
- 완화 전략: 실시간 크롤링을 통해 최신 데이터를 수집하고 모델을 주기적으로 업데이트합니다.

**3. 보안 문제:** 개인 정보가 포함된 데이터를 다룰 경우, 데이터 보안 문제 발생 가능성
- 완화 전략: 데이터 암호화, 접근 제어 및 규정 준수를 위한 보안 프로토콜을 구현하여 데이터 보안을 강화합니다.

## 9. Resources
- 장비: 학교 서버
- 소프트웨어: Python, TensorFlow 또는 PyTorch, 웹 크롤링 도구 (Scrapy)

## 10. Technical Specifications
**데이터 원본 (Data Sources):**

>싸이월드와 인스타그램의 웹 데이터를 수집하기 위해 Scrapy 웹 크롤링 프레임워크를 사용합니다.
텍스트 및 메타데이터를 수집하여 언어 스타일 및 특징을 분석합니다.

**데이터 변환 (Data Transformation):**

>수집한 데이터를 정제하고 표준화하기 위해 데이터 전처리 단계를 구현합니다.
>데이터를 토큰화하고 형태소 분석을 수행하여 처리 가능한 형태로 변환합니다.

**알고리즘 (Algorithms):**
>
>GPT-3 모델 (챗지피티)를 사용하여 텍스트 생성 및 변환 작업을 수행합니다.
>GPT-3 모델을 훈련하여 과거와 현재의 언어 스타일을 반영하도록 조정합니다.

**프로그래밍 언어 및 프레임워크 (Programming Languages and Frameworks):**
>
>파이썬 (Python) 언어를 사용하여 프로젝트를 개발합니다.
>Scrapy를 웹 크롤링에 사용하고, PyTorch를 GPT-3 모델 훈련 및 사용에 활용합니다.

**라이브러리 (Libraries):**
>
>PyTorch 및 Hugging Face Transformers 라이브러리를 사용하여 GPT-3 모델을 구현하고 관리합니다.
>자연어 처리 및 텍스트 분석을 위해 NLTK 또는 spaCy와 같은 라이브러리를 활용합니다.

## 11. Timeline and Deliverables
- 6주 : 학습 데이터 수집 및 전처리 완료
- 3주 : LLM 모델 훈련 및 테스트 완료
- 2주 : 시스템 구현 및 테스트 완료
- 6주 : 테스트 및 오류 수정
- 1주 : 사용자 피드백 및 모델 업데이트 계획

## 12. Conclusion
- 이 프로젝트는 데이터 수집의 어려움을 예상하지만, 크롤링을 통해 다양한 소스에서 데이터를 수집하는 데 가능성이 있다고 판단합니다.
- 제한된 시간 내에 프로젝트를 완료해야 하므로 초기에는 부족한 점이 있을 것으로 예상되지만, 정확한 시스템을 초기에 구현하면 그 후에는 수정이 수월하게 이루어질 것으로 기대합니다.

- 이 프로젝트는 과거와 현재의 소셜 미디어 플랫폼 간의 언어 및 콘텐츠 생성 양식의 차이를 탐구하고, 사용자의 입력을 싸이월드버전과 인스타그램버전으로 변환하여 문화적 이해를 촉진하며 창의적 콘텐츠를 제공하는 것을 목표로 합니다.
첫째로, 이 프로젝트는 소셜 미디어 플랫폼 사용자 간의 상호 이해를 높이는 데 기여합니다. 각 플랫폼에서 흔히 사용되는 언어와 유행어를 파악하고 사용자의 입력을 해당 플랫폼 버전으로 변환하는 데는 문화적 이해가 필수입니다. 이를 통해 다양한 세대와 백그라운드를 가진 사용자들 간의 원활한 소통이 가능해집니다.
둘째로, 이 프로젝트는 콘텐츠 생성에 창의성을 불어넣고 사용자들에게 재미를 제공합니다. 사용자가 입력한 텍스트를 각 플랫폼의 특징에 맞게 변환함으로써, 그들은 다양한 언어 스타일과 말투를 경험할 수 있습니다. 이는 콘텐츠 생성자와 소셜 미디어 사용자들에게 혁신적인 기회를 제공하며, 새로운 아이디어와 흥미로운 콘텐츠를 유발합니다.
이러한 이점은 소셜 미디어 경험을 더 풍부하고 다양하게 만들며, 사용자들에게 새로운 시각과 이해를 제공할 것입니다. 이 프로젝트의 중요성을 강조하며, 사용자들이 더 나은 소셜 미디어 상호작용을 즐길 수 있도록 동기를 부여합니다.