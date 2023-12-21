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
