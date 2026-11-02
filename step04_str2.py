#json 형식의 문자열을 작성하고 python에서 활용해보자

#import 해야지만 사용할 수 있는 모듈
import json


info='''
{
    "name": "Alice",
    "addr": "노량진",
    "city": ["New York", "Seoul"]
}

'''

result =json.loads(info) #json 형식의 문자열을 python dict type 으로 변환

print(result["name"])
print(result["addr"])
print(result["city"])
print(result["city"][0])
print(result["city"][1])

result2 = json.dumps(result) #python dict type 을 json 형식의 문자열로 변환

print("종료합니다")