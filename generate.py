import torch
from transformers import pipeline

def generateDescription(taskTitle:str):
    pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")

    # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
    messages = [
        {
            "role": "system",
            "content": "task descriptions with maximum 160 characters",
        },
        {"role": "user", "content": taskTitle},
    ]

    return (pipe(messages, max_new_tokens=5)[0]['generated_text'][-1])