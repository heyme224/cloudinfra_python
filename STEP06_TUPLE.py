# Tuple (튜플)

'''
0. 튜플은 변경할 수 없는 리스트입니다.
1. list type과 유사
2. 읽기 전용
3. 기능이 적기 때문에 처리 속도가 빠름

만드는법
    ()로 감싸서 만들거나, ,(콤마)로 구분하여 만들 수 있다.
    ()로 감싸지 않아도 ,(콤마)로 구분하면 튜플로 인식한다.
    (v1, v2, v3)
'''

#"one", "two", "three"라는 3개의 str type 데이터를 갖는 튜플 생성
#그 객체의 참조값을 tuple type tuple1에 대입

tuple1: tuple = ("one", "two", "three")

result = tuple1[0] #tuple1의 0번째 index에 있는 데이터를 result에 대입
result2 = tuple1[1] #tuple1의 1번째 index에 있는 데이터를 result2에 대입
result3 = tuple1[2] #tuple1의 2번째 index에 있는 데이터를 result3에 대입

tuple2 = 1, 2, 3 #()로 감싸지 않아도 ,(콤마)로 구분하면 튜플로 인식한다.
tuple3=("김구라",)

a,b,c=tuple2 #tuple2에 있는 데이터를 각각 a,b,c에 대입

first ="girl"
second="boy"

first, second = second, first #변수의 값을 서로 바꾸는 방법

print("종료")