#step14_fil.py


import os

if __name__ =="__main__":
    #새로운 파일을 만들어서 문자열 파일에 출력하기
    letter:str = input("문자열 입력")
    letter_path = os.path.join(os.getcwd(),"letter.txt")

    #w 는 없으면 새로 만들고 write , 있으면 기존 내용을 덮어쓰기
    with open(letter_path, "w", encoding="utf-8")as f:
        f.write(letter+"\n")
    print(f"{letter_path} 파일에 저장이 완료되었습니다!")
       # f.write("Hello \n")
       # f.write("Bye \n")
    