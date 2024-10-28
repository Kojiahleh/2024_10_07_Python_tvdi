from pytube import YouTube

def download_youtube_to_mp3(url):
  """
  下載YouTube影片並轉換為MP3格式

  Args:
    url: YouTube影片網址

  Returns:
    None
  """

  try:
    # 建立YouTube物件
    yt = YouTube(url)

    # 取得音訊串流
    audio = yt.streams.filter(only_audio=True).first()

    # 下載音訊，並自動將副檔名改為mp3
    out_file = audio.download(filename=yt.title + ".mp3")

    print(f"下載完成: {out_file}")

  except Exception as e:
    print(f"發生錯誤: {e}")

# 輸入YouTube網址
youtube_url = input("請輸入YouTube影片網址: ")

# 呼叫函數下載影片
download_youtube_to_mp3(youtube_url)


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()