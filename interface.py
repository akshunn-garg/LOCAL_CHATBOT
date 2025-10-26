from model_loader import load_chatbot_model
from chat_memory import ChatMemory

def main():
    print(">>")
    print("Local Command-Line Chatbot (type /exit to quit)")
    chatbot=load_chatbot_model()
    memory=ChatMemory(window_size=5)

    while True:
        user_input=input("User: ").strip()
        if user_input.lower()=="/exit":
            print("Exiting chatbot. Goodbye!")
            break

        context=memory.get_context()
        context+=f"User: {user_input}\nBot:"

        response=chatbot(context,max_new_tokens=150,do_sample=True)
        bot_reply=response[0]['generated_text'].split("Bot:")[-1].strip()
        print(f"Bot: {bot_reply}\n")

        memory.add(user_input,bot_reply)

if __name__=="__main__":
    main()
