import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import problem_description

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(problem_description.router, prefix="/api/problem-description", tags=["Problem Descriptions"])


@app.get("/")
def read_root():
    return {"Hello": "World from Main App"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=1455, log_level="info")
