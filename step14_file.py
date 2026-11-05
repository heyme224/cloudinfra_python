#step14_file.py



import os


if __name__ =="__main__":

    #현재 작업 경로 얻어내기
    cwd: str = os.getcwd()

    #현재 운영체제의 파일 구분자 얻어내기(window는 역슬래시 , linux는 슬래시)

    sep: str =os.sep

    print(f"cwd:{cwd}")
    print(f"sep:{sep}")
   
   
    #memo.txt 파일이 위치하는 절대 경로 구성하기
    #.join()운영체제에 맞는 적절한 파일 구분자를 이용해서 두 경로를 합쳐준다

    path: str = os.path.join(os.getcwd(),"memo.txt")
    print(f"path:{path}")

    f=open(path,"r", encoding="utf-8")
    try:
        result = f.read()
    except Exception as e:
        print(e)
    finally:
        f.close()

    print(result)

    with open(path, "r", encoding="utf-8")as f2:
        result2 = f2.read()
        print(result2)
