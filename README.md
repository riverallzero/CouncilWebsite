# 2022년도 "응용소프트웨어" 프로젝트 팀

## 역할 분담
- 강다영 | 홈화면, 공지사항, 문의사항, 일정참여
- 이수연 | 학과위치(지도, 검색기능), 학과제휴(지도)
- 최수영 | 학과제휴(인스타그램 게시물), 학생회조직(이미지), 과방관리(블로그형식, 댓글기능까지)

### 처음 코드 다운 시 User 설정(본인꺼 만들기)
```python
python manage.py migrate
python manage.py createsuperuser
```

### 모델 변경시 필수
```python
python manage.py makemigrations
python manage.py migrate
```

### 서버 실행
```python
python manage.py runserver
```
### 개인 작업 시
Branch를 만들어 코드를 수정
- <a href="https://git-fork.com/">Fork</a> 다운로드
- <a href="https://velog.io/@riverallzero/Fork-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0">Fork 사용 방법</a>
- <a href="https://velog.io/@riverallzero/Fork%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Git-Branch-dcebao11">Branch 사용 방법</a>
