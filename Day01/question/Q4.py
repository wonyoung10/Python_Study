'''
🔥 문제 4
scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

👉 아래 형태로 출력하는 함수 작성

a : 10
b : 21
c : 30
📌 조건
함수 이름: print_scores
print() 사용
items() 사용

'''

def print_scores(sc:dict[str,int]) -> None :
    for key,   val in sc.items() :
        print(f"{key} : {val}")

scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

print_scores(scores)