from memory.ChatHistory import get_session_history,add_chat_history
from langchain_core.messages import HumanMessage,AIMessage

print(get_session_history("test_session_id"))
add_chat_history("test_session_id",[HumanMessage("hi hi"),AIMessage("hello hello")])
print(get_session_history("test_session_id"))