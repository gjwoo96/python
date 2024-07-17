# 가상환경 생성 
# pthron -m venv 가상환경이름

# 가상환경 실행
# source ./가상환경폴더/bin/activate

# 가상환경 종료
deactivate

# vscode설정
# Python:Select Interpreter 클릭후 가상환경 선택

# sqlite3 version확인
- 가상환경 실행후 python > import sqlite3 > sqlite3.sqlite_version

# sqlite3 version에러
- sqlite3 버전이 낮아서 최신버전으로 설치후 새로운 가상환경 생성후 테스트 진행중