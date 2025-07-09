import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
from pygame import mixer
import time

class ButtlePage(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=800, height=400)
    self.pack()
    
    self.master = master
    master.geometry('800x400')
    master.title('Hello Tkinter')
    self.configure(bg='lightblue')

    self.create_widgets()
    self.master.bind("<Return>", self.click_enter)
    self.master.bind("<Up>", self.command_evend)
    self.master.bind("<Down>", self.command_evend)
    self.master.bind("<Right>", self.command_evend)
    self.master.bind("<Left>", self.command_evend)
    self.master.bind("<BackSpace>", self.backspace_event)
    self.master.bind("<q>", self.ctl_setumei_event)

  # ウィジェットを配置して画面作るメソッド
  def create_widgets(self):
    # bgm
    mixer.init()
    mixer.music.load('C:/Users/yuze/Music/パチモン/戦闘ｂｇｍ.mp3')
    mixer.music.play(-1)
    # 効果音
      # 味方の攻撃
    self.se_ally_atk = mixer.Sound("C:/Users/yuze/Music/パチモン/たいあたり.mp3")
    self.se_ally_atk2 = mixer.Sound('C:/Users/yuze/Music/パチモン/風切り音（重）.mp3')
    self.se_ally_move = mixer.Sound('C:/Users/yuze/Music/パチモン/ぷいッ！.mp3')
      # 敵の攻撃
    self.se_enemy_atk = mixer.Sound("C:/Users/yuze/Music/パチモン/ひっかく.mp3")
    self.se_enemy_apper = mixer.Sound("C:/Users/yuze/Music/パチモン/熊登場.mp3")
      # 逃げる
    self.se_escape = mixer.Sound("C:/Users/yuze/Music/パチモン/逃げる.mp3")
      # 空振り
    self.se_miss = mixer.Sound("C:/Users/yuze/Music/パチモン/空振り.mp3")
       # 回復
    self.se_cure = mixer.Sound('C:/Users/yuze/Music/パチモン/回復.mp3')
       #  ファンファーレ
    self.se_clear = mixer.Sound('C:/Users/yuze/Music/パチモン/ファンファーレ12.mp3')


    # 画像読み込み
    cimg1 = Image.open('C:/Users/yuze/Pictures/poke/パンダ（味方）.png')
    cimg2 = Image.open('C:/Users/yuze/Pictures/poke/熊（敵）.png')
    cimg3 = Image.open('C:/Users/yuze/Pictures/poke/たいあたり.png')
    cimg4 = Image.open('C:/Users/yuze/Pictures/poke/バックパック.png')
    cimg5 = Image.open('C:/Users/yuze/Pictures/poke/パンダ表.png')
    cimg6 = Image.open('C:/Users/yuze/Pictures/poke/犬.png')
    cimg7 = Image.open('C:/Users/yuze/Pictures/poke/犬裏.png')
    cimg8 = Image.open('C:/Users/yuze/Pictures/poke/パンダ表（手持）.png')
    cimg9 = Image.open('C:/Users/yuze/Pictures/poke/犬 （ナウ）.png')
    # 画像ファイルのオブジェクトの作成
    self.img1 = ImageTk.PhotoImage(cimg1)
    self.img2 = ImageTk.PhotoImage(cimg2)
    self.img3 = ImageTk.PhotoImage(cimg3)
    self.img4 = ImageTk.PhotoImage(cimg4)
    self.img5 = ImageTk.PhotoImage(cimg5)
    self.img6 = ImageTk.PhotoImage(cimg6)
    self.img7 = ImageTk.PhotoImage(cimg7)
    self.img8 = ImageTk.PhotoImage(cimg8)
    self.img9 = ImageTk.PhotoImage(cimg9)
    # 画像オブジェクトをラベルに張り付けて表示
        # 味方と敵の足場 
    self.label_ally_field = tk.Label(self, bg='lightblue', image=self.img1)
    self.label_enemy_field = tk.Label(self, bg='lightblue', image=self.img2)
    self.label_taiatari = tk.Label(self, bg='lightblue', image=self.img3)
    self.label_backpack  = tk.Label(self, bg='lightblue', image=self.img4)
    self.label_pand_omote  = tk.Label(self, bg='lightyellow', image=self.img5)
    self.label_inu_omote  = tk.Label(self, bg='lightblue', image=self.img6)
    self.label_inu_ura  = tk.Label(self, bg='lightblue', image=self.img7)
    self.label_pand_omote_poke  = tk.Label(self, bg='lightblue', image=self.img8)
    self.label_inu_omote_poke  = tk.Label(self, bg='lightyellow', image=self.img9)
    # 味方のステータス
    self.ally_A = 3
    self.ally_pp1 = 10
    self.ally_pp2 = 3
    self.ally_rest = 2
              # スタイルの作成
    style = ttk.Style()
    style.theme_use('default')
    style.configure("HP.Horizontal.TProgressbar", troughcolor='black', background='green')
    style.configure("HP_poke.Horizontal.TProgressbar", troughcolor='black', background='green')
    style.configure("EXP.Horizontal.TProgressbar", troughcolor='lightgray', background='navy blue')
    style.configure("enemy.Horizontal.TProgressbar", troughcolor='black', background='green')
    style.configure("HP_inu.Horizontal.TProgressbar", troughcolor='black', background='green')
    style.configure("HP_inu_poke.Horizontal.TProgressbar", troughcolor='black', background='green')
    style.configure("EXP_inu.Horizontal.TProgressbar", troughcolor='lightgray', background='navy blue')

              # プログレスバーの作成
    self.progressbar_ally_HP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="HP.Horizontal.TProgressbar", maximum=20, value=20)
    self.progressbar_ally_EXP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="EXP.Horizontal.TProgressbar", maximum=20, value=5)
    self.progressbar_ally_HP_poke = ttk.Progressbar(self, orient="horizontal", length=150, mode="determinate", style="HP_poke.Horizontal.TProgressbar", maximum=20, value=20)

                    #  犬のプログレスバー
    self.progressbar_inu_HP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="HP_inu.Horizontal.TProgressbar", maximum=15, value=15)
    self.progressbar_inu_HP_poke = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="HP_inu_poke.Horizontal.TProgressbar", maximum=15, value=15)
    self.progressbar_inu_EXP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="EXP_inu.Horizontal.TProgressbar", maximum=20, value=5)

              #犬のステータス
    self.inu_HP_child = self.progressbar_inu_HP['value']
    self.inu_HP_mother = self.progressbar_inu_HP['maximum']
    self.inu_HP_point = tk.Label(self, text=f'{self.inu_HP_child}/{self.inu_HP_mother}', bg='lightblue')
    self.inu_A = 2
    self.inu_pp1 = 10
    self.inu_lv = 4
    self.inu_flag = False
    
    self.ally_lv = 5
    self.ally_hp_child = self.progressbar_ally_HP["value"]
    self.ally_hp_mother = self.progressbar_ally_HP["maximum"]
    self.label_ally_name_lv = tk.Label(self, text=f'パンダ　　Lv.{self.ally_lv}', bg='lightblue')
    self.label_ally_HP = tk.Label(self, text='HP', bg='lightblue')      
    self.label_ally_HP_point = tk.Label(self, text= f'{self.ally_hp_child}/{self.ally_hp_mother}', bg='lightblue', font=('','10'))
    self.label_ally_EXP = tk.Label(self, text='EXP', bg='lightblue')
              # プログレスバーの再作成
    self.progressbar_ally_HP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="HP.Horizontal.TProgressbar", maximum=20, value=20)
    self.progressbar_ally_EXP = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="EXP.Horizontal.TProgressbar", maximum=20, value=5)
    
    # バック
    self.index = 0
    self.kaihuku_flag = False
    self.bag_flag = False
           #  スタイルを定義
    style = ttk.Style()
    style.configure("Treeview", background="orange", foreground="black", fiedldbackground="orange")

           # treeviewのインスタンスの生成
    self.tv_back = ttk.Treeview(self,height=25, show='headings', style="Treeview")
           #  列の名前を設定
    header = ('name', 'stock')
    self.tv_back.configure(columns=header)
           #  列名を設定
    self.tv_back.heading('name', text='名前')
    self.tv_back.heading('stock', text='個数')
           #  列幅の設定
    self.tv_back.column('name', width=500)
    self.tv_back.column('stock', width=20)
           #  データの挿入
    item1 = ('きずぐすり', 20)
    item2 = ('バッグをとじる',)
    item3 = ('',)
    item4 = ('',)
    item5 = ('',)
    item6 = ('',)
    item7 = ('',)
    item8 = ('',)
    item9 = ('',)
    item10 = ('',)
    item11 = ('',)
    item12 = ('',)
    item13 = ('',)
    item14 = ('',)
    item15 = ('',)
    item16 = ('',)
    item17 = ('',)
    item18 = ('',)
    item19 = ('',)
    item20 = ('',)
    self.tv_back.insert('',index='end',values=item1)
    self.tv_back.insert('',index='end',values=item2)
    self.tv_back.insert('',index='end',values=item3)
    self.tv_back.insert('',index='end',values=item4)
    self.tv_back.insert('',index='end',values=item5)
    self.tv_back.insert('',index='end',values=item6)
    self.tv_back.insert('',index='end',values=item7)
    self.tv_back.insert('',index='end',values=item8)
    self.tv_back.insert('',index='end',values=item9)
    self.tv_back.insert('',index='end',values=item10)
    self.tv_back.insert('',index='end',values=item11)
    self.tv_back.insert('',index='end',values=item12)
    self.tv_back.insert('',index='end',values=item13)
    self.tv_back.insert('',index='end',values=item14)
    self.tv_back.insert('',index='end',values=item15)
    self.tv_back.insert('',index='end',values=item16)
    self.tv_back.insert('',index='end',values=item17)
    self.tv_back.insert('',index='end',values=item18)
    self.tv_back.insert('',index='end',values=item19)
    self.tv_back.insert('',index='end',values=item20)

           #  アイテム説明ラベル
    self.label_item_setumei = tk.Label(self, text='ポケモンの　たいりょくを\n6　かいふくする', font=('', '20'), bg='white', justify='left', anchor='nw',height=50)      

      # ポケモン入れ替え
    self.poke_flag = False
            # 枠
    self.label_poke_chenge = tk.Label(self, bg='green',width=140,height=50)
    self.label_poke_now = tk.Label(self, text='', width=40, height=9,relief='solid', bg='lightyellow')
    self.label_poke2 = tk.Label(self, text='', width=55,height=3,relief='solid', bg='lightblue')
    self.label_poke3 = tk.Label(self, text='', width=55,height=3,relief='solid', bg='lightblue')
    self.label_poke4 = tk.Label(self, text='', width=55,height=3,relief='solid', bg='lightblue')
    self.label_poke5 = tk.Label(self, text='', width=55,height=3,relief='solid', bg='lightblue')
    self.label_poke6 = tk.Label(self, text='', width=55,height=3,relief='solid', bg='lightblue')
            #  テキスト
    self.label_poke_now_txt = tk.Label(self, text='パンダ', font=('','40'), bg='lightyellow')
    self.label_poke2_txt = tk.Label(self, text='犬', font=('','20'), bg='lightblue')
    self.label_poke3_txt = tk.Label(self, text='', font=('','20'), bg='lightblue')
    self.label_poke4_txt = tk.Label(self, text='', font=('','20'), bg='lightblue')
    self.label_poke5_txt = tk.Label(self, text='', font=('','20'), bg='lightblue')
    self.label_poke6_txt = tk.Label(self, text='', font=('','20'), bg='lightblue')
    self.poke_select = 'panda'            #ポケモン選択
    self.label_poke_back = tk.Label(self, text='もどる', font=('','20'), bg='lightgray', relief='solid')   #入れ替え画面から戻る
    self.label_select_poke = tk.Label(self, text=('ポケモンを　えらんで　ください'), font=('', '25'), bg='white', relief='solid') #ポケモンを　えらんで　ください

    # 敵のステータス
    self.atk_list = ['ひっかく']
    self.enemy_A = 3
    self.enemy_lv = 6
    self.label_enemy_name_lv = tk.Label(self, text=f'熊　　Lv.{self.enemy_lv}', bg='lightblue')
    self.label_enemy_HP = tk.Label(self, text='HP', bg='lightblue')
    
    self.progressbar_enemy = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", style="enemy.Horizontal.TProgressbar", maximum=40, value=40)
    
    self.label_enemy_HPbarW = tk.Label(self, width=100, font=('', '1'), bg='white')
    self.label_enemy_HPbarG = tk.Label(self, width=100, font=('', '1'), bg='green')
      # 戦闘コマンド欄
    self.canvas_buttle_txt = tk.Canvas(self, width=800, height=200, bg='red', bd=2, highlightthickness=0)
    self.label_buttle_txt = tk.Label(self.canvas_buttle_txt, width=110,height=9, bg='green')
    self.label_buttle_txt.place(x=10, y=10)
    self.label_buttle_txt2 = tk.Label(self, bg='green', font=('','30'), anchor='nw', fg='white', justify='left')
    self.label_buttle_cmd_list1 = tk.Label(self, width=40, height=10, bg='white', relief='solid')
    self.label_buttle_cmd_list2 = tk.Label(self, width=72, height=10, bg='white', relief='solid')
      # コマンドボタン
    self.label_atk = tk.Label(self, text='たたかう', width=15, height=4, relief='solid')
    self.label_bag = tk.Label(self, text='バッグ', width=15, height=4, relief='solid')
    self.label_poke = tk.Label(self, text='ポケモン', width=15, height=4, relief='solid')
    self.label_escape = tk.Label(self, text='にげる', width=15, height=4, relief='solid')
    
    # 技ボタン
    self.label_atk1 = tk.Label(self, text='たいあたり', font=('', '30'), bg='white')
    self.label_atk2 = tk.Label(self, text='すなかけ',font=('', '30'), bg='white')
        # 説明
    self.label_atk_setumei  = tk.Label(self, text=f'PP　{self.ally_pp1}/10\nわざたいぷ/ノーマル', font=('', '20'), bg='white', justify='left', anchor='nw')

      # 配置
    self.label_enemy_field.place(x=500, y=10)

    self.label_ally_name_lv.place(x=580, y=150)
    self.label_ally_HP.place(x=540, y=170)
    self.label_ally_HP_point.place(x=630, y=185)
    self.progressbar_ally_HP.place(x=570, y=170)
    self.progressbar_ally_EXP.place(x=570, y=200)
    self.label_ally_EXP.place(x=540, y=200)

    self.label_enemy_name_lv.place(x=100, y=50)
    self.label_enemy_HP.place(x=70, y=70)
    self.progressbar_enemy.place(x=100, y=70)

    self.canvas_buttle_txt.place(x=0, y=240)
    self.label_buttle_txt2.place(x=20, y=250)
    self.label_buttle_cmd_list1.place(x=514, y=242)
    self.label_buttle_cmd_list2.place(x=1, y=242)
    
    self.label_atk.place(x=530, y=250)
    self.label_bag.place(x=670, y=250)
    self.label_poke.place(x=530, y=320)
    self.label_escape.place(x=670, y=320)
    
      # 戦闘    
    self.enter_count = 0
    self.enter_count_atk = 0
    self.enter_count_atk2 =0
    self.label_buttle_cmd_list2.place_forget()
    self.label_buttle_cmd_list1.place_forget()
    self.label_atk.place_forget()
    self.label_poke.place_forget()
    self.label_bag.place_forget()
    self.label_escape.place_forget()
    self.label_atk.config(text='>たたかう')
    self.label_bag.config(bg='lightgray')
    self.label_escape.config(bg='lightgray')
    self.label_poke.config(bg='lightgray')
     
     #説明
    self.label_ctl_setumei = tk.Label(self, text='そうさせつめい：Ｑ', font=('','10'), bg='white', fg=('black'))
    self.label_ctl_setumei.place(x=0, y=0)
    self.ctl_setumei_flag = True
    self.label_ctl_list = tk.Label(self, text='BackSpace：もどる\nEnter：けってい\nやじるしキー：せんたく',justify='left', font=('','25'), bg='white', relief='solid',width=40, height=10)
    
  def click_enter(self, event):
    print('enter')
    self.enter_count += 1
    if self.enter_count == 1:
      self.se_enemy_apper.play()
      self.label_buttle_txt2.configure(text='あ！　やせいの\n熊が飛び出してきた！')
    elif self.enter_count == 2:
      self.label_buttle_txt2.configure(text='ゆけ！　パンダ！')
      self.label_ally_field.place(x=100, y=100)
    elif self.enter_count == 3:
      self.label_buttle_txt2.configure(text='パンダは　どうする？')
      self.label_buttle_cmd_list1.place(x=514, y=242)
      self.label_atk.place(x=530, y=250)
      self.label_bag.place(x=670, y=250)
      self.label_poke.place(x=530, y=320)
      self.label_escape.place(x=670, y=320)
    elif self.enter_count >=3 : 
      self.label_ally_field.lower()
      if self.label_bag.cget('text') == '>バッグ':                                                                    #バッグ
        print('バッグ')
        self.label_atk.place_forget()
        self.label_bag.place_forget()
        self.label_escape.place_forget()
        self.label_poke.place_forget()
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_txt.place_forget()
        self.label_buttle_txt2.place_forget()
        self.canvas_buttle_txt.place_forget()
        self.progressbar_enemy.place_forget()
        self.label_enemy_HP.place_forget()
        self.label_enemy_name_lv.place_forget()
        self.progressbar_ally_HP.place_forget()
        self.progressbar_ally_EXP.place_forget()
        self.progressbar_inu_HP.place_forget()
        self.progressbar_inu_EXP.place_forget()
        self.label_ally_HP_point.place_forget()
        self.tv_back.place(x=278, y=-18)
        self.label_item_setumei.place(x=0, y=200)
        self.label_backpack.place(x=0, y=0)
        self.tv_back.selection_set(self.tv_back.get_children()[0])
        self.label_bag.configure(text='バッグ')
        self.label_inu_ura.place_forget()
        self.bag_flag = True
        
        
      elif self.label_escape.cget('text') == '>にげる':                                                         #逃げる
        print('逃げる')
        self.label_buttle_txt2.configure(text='にげだした！')
        self.se_escape.play()
        self.label_ally_field.lift(self.label_inu_omote)
        messagebox.showinfo('しっぱい！', '終了')
        self.back_title()
      elif self.label_atk.cget('text') == '>たたかう':                                                          #たたかう
        print('たたかう')
        self.tatakau()
      elif self.label_poke.cget('text') == '>ポケモン':                                                         #ポケモン
        print('ポケモン')
        self.progressbar_ally_EXP.lower()
        self.label_atk.place_forget()
        self.label_bag.place_forget()
        self.label_escape.place_forget()
        self.label_poke.place_forget()
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_txt.place_forget()
        self.label_buttle_txt2.place_forget()
        self.canvas_buttle_txt.place_forget()
        self.progressbar_enemy.place_forget()
        self.label_enemy_HP.place_forget()
        self.label_enemy_name_lv.place_forget()
        self.progressbar_ally_HP.place_forget()
        
        self.label_poke_chenge.place(x=0, y=0)
        self.label_poke_now.place(x=20, y=100)
        self.label_poke2.place(x=400, y=35)
        self.label_poke3.place(x=400, y=105)
        self.label_poke4.place(x=400, y=175)
        self.label_poke5.place(x=400, y=245)
        self.label_poke6.place(x=400, y=315)
        
        self.label_poke_now_txt.place(x=120, y=110)
        self.label_poke2_txt.place(x=500, y=40)
        self.label_poke3_txt.place(x=500, y=110)
        self.label_poke4_txt.place(x=500, y=180)
        self.label_poke5_txt.place(x=500, y=250)
        self.label_poke6_txt.place(x=500, y=320)
        
        self.label_poke_back.place(x=650, y=367)
        self.label_poke_back.lift(self.label_poke_chenge)
        
        self.label_select_poke.place(x=10, y=360)

        self.label_ally_HP_point.place(x=150, y=200)
        self.label_ally_HP_point.configure(font=('','20'), bg='lightyellow')
        self.label_ally_HP_point.lift(self.label_poke_chenge)
        self.label_ally_HP_point.lift(self.label_poke_now)
             
        if self.inu_flag:
          self.label_pand_omote_poke.place(x=420, y=40)
          self.label_inu_omote_poke.place(x=30, y=105)
          self.label_pand_omote_poke.lift(self.label_poke_chenge)
          self.label_inu_omote_poke.lift(self.label_poke_chenge)
          self.label_pand_omote_poke.lift(self.label_poke2)
          self.label_inu_omote_poke.lift(self.label_poke_now)
          self.label_poke_now_txt.configure(text='いぬ')
          self.label_poke2_txt.configure(text='パンダ')
          self.progressbar_inu_HP.lower()
          self.progressbar_inu_EXP.lower()
          self.progressbar_ally_HP_poke.place(x=620, y=43)
          self.progressbar_ally_HP_poke.lift(self.label_poke_chenge)
          self.progressbar_ally_HP_poke.lift(self.label_poke2)
          self.progressbar_inu_HP_poke.place(x=130, y=170)
          self.progressbar_inu_HP_poke.configure(length=150)
          self.progressbar_inu_HP_poke.lift(self.label_poke_chenge)
          self.progressbar_inu_HP_poke.lift(self.label_poke2)
          self.inu_HP_point.place(x=620, y=60)
          self.inu_HP_point.configure( text= f'{self.ally_hp_child}/{self.ally_hp_mother}')
          self.inu_HP_point.lift(self.label_poke_chenge)
          self.inu_HP_point.lift(self.label_poke2)
        else:          
          self.progressbar_inu_HP_poke.configure(length=200)
          self.inu_HP_point.configure( text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
          
          
          self.progressbar_inu_HP_poke.place(x=570, y=43)
          self.progressbar_inu_HP_poke.lift(self.label_poke_chenge)
          self.progressbar_inu_HP_poke.lift(self.label_poke2)
          
          self.inu_HP_point.place(x=570, y=60)
          self.inu_HP_point.lift(self.label_poke_chenge)
          self.inu_HP_point.lift(self.label_poke2)
          
          self.progressbar_inu_HP_poke.place(x=570, y=43)
          self.progressbar_inu_HP_poke.lift(self.label_poke_chenge)
          self.progressbar_inu_HP_poke.lift(self.label_poke2)
          
          self.inu_HP_point.place(x=570, y=60)
          self.inu_HP_point.lift(self.label_poke_chenge)
          self.inu_HP_point.lift(self.label_poke2)
          
          self.label_poke_back.place(x=650, y=367)
          self.label_poke_back.lift(self.label_poke_chenge)
          
          self.label_select_poke.place(x=10, y=360)
        
          self.progressbar_ally_HP_poke.place(x=130,y=170)
          self.progressbar_ally_HP_poke.lift()

          self.label_inu_omote.place(x=420, y=40)
          self.label_pand_omote.place(x=30, y=105)
          self.label_inu_omote.lift(self.label_poke_chenge)
          self.label_pand_omote.lift(self.label_poke_chenge)
          self.label_inu_omote.lift(self.label_poke2)
          self.label_pand_omote.lift(self.label_poke_now)
        
        self.label_poke.configure(text='ポケモン')
        self.poke_flag = True
        
      elif self.label_atk1.cget('text') == '>たいあたり':                                                         #たいあたり
        print('たいあたり')
        self.label_ally_field.lift(self.label_inu_omote)
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_cmd_list2.place_forget()
        self.label_atk1.place_forget()
        self.label_atk2.place_forget()
        self.label_atk_setumei.place_forget()
        if self.ally_pp1 > 0:
          self.label_buttle_txt2.configure(text='パンダの\nたいあたり　こうげき！')
        else:
          self.label_buttle_txt2.configure(text='ppがたりない')
        self.enter_count_atk += 1
        if self.enter_count_atk == 2:
          if self.ally_pp1 > 0:
            if self.kaihuku_flag:
              pass
            else:
              self.se_ally_atk.play()
              self.progressbar_enemy['value'] -= self.ally_A
          else:
            pass
          if self.progressbar_enemy['value'] <= 0:
            self.label_buttle_txt2.configure(text='やせいの　熊は　たおれた！')
            self.label_enemy_field.place_forget()
          else:    
            self.atk = random.choice(self.atk_list)
            if self.atk == 'すなかけ':
              self.label_buttle_txt2.configure(text=f'やせいの　熊は\nこうげきをはずした！')
            else:
              self.label_buttle_txt2.configure(text=f'やせいの　熊の\n{self.atk}！')
        elif self.enter_count_atk == 3:
          if self.progressbar_enemy['value'] <= 0:
            self.label_buttle_txt2.configure(text='パンダは\n10　けいけんちを　もらった！')
            self.label_atk1.configure(text='たいあたり')
            self.label_atk2.configure(text='すなかけ')
            messagebox.showinfo('クリア', '終了')
            self.se_clear.play()
            self.se_clear.play()
            self.back_title()
          else:
            self.enemy_atack()
            if self.progressbar_ally_HP['value'] <= 0:
              self.label_buttle_txt2.configure(text='パンダは　たおれた！')
              self.label_ally_field.place_forget()
            else:
              self.ally_pp1 -= 1
              self.enter_count_atk = 0
              self.label_buttle_txt2.configure(text='パンダは　どうする？')
              self.label_buttle_cmd_list1.place(x=514, y=242)
              self.label_atk.place(x=530, y=250)
              self.label_bag.place(x=670, y=250)
              self.label_poke.place(x=530, y=320)
              self.label_escape.place(x=670, y=320)
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              self.kaihuku_flag = False              
        elif self.enter_count_atk == 4:
            if self.ally_rest <= 1:
              self.label_buttle_txt2.configure(text='めのまえが　まっくらになった！')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              messagebox.showinfo('クリア', '終了')
              self.back_title()
            else:
              self.ally_rest -= 1
              self.label_buttle_txt2.configure(text='パンダ　よくやった　いけ　いぬ！')
              self.change()        
              self.progressbar_ally_EXP.lift()      
              self.label_ally_field.place_forget()
              self.label_inu_ura.place(x=100, y=100)
              self.label_buttle_txt2.configure(text='いぬは　　どうする？')
              self.label_ally_name_lv.configure(text=f'いぬ　　　Lv.{self.inu_lv}')
              self.progressbar_ally_HP.place_forget()
              self.progressbar_ally_EXP.place_forget()
              self.progressbar_inu_HP.place(x=570, y=170)
              self.progressbar_inu_EXP.place(x=570, y=200)
              self.progressbar_inu_HP.lift()
              self.label_ally_field.lift(self.label_inu_omote)
              self.progressbar_inu_EXP.lift()
              self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
              self.inu_flag = True
              self.label_atk2.configure(text='すなかけ')
              self.label_atk1.configure(text='たいあたり')
              self.enter_count_atk = 0

              
      elif self.label_atk2.cget('text') == '>すなかけ':                                                         #すなかけ
        print('すなかけ')
        self.label_ally_field.lift(self.label_inu_omote)
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_cmd_list2.place_forget()
        self.label_atk1.place_forget()
        self.label_atk2.place_forget()
        self.label_atk_setumei.place_forget()
        if self.ally_pp2 > 0:
          self.label_buttle_txt2.configure(text='パンダの\nすなかけ　こうげき！')
          self.enter_count_atk += 1
        else:
          self.label_buttle_txt2.configure(text='ppがたりない')
          self.enter_count_atk += 1
        if self.enter_count_atk == 2:
          if self.ally_pp2 > 0:
            self.se_ally_atk2.play()
            if len(self.atk_list) <= 3:
              self.atk_list.append('すなかけ')
              self.atk_list.append('ひっかく')
              self.label_buttle_txt2.configure(text='やせいの熊の\nめいちゅうがさがった！')
            else:
              self.label_buttle_txt2.configure(text='やせいの熊の\nめいちゅうは\nこれ以上さがらない！')
          else:
              self.atk = random.choice(self.atk_list)
              if self.atk == 'すなかけ':
                self.label_buttle_txt2.configure(text=f'やせいの　熊は\nこうげきをはずした！')
              else:
                self.label_buttle_txt2.configure(text=f'やせいの　熊の\n{self.atk}！')
        elif self.enter_count_atk == 3:
          if self.ally_pp2 > 0:
            self.atk = random.choice(self.atk_list)
            if self.atk == 'すなかけ':
              self.label_buttle_txt2.configure(text=f'やせいの　熊は\nこうげきをはずした！')
            else:
              self.label_buttle_txt2.configure(text=f'やせいの　熊の\n{self.atk}！')
          else:
            self.enemy_atack()
            if self.progressbar_ally_HP['value'] <= 0:
              self.label_buttle_txt2.configure(text='パンダは　たおれた！')
              self.label_ally_field.place_forget()
            else:
              self.ally_pp2 -= 1
              self.enter_count_atk = 0
              self.label_buttle_txt2.configure(text='パンダは　どうする？')
              self.label_buttle_cmd_list1.place(x=514, y=242)
              self.label_atk.place(x=530, y=250)
              self.label_bag.place(x=670, y=250)
              self.label_poke.place(x=530, y=320)
              self.label_escape.place(x=670, y=320)
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
        elif self.enter_count_atk == 4:
          if self.ally_pp2 > 0:
            self.enemy_atack()
            if self.progressbar_ally_HP['value'] <= 0:
              self.label_buttle_txt2.configure(text='パンダは　たおれた！')
              self.label_ally_field.place_forget()
            else:
              self.ally_pp2 -= 1
              self.enter_count_atk = 0
              self.label_buttle_txt2.configure(text='パンダは　どうする？')
              self.label_buttle_cmd_list1.place(x=514, y=242)
              self.label_atk.place(x=530, y=250)
              self.label_bag.place(x=670, y=250)
              self.label_poke.place(x=530, y=320)
              self.label_escape.place(x=670, y=320)
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              self.kaihuku_flag = False              
          else:
              self.label_buttle_txt2.configure(text='めのまえが　まっくらになった！')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              messagebox.showinfo('クリア', '終了')
              self.back_title()
        elif self.enter_count_atk == 5:
          if self.ally_pp2 > 0:
            if self.ally_rest <= 1:
              self.label_buttle_txt2.configure(text='めのまえが　まっくらになった！')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              messagebox.showinfo('クリア', '終了')
              self.back_title()
            else:
              self.ally_rest -= 1
              self.label_buttle_txt2.configure(text='パンダ　よくやった　いけ　いぬ！')
              self.change()        
              self.progressbar_ally_EXP.lift()      
              self.label_ally_field.place_forget()
              self.label_inu_ura.place(x=100, y=100)
              self.label_buttle_txt2.configure(text='いぬは　　どうする？')
              self.label_ally_name_lv.configure(text=f'いぬ　　　Lv.{self.inu_lv}')
              self.progressbar_ally_HP.place_forget()
              self.progressbar_ally_EXP.place_forget()
              self.progressbar_inu_HP.place(x=570, y=170)
              self.progressbar_inu_EXP.place(x=570, y=200)
              self.progressbar_inu_HP.lift()
              self.label_ally_field.lift(self.label_inu_omote)
              self.progressbar_inu_EXP.lift()
              self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
              self.inu_flag = True
              self.label_atk2.configure(text='すなかけ')
              self.enter_count_atk = 0
      
      elif self.label_atk1.cget('text') == '>かみつく':                                                         #かみつく
        print('かみつく')
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_cmd_list2.place_forget()
        self.label_atk1.place_forget()
        self.label_atk_setumei.place_forget()
        if self.inu_pp1 > 0:
          self.label_buttle_txt2.configure(text='いぬの\nかみつく　こうげき！')
        else:
          self.label_buttle_txt2.configure(text='ppがたりない')
        self.enter_count_atk += 1
        if self.enter_count_atk == 2:
          if self.inu_pp1 > 0:
            if self.kaihuku_flag:
              pass
            else:
              self.se_ally_atk.play()
              self.progressbar_enemy['value'] -= self.inu_A
          else:
            pass
          if self.progressbar_enemy['value'] <= 0:
            self.label_buttle_txt2.configure(text='やせいの　熊は　たおれた！')
            self.label_enemy_field.place_forget()
          else:    
            self.atk = random.choice(self.atk_list)
            if self.atk == 'すなかけ':
              self.label_buttle_txt2.configure(text=f'やせいの　熊は\nこうげきをはずした！')
            else:
              self.label_buttle_txt2.configure(text=f'やせいの　熊の\n{self.atk}！')
        elif self.enter_count_atk == 3:
          if self.progressbar_enemy['value'] <= 0:
            self.label_buttle_txt2.configure(text='いぬは\n10　けいけんちを　もらった！')
            self.label_atk1.configure(text='かみつく')
            messagebox.showinfo('クリア', '終了')
            self.se_clear.play()
            self.back_title()
          else:
            self.enemy_atack()
            if self.progressbar_inu_HP['value'] <= 0:
              self.label_buttle_txt2.configure(text='いぬは　たおれた！')
              self.label_ally_field.place_forget()
            else:
              self.inu_pp1 -= 1
              self.enter_count_atk = 0
              self.label_buttle_txt2.configure(text='いぬは　どうする？')
              self.label_buttle_cmd_list1.place(x=514, y=242)
              self.label_atk.place(x=530, y=250)
              self.label_bag.place(x=670, y=250)
              self.label_poke.place(x=530, y=320)
              self.label_escape.place(x=670, y=320)
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='かみつく')
              self.kaihuku_flag = False              
        elif self.enter_count_atk == 4:
            if self.ally_rest <= 1:
              self.label_buttle_txt2.configure(text='めのまえが　まっくらになった！')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')
              messagebox.showinfo('クリア', '終了')
              self.back_title()
            else:
              self.ally_rest -= 1
              self.label_buttle_txt2.configure(text='いぬ　よくやった　いけ　パンダ！')
              self.change()        
              self.progressbar_ally_EXP.lift()      
              self.label_ally_field.place_forget()
              self.label_inu_ura.place(x=100, y=100)
              self.label_buttle_txt2.configure(text='パンダは　　どうする？')
              self.label_ally_name_lv.configure(text=f'パンダ　　　Lv.{self.ally_lv}')
              self.inu_HP_child = 0
              self.progressbar_inu_HP.place_forget()
              self.progressbar_inu_EXP.place_forget()
              self.progressbar_ally_HP.place(x=570, y=170)
              self.progressbar_ally_EXP.place(x=570, y=200)
              self.progressbar_ally_HP.lift()
              self.label_ally_field.lift(self.label_inu_omote)
              self.progressbar_ally_EXP.lift()
              self.label_ally_HP_point.configure(text= f'{self.ally_hp_child}/{self.ally_hp_mother}')
              self.inu_flag = False
              self.label_inu_ura.place_forget()
              self.label_ally_field.place(x=100, y=100)
              self.label_atk2.configure(text='すなかけ')
              self.label_atk1.configure(text='かみつく')
              self.label_atk1.configure(text='たいあたり')
              self.enter_count_atk = 0


      
      elif self.bag_flag:                                                                            #バッグの中身操作
        crrent_item = self.tv_back.selection()
        values = self.tv_back.item(crrent_item)['values']
        if self.tv_back.item(crrent_item)['values'][0] == 'きずぐすり':
          if values[1] > 0:
            result = messagebox.askyesno('', 'つかう？')
            if self.inu_flag:
              self.inu_pp1 += 1
            else:
              self.ally_pp1 += 1
          if result:
            self.se_cure.play()
            stock_value = values[1] - 1
            self.tv_back.item(crrent_item, values=(values[0], stock_value))
            if self.inu_flag:
              if self.progressbar_inu_HP['value'] >= 9:
                self.progressbar_inu_HP['value'] = 15
                self.progressbar_inu_HP_poke['value'] = 15
                self.inu_HP_child = 15
                self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')    
                self.bag_back()
                self.kaihuku()
              else:
                self.progressbar_inu_HP['value'] += 6
                self.progressbar_inu_HP_poke['value'] += 6
                self.inu_HP_child = self.progressbar_inu_HP["value"]
                self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
                self.bag_back()
                self.kaihuku()
            else:
              if self.progressbar_ally_HP['value'] >= 14:
                self.progressbar_ally_HP['value'] = 20
                self.progressbar_ally_HP_poke['value'] = 20
                self.ally_hp_child = 20
                self.label_ally_HP_point.configure(text= f'{self.ally_hp_child}/{self.ally_hp_mother}')    
                self.bag_back()
                self.kaihuku()
              else:
                self.progressbar_ally_HP['value'] += 6
                self.progressbar_ally_HP_poke['value'] += 6
                self.ally_hp_child = self.progressbar_ally_HP["value"]
                self.label_ally_HP_point.configure(text= f'{self.ally_hp_child}/{self.ally_hp_mother}')
                self.bag_back()
                self.kaihuku()
        elif self.tv_back.item(crrent_item)['values'][0] == 'バッグをとじる':
          self.bag_back()
          self.label_item_setumei.configure(text='ポケモンの　たいりょくを\n6　かいふくする')

      elif self.poke_flag:                                                                       #ポケモン交換
          if self.poke_select == 'back':
            print('bag back')
            self.label_poke_chenge.place_forget()
            self.label_poke_now.place_forget()
            self.label_poke2.place_forget()
            self.label_poke3.place_forget()
            self.label_poke4.place_forget()
            self.label_poke5.place_forget()
            self.label_poke6.place_forget()
            self.label_poke_now_txt.place_forget()
            self.label_poke2_txt.place_forget()
            self.label_poke3_txt.place_forget()
            self.label_poke4_txt.place_forget()
            self.label_poke5_txt.place_forget()
            self.label_poke6_txt.place_forget()
            self.label_inu_omote.place_forget()
            self.label_pand_omote.place_forget()
            self.progressbar_ally_HP_poke.place_forget()
            self.label_ally_HP_point.place_forget()
            self.progressbar_inu_HP_poke.place_forget()
            self.inu_HP_point.place_forget()
            self.label_poke_back.place_forget()
            self.label_select_poke.place_forget()
            
            self.label_pand_omote_poke.place_forget()
            self.label_inu_omote_poke.place_forget()
            self.label_ally_HP_point.lower()
            self.progressbar_inu_HP.lift()
            self.label_inu_omote_poke.configure(bg='lightyellow')
            
            self.label_atk.place(x=530, y=250)
            self.label_bag.place(x=670, y=250)
            self.label_escape.place(x=670, y=320)
            self.label_poke.place(x=530, y=320)
            self.label_buttle_cmd_list1.place(x=514, y=242)
            self.label_buttle_txt.place(x=10, y=10)
            self.label_buttle_txt2.place(x=20, y=250)
            self.canvas_buttle_txt.place(x=0, y=240)
            self.progressbar_enemy.place(x=100, y=70)
            self.label_enemy_HP.place(x=70, y=70)
            self.label_enemy_name_lv.place(x=100, y=50)  
            self.label_ally_HP_point.place(x=630, y=185)   
            self.progressbar_ally_HP.place(x=570, y=170)
            
            self.label_atk.configure(text='>たたかう', bg='white')
            self.label_poke.configure(bg='lightgray')
            self.label_poke_now.configure(bg='lightyellow')
            self.label_pand_omote.configure(bg='lightyellow')
            self.label_ally_HP_point.configure(bg='lightblue', font=('','10'))
            self.label_poke_now_txt.configure(bg='lightyellow')
            self.label_poke_back.configure(bg='lightgray')
            self.progressbar_ally_HP.lift()
            self.progressbar_ally_EXP.lift()
            self.label_ally_field.lift(self.label_inu_omote)
            self.poke_select = 'panda'
            self.poke_flag = False
            if self.ally_rest <= 1:
              if self.inu_flag:
                self.progressbar_ally_HP.place_forget()
                self.progressbar_ally_EXP.place_forget()
                self.progressbar_inu_HP.place(x=570, y=170)
                self.progressbar_inu_EXP.place(x=570, y=200)
                self.progressbar_inu_HP.lift()
                self.progressbar_inu_EXP.lift()
          elif self.poke_select == 'inu':
            print('change')
            if self.ally_rest <= 1:
              pass
            else:
              change = messagebox.askyesno('', 'いれかえる')    
              if change:
                if self.inu_flag:
                  self.change()
                  self.inu_flag = False
                  self.label_pand_omote_poke.place_forget()
                  self.label_inu_omote_poke.place_forget()                
                  self.label_inu_omote.place_forget()
                  self.label_ally_field.place(x=100, y=100)
                  self.label_ally_field.lift(self.label_inu_omote)
                  self.label_buttle_txt2.configure(text='パンダは　どうする？')
                  self.label_ally_name_lv.configure(text=f'パンダ　　Lv.{self.ally_lv}')
                  self.progressbar_inu_HP.place_forget()
                  self.progressbar_inu_EXP.place_forget()
                  self.progressbar_ally_HP.place(x=570, y=170)
                  self.progressbar_ally_EXP.place(x=570, y=200)
                  self.progressbar_ally_HP.lift()
                  self.progressbar_ally_EXP.lift()
                  self.label_ally_HP_point.configure(text= f'{self.ally_hp_child}/{self.ally_hp_mother}')
                  self.label_poke_now_txt.configure(text='パンダ')
                  self.label_poke2_txt.configure(text='いぬ')
                  self.inu_HP_point.configure(text=f'{self.inu_HP_child}/{self.inu_HP_mother}')
                  self.progressbar_ally_EXP.lower()
                  self.progressbar_ally_EXP.lift(self.label_ally_HP_point)
                else:
                  self.change()        
                  self.progressbar_ally_EXP.lift()      
                  self.label_ally_field.place_forget()
                  self.label_inu_ura.place(x=100, y=100)
                  self.label_buttle_txt2.configure(text='いぬは　　どうする？')
                  self.label_ally_name_lv.configure(text=f'いぬ　　　Lv.{self.inu_lv}')
                  self.progressbar_ally_HP.place_forget()
                  self.progressbar_ally_EXP.place_forget()
                  self.progressbar_inu_HP.place(x=570, y=170)
                  self.progressbar_inu_EXP.place(x=570, y=200)
                  self.progressbar_inu_HP.lift()
                  self.progressbar_inu_EXP.lift()
                  self.label_ally_field.lift(self.label_inu_omote)
                  self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
          
                 
  def command_evend(self, event):
    if event.keysym == 'Up':                                                                     #up
      if self.label_poke.cget('text') == '>ポケモン':
        self.label_atk.config(text='>たたかう', bg='white')
        self.label_bag.config(bg='lightgray')
        self.label_escape.config(bg='lightgray')
        self.label_poke.config(bg='lightgray', text='ポケモン')
      elif self.label_escape.cget('text') == '>にげる':
        self.label_bag.config(text='>バッグ', bg='white')
        self.label_atk.config(bg='lightgray')
        self.label_escape.config(bg='lightgray', text='にげる')
        self.label_poke.config(bg='lightgray')
      elif self.bag_flag:
        if self.index > 0:
          self.index -= 1
          self.tv_back.selection_set(self.tv_back.get_children()[self.index])
          crrent_item = self.tv_back.selection()
          if self.tv_back.item(crrent_item)['values'][0] == 'きずぐすり':
            self.label_item_setumei.configure(text='ポケモンの　たいりょくを\n6　かいふくする')
          else:
            self.label_item_setumei.configure(text='　　　　　　　　　　　　　　　　　')
            self.label_item_setumei.lower(self.tv_back)
      elif self.poke_flag:
        if self.poke_select == 'back':
          self.label_poke_back.configure(bg='lightgray')
          self.label_poke6.configure(bg='lightyellow')
          self.label_poke6_txt.configure(bg='lightyellow')
          self.poke_select = 'poke6'
          
        elif self.poke_select == 'poke6':
          self.label_poke6.configure(bg='lightblue')
          self.label_poke6_txt.configure(bg='lightblue')
          self.label_poke5.configure(bg='lightyellow')
          self.label_poke5_txt.configure(bg='lightyellow')
          self.poke_select = 'poke5'
          
        elif self.poke_select == 'poke5':
          self.label_poke5.configure(bg='lightblue')
          self.label_poke5_txt.configure(bg='lightblue')
          self.label_poke4.configure(bg='lightyellow')
          self.label_poke4_txt.configure(bg='lightyellow')
          self.poke_select = 'poke4'
          
        elif self.poke_select == 'poke4':
          self.label_poke4.configure(bg='lightblue')
          self.label_poke4_txt.configure(bg='lightblue')
          self.label_poke3.configure(bg='lightyellow')
          self.label_poke3_txt.configure(bg='lightyellow')
          self.poke_select = 'poke3'
        elif self.poke_select == 'poke3':
          self.label_poke3.configure(bg='lightblue')
          self.label_poke3_txt.configure(bg='lightblue')
          self.label_poke2.configure(bg='lightyellow')
          self.label_poke2_txt.configure(bg='lightyellow')
          self.label_inu_omote.configure(bg='lightyellow')
          self.inu_HP_point.configure(bg='lightyellow')
          self.label_pand_omote_poke.configure(bg='lightyellow')
          self.poke_select = 'inu'

        
    elif event.keysym == 'Down':                                                                     #down
      if self.label_atk.cget('text') == '>たたかう':
        self.label_atk.config(text='たたかう', bg='lightgray')
        self.label_bag.config(bg='lightgray')
        self.label_escape.config(bg='lightgray')
        self.label_poke.config(bg='white', text='>ポケモン')
      elif self.label_bag.cget('text') == '>バッグ':
        self.label_bag.config(text='バッグ', bg='lightgray')
        self.label_atk.config(bg='lightgray')
        self.label_escape.config(bg='white', text='>にげる')
        self.label_poke.config(bg='lightgray')
      elif self.bag_flag:
        self.index += 1
        self.tv_back.selection_set(self.tv_back.get_children()[self.index])
        crrent_item = self.tv_back.selection()
        if self.tv_back.item(crrent_item)['values'][0] == 'きずぐすり':
          self.label_item_setumei.configure(text='ポケモンの　たいりょくを\n6　かいふくする')
        else:
            self.label_item_setumei.configure(text='　　　　　　　　　　　　　　　　　')
            self.label_item_setumei.lower(self.tv_back)
      elif self.poke_flag:
        if self.poke_select == 'inu':
          self.label_poke2.configure(bg='lightblue')
          self.label_poke2_txt.configure(bg='lightblue')
          self.label_inu_omote.configure(bg='lightblue')
          self.inu_HP_point.configure(bg='lightblue')
          self.label_poke3.configure(bg='lightyellow')
          self.label_poke3_txt.configure(bg='lightyellow')
          self.label_pand_omote_poke.configure(bg='lightblue')
          self.poke_select = 'poke3'
          
        elif self.poke_select == 'poke3':
          self.label_poke3.configure(bg='lightblue')
          self.label_poke3_txt.configure(bg='lightblue')
          self.label_poke4.configure(bg='lightyellow')
          self.label_poke4_txt.configure(bg='lightyellow')
          self.poke_select = 'poke4'
          
        elif self.poke_select == 'poke4':
          self.label_poke4.configure(bg='lightblue')
          self.label_poke4_txt.configure(bg='lightblue')
          self.label_poke5.configure(bg='lightyellow')
          self.label_poke5_txt.configure(bg='lightyellow')
          self.poke_select = 'poke5'
          
        elif self.poke_select == 'poke5':
          self.label_poke5.configure(bg='lightblue')
          self.label_poke5_txt.configure(bg='lightblue')
          self.label_poke6.configure(bg='lightyellow')
          self.label_poke6_txt.configure(bg='lightyellow')
          self.poke_select = 'poke6'
          
        elif self.poke_select == 'poke6':
          self.label_poke6.configure(bg='lightblue')
          self.label_poke6_txt.configure(bg='lightblue')
          self.label_poke_back.configure(bg='lightyellow')
          self.label_poke_back.configure(bg='lightyellow')
          self.poke_select = 'back'
           
        
    elif event.keysym == 'Right':                                                                     #right
      if self.label_poke.cget('text') == '>ポケモン':
        self.label_atk.config(text='たたかう', bg='lightgray')
        self.label_bag.config(bg='lightgray', text='バッグ')
        self.label_escape.config(bg='white', text='>にげる')
        self.label_poke.config(bg='lightgray', text='ポケモン')
      elif self.label_atk.cget('text') == '>たたかう':
        self.label_bag.config(text='>バッグ', bg='white')
        self.label_atk.config(bg='lightgray', text='たたかう')
        self.label_escape.config(bg='lightgray', text='にげる')
        self.label_poke.config(bg='lightgray')
      elif self.label_atk1.cget('text') == '>たいあたり':
        self.label_atk2.configure(text='>すなかけ')
        self.label_atk1.configure(text='たいあたり')
        if self.ally_pp2 <= 0:
          self.ally_pp2 = 0
        self.label_atk_setumei.configure(text=f'PP　{self.ally_pp2}/3\nわざたいぷ/ノーマル')
      elif self.poke_flag:
        if self.poke_select == 'panda':
          self.poke_select = 'inu'
          self.label_poke2.configure(bg='lightyellow')
          self.label_poke2_txt.configure(bg='lightyellow')
          self.label_inu_omote.configure(bg='lightyellow')
          self.inu_HP_point.configure(bg='lightyellow')
          self.label_inu_omote_poke.configure(bg='lightblue')
          self.label_poke_now.configure(bg='lightblue')
          self.label_pand_omote.configure(bg='lightblue')
          self.label_pand_omote_poke.configure(bg='lightyellow')
          self.label_ally_HP_point.configure(bg='lightblue')
          self.label_poke_now_txt.configure(bg='lightblue')

    elif event.keysym == 'Left':                                                                     #left
      if self.label_bag.cget('text') == '>バッグ':
        self.label_atk.config(text='>たたかう', bg='white')
        self.label_bag.config(bg='lightgray', text='バッグ')
        self.label_escape.config(bg='lightgray')
        self.label_poke.config(bg='lightgray', text='ポケモン')
      elif self.label_escape.cget('text') == '>にげる':
        self.label_bag.config(text='バッグ', bg='lightgray')
        self.label_atk.config(bg='lightgray')
        self.label_escape.config(bg='lightgray', text='にげる')
        self.label_poke.config(bg='white', text='>ポケモン')
      elif self.label_atk2.cget('text') == '>すなかけ':
        self.label_atk2.configure(text='すなかけ')
        self.label_atk1.configure(text='>たいあたり')
        self.label_atk_setumei.configure(text=f'PP　{self.ally_pp1}/10\nわざたいぷ/ノーマル')
      elif self.poke_flag:
        if self.poke_select == 'inu' or self.poke_select == 'poke3' or self.poke_select == 'poke4' or self.poke_select == 'poke5' or self.poke_select == 'poke6' or self.poke_select == 'back': 
          self.label_poke2.configure(bg='lightblue')
          self.label_poke2_txt.configure(bg='lightblue')
          self.label_inu_omote.configure(bg='lightblue')
          self.inu_HP_point.configure(bg='lightblue')
          self.label_poke3.configure(bg='lightblue')
          self.label_poke3_txt.configure(bg='lightblue')
          self.label_poke4.configure(bg='lightblue')
          self.label_poke4_txt.configure(bg='lightblue')
          self.label_poke5.configure(bg='lightblue')
          self.label_poke5_txt.configure(bg='lightblue')
          self.label_poke6.configure(bg='lightblue')
          self.label_poke6_txt.configure(bg='lightblue')
          self.label_poke_back.configure(bg='lightgray')
          self.label_poke_now.configure(bg='lightyellow')
          self.label_pand_omote.configure(bg='lightyellow')
          self.label_ally_HP_point.configure(bg='lightyellow')
          self.label_poke_now_txt.configure(bg='lightyellow')
          self.label_pand_omote_poke.configure(bg='lightblue')
          self.label_inu_omote_poke.configure(bg='lightyellow')
          self.poke_select = 'panda'
        
  def enemy_atack(self):
    if self.atk == 'ひっかく':
      if self.inu_flag:
        self.se_enemy_atk.play()
        self.progressbar_inu_HP['value'] -= self.enemy_A
        self.progressbar_inu_HP_poke['value'] -= self.enemy_A
        self.inu_HP_child = self.progressbar_inu_HP['value']
        if self.inu_HP_child <= 0:
          self.label_ally_HP_point.configure(text= f'0/{self.inu_HP_mother}')
        else:  
          self.label_ally_HP_point.configure(text= f'{self.inu_HP_child}/{self.inu_HP_mother}')
      else:
        self.se_enemy_atk.play()
        self.progressbar_ally_HP['value'] -= self.enemy_A
        self.progressbar_ally_HP_poke['value'] -= self.enemy_A
        self.ally_hp_child = self.progressbar_ally_HP["value"]
        if self.ally_hp_child <= 0:
          self.ally_hp_child = 0
          self.label_ally_HP_point.configure(text= f'0/{self.ally_hp_mother}')
        else:  
          self.label_ally_HP_point.configure(text= f'{self.ally_hp_child}/{self.ally_hp_mother}')
    elif self.atk == 'すなかけ':
      self.se_miss.play()
      
  def backspace_event(self, event):
    if self.ctl_setumei_flag == False:
      self.label_ctl_list.place_forget()
      self.ctl_setumei_flag = True
    elif self.bag_flag:
            self.label_item_setumei.configure(text='ポケモンの　たいりょくを\n6　かいふくする')
            self.tv_back.place_forget()
            self.label_item_setumei.place_forget()
            self.label_backpack.place_forget()
            self.label_atk.configure(text='>たたかう', bg='white')
            self.label_bag.configure(bg='lightgray')
            self.bag_flag = False
            self.index = 0
            self.label_atk.place(x=530, y=250)
            self.label_bag.place(x=670, y=250)
            self.label_poke.place(x=530, y=320)
            self.label_escape.place(x=670, y=320)
            self.label_buttle_cmd_list1.place(x=514, y=242)
            self.label_buttle_txt.place(x=10, y=10)
            self.label_buttle_txt2.place(x=20, y=250)
            self.canvas_buttle_txt.place(x=0, y=240)
            self.progressbar_enemy.place(x=100, y=70)
            self.label_enemy_HP.place(x=70, y=70)
            self.label_enemy_name_lv.place(x=100, y=50)
            self.label_ally_HP_point.place(x=630, y=185) 
            if self.inu_flag:
              self.label_inu_ura.place(x=100, y=100)
              self.progressbar_inu_HP.place(x=570, y=170)
              self.progressbar_inu_EXP.place(x=570, y=200)
            else:
              self.progressbar_ally_HP.place(x=570, y=170)
              self.progressbar_ally_EXP.place(x=570, y=200)
    elif self.poke_flag:
            self.label_poke_chenge.place_forget()
            self.label_poke_now.place_forget()
            self.label_poke2.place_forget()
            self.label_poke3.place_forget()
            self.label_poke4.place_forget()
            self.label_poke5.place_forget()
            self.label_poke6.place_forget()
            self.label_poke_now_txt.place_forget()
            self.label_poke2_txt.place_forget()
            self.label_poke3_txt.place_forget()
            self.label_poke4_txt.place_forget()
            self.label_poke5_txt.place_forget()
            self.label_poke6_txt.place_forget()
            self.label_inu_omote.place_forget()
            self.label_pand_omote.place_forget()
            self.progressbar_ally_HP_poke.place_forget()
            self.label_ally_HP_point.place_forget()
            self.progressbar_inu_HP_poke.place_forget()
            self.inu_HP_point.place_forget()
            self.label_poke_back.place_forget()
            self.label_select_poke.place_forget()
            
            self.label_pand_omote_poke.place_forget()
            self.label_inu_omote_poke.place_forget()
            self.label_ally_HP_point.lower()
            self.progressbar_inu_HP.lift()
            self.label_inu_omote_poke.configure(bg='lightyellow')
            self.label_pand_omote_poke.configure(bg='lightblue')

            self.label_atk.place(x=530, y=250)
            self.label_bag.place(x=670, y=250)
            self.label_escape.place(x=670, y=320)
            self.label_poke.place(x=530, y=320)
            self.label_buttle_cmd_list1.place(x=514, y=242)
            self.label_buttle_txt.place(x=10, y=10)
            self.label_buttle_txt2.place(x=20, y=250)
            self.canvas_buttle_txt.place(x=0, y=240)
            self.progressbar_enemy.place(x=100, y=70)
            self.label_enemy_HP.place(x=70, y=70)
            self.label_enemy_name_lv.place(x=100, y=50)  
            self.label_ally_HP_point.place(x=630, y=185)   
            self.progressbar_ally_HP.place(x=570, y=170)
            
            self.label_atk.configure(text='>たたかう', bg='white')
            self.label_poke2.configure(bg='lightblue')
            self.label_poke2_txt.configure(bg='lightblue')
            self.label_inu_omote.configure(bg='lightblue')
            self.inu_HP_point.configure(bg='lightblue')
            self.label_poke3.configure(bg='lightblue')
            self.label_poke3_txt.configure(bg='lightblue')
            self.label_poke4.configure(bg='lightblue')
            self.label_poke4_txt.configure(bg='lightblue')
            self.label_poke5.configure(bg='lightblue')
            self.label_poke5_txt.configure(bg='lightblue')
            self.label_poke6.configure(bg='lightblue')
            self.label_poke6_txt.configure(bg='lightblue')
            self.label_poke.configure(bg='lightgray')
            self.label_poke_now.configure(bg='lightyellow')
            self.label_pand_omote.configure(bg='lightyellow')
            self.label_ally_HP_point.configure(bg='lightblue', font=('','10'))
            self.label_poke_now_txt.configure(bg='lightyellow')
            self.label_poke_back.configure(bg='lightgray')
            self.progressbar_ally_HP.lift()
            self.progressbar_ally_EXP.lift()
            self.poke_select = 'panda'
            self.poke_flag = False
            self.label_ally_field.lift(self.label_inu_omote)
            if self.ally_rest <= 1:
              if self.inu_flag:
                self.progressbar_ally_HP.place_forget()
                self.progressbar_ally_EXP.place_forget()
                self.progressbar_inu_HP.place(x=570, y=170)
                self.progressbar_inu_EXP.place(x=570, y=200)
                self.progressbar_inu_HP.lift()
                self.progressbar_inu_EXP.lift()
    elif self.label_atk1.cget('text') == '>たいあたり' or self.label_atk2.cget('text') == '>すなかけ' or self.label_atk1.cget('text') == '>かみつく':
            self.label_buttle_cmd_list1.place_forget()
            self.label_buttle_cmd_list2.place_forget()
            self.label_atk1.place_forget()
            self.label_atk2.place_forget()
            self.label_atk_setumei.place_forget()
            self.enter_count_atk = 0
            if self.inu_flag:
              self.label_buttle_txt2.configure(text='いぬは　　どうする？')
            else:
              self.label_buttle_txt2.configure(text='パンダは　どうする？')
            self.label_buttle_cmd_list1.place(x=514, y=242)
            self.label_atk.place(x=530, y=250)
            self.label_bag.place(x=670, y=250)
            self.label_poke.place(x=530, y=320)
            self.label_escape.place(x=670, y=320)
            if self.inu_flag:
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='かみつく')
            else:
              self.label_atk.config(text='>たたかう')
              self.label_atk1.configure(text='たいあたり')
              self.label_atk2.configure(text='すなかけ')  

  def back_title(self):
    self.destroy()
    from title import Application
    Application(self.master)
  
  def ctl_setumei_event(self, event):
    if self.ctl_setumei_flag:
      self.label_ctl_list.place(x=50, y=20)
      self.label_ctl_list.lift()
      self.ctl_setumei_flag = False
    else:
      self.label_ctl_list.place_forget()
      self.ctl_setumei_flag = True
  
  def bag_back(self):
            self.tv_back.place_forget()
            self.label_item_setumei.place_forget()
            self.label_backpack.place_forget()
            self.label_atk.configure(text='>たたかう', bg='white')
            self.label_bag.configure(bg='lightgray')
            self.bag_flag = False
            self.index = 0
            self.label_atk.place(x=530, y=250)
            self.label_bag.place(x=670, y=250)
            self.label_poke.place(x=530, y=320)
            self.label_escape.place(x=670, y=320)
            self.label_buttle_cmd_list1.place(x=514, y=242)
            self.label_buttle_txt.place(x=10, y=10)
            self.label_buttle_txt2.place(x=20, y=250)
            self.canvas_buttle_txt.place(x=0, y=240)
            self.progressbar_enemy.place(x=100, y=70)
            self.label_enemy_HP.place(x=70, y=70)
            self.label_enemy_name_lv.place(x=100, y=50)
            self.label_ally_HP_point.place(x=630, y=185) 
            if self.inu_flag:
              self.progressbar_inu_HP.place(x=570, y=170)
              self.progressbar_inu_EXP.place(x=570, y=200)
              self.label_inu_ura.place(x=100, y=100)
            else:
              self.progressbar_ally_HP.place(x=570, y=170)
              self.progressbar_ally_EXP.place(x=570, y=200)
  def tatakau(self):
        if self.inu_flag:                      #いぬ
          self.label_buttle_cmd_list2.place(x=1, y=242)
          self.label_atk.configure(text='たたかう')
          self.label_atk1.configure(text='>かみつく')
          self.label_atk.place_forget()
          self.label_poke.place_forget()
          self.label_bag.place_forget()
          self.label_escape.place_forget()
          self.label_atk1.place(x=10, y=250)
          self.label_atk_setumei.place(x=530, y=250)
          self.label_atk_setumei.configure(text=f'PP　{self.inu_pp1}/10\nわざたいぷ/ノーマル')
          if self.ally_pp1 <= 0:
            self.ally_pp1 = 0
          self.label_atk_setumei.configure(text=f'PP　{self.inu_pp1}/10\nわざたいぷ/ノーマル')
        else:
          self.label_buttle_cmd_list2.place(x=1, y=242)
          self.label_atk.configure(text='たたかう')
          self.label_atk1.configure(text='>たいあたり')
          self.label_atk.place_forget()
          self.label_poke.place_forget()
          self.label_bag.place_forget()
          self.label_escape.place_forget()
          self.label_atk1.place(x=10, y=250)
          self.label_atk2.place(x=300, y=250)
          self.label_ally_field.lift(self.label_inu_omote)
          self.label_atk_setumei.place(x=530, y=250)
          if self.ally_pp1 <= 0:
            self.ally_pp1 = 0
          self.label_atk_setumei.configure(text=f'PP　{self.ally_pp1}/10\nわざたいぷ/ノーマル')
          
  def kaihuku(self):
        if self.inu_flag:                      #いぬ
          self.label_buttle_cmd_list2.place(x=1, y=242)
          self.label_atk.configure(text='たたかう')
          self.label_atk1.configure(text='>かみつく')
          self.label_atk.place_forget()
          self.label_poke.place_forget()
          self.label_bag.place_forget()
          self.label_escape.place_forget()
          self.label_atk1.place(x=10, y=250)
          self.label_atk_setumei.place(x=530, y=250)
          self.label_atk_setumei.configure(text=f'PP　{self.inu_pp1}/10\nわざたいぷ/ノーマル')
          if self.ally_pp1 <= 0:
            self.ally_pp1 = 0
          self.label_atk_setumei.configure(text=f'PP　{self.inu_pp1}/10\nわざたいぷ/ノーマル')
        else:
          self.label_buttle_cmd_list2.place(x=1, y=242)
          self.label_atk.configure(text='たたかう')
          self.label_atk1.configure(text='>たいあたり')
          self.label_atk.place_forget()
          self.label_poke.place_forget()
          self.label_bag.place_forget()
          self.label_escape.place_forget()
          self.label_atk1.place(x=10, y=250)
          self.label_atk2.place(x=300, y=250)
          self.label_atk_setumei.place(x=530, y=250)
          if self.ally_pp1 <= 0:
            self.ally_pp1 = 0
          self.label_atk_setumei.configure(text=f'PP　{self.ally_pp1}/10\nわざたいぷ/ノーマル')
      
        self.label_buttle_cmd_list1.place_forget()
        self.label_buttle_cmd_list2.place_forget()
        self.label_atk1.place_forget()
        self.label_atk2.place_forget()
        self.label_atk_setumei.place_forget()
        if self.inu_flag:
          self.label_buttle_txt2.configure(text='いぬのたいりょくが　かいふくした')
          self.enter_count_atk = 1
          self.kaihuku_flag = True
        else:
          self.label_buttle_txt2.configure(text='パンダのたいりょくが　かいふくした')
          self.enter_count_atk = 1
          self.kaihuku_flag = True
    
  def change(self):
          self.label_poke_chenge.place_forget()
          self.label_poke_now.place_forget()
          self.label_poke2.place_forget()
          self.label_poke3.place_forget()
          self.label_poke4.place_forget()
          self.label_poke5.place_forget()
          self.label_poke6.place_forget()
          self.label_poke_now_txt.place_forget()
          self.label_poke2_txt.place_forget()
          self.label_poke3_txt.place_forget()
          self.label_poke4_txt.place_forget()
          self.label_poke5_txt.place_forget()
          self.label_poke6_txt.place_forget()
          self.label_inu_omote.place_forget()
          self.label_pand_omote.place_forget()
          self.progressbar_ally_HP_poke.place_forget()
          self.label_ally_HP_point.place_forget()
          self.progressbar_inu_HP_poke.place_forget()
          self.inu_HP_point.place_forget()
          self.label_poke_back.place_forget()
          self.label_select_poke.place_forget()

          self.label_atk.place(x=530, y=250)
          self.label_bag.place(x=670, y=250)
          self.label_escape.place(x=670, y=320)
          self.label_poke.place(x=530, y=320)
          self.label_buttle_cmd_list1.place(x=514, y=242)
          self.label_buttle_txt.place(x=10, y=10)
          self.label_buttle_txt2.place(x=20, y=250)
          self.canvas_buttle_txt.place(x=0, y=240)
          self.progressbar_enemy.place(x=100, y=70)
          self.label_enemy_HP.place(x=70, y=70)
          self.label_enemy_name_lv.place(x=100, y=50)  
          self.label_ally_HP_point.place(x=630, y=185)   
          self.progressbar_ally_HP.place(x=570, y=170)

          self.label_atk.configure(text='>たたかう', bg='white')
          self.label_poke2.configure(bg='lightblue')
          self.label_poke2_txt.configure(bg='lightblue')
          self.label_inu_omote.configure(bg='lightblue')
          self.inu_HP_point.configure(bg='lightblue')
          self.label_poke3.configure(bg='lightblue')
          self.label_poke3_txt.configure(bg='lightblue')
          self.label_poke4.configure(bg='lightblue')
          self.label_poke4_txt.configure(bg='lightblue')
          self.label_poke5.configure(bg='lightblue')
          self.label_poke5_txt.configure(bg='lightblue')
          self.label_poke6.configure(bg='lightblue')
          self.label_poke6_txt.configure(bg='lightblue')
          self.label_poke.configure(bg='lightgray')
          self.label_poke_now.configure(bg='lightyellow')
          self.label_pand_omote.configure(bg='lightyellow')
          self.label_ally_HP_point.configure(bg='lightblue', font=('','10'))
          self.label_poke_now_txt.configure(bg='lightyellow')
          self.label_poke_back.configure(bg='lightgray')
          self.progressbar_ally_HP.lift(self.label_ally_HP_point)
          self.progressbar_ally_EXP.lift(self.label_ally_HP_point)
          self.poke_select = 'panda'
          self.poke_flag = False    
          self.inu_flag = True
          self.label_pand_omote_poke.configure(bg='lightblue')
          self.label_inu_omote_poke.configure(bg='lightyellow')

