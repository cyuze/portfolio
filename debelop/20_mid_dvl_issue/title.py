import tkinter as tk
from battle import ButtlePage
from pygame import mixer
from PIL import Image, ImageTk


class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=800, height=400)
    self.pack()
    
    self.master = master
    master.geometry('800x400')
    master.title('Hello Tkinter')    
    self.configure(bg='lightblue')
    self.create_widgets()
    
    self.master.bind("<Return>", self.click_enter)

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
      mixer.init()
      mixer.music.load('C:/Users/yuze/Music/パチモン/タイトルbgm.mp3')
      mixer.music.play(-1)
      
      
      # self.label_title = tk.Label(self,text='ポケットモンスター', font=('','50'),bg=('lightblue'))
      # self.label_title.place(x=150, y=0)
      
      # self.label_enter_start = tk.Label(self, text='enter to start', fg='white', bg='lightblue', font=('', '30'))
      # self.label_enter_start.place(x=400, y=100)
      
      cimg1 = Image.open('C:/Users/yuze/Pictures/poke/タイトル.jpg')
      self.img1 = ImageTk.PhotoImage(cimg1)
      self.label_title_img = tk.Label(self, image=self.img1)
      self.label_title_img.place(x=0, y=0)
      
  def click_enter(self, event):
      self.destroy()
      ButtlePage(self.master)

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()
