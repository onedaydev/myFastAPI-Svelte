# myFastAPI-Web

이 프로젝트는 [점프 투 FastAPI](https://wikidocs.net/book/8531)를 바탕으로 만들었으며,
[저자 추천 과제](https://wikidocs.net/177232)를 진행하기 위해 만들어졌습니다.
<br/>
<br/>
# 명세
| API 명| URL| 요청방법| 설명 | 기타 |
|---|---|---|---|---|
|질문 목록|/|GET||페이징, 답변 갯수 표시|
|질문 상세 조회|/api/question/detail/{question_id}|GET|||
|답변 등록|/api/answer/create/{question_id}|POST|||
|질문 등록|/api/question/create|POST|||
||||||

