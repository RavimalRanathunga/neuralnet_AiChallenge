import os 
import dotenv
from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import tools.tools

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
        # ("placeholder", "{messages}"),
        # ("placeholder", "{agent_scratchpad}"),
        ("human",user_input),
    ]
    )

    from langchain.agents import AgentExecutor, create_tool_calling_agent

    agent = create_tool_calling_agent(model, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

    
