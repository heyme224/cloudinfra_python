
from jinja2 import Template

info: dict = {
    "num": 1,
    "name": "kim",
    "body": {
        "height": 100,
        "weight": 80
    },
    "hobby": ["피아노", "당구", "프로그래밍"]
}
'''
위의 info 안에 들어있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력하세요

---
번호: 1
이름: kim
키: 180cm
몸무게: 80kg
취미 :
    - 피아노
    - 당구
    - 프로그래밍
---
'''

sample = '''

번호: {{num}}
이름: {{name}}
키: {{body.height}}cm
몸무게: {{body.weight}}kg
취미 :
    {%- for item in hobby%}
    - {{item}}
    {%-endfor%}
  '''

t1:Template=Template(sample)
result:str = t1.render(info)
print(result)