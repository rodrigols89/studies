from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv


load_dotenv()


CONNECTION_STRING = (
    "postgresql+psycopg2://"
    "lcuser:lcpass@localhost:6024/lcdb"
)

loader = TextLoader("data/example.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    connection_string=CONNECTION_STRING,
    collection_name="ex01_documents"
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

prompt = ChatPromptTemplate.from_template("""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, say "I don't know".
""")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

question = "What is LangChain and PGVector?"

docs = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in docs
)

chain = prompt | llm

answer = chain.invoke({
    "context": context,
    "question": question
})

print(answer.content)
