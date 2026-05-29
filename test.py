from app.services.groq_service import llm
response = llm.invoke("what is your 1st model")
print(response)