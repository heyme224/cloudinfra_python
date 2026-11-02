

"""
function type
- 특정시점에 여러줄의 code를 일괄 실행하고자 할때 사용한다
- 함수도 data이다(변수에 담을 수 있다)
- 함수 안에 저장된 code를 일괄실행 하는 것을 함수를 call이라고 한다.
- 함수는 저장된 code를 다 실행하고 나면 원래 call했던 위치로 실행의 흐름이 넘어온다
- call 했던 위치로 돌아오면서 어떤  data를 반드시 가져온다

"""

def test1():
    print("test1() 함수가 호출됨")

test1() #함수 호출
reult = test1() #함수 호출

print(reult) #함수 호출 후 return 값이 없으므로 None 출력

#매개변수가 선언되어 있는 함수
#매개변수에 의해 대입할 값을 전달해야지 호출 할 수 있다
#매개변수의 이름은 마음대로 지을 수 있다
def test2(arg):
    print("전달 받은 내용:", arg)
    print(f"전달 받은 내용: {arg}")
test2(None) #None 전달
test2("Hello") #Hello 전달
test2(2) #2 전달

def print_sum(a,b):
    sum=a+b
    print(f"{a} + {b} = {sum}")
    print(f"{a} + {b} = {a+b}")

print_sum(5, 3)
print_sum(10, 20)

def print_info(name:str, addr:str):
    print(f"이름: {name}, 주소: {addr}")

print_info("Alice","서울시")
print_info(addr="부산시", name="Bob") #매개변수의 순서가 바뀌면 의도한대로 출력되지 않지만 힌트를 줬으니 제대로 출력

def get_sum(a:int, b:int) -> int:
    return a+b

result = get_sum(5, 3)
print(f"5 + 3 = {result}")

print("종료")