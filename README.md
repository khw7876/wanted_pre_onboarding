# Wanted 선발과제

## 코드 컨벤션
- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)


## 1번문제
> ![image](https://user-images.githubusercontent.com/101394490/186111817-77e94fe0-195a-4f24-b58c-e5bf625e3cfd.png)<br><br>
> ### 요구사항:<br>
>필요한 모델을 구성하고 알맞은 데이터를 담아주어서 정상적으로 데이터 저장이 이루어지도록 함<br>
> ### 구현과정: <br>
> 1. 저장을 하기위한 모델들을 생성
> 2. 1번에서 생성한 모델을 바탕으로 serializer 생성
> 3. views.py에서 데이터 저장을 위해 post 메소드사용. serializer를 통하여 데이터 저장 구현
> 4. views.py에서 API와 관련이 없는 service단위 분리
> 5. TDD방식을 위하여 service와 API에 대한 Test구현 및 views.py Error 핸들링
<hr>

## 2번문제
> ![image](https://user-images.githubusercontent.com/101394490/186183174-0748abe6-5696-4334-a138-59b7be53d4de.png)
> ### 요구사항:<br>
>1번문제에서 생성한 데이터를 수정이 되도록 구현. (모든 데이터가 들어가지 않아도 수정이 되어야함)<br>
> ### 구현과정: <br>
> 1. views.py에 put메소드 구현
> 2. 필요한 service 분리 작성(partial = true를 통해 하나의 필드도 수정이 되도록 구현)
> 3. 해당 service에서 발생 가능한 Error를 Test코드로 검증
> 4. 3번에서 검증한 Error를 Views.py에서 핸들링
> 5. API test에서 4번의 핸들링 검증
<hr>

## 3번문제
> ![image](https://user-images.githubusercontent.com/101394490/186184928-98d465df-94a2-407b-90b6-7240875558db.png)
> ### 요구사항:<br>
>1번문제에서 생성한 데이터를 삭제가 되도록 구현. <br>
> ### 구현과정: <br>
> 1. views.py에 delete 메소드 구현
> 2. 필요한 service 분리작성
> 3. 해당 service에서 발생 가능한 Error를 Test코드로 검증
> 4. 3번에서 검증한 Error를 Views.py에서 핸들링
> 5. API test에서 4번의 핸들링 검증
<hr>

## 4-1번문제
> ![image](https://user-images.githubusercontent.com/101394490/186343464-1ad73937-e1d1-4a28-a71e-615d6350e4f6.png)
> ### 요구사항:<br>
>생성하거나 수정한 데이터볼 수 있도록 구현 <br>
> ### 구현과정: <br>
> 1. views.py에 get 메소드 구현
> 2. 필요한 service 분리작성
> 3. serializer 커스텀 작성
> 4. CaptureQueriesContext를 통한 쿼리수 파악
> 5. selected_related를 통해 쿼리수 최소화 (4 < 1)
> 6. 정상적인 상황에 맞춘 테스트코드 작성
<hr>


## 4-2번문제
> ![image](https://user-images.githubusercontent.com/101394490/186352441-5581d94d-7a1f-40b6-b805-17a36376e280.png)
> ### 요구사항:<br>
>생성된 데이터들에 특정 단어를 포함하는 데이터들을 검색하는 기능을 구현 <br>
> ### 구현과정: <br>
> 1. views.py에 검색기능을 담당하는 새로운 View 구현
> 2. get 메소드를 통하여 기능 구현
> 3. 필요한 service 분리작성
> 4. query_params를 통하여 검색할 단어 받아오기
> 5. contains를 통하여 특정 단어를 포함한 query_set들 반환
> 6. query_set들을 |(백슬래쉬)를 이용하여 5번의 query_set들을 병합
<hr>

## 5번문제
> ![image](https://user-images.githubusercontent.com/101394490/186374214-9865f577-2874-4c09-bb12-d9d406ea5455.png)
> ### 요구사항:<br>
>4번 문제에서 get하는 데이터에 추가적으로 같은 회사가 공고하는 job_post의 id들을 리스트로 반환하라 <br>
> ### 구현과정: <br>
> 1. views.py에 상세페이지를 담당하는 새로운 View 구현
> 2. 새로운 serializer를 생성하여 기존의 데이터에 추가로 method_field를 통하여 리스트 반환
> 3. get 메소드를 통하여 기능 구현
> 4. 필요한 service 분리작성
> 5. 같은 회사공고에서 자기 자신의 값 제거
<hr>

## 6번문제
> ![image](https://user-images.githubusercontent.com/101394490/186374149-96b3e9ac-3d0e-4441-8136-803754ce256c.png)
> ### 요구사항:<br>
>새로운 모델과 serializer를 사용하여 user가 해당 job_post에 지원하는 view생성. 단, 중복지원 불가br>
> ### 구현과정: <br>
> 1. 지원을 담당하는 새로운 model 생성
> 2. 새로운 모델에 맞추어 makemigrations 및 migrate 적용
> 3. 1번에서 생성한 모델에 맞추어 serializer를 생성
> 4. 1,3번에 만들어놓은 모델과 serializer에 맞추어서 post메소드 구현
> 5. 저장이 되었다면, 1번 모델에서 job_post를 기준으로 User 탐색
> 6. 이미 존재한다면 Return 400 Error를 반환
<hr>
