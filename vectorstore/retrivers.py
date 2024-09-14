from langchain_google_genai  import GoogleGenerativeAIEmbeddings
import os 
import dotenv
from langchain_chroma import Chroma
from .textSplitters import chunked_manifestoes
from langchain.docstore.document import Document 
dotenv.load_dotenv()

GEMINI_API_KEY=os.environ["GEMINI_API_KEY"]

def initilize_embedding_model():
    embedding_model= GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )
    return embedding_model

def create_vectorstore(embedding_model):
    vectorstore = Chroma(collection_name="candidate_manifesto",embedding_function=embedding_model)
    return vectorstore

def add_documents():
    for candidate in chunked_manifestoes:
        documents=chunked_manifestoes[candidate]
        vectorstore.from_documents(documents=documents,embedding=embedding_model)

def create_retrivers():
    retriver=vectorstore.as_retriever()
    return retriver

embedding_model=initilize_embedding_model()
vectorstore=create_vectorstore(embedding_model)
add_documents()
retriver=create_retrivers()

