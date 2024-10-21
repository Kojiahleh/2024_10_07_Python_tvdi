from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        #style==================================================
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #end style==============================================

        #topFrame=============================================================
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='個人資訊輸入:',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        #end topFrame=========================================================

        #bottomFrame================================================
        bottomFrame = ttk.Frame(self)
        ttk.Label(bottomFrame,text='UserName:').grid(column=0,row=0)
        ttk.Label(bottomFrame,text='Password:').grid(column=0,row=1)
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20))
        #end bottomFrame============================================

def main():
    window = Window(theme='radiance')
    window.mainloop()

if __name__ == '__main__':
    main()