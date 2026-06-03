from tavily import TavilyClient

from app.core.config import settings

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)
