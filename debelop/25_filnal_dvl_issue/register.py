import tkinter as tk
from function_py25 import insert_user
from function_py25 import get_account_by_id
from function_py25 import get_account_by_mail
from function_py25 import send_mail
from tkinter import messagebox
import random
from register_check import RegisterCheck


class Register(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack(fill=tk.BOTH, expand=True)
    self.master = master
    master.state('zoomed')

    master.geometry('400x400')
    master.title('新規登録画面')

    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # ウィンドウの縦横幅を入手
      self.master.update_idletasks()
      self.width = self.master.winfo_width()
      self.height = self.master.winfo_height()
    # 生成
      self.name_label = tk.Label(self, text='Name：')
      self.pw_label = tk.Label(self, text='PW：')
      self.mail_label = tk.Label(self, text='Mail：')
      self.auth_label = tk.Label(self, text='権限：')
      self.pw_entry = tk.Entry(self, show='*')
      self.name_entry = tk.Entry(self)
      self.mail_entry = tk.Entry(self)
      self.radio_status = tk.IntVar(value=-1)
      self.radio1 = tk.Radiobutton(self, text='管理者', variable=self.radio_status, value=0)
      self.radio2 = tk.Radiobutton(self, text='ユーザー', variable=self.radio_status, value=1)
      self.warning_label = tk.Label(self, text='')
      self.back_btn = tk.Button(self, text='戻る', command=self.back_event)
      self.register_btn = tk.Button(self, text='仮登録', command=self.register_event)
      self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20), )
      self.OTP = ''
      
    # 配置
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.name_label.place(x=self.width / 2 - 123, y=160)
      self.name_entry.place(x=self.width / 2 - 70, y=160)    
      self.pw_label.place(x=self.width / 2 - 110, y=190)
      self.pw_entry.place(x=self.width / 2 - 70, y=190)    
      self.mail_label.place(x=self.width / 2 - 115, y=220)
      self.mail_entry.place(x=self.width / 2 - 70, y=220)
      self.auth_label.place(x=self.width / 2 - 114, y=250)
      self.radio1.place(x=self.width / 2 - 70, y=250)
      self.radio2.place(x=self.width / 2, y=250)
      self.warning_label.place(x=self.width / 2 - 50, y=270)
      self.register_btn.place(x=self.width / 2 + 25, y=290)
      self.back_btn.place(x=self.width / 2 - 15, y=290)
      
  def register_event(self):
    name = self.name_entry.get()
    mail = self.mail_entry.get()
    pw = self.pw_entry.get()
    auth = self.radio_status.get()
    name_flag = False
    mail_flag = False
    pw_flag = False
    auth_flag = False
    if not name:
      self.name_entry.configure(bg='pink')
    else:
      self.name_entry.configure(bg='white')
      name_flag = True

    if not mail:
      self.mail_entry.configure(bg='pink')
    else:
      self.mail_entry.configure(bg='white')
      mail_flag = True

    if not pw:
      self.pw_entry.configure(bg='pink')
    else:
      self.pw_entry.configure(bg='white')
      pw_flag = True
      
    if auth == -1:
      self.warning_label.configure(text='権限を選択してください', fg='red')
    else:
      self.warning_label.pack_forget()
      auth_flag = True
    
    if name_flag and mail_flag and pw_flag and auth_flag:
      for i in range(4):
        self.OTP += str(random.randint(0,9) )
        print(self.OTP)
      self.destroy()
      RegisterCheck(self.master, self.OTP, name, mail, pw, auth)
      send_mail(mail, '図書管理アプリ', f'認証画面を開いて5分またはページを閉じると認証権限はなくなります。認証パスワード：{self.OTP}')

      
  def back_event(self):
    from login import Login
    self.destroy()
    Login(self.master)
    
if __name__ == '__main__':
  root = tk.Tk()
  app = Register(root)
  app.mainloop()