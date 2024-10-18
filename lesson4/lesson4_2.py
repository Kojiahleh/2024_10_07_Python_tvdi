import tkinter as tk

def main():
    root = tk.Tk()
    print(type(root))
    root.title('這是我的第一個視窗')
    root.geometry('800x300')
    messege=tk.Label(root,text='Hello! 這是我的第一個視窗')
    messege.pack()
    root.mainloop()

if __name__ == '__main__':
    main()