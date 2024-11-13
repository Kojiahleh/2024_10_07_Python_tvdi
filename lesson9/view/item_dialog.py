import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
from PIL import Image, ImageTk
import tkintermapview as tkmap

class MyCustomDialog(Dialog):
    def __init__(self,parent,record:list,title=None):
        print(f'傳過來的資料:{record}')
        self.date = record[0]
        self.county = record[1]
        self.sitename = record[2]
        self.aqi = record[3]
        self.pm25 = record[4]
        self.status = record[5]
        self.lat = float(record[6])
        self.lon = float(record[7])
        super().__init__(parent=parent,title=title)

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        ttk.Label(master, text=self.date, font=("Helvetica",24,"bold"), foreground='#724832').pack(pady=10)

        main_frame = ttk.Frame(master,borderwidth=1,relief='groove')
        
        canvas_left = tk.Canvas(main_frame,width=200,height=200,background='#1E88A8')
        
        if self.aqi <= 50:
            path = './images/green-light.png'
            self.aqi_status = '良好'
        elif self.aqi <= 100:
            path = './images/orange-light.png'
            self.aqi_status = '普通'
        else:
            self.aqi_status = '危險'
            path = './images/red-light.png' 

        canvas_left.create_rectangle(10,10,190,190,outline="#FEDFE1",width=2)
        canvas_left.create_text(100, 40, text=f'AQI:{self.aqi_status}', font=("Helvetica",20,"bold"), fill='#FEDFE1')
        aqi_img = Image.open(path)
        self.resize_image = aqi_img.resize((75,75))
        self.aqi_light = ImageTk.PhotoImage(self.resize_image)
        canvas_left.create_image(100, 100, anchor='center', image=self.aqi_light)
        canvas_left.create_text(100, 160, text=f'AQI:{self.aqi}', font=("Helvetica",20,"bold"), fill='#FEDFE1')  
        
        canvas_left.pack(side='left')

        canvas_right = tk.Canvas(main_frame,width=200,height=200,background='#1E88A8')
        
        if self.pm25 <= 15.4:
            path = './images/green-light.png'
            self.pm25_status = '良好'
        elif self.pm25 <= 35.4:
            path = './images/orange-light.png'
            self.pm25_status = '普通'
        else:
            self.pm25_status = '危險'
            path = './images/red-light.png' 

        canvas_right.create_rectangle(10,10,190,190,outline="#FEDFE1",width=2)
        canvas_right.create_text(100, 40, text=f'PM2.5:{self.pm25_status}', font=("Helvetica",20,"bold"), fill='#FEDFE1')
        pm25_img = Image.open(path)
        self.resize_image = pm25_img.resize((75,75))
        self.pm25_light = ImageTk.PhotoImage(self.resize_image)
        canvas_right.create_image(100, 100, anchor='center', image=self.pm25_light)   
        canvas_right.create_text(100, 160, text=f'PM2.5:{self.pm25}', font=("Helvetica",20,"bold"), fill='#FEDFE1')   
        
        canvas_right.pack(side='right')

        main_frame.pack(expand=True,fill='x')

        map_frame = ttk.Frame(master)
        map_widget = tkmap.TkinterMapView(map_frame, width=400, height=400, corner_radius=0)
        map_widget.set_position(self.lat, self.lon,marker=True) #台北市位置
        map_widget.set_zoom(15) #設定顯示大小
        map_widget.pack()
        map_frame.pack(padx=10,pady=10)

    def apply(self):
        # 當用戶按下確定時處理數據
        print("使用者按了apply")

    def buttonbox(self):
        # Add custom buttons (overriding the default buttonbox)
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self,event=None):
        print("使用者按了ok")
        super().ok()

    def cancel(self,event=None):
        print("使用者按下cancel")
        super().cancel()    