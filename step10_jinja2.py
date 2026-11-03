

'''
template 문자열을 정의하고 어떤 데이터를 template 문자열에 전달해서 
결과 문자열을 얻어내는 작업을 jinja2를 이용해서 수행할 수 있습니다.

python 가상환경 활성화 한 다음 설치 후에 사용해야 한다

pip install jinja2

'''
#테스트용 템플릿

#pip로 설치한 jinja2 로부터 Template 클래스를 import
from jinja2 import Template


my_template = '''
    번호 : {{ number }}
    이름 : {{ name }}
    주소 : {{ addr }}
'''

#template에 출력 할 데이터라고 가정하자
mem1 = {"number": 1,"name": "홍길동", "addr": "서울시 강남구"}
mem2 = {"number": 2,"name": "김철수", "addr": "서울시 강서구"}

#import 한 클래스를 이용해서 객체를 생성하고 template 문자열을 전달한다

t1:Template = Template(my_template)
result1:str = t1.render(mem1)
print(result1)

t2:Template = Template(my_template)
result2:str = t2.render(mem2)
print(result2)