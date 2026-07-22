from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def inicio():
    print("a função foi executadaa")
    return {
        "mensagem": "CorrigeFácil está funcionando"
    }