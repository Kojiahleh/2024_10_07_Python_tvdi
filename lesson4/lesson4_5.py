from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('使用ttk的套件')
        self.geometry('400x300')
        style = ttk.Style(self)
     
        style.configure('Main.TButton',font=('Helvetica',15))
        btn1 = ttk.Button(self,text='Button Demo',style='Main.TButton')
        btn1.pack(padx=10,pady=10,ipadx=10,ipady=10)

def main():
    window = Window(theme='radiance')
    window.mainloop()

if __name__ == '__main__':
    main()