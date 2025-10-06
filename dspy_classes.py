import dspy

class Conversation(dspy.Signature):
    history: dspy.History = dspy.InputField()
    prompt: str = dspy.InputField()
    response: str = dspy.OutputField()