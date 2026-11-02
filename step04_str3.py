
#yaml 형식의 문자열 작성해보기
#yaml문자열을 다룰떄는 외부 모듈을 pip로 설치해서 import해서 사용해야함
#python 가상환경을 구성하고 pip install pyyaml 설치 후에 yaml을 사용 할수 있음


import yaml


info= '''
name: Alice
addr: 노량진
city:
  - New York
  - Seoul

isMan: true
body:
  weight: 50
  height: 170
'''

result=yaml.safe_load(info) #yaml 형식의 문자열을 python dict type 으로 변환
print(result)

#dict type 의 데이터를 yaml 형식의 문자열로 변환
result2=yaml.dump(result,allow_unicode=True, sort_keys=False) #dict type 의 데이터를 yaml 형식
print(result2)