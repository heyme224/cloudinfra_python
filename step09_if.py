'''
임의의 숫자를 입력 받아서 입력수가 양수이면 양수입니다, 짝수이면 짝수입니다, 음수면 음수입니다를 얻어내는 프로그램을 만들어 보세요
'''

input_num: int=int(input("숫자 입력:"))
if input_num > 0:
    if input_num % 2 == 0:
        print("양수이면서 짝수입니다")
    else:
        print("양수이면서 홀수입니다")
elif input_num < 0:
    if input_num % 2 == 0:
        print("음수이면서 짝수입니다")
    else:
        print("음수이면서 홀수입니다")   

else:
    print("숫자가 아닙니다")