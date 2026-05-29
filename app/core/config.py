from dotenv import load_dotenv
import os

load_dotenv()
class settings:
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY")
    
settings = settings()