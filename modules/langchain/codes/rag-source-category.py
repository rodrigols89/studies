from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = (
    "postgresql+psycopg2://"
    "lcuser:lcpass@localhost:6024/lcdb"
)

documents = [
    Document(
        page_content=open("data/langchain.txt").read(),
        metadata={"source": "documentation", "category": "langchain"}
    ),
    Document(
        page_content=open("data/pgvector.txt").read(),
        metadata={"source": "documentation", "category": "pgvector"}
    ),
    Document(
        page_content=open("data/history.txt").read(),
        metadata={"source": "history_book", "category": "philosophy"}
    ),
]

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
    connection=CONNECTION_STRING,  # ✅ AQUI
    collection_name="ex01_documents"
)

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 3,
        "filter": {
            "category": "pgvector"
        }
    }
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

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

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)

response = rag_chain.invoke("What is PGVector used for?")
print(response.content)
