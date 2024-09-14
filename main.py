import os 
import dotenv
from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from tools.tools import tools
from memory.ChatHistory import get_session_history,add_chat_history
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage,AIMessage

dotenv.load_dotenv()

GEMINI_API_KEY=os.environ["GEMINI_API_KEY"]

model = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)



user_input=input("User:")
prompt = ChatPromptTemplate.from_messages(
[
    (
        "system",
        """You are a helpful assistant you can always check {chat_history} if you want and answer questions accordingly. 
            your main task is to answer questions regarding the presidential election of sri lanka. you can use availavle tools to anwer 
            questions if nessasary.user may ask questions about general questions about the election,information about different candidates,
            information about manifestoes of different candidates,compare manifestoes of different candidates and win prediction for 
            different candidates. you should ask this this question using the tools available
            if you do not know answer to a question just say I don't know without making something up.""",
    ),
    ("placeholder", "{messages}"),
    ("placeholder", "{agent_scratchpad}"),
    
]
)

agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


conversational_agent_executor = RunnableWithMessageHistory(
agent_executor,
get_session_history,
input_messages_key="messages",
output_messages_key="output",
history_messages_key="chat_history"
)

response=conversational_agent_executor.invoke(
{"messages": [HumanMessage(user_input)]},
{"configurable": {"session_id": "test_session_id"}},
)

add_chat_history("test_session_id",[HumanMessage(user_input),AIMessage(response["output"])])

print(response["output"])
