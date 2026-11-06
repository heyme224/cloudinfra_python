#gui/binary01.py

#python 에서2진수 다루기 

num1 =0b1010

result = num1+5
print(result)

num2 = 150
#150의 2진수에 해당하는 문자열이 나온다
result2=bin(num2)
print(result2)

line = "adcde12345"
result3 = line[5:10] #5번 인덱스 이상, 10번 인덱스 미만 인덱스 문자열 얻어내기

result4= result2[2:] #2번 인덱스 이상 문자열 얻어내기
print(f"result3:{result3}")
print(f"result4:{result4}")