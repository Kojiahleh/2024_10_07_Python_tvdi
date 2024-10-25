from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('按鈕123456789101112')

        #style==================================================
        style = ttk.Style(self)
        style.configure('bottom.TFrame', background='lightgreen')
        #end style==============================================

        #topFrame=======================================================
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        btn1 = ttk.Button(topFrame,text='左上')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='中上')
        btn2.pack(side='left',expand=True,fill='x')
        btn3 = ttk.Button(topFrame,text='右上')
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        topFrame.pack(padx=10,pady=(10,0),ipady=10,fill='x')
        #end topFrame===================================================

        #bottomFrame=====================================================================
        bottomFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        
        #leftFrame============================================================================
        leftFrame = ttk.Frame(bottomFrame,borderwidth=1,relief='groove',style='bottom.TFrame')
        btn4 = ttk.Button(leftFrame,text='下左上')
        btn4.pack(expand=True,fill='both',padx=5,pady=5,ipady=25)
        btn5 = ttk.Button(leftFrame,text='下左中')
        btn5.pack(expand=True,fill='both',padx=5,ipady=10)
        btn6 = ttk.Button(leftFrame,text='下左下')
        btn6.pack(expand=True,fill='both',padx=5,pady=5,ipady=10)
        leftFrame.pack(side='left',padx=10,pady=10,expand=True,fill='both')
        #end leftFrame========================================================================

        #centerFrame============================================================================
        centerFrame = ttk.Frame(bottomFrame,borderwidth=1,relief='groove',style='bottom.TFrame')
        btn7 = ttk.Button(centerFrame,text='下中上')
        btn7.pack(expand=True,fill='both',padx=5,pady=5,ipady=20)
        btn8 = ttk.Button(centerFrame,text='下中中')
        btn8.pack(expand=True,fill='both',padx=5,ipady=5)
        btn9 = ttk.Button(centerFrame,text='下中下')
        btn9.pack(expand=True,fill='both',padx=5,pady=5,ipady=20)
        centerFrame.pack(side='left',pady=10,expand=True,fill='both')
        #end centerFrame========================================================================

        #rightFrame============================================================================
        rightFrame = ttk.Frame(bottomFrame,borderwidth=1,relief='groove',style='bottom.TFrame')
        btn10 = ttk.Button(rightFrame,text='下右上')
        btn10.pack(expand=True,fill='both',padx=5,pady=5)
        btn11 = ttk.Button(rightFrame,text='下右中')
        btn11.pack(expand=True,fill='both',padx=5)
        btn12 = ttk.Button(rightFrame,text='下右下')
        btn12.pack(expand=True,fill='both',padx=5,pady=5)
        rightFrame.pack(side='left',padx=10,pady=10,expand=True,fill='both')
        #end rightFrame========================================================================

        bottomFrame.pack(padx=10,pady=10,expand=True,fill='both')
        #endbottomFrame==================================================================

def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()