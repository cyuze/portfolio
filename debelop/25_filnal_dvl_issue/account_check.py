import tkinter as tk
from function_py25 import send_mail
from function_py25 import get_name
from function_py25 import update_mail
from function_py25 import get_account_by_mail
import time
import threading
import subprocess

class AccountCheck(tk.Frame):
  def __init__(self, master, mail, newMail, OTP, root):
    super().__init__(master, width=400, height=400)
    self.pack()
    
    self.root = root
    self.master = master
    self.OTP = OTP
    self.mail = mail
    self.newMail = newMail
    
    master.geometry('400x400')
    master.title('メール変更画面')

    self.create_widgets()
  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # ウィンドウの縦横幅を入手
      self.master.update_idletasks()
      self.width = self.master.winfo_width()
      self.height = self.master.winfo_height()
    # スレッドの作成
      t = threading.Thread(target=self.thread)
    # スレッドの開始
      t.start()
    # 生成
      self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20))
      self.text_label = tk.Label(self, text='メ ー ル に 届 い た 4 桁 の 数 字 を 入 力 し て く だ さ い 。\n\n※ 認 証 画 面 を 開 い て 5 分 ま た は ペ ー ジ を 閉 じ る \n　 と 認 証 権 限 は な く な り ま す 。', anchor='w', justify='left')
      self.text_label2 = tk.Label(self, text='', fg='red')
      self.OTP_entry = tk.Entry(self)
      self.final_register_btn = tk.Button(self, text='変更', command=self.register_event)  
      self.back_btn = tk.Button(self, text='戻る', command=self.back_event)    
      self.flag = False
      
    # 配置 
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.text_label.place(x=self.width/2 - 150, y=160)
      self.OTP_entry.place(x=self.width/2 - 70, y=250)
      self.final_register_btn.place(x=self.width/2 + 25, y=280)
      self.back_btn.place(x=self.width/2 - 15, y=280)
      self.text_label2.place(x=self.width/2 - 40, y=360)
      
  def register_event(self):
    input_OTP = self.OTP_entry.get()
    account = get_account_by_mail(self.newMail)
    if input_OTP == self.OTP:
        if account is None:
            update_mail(self.newMail, self.mail)
            self.text_label2.configure(text='メールを変更しました。')
            name = get_name(self.newMail)[0]
            send_mail(self.newMail, '図書管理アプリ', f'メールアドレスを変更しました！{name}さん、ご利用いただきありがとうございます。')
            from library import Library
            Library(self.root, self.newMail)
            self.master.destroy() 
        else:
            self.text_label2.configure(text='同じメールアドレスは使用できません。')

    else:
        self.text_label2.configure(text='数字が違います。')

  def back_event(self):
    from account import Account
    self.destroy()
    Account(self.master, self.mail)
    
  def thread(self):
    time.sleep(300)
    self.OTP = ''
    self.master.destroy()
    

    
# if __name__ == '__main__':
#   root = tk.Tk()
#   app = AccountCheck(root, 1,1,1)
#   app.mainloop()