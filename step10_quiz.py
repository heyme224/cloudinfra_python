#step10_quiz.py



'''
data 리스트에 담긴 문자열을 이용해서 아래와 같은 결과를 얻어내는 jinja2 템플릿을 작성하세요
<ul>
    <li>red<li>
    <li>green<li>
    <li>blue<li>
    
</ul>
'''

from jinja2 import Template

my_template = '''

<ul>
{% for item in nums %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

'''

data=["red", "green", "blue"]

c1 :Template =Template(my_template)
result:str = c1.render(nums=data)
print(result)


data2 = ["주뎅이","덩어리","개다리"]
result2:str = c1.render(nums=data2)
print(result2)
