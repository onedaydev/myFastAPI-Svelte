from datetime import datetime

from domain.question.question_schema import QuestionCreate, QuestionUpdate
from models import Question, User, Answer
from sqlalchemy.orm import Session


def get_question_list(db: Session, skip: int=0, limit: int = 10, keyword: str = ''):
    question_list = db.query(Question)
    if keyword:
        search = f'%%{keyword}%%'
        sub_query = db.query(Answer.question_id, Answer.content, User.username) \
            .outerjoin(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .outerjoin(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |        # 질문제목
                    Question.content.ilike(search) |        # 질문내용
                    User.username.ilike(search) |           # 질문작성자
                    sub_query.c.content.ilike(search) |     # 답변내용
                    sub_query.c.username.ilike(search)      # 답변작성자
                    )
    total = question_list.distinct().count()
    question_list = question_list.order_by(Question.create_date.desc())\
        .offset(skip).limit(limit).distinct().all()

    return total, question_list

# def get_so_question_list(db: Session, username: str):
#     question_list = db.query(Question).filter(User.username==username)
#     print(question_list)
#     return question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    question.views += 1
    db.add(question)
    db.commit()

    return question

def create_question(db: Session, question_create: QuestionCreate, user:User):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()


def update_question(db: Session, db_question: Question, question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()

def vote_question(db: Session, db_question: Question, db_user: User):
    db_question.voter.append(db_user)
    db.commit()