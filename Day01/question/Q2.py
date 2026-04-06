'''
🔥 문제 2
scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

👉 짝수 값만 더하는 함수 작성하라

📌 조건
함수 이름: sum_even_scores
return으로 결과 반환
조건문 반드시 사용

'''

def sum_even_scores(dict) -> int :
    sum = 0
    for values in dict.values() :
        if values%2 == 0 :
            sum += values    
    return sum


scores = {
    "a": 10,
    "b": 21,
    "c": 30
}
  
print(sum_even_scores(scores))

'''
리팩토링 ver
def sum_even_scores(scores: dict[str, int]) -> int:
    total = 0

    for value in scores.values():
        if value % 2 == 0:
            total += value

    return total
'''