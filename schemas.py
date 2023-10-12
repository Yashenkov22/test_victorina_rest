from datetime import datetime

from pydantic import BaseModel


class RequestModel(BaseModel):
    questions_num: int


class AnswerModel(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime