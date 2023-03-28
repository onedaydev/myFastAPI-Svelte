# myFastAPI-Svelte

이 프로젝트는 [점프 투 FastAPI](https://wikidocs.net/book/8531)를 바탕으로 만들었으며, 추가 기능을 구현하기 위해 만들어졌습니다.

<br/>
<br/>

# API 명세
| API 명| URL| 요청방법| 설명 |
|---|---|---|---|
|Domain: Question|
|질문 목록|/|GET||
|질문 목록|/api/question/list|GET||Paginated 질문 목록 조회
|질문 등록|/api/question/create|POST||
|질문 상세 조회|/api/question/detail/{question_id}|GET||
|질문 수정|/api/question/update|PUT||
|질문 삭제|/api/question/delete|DELETE||
|질문 추천|/api/question/vote|POST||
|특정 유저가 작성한 질문과 답변을 조회|/api/question/soql/{username}|GET||
|Domain: User|
|회원 가입|/api/user/create|POST||
|로그인|/api/user/login|POST||
|비밀번호 변경|/api/user/changepwd/|PUT||
|Domain: Answer|
|답변 등록|/api/answer/create/{question_id}|POST||
|답변 조회|/api/answer/detail/{answer_id}|GET||
|답변 수정|/api/answer/update|PUT||
|답변 삭제|/api/answer/delete|DELETE||
|답변 추천|/api/answer/vote|POST||

<br/>
<br/>

# Done
* ~~댓글 페이징~~(3.8)
* ~~조회 수~~(3.9) - 조회 수 컬럼 생성을 위해 alembic으로 revision 만들고 반영하는 과정에서 default=0, nullable=False 부분은 에러가 생성이 된다. 해결 방법은 [다음](https://medium.com/the-andela-way/alembic-how-to-add-a-non-nullable-field-to-a-populated-table-998554003134)과 같다. 필자는 db browser에서 직접 column을 생성했다.
* ~~프로필~~(3.10)
* ~~비밀번호 변경~~(3.14)
* ~~회원 탈퇴~~(3.16)

<br/>
<br/>

# Requirements
- python 3.11.2
- node.js 18.15.0

# How to Run

## DB setting
```

```

## Web Build
```

```

Optional : secrets copy.json에 ```openssl rand -hex 32``` 또는 ```import secrests;secrets.token_hex(32)```명령어로 생성한 Secret key 값을 대입

```
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```

<br/>
<br/>

## QnA : https://pybo.kr
