import tkinter as tk
from register import Register
from function_py25 import login
from function_py25 import get_account_by_mail
from tkinter import messagebox
from library import Library
from PIL import Image, ImageTk
from reset_pw import PwReset
from adominLibrary import AdominLibrary

class Login(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack(fill=tk.BOTH, expand=True)
    self.master = master
    master.state('zoomed')
    master.geometry('400x400')
    master.title('ログイン画面')

    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # ウィンドウの縦横幅を入手
      self.master.update_idletasks()
      self.width = self.master.winfo_width()
      self.height = self.master.winfo_height()
    # 生成 
      self.mail_label = tk.Label(self, text='Mail：', )
      self.pw_label = tk.Label(self, text='PW：', )
      self.mail_entry = tk.Entry(self)
      self.pw_entry = tk.Entry(self, show='*')
      self.login_btn = tk.Button(self, text='ログイン', command=self.login_event)
      self.register_btn = tk.Button(self, text='新規登録', command=self.register_event)
      self.pw_reset_btn = tk.Button(self, text='PW変更', command=self.pw_reset_event)
      self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20), )
      self.register_recomend_label = tk.Label(self, text='アカウントがない方→→→→', )
      self.pw_reset_label = tk.Label(self, text='パスワードを忘れた方→→→→', )
    # 配置
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.mail_label.place(x=self.width/2 - 115, y=160)
      self.mail_entry.place(x=self.width/2 - 70, y=160)
      self.pw_label.place(x=self.width/2 - 110, y=190)
      self.pw_entry.place(x=self.width/2 - 70, y=190)
      self.login_btn.place(x=self.width/2 + 15, y=240)
      self.register_btn.place(x=self.width/2 + 60, y=297) 
      self.pw_reset_btn.place(x=self.width/2 + 60, y=330)
      self.register_recomend_label.place(x=self.width/2 - 90, y=299)
      self.pw_reset_label.place(x=self.width/2 - 90, y=330)


      
      
            
  def register_event(self):
    self.destroy()
    Register(self.master)
      
  def login_event(self):
    mail = self.mail_entry.get()
    input_pw = self.pw_entry.get()
    mail_flag = False
    input_pw_flag = False
        
    if not mail:
      self.mail_entry.configure(bg='pink')
    else:
      self.mail_entry.configure(bg='white')
      mail_flag = True
      
    if not input_pw:
      self.pw_entry.configure(bg='pink')
    else:
      self.pw_entry.configure(bg='white')
      input_pw_flag = True

    if input_pw_flag and mail_flag:
      account = login(mail, input_pw)
      if account is None:
        messagebox.showwarning('ログインできません', 'MailまたはPWが違います')
      else:
        print(account[4])
        self.destroy()
        if account[4] == '1':
          Library(self.master, mail)
        elif account[4] == '0':
          AdominLibrary(self.master, mail)
        
  def pw_reset_event(self):
    self.destroy()
    PwReset(self.master)
    

if __name__ == '__main__':
  root = tk.Tk()
  app = Login(root)
  app.mainloop()