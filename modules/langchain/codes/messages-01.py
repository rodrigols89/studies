from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

messages = [
    SystemMessage(content="You are a tutor."),
    HumanMessage(content="Explain LangChain in one sentence.")
]

response = chat.invoke(messages)
print(response.content)
