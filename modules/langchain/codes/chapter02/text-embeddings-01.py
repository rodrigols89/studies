from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings()

embeddings = model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!",
    ]
)
