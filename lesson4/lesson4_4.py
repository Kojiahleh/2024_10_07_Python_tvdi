import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('使用ttk的套件')
        self.geometry('400x300')
        style = ttk.Style(self)
        '''
        style.configure('TLabel',font=('Helvetica',11)) #修改現有的
        style.configure('Title.TLabel',font=('Helvetica',15),background='lightblue',foreground='darkgreen') #自訂的style

        # messege = ttk.Label(self,text='使用ttk的Label')
        messege = ttk.Label(self,text='使用ttk的Label',style='Title.TLabel') #使用自訂的
        print(messege.winfo_class())
        messege.pack()
        '''
        style.configure('Main.TButton',font=('Ariel',15))
        btn1 = ttk.Button(self,text='Button Demo')
        btn1.pack(padx=10,pady=10,ipadx=10,ipady=10)

def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()