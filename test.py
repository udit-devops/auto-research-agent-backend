# from app.services.groq_service import llm
# response = llm.invoke("what is your 1st model")
# print(response)

# from tavily import TavilyClient

# from app.core.config import settings

# tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)
# search = tavily_client.search("What is the name of nvidia's CEO?")
# print(search)

from app.graph.builder import app 


result = app.invoke({
    "topic": "SpaceX business model"
    
})
print(result['report'])