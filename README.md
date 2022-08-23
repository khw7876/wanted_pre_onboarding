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
