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

while True:

    user_input=input("User:")
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant you can always check {chat_history} and answer question accordingly. You may not need to use tools for every query - the user may just want to chat!",
        ),
        ("human", "{messages}"),
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
    {"configurable": {"session_id": "unused"}},
    )

    add_chat_history("test_session_id",[HumanMessage(user_input),AIMessage(response["output"])])


