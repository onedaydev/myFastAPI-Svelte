from pydantic import BaseModel, validator

import datetime  

from domain.user.user_schema import User

class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Empty Value is not permitted')
        return v
    
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: User | None
    question_id: int
    modify_date: datetime.datetime | None = None    
    voter: list[User] = []

    class Config:
        orm_mode = True

class AnswerUpdate(AnswerCreate):
    answer_id: int

class AnswerDelete(BaseModel):
    answer_id: int

class AnswerVote(BaseModel):
    answer_id: int