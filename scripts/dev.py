import uvicorn

def main():
    uvicorn.run("src.messages_service.main:app", host="127.0.0.1", port=8003, reload=True)
