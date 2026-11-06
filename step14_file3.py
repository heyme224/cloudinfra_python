#step14_file3.py

import os

if __name__ =="__main__":
    #파일의 
    file_path =os.path.join(os.getcwd(),"user_input.txt")

    with open(file_path, "r",encoding="utf-8") as f :
        content= f.read()

    print("---저장된 내용---")
    print(content)