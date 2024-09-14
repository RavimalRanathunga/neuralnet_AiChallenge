from memory.ChatHistory import get_session_history,add_chat_history
from langchain_core.messages import HumanMessage,AIMessage
from vectorstore.documentLoader import DocumentLoader 

# class Memory:
#     def __init__(self,session_id) -> None:
#         self.session_id=session_id

#     def check_chathistory_database_connection(self):
#         print(get_session_history(self.session_id))
        
#     def add_messages_to_chat_history(self):
#         add_chat_history(self.session_id,[HumanMessage("hi hi"),AIMessage("hello hello")])
#         print(get_session_history(self.session_id))

# memory=Memory("test_session_id")
# memory.check_chathistory_database_connection()
# memory.add_messages_to_chat_history()

# file_path="docs\manifesto-ranil.pdf"
# document=DocumentLoader(file_path)
# pdf_data=document.load_documents()
# print(pdf_data)
# print(document.sort_pdf_documents(pdf_data))
