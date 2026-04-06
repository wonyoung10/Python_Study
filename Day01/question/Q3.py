'''
🔥 문제 3 (난이도 ↑)
scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

👉 가장 큰 값을 반환하는 함수 작성

📌 조건
함수 이름: get_max_score
max() 함수 사용 금지
직접 구현
return 필수
'''
def get_max_score(sc : dict[str,int]) -> int :
    max_value = 0
    for i in sc.values():
        if max_value < i :
            max_value = i
    return max_value 

scores = {
    "a": 10, 
    "b": 21,
    "c": 30
}

print(get_max_score(scores))

'''
리팩토링 ver

def get_max_score(sc : dict[str,int]) -> int :
    max_value = None
    for i in sc.values():
        if max_value is None or max_value < i :
            max_value = i
    return max_value

scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

print(get_max_score(scores))

'''