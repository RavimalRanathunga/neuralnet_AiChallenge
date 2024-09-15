from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools import DuckDuckGoSearchRun
class Tool:
    def __init__(self) -> None:
        self.tools=[]
    def creating_retriver_tools(self,retrivers):
        for retriver in retrivers:
            first,last=retriver.split()
            retriever_tool = create_retriever_tool(
            retrivers[retriver],
            f"{first}_manifesto_search",
            f"Search for information about {retriver}'s manifesto",
            )

            self.tools.append(retriever_tool)
        return self.tools    
    
    def create_search_tool(self):
        search_tool=DuckDuckGoSearchRun()
        self.tools.append(search_tool)

        return self.tools