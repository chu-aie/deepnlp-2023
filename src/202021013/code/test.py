import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_path = "/home/dev/workspace/deepnlp-2023/src/202021013/code/LDCC/csve2-jiyeon/checkpoint-42"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# tokenizer = AutoTokenizer.from_pretrained("LDCC/LDCC-Instruct-Llama-2-ko-13B-v1.4")

bnb_config = BitsAndBytesConfig(
    load_in_8bit=False,
    load_in_4bit=True,
    llm_int8_threshold=6.0,
    llm_int8_skip_modules=None,
    llm_int8_enable_fp32_cpu_offload=False,
    llm_int8_has_fp16_weight=False,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=False,
    bnb_4bit_compute_dtype="float16",
)

model = AutoModelForCausalLM.from_pretrained(model_path, quantization_config=bnb_config , device_map="auto")

input_text = "좋아하는 사람한테 편지쓸거야. 받는사람이름은 정국이고 싸이월드 감성으로 적으면 돼."
input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda:0")

# Generate multiple sequences with specified parameters
sample_outputs = model.generate(
    input_ids,
    do_sample=True,    # Use sampling strategy
    max_length=500,     # Maximum decoding length is 50
    top_k=50,          # Exclude tokens outside the top 50 in probability rank
    top_p=0.95,        # Generate from candidates with cumulative probability up to 95%
    no_repeat_ngram_size=2,
    num_return_sequences=2  # Generate different sequences
)

# Decode and print the generated sequences
for i, sample_output in enumerate(sample_outputs):
    generated_text = tokenizer.decode(sample_output, skip_special_tokens=False)
    print(f"Generated Sequence {i + 1}: {generated_text}")