# WeSki
## 프로젝트 자료

### 핵심 기능

<aside>
☃️ Places App

</aside>

![weski_main_01.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67878bd7-9816-487a-bc3e-d87ceaedd008/weski_main_01.png)

![weski_main_02.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1bd75e69-74b8-49b4-a070-a8195dbc3604/weski_main_02.png)

- 스키장 정보 : 그리드 시스템과 카드를 사용하여 Event와 Package를 나열했습니다. 그리고 {% static 'css/ski.mp4 %}를 추가하여 스키영상을 index 페이지에 렌더링했습니다.
- 스키장 정보 CRUD : 스키장의 상호명, 주소, 설명, 사진 등을 작성하고 작성한 글을 읽을 수 있습니다. 그리고 글을 수정하고 삭제할 수 있는 기능을 추가했습니다.
- 스키장 위치 카카오map 연동 : 스키장에 대한 다양한 정보와 스키장의 위치정보 확인이 가능한 카카오 map 기능을 사용했습니다.

<aside>
☃️ Reviews App

</aside>

![weski_review.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a1b5312-c493-4c1f-96eb-f09d9d87e3d6/weski_review.png)

- 스키장 리뷰 카테고리 : 작성한 리뷰 목록을 렌더링했습니다.
- 후기 CRUD : 리뷰 제목, 본문, 별점, 스키장에 대하여 작성하고 작성한 후기를 읽을 수 있습니다. 또한, 후기를 수정하고 삭제할 수 있는 기능을 구현했습니다. 또한 다중 이미지를 업로드 할 수 있도록 했습니다.
- 후기 ‘좋아요’ 기능 : 작성한 후기에 좋아요 기능을 추가했습니다.

<aside>
☃️ Accounts App

</aside>

![weski_signup_for.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/39041ecb-d1b9-4319-920f-f26a6a1d1450/weski_signup_for.png)

![마이위스키.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1f8c068-d072-4773-8f9d-4c152a79f512/%EB%A7%88%EC%9D%B4%EC%9C%84%EC%8A%A4%ED%82%A4.png)

- 회원 가입 : SignupForm을 통해 회원의 이름, 이메일, 비밀번호, 프로필 사진을 입력하면 가입할 수 있는 기능을 구현했습니다.
- 로그인 : AuthenticationForm을 사용하여 사용자 이름과 비밀번호를 입력하면 로그인하고 로그아웃할 수 있는 기능을 추가했습니다.
- 마이페이지 : 특정 사용자의 프로필 이미지, 아이디, 이메일을 확인하고 리뷰내역을 화면에 렌더링하였습니다.
- 회원정보 수정 : ChangeUserForm을 통해 특정 사용자의 아이디와 이메일을 수정할 수 있는 기능입니다.
- 회원 탈퇴 : 특정 고객이 탈퇴할 수 있는 기능을 구현했습니다.

추가 기능 

- 실시간 채팅상담: 고객 문의를 실시간으로 받을 수 있는 채팅 상담 기능을 메인 페이지에 렌더링했습니다.

## 프로젝트 후기

☃️ 김민찬

자연스럽고 화려한 프론트엔드를 꿈꿨지만 뜻대로 안 돼서 아쉬웠습니다. (carousel에 영상이나 hover 기능 등) 그리고 팀원분들이 적극적으로 해주셔서 정말 감사했습니다.

☃️ 이동영 

계획한대로 잘 진행 되었습니다. 테스트 코드까지 짜보려고 했는데 시간이 부족했습니다.

☃️ 최정아 

Accounts 앱을 구현하면서 풀스택의 다양한 방법을 배워서 적용했는데 기획 의도에 맞는 결과물을 표현할 수 있었습니다. 최종 프로젝트 마지막까지 개발의 완성도를 높여주신 팀원분들께 감사하고 모두 수고하셨습니다.

☃️ 강문주 

반응형 수정이 처음이라 힘들었습니다. css midia 사이즈를 통해서 반응형 수정을 하였는데, 안되는부분 정아님 조언대로 grid를 사용해서 문제를 잘 해결할 수 있었습니다. 문제나 요구사항이 있을때 도움을 주신 동영님 강섭님 준영님 덕분에 문제를 효율적으로 처리할 수 있었습니다.

☃️ 전준영 

다중 이미지 처리가 어려웠습니다. DRF 를 이용한 다중이미지 업로드 구현 대신 모델을 수정해서 구현해서 아쉬웠습니다.

☃️ 송강섭 

이쁘게 꾸미고 싶었는데 창작의 고통이 너무 힘들었습니다. 결제, 예약 같은 서비스를 구현하지 못해서 아쉽습니다.
