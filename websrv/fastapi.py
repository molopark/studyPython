from fastapi  import FastAPI

# 터미널에서 실행해야함 : uvicorn main:app --reload
# main.py 의 app 오브젝트 실행
# --reload 옵션은 개발환경에서만 실행, 서버 재시작
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    