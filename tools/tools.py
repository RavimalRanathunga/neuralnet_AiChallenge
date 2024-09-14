from langchain.tools.retriever import create_retriever_tool
from vectorstore.retrivers import retriver

retriever_tool = create_retriever_tool(
    retriver,
    "candidate_manifesto_search",
    "Search for information about candidates and their manifestoes",
)
tools=[retriever_tool]