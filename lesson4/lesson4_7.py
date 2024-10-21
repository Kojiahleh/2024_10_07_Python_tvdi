from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('多層次按鈕視窗')
        style = ttk.Style(self)
        
        # 頂部框架
        topFrame = ttk.Frame(self, relief='groove', borderwidth=2)
        btn1 = ttk.Button(topFrame, text='按鈕1')
        btn1.pack(side='left', padx=5, pady=5, fill='x', expand=True)
        btn2 = ttk.Button(topFrame, text='按鈕2')
        btn2.pack(side='left', padx=5, pady=5, fill='x', expand=True)
        btn3 = ttk.Button(topFrame, text='按鈕3')
        btn3.pack(side='left', padx=5, pady=5, fill='x', expand=True)
        topFrame.pack(pady=10, padx=10, fill='x')
        
        # 底部主框架
        bottomFrame = ttk.Frame(self)
        
        # 左側框架
        leftFrame = ttk.Frame(bottomFrame, relief='groove', borderwidth=2)
        
        # 創建上半部分框架（固定50%高度）
        upperFrame = ttk.Frame(leftFrame)
        btn4 = ttk.Button(upperFrame, text='按鈕4')
        btn4.pack(pady=10, padx=10, fill='both', expand=True)
        upperFrame.pack(fill='both', expand=True)  # expand=True 使其佔50%空間
        
        # 創建下半部分框架（固定50%高度）
        lowerFrame = ttk.Frame(leftFrame)
        # 在下半部分平均分配按鈕5和6
        btn5 = ttk.Button(lowerFrame, text='按鈕5')
        btn5.pack(pady=5, padx=10, fill='both', expand=True)
        btn6 = ttk.Button(lowerFrame, text='按鈕6')
        btn6.pack(pady=5, padx=10, fill='both', expand=True)
        lowerFrame.pack(fill='both', expand=True)  # expand=True 使其佔50%空間
        
        leftFrame.pack(side='left', padx=10, fill='both', expand=True)
        
        # 中間框架
        middleFrame = ttk.Frame(bottomFrame, relief='groove', borderwidth=2)
        
        # 按鈕7佔據較大空間
        btn7 = ttk.Button(middleFrame, text='按鈕7')
        btn7.pack(pady=(10,5), padx=10, fill='both', expand=True)
        
        # 按鈕8為較小按鈕
        btn8 = ttk.Button(middleFrame, text='按鈕8')
        btn8.pack(pady=5, padx=10, fill='x')
        
        # 按鈕9佔據較大空間
        btn9 = ttk.Button(middleFrame, text='按鈕9')
        btn9.pack(pady=(5,10), padx=10, fill='both', expand=True)
        
        middleFrame.pack(side='left', padx=10, fill='both', expand=True)
        
        # 右側框架
        rightFrame = ttk.Frame(bottomFrame, relief='groove', borderwidth=2)
        
        # 按鈕10、11、12平均分配空間
        btn10 = ttk.Button(rightFrame, text='按鈕10')
        btn10.pack(pady=(10,5), padx=10, fill='both', expand=True)
        btn11 = ttk.Button(rightFrame, text='按鈕11')
        btn11.pack(pady=5, padx=10, fill='both', expand=True)
        btn12 = ttk.Button(rightFrame, text='按鈕12')
        btn12.pack(pady=(5,10), padx=10, fill='both', expand=True)
        
        rightFrame.pack(side='left', padx=10, fill='both', expand=True)
        
        bottomFrame.pack(pady=10, padx=10, fill='both', expand=True)

def main():
    window = Window(theme='breeze')  
    window.geometry('800x600')  
    window.mainloop()

if __name__ == '__main__':
    main()