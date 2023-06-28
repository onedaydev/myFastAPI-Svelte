from database import SessionLocal
from models import Question
from datetime import datetime


db = SessionLocal()

cnt = 300

for i in range(cnt):
    q = Question(subject=f'test data:{i}', content='None', create_date=datetime.now())
    db.add(q)
db.commit()
