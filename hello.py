from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

# 1. запрос без передачи информации
# uv run http localhost:8000/hi
@app.get("/hi")
def no_param_greet():
    return f"1. NO params"

# 2. передача информации с помощью директории в адресе
# uv run http localhost:8000/hi/slava
@app.get("/hi/{who}")
def url_greet(who):
    return f"2. URL PATH, {who}?"

# 3. передача информации с помощью ключ-значение в адресе
# uv run http PATCH localhost:8000/hi?who=slava
@app.patch("/hi")
def query_greet(who):
    return f"3. QUERY PARAMS, {who}?"

# 4. передача информации в теле запроса
# uv run http -v POST localhost:8000/hi who=slava
@app.post("/hi")
def body_greet(who:str=Body(embed=True)):
    return f"4. BODY, {who}?"

# 5. передача информации в заголовке запроса
# uv run http -v PUT localhost:8000/hi who:slava
@app.put("/hi")
def header_greet(who:str = Header()):
    return f"5. HEADER, {who}?"

# вывод информации из заголовка запроса
@app.get("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

# инъекция кода состояния
code=402
@app.get("/happy", status_code=code)
def greet():
    return code

# инъекция HTTP-заголовков в ответе
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

