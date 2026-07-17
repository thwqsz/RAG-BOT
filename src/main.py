from fastapi import FastAPI
from pydantic import BaseModel
from rag import answer_question

app = FastAPI()


class Question(BaseModel):
    text: str


@app.post("/ask")
def ask(question: Question):
    answer = answer_question(question.text)
    return {"answer": answer}