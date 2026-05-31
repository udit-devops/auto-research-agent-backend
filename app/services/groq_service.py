from langchain_groq import ChatGroq
from app.core.config import settings

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=settings.GROQ_API_KEY
)

planner_llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=settings.GROQ_API_KEY
)