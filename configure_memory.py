from memory.ChatHistory import get_session_history,add_chat_history,clear_chat_history
from langchain_core.messages import HumanMessage,AIMessage

class Memory:
    def __init__(self,session_id) -> None:
        self.session_id=session_id

    def check_chathistory_database_connection(self):
        print(get_session_history(self.session_id))
        
    def add_messages_to_chat_history(self):
        add_chat_history(self.session_id,[HumanMessage("hi hi"),AIMessage("hello hello")])

    def clear_chat_messagess(self):  
        clear_chat_history(self.session_id) 

memory=Memory("test_session_id")
memory.check_chathistory_database_connection()
memory.add_messages_to_chat_history()
memory.check_chathistory_database_connection()
memory.clear_chat_messagess()
memory.check_chathistory_database_connection()