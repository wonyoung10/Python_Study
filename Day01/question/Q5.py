'''
🔥 문제 5 (마지막 테스트)
scores = {
    "a": 10,
    "b": 21,
    "c": 30
}

👉 평균값을 반환하는 함수 작성

📌 조건
함수 이름: get_average
return으로 값 반환
sum() 함수 사용 금지
0개일 경우 대비해야 함
'''

def get_average(sc:dict[str, int]) -> float :
    val = 0
    n = 0
    for i in sc.values() :
        val += i
        n+=1
    if n == 0 :
        return 0.0
    else :  
        return val/n


scores = {
    "a": 10,
    "b": 21,
    "c": 30
}
s={}
print(get_average(s))