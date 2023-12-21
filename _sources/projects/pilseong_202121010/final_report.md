# 기말 보고서
- 주제: 공감형 대화 생성 모델
- 기본 모델: LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4
- 데이터: ypilseong/deepnlp_autotrain_Empathy_chat_data

## Test1 - 기본 모델 inference
### 기본 test.py
- generate의 args 추가
'''python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"


model_path = "LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4 "
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path,load_in_4bit=True, device_map="auto")



input_text = "부장님한테 혼났어 ㅠㅠ"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda")

output = model.generate(input_ids, 
                        max_new_tokens=1024,
                        early_stopping=True,
                        do_sample=True,
                        num_beams=3
                        )
predicted_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(predicted_text)
'''

### 결과

<img src="book/projects/pilseong_202121010/img_folder/ldcc_model.png" >

<img src="book/projects/pilseong_202121010/img_folder/ldcc_model_2.png">

- 기본 모델이 공감을 못해주며 맥락이 없는 대답을 해준다.

## Test2 - 기본 모델 Fine-Tunning 진행
### 데이터(ypilseong/deepnlp_autotrain_Empathy_chat_data) 공공 데이터를 통해 학습 진행

- generate() args는 그대로 유지하고 진행
'''python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"


model_path = "ypilseong/deepnlp_autotrain_llm_kor_llama_v7"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path,load_in_4bit=True, device_map="auto")



input_text = "부장님한테 혼났어 ㅠㅠ"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda")

output = model.generate(input_ids, 
                        max_new_tokens=1024,
                        early_stopping=True,
                        do_sample=True,
                        no_repeat_ngram_size=3,
                        num_beams=3
                        )
predicted_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(predicted_text)
'''

### 결과

<img src="book/projects/pilseong_202121010/img_folder/model7_2.png">

<img src="book/projects/pilseong_202121010/img_folder/model7_3.png">

- Fine-Tunning을 시켰지만 공감을 못해주며 한국말도 잘 나오지 않는 상황이 됐다.

## Test3 - Inference code Edit
### Test.py 사용하지 않고 새로운 Inference code 사용
- Prompt template 생성 후 Prompt로 넣겨줌
- Top_k, Top_p 방식을 통해 Text generate
- repetition penalty 반복 통제

'''python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def gen(x, model, tokenizer, device):
    prompt = (
        f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### Prompt:\n{x}\n\n### Answer:"
    )
    len_prompt = len(prompt)
    gened = model.generate(
        **tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to(
            device
        ),
        max_new_tokens=1024,
        early_stopping=True,
        do_sample=True,
        top_k=15,
        top_p=0.92,
        no_repeat_ngram_size=3,
        eos_token_id=2,
        repetition_penalty=1.2,
        num_beams=3
    )
    return tokenizer.decode(gened[0], skip_special_tokens=True)[len_prompt:]

def LLM_infer(input):
    device = (
        torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    )
    model_id = "ypilseong/deepnlp_autotrain_llm_kor_llama_v7"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, device_map={"": 0},torch_dtype=torch.float16, low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model.eval()
    model.config.use_cache = (True)
    tokenizer.pad_token = tokenizer.eos_token
    output = gen(input, model=model, tokenizer=tokenizer, device=device)

    return output


if __name__ == "__main__":
    #input_text = input("you: ").decode('utf-8')
    text = LLM_infer("부장님한테 혼났어 ㅠㅠ")
    print(text)
'''

### 결과

<img src="book/projects/pilseong_202121010/img_folder/model7prompt.png">

<img src="book/projects/pilseong_202121010/img_folder/model7prompt2.png">

- Test1, Test2 보다 공감 능력이 상승되며 한국말을 잘하게 됨
- 문장을 잘 끊으며 대화 형식의 대답을 생성함
