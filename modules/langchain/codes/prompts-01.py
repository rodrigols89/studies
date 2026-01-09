from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in one sentence.")
])

chain = prompt | ChatOpenAI()

response = chain.invoke({"topic": "LangChain"})
print(response.content)
