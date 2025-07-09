import tkinter as tk
from function_py25 import get_name
from function_py25 import update_name
from function_py25 import update_mail
from function_py25 import send_mail
from tkinter import messagebox
from account_check import AccountCheck
import random



class Account(tk.Frame):
  def __init__(self, master, mail, root):
    super().__init__(master, width=400, height=400)
    self.pack()
    self.master = master
    
    self.root = root
    self.mail = mail
    master.geometry('400x400')
    master.title('アカウント画面')

    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # ウィンドウの縦横幅を入手
      self.master.update_idletasks()
      self.width = self.master.winfo_width()
      self.height = self.master.winfo_height()
    # 生成 
      self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20), )
      self.name = get_name(self.mail)[0]
      self.name_entry = tk.Entry(self, width=30)
      self.mail_entry = tk.Entry(self, width=30)
      self.name_entry.insert(0, self.name)
      self.mail_entry.insert(0, self.mail)
      self.name_label = tk.Label(self, text='名前：')
      self.mail_label = tk.Label(self, text='メール：')
      self.name_btn = tk.Button(self, text='名前を保存する', command=self.update_name_event)
      self.mail_btn = tk.Button(self, text='メールアドレスを保存する', command=self.update_mail_event)

    # 配置
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.name_entry.place(x=self.width/2 - 80, y=160)
      self.mail_entry.place(x=self.width/2 - 80, y=190)
      self.name_label.place(x=self.width/2 - 120, y=160)
      self.mail_label.place(x=self.width/2 - 122, y=190)
      self.name_btn.place(x=self.width/2 - 100, y=250)
      self.mail_btn.place(x=self.width/2, y=250)
      
  def update_name_event(self):
       n = self.name_entry.get()
       self.master.wm_attributes("-topmost", 1)
       ask = messagebox.askyesno('アカウント画面', f'名前を{n}に変更します。')
       self.master.wm_attributes("-topmost", 0)  # 設定を戻す
       if ask:
           update_name(n, self.mail)

  def update_mail_event(self):
       m = self.mail_entry.get()
       self.OTP = ''
       self.master.wm_attributes("-topmost", 1)
       ask = messagebox.askyesno('アカウント画面', f'メールアドレスを{m}に変更します。')
       self.master.wm_attributes("-topmost", 0)  # 設定を戻す
       if ask:
           for i in range(4):
               self.OTP += str(random.randint(0,9) )
           self.destroy()
           AccountCheck(self.master, self.mail, m, self.OTP, self.root)
           send_mail(m, '図書管理アプリ', f'認証画面を開いて5分またはページを閉じると認証権限はなくなります。認証パスワード：{self.OTP}')


# if __name__ == '__main__':
#   root2 = tk.Tk()
#   app2 = Account(root2, "aaa")
#   app2.mainloop()