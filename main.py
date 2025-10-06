import dspy
import os
from dotenv import load_dotenv
import dspy_classes as dspyc

load_dotenv()

meituan_longcat_flash = dspy.LM("openrouter/meituan/longcat-flash-chat:free", api_base="https://openrouter.ai/api/v1", api_key=os.getenv('open_router_key'), max_tokens=8192, num_retries=7)
gemini2_5_flash = dspy.LM("gemini/gemini-2.5-flash", api_key=os.getenv('google_ai_studio_key'), max_tokens=8192, num_retries=7)
gemini2_5_pro = dspy.LM("gemini/gemini-2.5-pro", api_key=os.getenv('google_ai_studio_key'), max_tokens=8192, num_retries=7)
dspy.configure(lm=gemini2_5_pro)

def flash_describe(text):
    with dspy.context(lm=gemini2_5_flash, max_tokens=4096):
        predictor = dspy.Predict("large_text->summary")
        result = predictor(large_text=text)
        return result['summary']
    
def pro_add_depth(text):
    with dspy.context(lm=gemini2_5_pro, max_tokens=8192):
        predictor = dspy.ChainOfThought("summary->defined_explanation")
        result = predictor(summary=text)
        return result['defined_explanation']
    
def longcat_conversation(text, history):
    with dspy.context(lm=meituan_longcat_flash, max_tokens=4096):
        predictor = dspy.Predict(dspyc.Conversation)
        result = predictor(prompt=text, history=history)
        return result


def main():
    print("Have a conversation, type exit when you are done.")
    history = dspy.History(messages=[])
    while True:
        prompt = ""
        prompt = input()
        if prompt == 'exit':
            return
        
        result = longcat_conversation(prompt, history)
        print(result['response'])
        history.messages.append({"prompt": prompt, **result})


if __name__ == "__main__":
    main()
