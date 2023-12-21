# 텍스트요약기 프로젝트 보고서

202332012 양권우

## 목적

TextRank라는 2004년에 발표된 알고리즘으로 PageRank을 기반하여 특정단어가 얼마나 관계가 있는지 계산하는 알고리즘을 구현해 만든 텍스트 요약기 제작

## 개요 및 소스코드 서술

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/66134289-4850-4d91-9485-b9028c1508db)

Gensim라이브러리를 설치하고 해당 라이브러리의 summarization모듈에서 summarize함수를 불러오는 함수이다.
자연어처리와 토픽 모델링을 위한 라이브러리중 하나이며, 불러온 함수는 원래문장보자 짧게 요약하는 텍스트 요약에 사용된다.

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/f76c000f-9d72-4692-9701-7e79f515b339)

또다른 자연어처리 라이브러리인 Sumy를 설치하여, 그중 LexRank로 문장을 하나의 노드를 정리한뒤, 단어하나하나를 토큰화하여 텍스트 데이터를 요약하는 기능을 수행한다.(2차수단)
그리고 그림등의 불필요한 오브젝트를 제외하고 읽을수있는 문자열을 정리하여 문법적 관계를 해석해주는 plaintextpaser을 추가하여 요약효율을 높인다.

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/eed92349-efc7-419b-995a-a8c7713b319f)

위의 라이브러리들을 가져온 뒤, 텍스트 데이터를 가져오는 함수를 작성한다

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/d18e351b-91cf-40b3-b9ec-00c752b1472c)

그뒤, 요약함수를 작성한후 한국어로 출력해낼수 있도록 설정한다

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/af90da4f-4c43-4fcf-813f-56f44de4b3fd)

기획서를 읽을수 있도록 한다.

## 역할

-코딩:양권우 (202332012)

## 시행착오

첫째로 텍스트 요약 알고리즘을 작성하던중 gensim sumarize함수를 import하는데에 사양문제로 인하여 원인을 찾다가 아예 안되는것을 확인하고는 다른 임시 라이브러리를 불러와 sumy로서 텍스트 요약 알고리즘을 작성하게되었다.
![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/e9b8c821-2261-4c18-b538-fd8673e75486)

> ![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/a2c3121b-679d-4f15-85bd-96758e8f94ed)
>
> ![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/e06ba03f-7ae0-4c3a-8f99-b60a711f9f25)

둘째로 파일 문제였다.
자신의 기획서를 바탕으로 요약을 하기위해 시도하려했으나 이번에도 오류가 발생하게되었다.

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/ef21eeb5-11d3-4914-b63c-31d2c4495cad)

이번에는 한글파일이 해석이 안된건지 파일을 못찾았다고 뜨게되었다. 따라서 한글파일을 읽을수 있도록 또다른 라이브러리 파일을 다운받았다

![image](https://github.com/GreatBritanBias/deepnlp-2023/assets/88702293/0a5ba494-6b51-46a2-b6c0-fd2dbaea4e4e)

그럼에도 불구하고 해당 한글 파일까지 에러가 발생하여 난항을 겪었고, 끝내 해결되지못했다.

## 결론

소스코드 작성중 위의 끝까지 해결되지못한 점으로 인하여 결국 결과를 도출해내는데 실패하였다. 과정중에서는 초기에 제안서를 작성했을때 드론 관련으로 목표를 잡았으나, 해당 목표는 본인의 능력을 매우 넘어서는 목표였기에 문장요약기로 목표를 수정하고 초기의 발판을 닦을수 있도록 하였다. 그러나 진행하고보니 제안서에서 설정했던 위험요소보다도 더 많은 문제에 부딫히게되어서 난항을 겪었었다. 그럼에도 불구하고 처음으로 혼자 맡은 프로젝트중에서 가장 의미 있었다고 생각된다. 시행착오들을 거쳐서 특정 요약 라이브러리가 먹히지않는다면 다른 라이브러리를 사용하는 등의 2차적인 수단을 생각했을때가 있었기 때문에, 향후 프로젝트를 진행할때도 항상 2차적 수단을 생각해야한다는것을 알게되었다.

## 참고문헌

-PageRank논문(1998) - The PageRank Citation Ranking: Bringing Order to the Web https://www.cis.upenn.edu/~mkearns/teaching/NetworkedLife/pagerank.pdf (PageRank개념)

-[파이썬]TextRank(텍스트랭크란..간단히 구현해보기) - Seolini (2021.07.06) https://velog.io/@seolini43/%ED%8C%8C%EC%9D%B4%EC%8D%AC-TextRank%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%9E%AD%ED%81%AC%EB%9E%80..-%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EA%B8%B0

-[파이썬]텍스트 요약 알고리즘 - sjb2010 (2023.04.07) https://velog.io/@sjb2010/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%9A%94%EC%95%BD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 (알고리즘 코드 관련)

-Tokenization이란? 토큰화? 토크나이제이션? - The Yellow lion king 데이터와 함께 살아가기 (2022.04.16) https://bigdatamaster.tistory.com/175 (단어토큰화 관련 개념습득)
