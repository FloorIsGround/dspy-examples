import dspy
import os
from dotenv import load_dotenv
import dspy_classes as dspyc

load_dotenv()

meituan_longcat_flash = dspy.LM("openrouter/meituan/longcat-flash-chat:free", api_base="https://openrouter.ai/api/v1", api_key=os.getenv('open_router_key'), max_tokens=8192, num_retries=7)
# Example AI: Meituan's longcat-flash-chat, via OpenRouter
dspy.configure(lm=meituan_longcat_flash)

def longcat_conversation(text, history):
    predictor = dspy.Predict(dspyc.Conversation)
    result = predictor(prompt=text, history=history)
    return result

def start_convo():
    print("Have a conversation, type exit when you are done.")
    history = dspy.History(messages=[])
    while True:
        prompt = ""
        prompt = input()
        if prompt == 'exit':
            print("\n\nExiting...\n\n")
            dspy.inspect_history()
            return
        
        result = longcat_conversation(prompt, history)
        print(result['response'])
        history.messages.append({"prompt": prompt, **result})

        
if __name__ == "__main__":
    start_convo()
