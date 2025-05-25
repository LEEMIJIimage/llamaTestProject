from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "codellama-7b-instruct.Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=-1,
    use_mlock=True,
    verbose=True
)

# LLaMA instruct 포맷 사용
PROMPT_TEMPLATE = "<s>[INST] {prompt} [/INST]"

def generate_text(prompt):
    full_prompt = PROMPT_TEMPLATE.format(prompt=prompt)
    print("=== [DEBUG] Full Prompt ===")
    print(full_prompt)
    
    output = llm(
        full_prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
        stream=False
    )
    
    print("=== [DEBUG] Raw Output ===")
    print(output)
    
    return output["choices"][0]["text"].strip()