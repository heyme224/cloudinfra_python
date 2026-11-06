#test01.py

# as 별칭 사용 
import tkinter as tk

if __name__ =="__main__":
    #TK 객체 생성해서 참조값을 root에 담기
    root=tk.Tk()
    root.geometry("300X300")
    entry = tk.Entry(root)
    entry.pack(pady=10)

    root.mainloop()