import tkinter as tk
from register import Register
from function_py25 import login
import random
from reset_pw_check import ResetPwCheck
from function_py25 import send_mail


class PwReset(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack(fill=tk.BOTH, expand=True)
    self.master = master
    master.state('zoomed')
    master.geometry('400x400')
    master.title('パスワード変更画面')

    self.create_widgets()

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # ウィンドウの縦横幅を入手
      self.master.update_idletasks()
      self.width = self.master.winfo_width()
      self.height = self.master.winfo_height()
    # 生成 
      self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20), )
      self.mail_label = tk.Label(self, text='Mail：')
      self.newPw_label = tk.Label(self, text='新しいPW：')
      self.mail_entry = tk.Entry(self)
      self.newPw_entry = tk.Entry(self, show='*')
      self.back_btn = tk.Button(self, text='戻る', command=self.back_event)
      self.register_btn = tk.Button(self, text='仮登録', command=self.register_event)

      

    # 配置
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.mail_label.place(x=self.width/2 - 115, y=160)
      self.newPw_label.place(x=self.width/2 - 140, y=190)
      self.mail_entry.place(x=self.width/2 - 70, y=160)
      self.newPw_entry.place(x=self.width/2 - 70, y=190)
      self.back_btn.place(x=self.width / 2 - 15, y=260)
      self.register_btn.place(x=self.width / 2 + 30, y=260)
      
  def back_event(self):
      from login import Login
      self.destroy()
      Login(self.master)

  def register_event(self):
    mail_flag = False
    newPw_flag = False
    self.OTP = ''

    mail = self.mail_entry.get()
    newPw = self.newPw_entry.get()
    
    if not mail:
      self.mail_entry.configure(bg='pink')
    else:
      self.mail_entry.configure(bg='white')
      mail_flag = True
      
    if not newPw:
      self.newPw_entry.configure(bg='pink')
    else:
      self.newPw_entry.configure(bg='white')
      newPw_flag = True
      
    if newPw_flag and mail_flag:
      for i in range(4):
        self.OTP += str(random.randint(0,9) )
      self.destroy()
      ResetPwCheck(self.master, mail, newPw, self.OTP)
      send_mail(mail, '図書管理アプリ', f'認証画面を開いて5分またはページを閉じると認証権限はなくなります。認証パスワード：{self.OTP}')

  
  
if __name__ == '__main__':
  root = tk.Tk()
  app = PwReset(root)
  app.mainloop()