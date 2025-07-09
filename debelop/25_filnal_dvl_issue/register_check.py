import tkinter as tk
from function_py25 import get_account_by_mail
from function_py25 import insert_user
from function_py25 import send_mail
from function_py25 import get_name
import time
import threading

class RegisterCheck(tk.Frame):
  def __init__(self, master, OTP, name, mail, pw, auth):
    super().__init__(master)
    master.state('zoomed')
    self.pack(fill=tk.BOTH, expand=True)
    
    self.master = master
    self.OTP = OTP
    self.name = name
    self.mail = mail
    self.pw = pw
    self.auth = auth
    master.geometry('400x400')
    master.title('登録認証画面')

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
      self.final_register_btn = tk.Button(self, text='登録', command=self.register_event)  
      self.back_btn = tk.Button(self, text='戻る', command=self.back_event)    
      
    # 配置 
      self.title_label.place(x=self.width/2 - 100, y=40)
      self.text_label.place(x=self.width/2 - 150, y=160)
      self.OTP_entry.place(x=self.width/2 - 70, y=250)
      self.final_register_btn.place(x=self.width/2 + 25, y=280)
      self.back_btn.place(x=self.width/2 - 15, y=280)
      self.text_label2.place(x=self.width/2 - 40, y=360)
      
  def register_event(self):
    input_OTP = self.OTP_entry.get()
    if input_OTP == self.OTP:
      account = get_account_by_mail(self.mail)
      if account is not None:
        self.text_label2.configure(text='入力されたアドレスは既に登録しています。')
      else:
        insert_user(self.name, self.mail, self.pw, self.auth)
        self.text_label2.configure(text='登録完了しました。')
        name = get_name(self.mail)[0]
        send_mail(self.mail, '図書管理アプリ', f'登録完了しました！{name}さん、ご利用ありがとうございます。')

    else:
        self.text_label2.configure(text='数字が違います。')

  def back_event(self):
    from register import Register
    self.destroy()
    Register(self.master)
    
  def thread(self):
    time.sleep(300)
    self.OTP = ''
    self.destroy()
    

    
if __name__ == '__main__':
  root = tk.Tk()
  app = RegisterCheck(root, 1,1,1,1,1)
  app.mainloop()