from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = (
    "postgresql+psycopg2://"
    "lcuser:lcpass@localhost:6024/lcdb"
)

# ----------------------------
# Indexação
# ----------------------------

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

# ----------------------------
# RAG
# ----------------------------

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

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

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)

question = "What is LangChain and PGVector?"

docs = retriever.invoke(question)
context = format_docs(docs)

answer = rag_chain.invoke(question)

# ----------------------------
# Avaliação do RAG
# ----------------------------

evaluation_prompt = ChatPromptTemplate.from_template("""
You are evaluating a RAG system.

Question:
{question}

Context:
{context}

Answer:
{answer}

Evaluate the answer based on:
1. Faithfulness
2. Relevance
3. Completeness

Score each from 1 to 5 and explain briefly.
""")

evaluation_chain = evaluation_prompt | llm

evaluation = evaluation_chain.invoke({
    "question": question,
    "context": context,
    "answer": answer.content
})

print("ANSWER:\n", answer.content)
print("\nEVALUATION:\n", evaluation.content)
