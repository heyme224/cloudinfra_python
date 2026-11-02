#step04_str.py

#양쪽에 공백이 포함되거나 포함 될 가능성이 있는 문자열이 있다고 가정하자
#만일 공백을 제거하고 싶다면?

text = "   Hello, World!   "
#양쪽 공백 제거 
result = text.strip()

mtIp="192.168.0.2"
#.으로 분리하기
result2 = mtIp.split(".")

#join() 함수는 list type 의 데이터를 하나의 문자열로 합쳐주는 함수이다.
#list type 의 데이터를 합칠때 구분자를 지정할수 있다.
result3 = ".".join(result2)
result4 = "python".upper()
result5 = "PYTHON".lower()

