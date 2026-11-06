#test02.py

# as 별칭 사용 
import tkinter as tk

if __name__ =="__main__":
    #root 창 생성
    root=tk.Tk()
    #제목 설정
    root.title("나의 App")
    #창의 크기
    root.geometry("400x200")

    #레이블
    lable = tk.Label(root,text="안녕하세요 gui임")
    #pady => padding y => y 축 padding => 위아래 padding
    lable.pack(pady=20)

    #입력창
    name_entry=tk.Entry(root,font=("Arial",12))
    name_entry.pack(pady=5)
    name_entry.focus() #포커스 주기

    lable2 = tk.Label(root,text="결과:")
        #pady => padding y => y 축 padding => 위아래 padding
    lable2.pack(pady=20)

    def clicked():
        name=name_entry.get()
        print("적은 값:",name)
        lable2.config(text=f"입력한 이름:{name}")

    #버튼
    btn = tk.Button(root,text="전송", width=10, bg="lightgray",command=clicked)
    btn.pack(pady=15)



    root.mainloop()