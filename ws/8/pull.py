import os, subprocess

current_folder = os.getcwd()

id = input("ID를 입력해주세요: ")
subject = input("과목을 입력해주세요: ")
types = ['ws', 'hw'] # ws: 실습, hw: 과제
set_number = input("차시를 입력해주세요: ")
stages = [1,2,3,4,5,'a','b','c'] # 보충수업 문제 제외하고 싶다면 a,b,c 제거

for type in types:
    for stage in stages:
        URL = f"http://lab.ssafy.com/{id}/{subject}_{type}_{set_number}_{stage}"
        subprocess.run(['git', 'clone', URL])