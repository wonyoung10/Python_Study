'''
🧠 문제 1
scores = {
    "a": 10,
    "b": 20,
    "c": 30
}

👉 딕셔너리의 모든 값의 합을 구하는 코드를 작성하라.

📌 규칙
함수로 작성해라
함수 이름: sum_scores
반환값 있어야 함 (return)
출력 말고 return으로 값 반환
'''

def sum_scores(a) -> int:
    num = 0
    for i in a.values() :
        num += i
    return num

scores = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(sum_scores(scores))
'''
수정 ver
def sum_scores(a) -> int:
    num = 0
    for i in a.values() :
        num += i
    return num

scores = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(sum_scores(scores))  

'''