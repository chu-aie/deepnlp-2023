# 소셜 미디어 언어 다변환 시스템: 싸이월드
- 딥러닝 자연어처리 기말고사 구현 결과 보고서

    _Prepared by: 김지연_202021013_

# Hugging Face AutoTrain을 사용한 LLM Fine-Tuning
- src/202021013
    
    - dataset = 훈련시키기 위해 csv로 가공된 데이터

    - ori_data = 원본데이터를 dataset으로 만들기 위해 가공한 데이터

    - code
        
        datamake.ipynb = dataset과 ori_data를 만들기 위해   실행한 코드

        test_practice.ipynb = 만든 model을 테스트 하기위해 시도한 코드

        test.py = 가장 잘되는 테스트 코드



## src/202021013 코드 실행 과정

[**LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4**](https://huggingface.co/LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4) 모델과 싸이월드 말투 데이터를 제작하여 사용함. 

### step1 : LDCC모델 테스트
- src/202021013/code/test.py
<img src="img/ldcc_test.py.png">
<img src="img/ldcc_test결과.png">
 
- "좋아하는 사람한테 편지쓸거야. 받는사람이름은 정국이고 싸이월드 감성으로 적으면 돼."라는 질문을 던졌을때 나오는 결과를 보면 편지형태는 알지만 싸이월드 말투 이해 부족

### step2 : 싸이월드 말투 데이터 제작 - src/202021013/code/datamake.ipynb

 - txt 파일
 <img src="img/txt.png">
 
 - txt 파일 json으로 수정
 <img src="img/txt_json.png">
 
 - json파일 csv로 수정(2442개)
 <img src="img/json_csv.png">

### step3 : LDCC 모델 fine tuning
- **참고:** examples/autotrain

    1. examples/autotrain/requirements.txt에 따라 진행

    2. src/202021013/code/mymodel.env파일 실행
        ```
        PROJECT_ID=${PROJECT_ID:="202021013"}
        AUTOTRAIN_PROJECT_NAME="LDCC/2-${PROJECT_ID}"
        MODEL_NAME="LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4"
        DATA_PATH="src/202021013/dataset"
        DATA_FILE="src/202021013/dataset/output.csv"
        TEXT_COLUMM="text"
        LEARNING_RATE=2e-4
        NUM_EPOCHS=2
        BATCH_SIZE=2
        BLOCK_SIZE=1024
        TRAINER="sft"
        WARMUP_RATIO=0.1
        WEIGHT_DECAY=0.01
        GRADIENT_ACCUMULATION=4
        USE_FP16="True"
        USE_PEFT="True"
        USE_INT4="True"
        LORA_R=16
        LORA_ALPHA=32
        LORA_DROPOUT=0.05
        PUSH_TO_HUB="False"
        HF_TOKEN=${HF_TOKEN:="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"}
        REPO_ID="username/repo_name"
        ```

    3. NUM_EPOCHS=5 결과 >
    
        src/202021013/code/test.py실행
        <img src="img/test_mymodel.png">
        <img src="img/epoch5.png">
        데이터에 프롬프트 템플릿 형식이 나옴.

    4. NUM_EPOCHS=2 결과
    <img src="img/epoch2.png">
    가장 잘 나온 결과

    5. NUM_EPOCHS=3 결과
    <img src="img/epoch3.png">
    데이터에 프롬프트 템플릿 형식이 나옴.

    6. NUM_EPOCHS=1 결과
    <img src="img/epoch1.png">
    결과가 LDCC모델과 유사함. 싸이월드 말투가 안나옴.    

### step4 : 가장 잘나오는 epoch2로 lora_r,lora_alpha값 바꿔서 test
- NUM_EPOCHS=2 결과
    
    "lora_r": 16,
    "lora_alpha": 32
    
    <img src="img/epoch2.png">

- NUM_EPOCHS=2 결과

    "lora_r": 8,
    "lora_alpha": 16
    
    <img src="img/epoch2_lorar8.png">

### step5 : test.py 다양한 시도 - src/202021013/code/test_practice.ipynb
- 이 결과가 가장 잘 나와서 test.py로 실행
<img src="img/test_pra1.png">
- 2번째 결과
<img src="img/test_pra2.png">

- 3번째 결과

        2006.05.24.싸이월드 싸이버스타 정 국 ♡ 10년후에도 30년이후 40이후에 50 60세가 되어도 70.80세 되서도 그대만 생각할거야 나만을 사랑해줘 싸이버사랑 싸이월드가 영원토록 같이해. 싸이코가 될때까지 싸이사랑해 싸이라이프를 살아갈거야 싸이싸이트가 없어질때까지 싸이를 평생동안 사랑할것이다 싸이마음을 영원히 간직할 것이다 싸이미니홈피에 싸이가 되어 영원히 있을 것이다 영원히 싸이인생을 살아볼 것이다 싸이나랑 평생사랑해줄래? 싸이감성을 영원히 가지고 살아줄래싸이여생을 싸이생명을 싸이영혼을 싸이라이프를 싸이생활을싸이를 영원히 함께싸이와

- 4번째 결과
<img src="img/test_pra4.png">


## 결론
- 발표자료 딥러닝 기말.pptx 
<img src="img/결과.png">