from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# print("Check")
device = "cuda:0" if torch.cuda.is_available() else "cpu"

model_path = "BBBGYU/DL_LDCC_v6"

# tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4")

model = AutoModelForCausalLM.from_pretrained(model_path, load_in_4bit=True, device_map="auto")

# model = AutoModelForCausalLM.from_pretrained(model_path)
# input_text = "부자 남자와 가난한 여자가 사랑을 하는 대본 작성해줘, 남자는 20살이고 여자는 25살, 남자는 성격이 온화하다, 여자는 성격이 고약하다."
input_text = "바다에서 남자와 여자가 사랑을 하는 대본 작성해줘"


inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

output = model.generate(
    **inputs, # input text
    max_new_tokens=1000, # max length of output text
    num_beams=5, # beam search size
    no_repeat_ngram_size=2, # no repeat
    num_return_sequences=1, # number of output text
    do_sample=True # sampling
    )
print(tokenizer.decode(output[0], skip_special_tokens=True))

