import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id: int
    subject: str | None = None
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    user: User | None
    modify_date: datetime.datetime | None = None
    voter: list[User] = []

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Null Value is not permitted')
        return v
    
class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []

class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

class QuestionVote(BaseModel):
    question_id: int