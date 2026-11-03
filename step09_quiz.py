
'''
비밀번호를 입력받아서 입력한 비밀번호가 8자 이상이면 '사용가능한 비밀번호입니다'
'''

input_password: str = input("비밀번호 입력:")

if len(input_password) >= 8:
    print("사용가능한 비밀번호입니다")
else:
    print("사용할 수 없는 비밀번호입니다")