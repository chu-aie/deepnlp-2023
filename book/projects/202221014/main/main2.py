from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

print("Check")  # "Check" 출력으로 스크립트 시작 확인
device = "cuda:0" if torch.cuda.is_available() else "cpu"  # CUDA가 사용 가능한 경우 device를 GPU로 설정, 아니면 CPU 사용
model_path = "BBBGYU/DL_LDCC_v6"  # 모델 경로 설정
tokenizer = AutoTokenizer.from_pretrained(model_path)  # 설정된 경로에서 토크나이저 로드
# tokenizer = AutoTokenizer.from_pretrained(LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4)

model = AutoModelForCausalLM.from_pretrained(model_path,  # 설정된 경로에서 인과적 언어 모델 로드
                                             load_in_4bit=True, 
                                             device_map="auto")

# 입력 텍스트와 결합할 prompt 정의
prompt = "다음은 특정 상황에 대한 대본을 생성하는 요청입니다.:"

# 입력 텍스트 설정
input_text = "바다에서 남자와 여자가 사랑을 하는 대본 작성해줘"

# 입력 텍스트와 prompt 결합
combined_input = f"{prompt}\n{input_text}"

inputs = tokenizer(combined_input, return_tensors="pt").to(device)  # 결합된 텍스트를 토크나이징하여 텐서로 변환, 디바이스로 이동
output = model.generate(
    **inputs,  # 입력 텍스트
    max_new_tokens=1024,  # 출력 텍스트의 최대 길이
    num_beams=5,  # 빔 서치 크기
    no_repeat_ngram_size=2,  # 반복되지 않는 n-gram 크기
    num_return_sequences=1,  # 출력 텍스트 수
    do_sample=True  # 샘플링 사용
)
print(tokenizer.decode(output[0], skip_special_tokens=True))  # 생성된 출력 텍스트 디코딩 및 출력, 특수 토큰 제외
