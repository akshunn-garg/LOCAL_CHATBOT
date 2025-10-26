# Local Command-Line Chatbot

A simple local command-line chatbot using Hugging Face Transformers (`microsoft/phi-2`) with context memory.

## Setup Instructions
1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
2. Install required packages:
    pip install transformers torch
3. Make sure interface.py, model_loader.py, and chat_memory.py are in the same folder.

## How to Run
1. run python interface.py in terminal
2. Type messages to chat. 
3. Exit with: /exit

## Sample Interaction
Local Command-Line Chatbot (type /exit to quit)
User: Hello
Bot: Hi there! How can I help you today?

User: What is the capital of France?
Bot: The capital of France is Paris.

User: Who wrote Hamlet?
Bot: Hamlet was written by William Shakespeare.

User: /exit
Exiting chatbot. Goodbye!
