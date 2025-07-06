import os

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


pdf_pah = "perceptron.pdf"     # PDF path
loader = PyPDFLoader(pdf_pah)  # PDF loader
pdf = loader.load()            # PDF documents

# Cria um splitter de 500 (documentos) e overlap de 100 (100 palavras casa)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# Divide (splita) o PDF em chunks
chunks = splitter.split_documents(pdf)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db_path = "faiss_database"  # Database path

if os.path.exists(db_path):
    vectordb = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    vectordb.add_documents(chunks)
else:
    vectordb = FAISS.from_documents(chunks, embeddings)

vectordb.save_local(db_path)
