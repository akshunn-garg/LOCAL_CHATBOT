from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def load_chatbot_model():
    model_name="microsoft/phi-2"

    print(f"Loading model: {model_name} ...")
    tokenizer=AutoTokenizer.from_pretrained(model_name)
    model=AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype="auto"
    )

    chatbot=pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=200,
        temperature=0.7,
        top_p=0.9
    )
    print("Model loaded successfully!")
    return chatbot
