#step10_quiz.py
from jinja2 import Template

posts:list = [
    {"id":1, "writer":"작성자1", "title":"제목1"},
    {"id":2, "writer":"작성자2", "title":"제목2"},
    {"id":3, "writer":"작성자3", "title":"제목3"}
]

'''
    위의 posts에 담긴 데이터를 이용해서 아래와 같이 출력되도록 해보세요

글목록 입니다
 - 글번호: 1 작성자: 작성자1 제목: 제목1
 - 글번호: 1 작성자: 작성자1 제목: 제목1
 - 글번호: 1 작성자: 작성자1 제목: 제목1
 '''

sample ='''
글목록 입니다
{%- for item in posts %}
 - 글번호: {{item.id}} 작성자: {{item.writer}} 제목{{item.title}}
 {%-endfor%}
'''

t:Template = Template(sample)
result:str = t.render(posts=posts)
print(result)
