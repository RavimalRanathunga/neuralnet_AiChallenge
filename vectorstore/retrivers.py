from langchain_google_genai  import GoogleGenerativeAIEmbeddings
import os 
import dotenv
from langchain_community.vectorstores import Chroma
dotenv.load_dotenv()

GEMINI_API_KEY=os.environ["GEMINI_API_KEY"]

class Retriver:
    def __init__(self) -> None:
         self.retrivers={}

    def initilize_embedding_model(self):
        embedding_model= GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GEMINI_API_KEY
        )
        return embedding_model

    
    def add_documents(self,candidate_name,embedding_model,documents):
            vectorstore=Chroma.from_documents(documents=documents,embedding=embedding_model,persist_directory="./chroma_db_"+candidate_name)
            retriver=vectorstore.as_retriever()
            # print(retriver.invoke(f"what is public tranportation policy of {candidate_name}"))
            self.retrivers[candidate_name] = retriver
            print(self.retrivers)

