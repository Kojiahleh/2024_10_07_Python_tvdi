import tkinter as tk

class Window(tk.Tk):
    # def __init__(self,screenName=None,baseName=None,className='Tk',useTk=True,sync=False,use=None):
    #     super().__init__(screenName=screenName,baseName=baseName,className=className,useTk=useTk,sync=sync,use=use)
     def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('這是我的第一個視窗')
        self.geometry('800x300')
        messege=tk.Label(self,text='Hello! 這是我的第一個視窗')
        messege.pack()

def main():
    # root = tk.Tk()

    # root = Window()
    # print(type(root))
    # root.title('這是我的第一個視窗')
    # root.geometry('800x300')
    # messege=tk.Label(root,text='Hello! 這是我的第一個視窗')
    # messege.pack()
    # root.mainloop()

    window=Window()
    window.mainloop()

if __name__ == '__main__':
    main()