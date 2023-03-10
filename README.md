# myFastAPI-Web

이 프로젝트는 [점프 투 FastAPI](https://wikidocs.net/book/8531)를 바탕으로 만들었으며,
[저자 추천 과제](https://wikidocs.net/177232)를 진행하기 위해 만들어졌습니다.

<br/>
<br/>
<br/>

# API 명세
| API 명| URL| 요청방법| 설명 | 기타 |
|---|---|---|---|---|
|질문 목록|/|GET||페이징, 답변 갯수 표시|
|질문 목록|/api/question/list|GET||Paginated 질문 목록 조회|
|질문 등록|/api/question/create|POST|||
|질문 상세 조회|/api/question/detail/{question_id}|GET|||
|질문 수정|/api/question/update|PUT|||
|질문 삭제|/api/question/delete|DELETE|||
|질문 추천|/api/question/vote|POST|||
||||||
|회원 가입|/api/user/create|POST|||
|로그인|/api/user/login|POST|||
||||||
|답변 등록|/api/answer/create/{question_id}|POST|||
|답변 조회|/api/answer/detail/{answer_id}|GET|||
|답변 수정|/api/answer/update|PUT|||
|답변 삭제|/api/answer/delete|DELETE|||
|답변 추천|/api/answer/vote|POST|||

<br/>
<br/>
<br/>

# ToDo(Recommended)
* ~~댓글 페이징~~(3.8)
* 질문 또는 답변에 댓글을 달 수 있는 기능
* 카테고리
* 비밀번호 찾기와 변경
* ~~프로필~~(3.10)
* 최근 답변과 최근 댓글 
* ~~조회 수~~(3.9) - 조회 수 컬럼 생성을 위해 alembic으로 revision 만들고 반영하는 과정에서 default=0, nullable=False 부분은 에러가 생성이 된다. 해결 방법은 [다음](https://medium.com/the-andela-way/alembic-how-to-add-a-non-nullable-field-to-a-populated-table-998554003134)과 같다. 필자는 db browser에서 직접 column을 생성했다.
* 소셜 로그인
* 마크다운 에디터([simplemde](simplemde.com) 추천)

QnA : [pybo](https://pybo.kr)