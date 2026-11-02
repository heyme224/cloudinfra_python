#List type에 대해 알아보기

nums = [10, 20, 30, 40, 50 ]
names = ["kim", "lee", "park", "oh","jo", "choi"]

#list에 들어 있는 데이터를 앞에서부터 순서대로 참조하면서 어떤 동작을 할 일이 많다
#nums에 저장되어 있는 데이터를 순서대로 참조하면서 콘솔창에 출력하기

for item in nums:
    print(item)

for item in names:
    print(item)


r1=range(10) # 0~9까지의 숫자를 만들어서 반환해주는 함수
r2=range(1, 11) # 1~10까지의 숫자를 만들어서 반환해주는 함수

print(r1)
print(r2)

print(list(range(5)))

for item in r1:
    print(item)

for item in range(len(names)):
    print(names[item])

for idx in range(1, len(names) + 1):
    print(f"{idx}번째 이름: {names[idx-1]}")