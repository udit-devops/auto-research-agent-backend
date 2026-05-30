from app.graph.builder import app

res = app.invoke({
    "topic": "why andrej karpathy is so popular"
})

print (res)