from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence."
)

chain = prompt | model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=100,
)

response = chain.invoke({"topic": "LangChain"})
print(response.content)
