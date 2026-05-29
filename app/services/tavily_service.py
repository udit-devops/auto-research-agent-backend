from tavily import TavilyClient

from app.core.config import settings

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)
search = tavily_client.search("What is the name of nvidia's CEO?")
print(search)