import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from function_py25 import get_books
from function_py25 import get_search_books
from function_py25 import get_rental_books
from function_py25 import get_return_books
from function_py25 import send_mail
from function_py25 import get_name
from function_py25 import get_mail
from function_py25 import return_book
from function_py25 import insert_rental_return
from tkinter import messagebox
from pygame import mixer
from account import Account
import threading
import time

class Library(tk.Frame):
    def __init__(self, master, mail):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.master = master
        master.state('zoomed')
        master.title('図書管理アプリ')
        self.mail = mail

        
        self.create_widgets()

    # ウィジェットを配置して画面作るメソッド
    def create_widgets(self):
        t1 = threading.Thread(target=self.thread)
        t1.start()
        print('library')
        print(self.mail)
        # BGM 
        mixer.init()
        mixer.music.load('C:/Users/yuze/Music/図書管理/maou_bgm_piano27.mp3')
        # ウィンドウの縦横幅を入手
        self.master.update_idletasks()
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()
        # 画像読み込み
        cimg1 = Image.open('C:/Users/yuze/Pictures/図書管理アプリ/本棚.png')
        cimg1 = cimg1.resize((self.width, self.height), Image.Resampling.LANCZOS)
        # 画像ファイルオブジェクトの生成
        self.img1 = ImageTk.PhotoImage(cimg1)
        # 画像オブジェクトをラベルに張り付けて表示
        self.bg_img_label = tk.Label(self, image=self.img1)
        self.bg_img_label.place(x=0, y=0)
        self.bg_img_label.lower()
        # タイトル生成と配置
        self.title_label = tk.Label(self, text='図書管理アプリ', font=('', 20))
        self.title_label.place(x=self.width/2 - 100, y=40)
        # 検索バー生成と配置
        self.search_entry = tk.Entry(self,width=50)
        self.search_entry.place(x=self.width/2 - 170, y=100)
        # 検索ボタン生成と配置
        self.search_btn = tk.Button(self, text='検索', command=self.search_event)
        self.search_btn.place(x=self.width/2 + 150, y=95)
        # 検索リセットボタン生成と配置
        self.search_btn = tk.Button(self, text='一覧リセット', command=self.search_reset_event)
        self.search_btn.place(x=self.width/2 + 200, y=95)
        # 借りるボタン生成と配置
        self.rental_btn = tk.Button(self, text='借りる', command=self.rental_event, font=('',20))
        self.rental_btn.place(x=self.width/2 + 350, y=500)   
        # 返すボタン生成と配置
        self.rental_btn = tk.Button(self, text='返す', command=self.return_event, font=('',20))
        self.rental_btn.place(x=self.width/2 + 250, y=500)       
        # ツリービュー生成と配置
        self.tree_view = ttk.Treeview(self, show='headings', height=15)
        self.tree_view.place(x=self.width/2 - 440, y=150)
        # ツリービューヘッダー生成と配置
        header = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN', 'loan-status')
        self.tree_view.configure(columns=header)
        # ツリービューヘッダーのテキスト生成と配置
        self.tree_view.heading('book_id', text='本ID')
        self.tree_view.heading('title', text='タイトル')
        self.tree_view.heading('genre', text='ジャンル')
        self.tree_view.heading('author', text='著者')
        self.tree_view.heading('publisher', text='出版社')
        self.tree_view.heading('ISBN', text='ISBN番号')
        self.tree_view.heading('loan-status', text='貸出状況')
        # ツリービューヘッダーの横幅設定
        self.tree_view.column('book_id', width=50)
        self.tree_view.column('title', width=150)
        self.tree_view.column('genre', width=100)
        self.tree_view.column('author', width=200)
        self.tree_view.column('publisher', width=200)
        self.tree_view.column('ISBN', width=100)
        self.tree_view.column('loan-status', width=80)
        # ツリービューにデータ生成と挿入
        books = get_books(self.mail)
        book1 = 0
        book2 = 0    
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        for book in books:
            book2 = book[0]
            if book2 != book1:
                self.tree_view.insert('', index='end', values=book)
            else:
                pass
            book1 = book[0]
        # メニューバーの生成
        menubar = tk.Menu(self.master)
        # メニューバーを配置
        self.master.configure(menu=menubar)
        # メニューバーに追加するメニューを生成
        history_menu = tk.Menu(menubar, tearoff=0)
        account_menu = tk.Menu(menubar, tearoff=0)
        # メニューバーに追加
        menubar.add_cascade(label='アカウント', menu=account_menu)
        menubar.add_cascade(label='履歴', menu=history_menu)
        # メニューにイベントを追加
        history_menu.add_command(label='借りてる本', command=self.rental_book_event)
        history_menu.add_command(label='返した本', command=self.return_book_event)
        account_menu.add_command(label='アカウント', command=self.account_event)
        account_menu.add_command(label='ログイン', command=self.login_event)
        # 借りてるメニューフラグと返した本フラグ
        self.kariteru_flag = False
        self.kaesita_flag = False

    # 検索ボタンのイベント
    def search_event(self):
        if self.kariteru_flag: 
            self.tree_view3.place_forget()
            self.kariteru_flag = False
        if self.kaesita_flag: 
            self.tree_view2.place_forget()
            self.kaesita_flag = False
        self.title_label.configure(bg = 'white')
        search_value = self.search_entry.get()
        book1 = 0
        book2 = 0
        books = get_search_books(search_value, self.mail) 
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        for book in books:
            book2 = book[0]
            if book1 != book2:
                self.tree_view.insert('', index='end', values=book)
            else:
                pass
            book1 = book[0]

    # 検索リセットボタンのイベント
    def search_reset_event(self):
        self.reset_tree()        

    # 借りるボタンのイベント
    def rental_event(self):
        select_item = self.tree_view.selection()[0]
        select_book = self.tree_view.item(select_item, 'values')
        if select_book[6] == '可能':
            if messagebox.askyesno('貸出', f'タイトル：{select_book[1]}\nジャンル：{select_book[2]}\n著者：{select_book[3]}\n\n間違いありませんか？'):
                insert_rental_return(self.mail, select_book[0])
                self.reset_tree()  
                name = get_name(self.mail)[0]
                send_mail(self.mail, '図書管理アプリ', f'『{select_book[1]}』の貸し出しを完了しました。{name}さん、ご利用いただきありがとうございます。')
        else:
            messagebox.showinfo('貸出不可', '貸出できません。')   

    # 返すボタンのイベント
    def return_event(self):
        if self.kariteru_flag:
            select_item = self.tree_view3.selection()[0]
            select_book = self.tree_view3.item(select_item, 'values')
        else:
            select_item = self.tree_view.selection()[0]
            select_book = self.tree_view.item(select_item, 'values')
        if select_book[6] == '借りてる本':
            if messagebox.askyesno('返却', f'タイトル：{select_book[1]}\nジャンル：{select_book[2]}\n著者：{select_book[3]}\n\n間違いありませんか？'):
                return_book(select_book[0])
                if self.kariteru_flag:
                    books = get_rental_books(self.mail)
                    for item in self.tree_view3.get_children():
                        self.tree_view3.delete(item)
                    for book in books:
                        self.tree_view3.insert('', index='end', values=book)
                else:
                    self.reset_tree()
        else:
            messagebox.showinfo('返却不可', '返却できません。')
    
    # ログインメニューのイベント
    def login_event(self):
        if messagebox.askyesno('再ログイン', 'ログイン画面に移動します。'):
            from login import Login
            self.master.config(menu='')
            self.destroy()
            Login(self.master)
            
    # 借りてるメニューのイベント
    def rental_book_event(self):
        self.title_label.configure(bg = 'tomato')
        if self.kaesita_flag: 
            self.tree_view2.place_forget()
            self.kaesita_flag = False

        
        if not self.kariteru_flag:
            # ツリービュー生成と配置
            self.tree_view3 = ttk.Treeview(self, show='headings', height=15)
            self.tree_view3.place(x=self.width/2 - 490, y=150)
            # ツリービューヘッダー生成と配置
            header3 = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN', 'loan-status', 'rental-date')
            self.tree_view3.configure(columns=header3)
            # ツリービューヘッダーのテキスト生成と配置
            self.tree_view3.heading('book_id', text='本ID')
            self.tree_view3.heading('title', text='タイトル')
            self.tree_view3.heading('genre', text='ジャンル')
            self.tree_view3.heading('author', text='著者')
            self.tree_view3.heading('publisher', text='出版社')
            self.tree_view3.heading('ISBN', text='ISBN番号')
            self.tree_view3.heading('loan-status', text='貸出状況')
            self.tree_view3.heading('rental-date', text='借りた日')
            # ツリービューヘッダーの横幅設定
            self.tree_view3.column('book_id', width=50)
            self.tree_view3.column('title', width=150)
            self.tree_view3.column('genre', width=100)
            self.tree_view3.column('author', width=200)
            self.tree_view3.column('publisher', width=200)
            self.tree_view3.column('ISBN', width=100)
            self.tree_view3.column('loan-status', width=80)
            self.tree_view3.column('rental-date', width=100)

            
            books = get_rental_books(self.mail)
            for item in self.tree_view3.get_children():
                self.tree_view3.delete(item)
            for book in books:
                self.tree_view3.insert('', index='end', values=book)
            self.kariteru_flag = True

    # 返したメニューのイベント
    def return_book_event(self):
        self.title_label.configure(bg = 'pale green')
        if self.kariteru_flag: 
            self.tree_view3.place_forget()
            self.kariteru_flag = False
            
        if not self.kaesita_flag:
            # ツリービュー生成と配置
            self.tree_view2 = ttk.Treeview(self, show='headings', height=15)
            self.tree_view2.place(x=self.width/2 - 500, y=150)
            # ツリービューヘッダー生成と配置
            header2 = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN', 'rental_date', 'return_date')
            self.tree_view2.configure(columns=header2)
            # ツリービューヘッダーのテキスト生成と配置
            self.tree_view2.heading('book_id', text='本ID')
            self.tree_view2.heading('title', text='タイトル')
            self.tree_view2.heading('genre', text='ジャンル')
            self.tree_view2.heading('author', text='著者')
            self.tree_view2.heading('publisher', text='出版社')
            self.tree_view2.heading('ISBN', text='ISBN番号')
            self.tree_view2.heading('rental_date', text='借りた日')
            self.tree_view2.heading('return_date', text='返した日')
            # ツリービューヘッダーの横幅設定
            self.tree_view2.column('book_id', width=50)
            self.tree_view2.column('title', width=150)
            self.tree_view2.column('genre', width=100)
            self.tree_view2.column('author', width=200)
            self.tree_view2.column('publisher', width=200)
            self.tree_view2.column('ISBN', width=100)
            self.tree_view2.column('rental_date', width=100)
            self.tree_view2.column('return_date', width=100)
            # ツリービューにデータ生成と挿入
            books = get_books(self.mail)
            book1 = 0
            book2 = 0    
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            for book in books:
                book2 = book[0]
                if book2 != book1:
                    self.tree_view2.insert('', index='end', values=book)
                else:
                    pass
                book1 = book[0]
            books = get_return_books(self.mail)
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            for book in books:
                self.tree_view2.insert('', index='end', values=book)
            self.kaesita_flag = True
            
            
    # リセットツリービュー
    def reset_tree(self):
        self.title_label.configure(bg = 'white')
        if self.kariteru_flag: 
            self.tree_view3.place_forget()
            self.kariteru_flag = False
        if self.kaesita_flag: 
            self.tree_view2.place_forget()
            self.kaesita_flag = False
        books = get_books(self.mail)
        book1 = 0
        book2 = 0    
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        for book in books:
            book2 = book[0]
            if book2 != book1:
                self.tree_view.insert('', index='end', values=book)
            else:
                pass
            book1 = book[0]
     
    def sound_label_event(self, event):
        bg= self.sound_label.cget('bg')
        if bg == 'lightblue':
            self.sound_label.configure(bg='light salmon')
            mixer.music.stop()
            
        else:
            self.sound_label.configure(bg='lightblue')
            mixer.music.play(-1)
            
    def account_event(self):
        root2 = tk.Tk()
        Account(root2, self.mail, self.master)
    
    def thread(self):
        while True:
            m = get_mail(self.mail)
            if m is None:
                self.destroy()