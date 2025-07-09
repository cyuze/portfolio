import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from function_py25 import get_books
from function_py25 import get_books_adomin
from function_py25 import get_books2_adomin
from function_py25 import get_search_books
from function_py25 import get_book
from function_py25 import delete_book
from function_py25 import get_mail
from tkinter import messagebox
from pygame import mixer
from account import Account
import threading
from book_register import BookRegister
from book_edit import BookEdit

class AdominLibrary(tk.Frame):
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
        self.title_label = tk.Label(self, text='図書管理アプリ(管理者)', font=('', 20))
        self.title_label.place(x=self.width/2 - 145, y=40)
        # 検索バー生成と配置
        self.search_entry = tk.Entry(self,width=50)
        self.search_entry.place(x=self.width/2 - 170, y=100)
        # 検索ボタン生成と配置
        self.search_btn = tk.Button(self, text='検索', command=self.search_event)
        self.search_btn.place(x=self.width/2 + 150, y=95)
        # 検索リセットボタン生成と配置
        self.search_btn = tk.Button(self, text='一覧リセット', command=self.search_reset_event)
        self.search_btn.place(x=self.width/2 + 200, y=95)
        # 図書登録ボタン生成と配置
        self.rental_btn = tk.Button(self, text='登録', command=self.book_register_event, font=('',20))
        self.rental_btn.place(x=self.width/2 + 330, y=500)   
        # 図書削除ボタン生成と配置
        self.rental_btn = tk.Button(self, text='削除', command=self.book_remove_event, font=('',20))
        self.rental_btn.place(x=self.width/2 + 228, y=500)     
        # 図書編集ボタン生成と配置
        self.rental_btn = tk.Button(self, text='編集', command=self.book_edit_event, font=('',20))
        self.rental_btn.place(x=self.width/2 + 126, y=500)      
        # ツリービュー生成と配置
        self.tree_view = ttk.Treeview(self, show='headings', height=15)
        self.tree_view.place(x=self.width/2 - 395, y=150)
        # ツリービューヘッダー生成と配置
        header = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN')
        self.tree_view.configure(columns=header)
        # ツリービューヘッダーのテキスト生成と配置
        self.tree_view.heading('book_id', text='本ID')
        self.tree_view.heading('title', text='タイトル')
        self.tree_view.heading('genre', text='ジャンル')
        self.tree_view.heading('author', text='著者')
        self.tree_view.heading('publisher', text='出版社')
        self.tree_view.heading('ISBN', text='ISBN番号')
        # ツリービューヘッダーの横幅設定
        self.tree_view.column('book_id', width=50)
        self.tree_view.column('title', width=150)
        self.tree_view.column('genre', width=100)
        self.tree_view.column('author', width=200)
        self.tree_view.column('publisher', width=200)
        self.tree_view.column('ISBN', width=100)
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

    # 図書登録ボタンのイベント
    def book_register_event(self):
        self.master.config(menu='')
        self.destroy()
        BookRegister(self.master, self.mail)

    # 図書削除ボタンのイベント
    def book_remove_event(self):
        if self.kaesita_flag:
            selected_item = self.tree_view2.selection()[0]
            item = self.tree_view2.item(selected_item, "values")
                        
        if self.kariteru_flag:
            selected_item = self.tree_view3.selection()[0]
            item = self.tree_view3.item(selected_item, "values")

            
        if not self.kariteru_flag and not self.kaesita_flag:
            selected_item = self.tree_view.selection()[0]     
            item = self.tree_view.item(selected_item, "values")  
        
        book = get_book(item[0])
        if messagebox.askyesno('確認', f'『{book[1]}』を削除します。'):
            if book[6] == '不可':
                print(book[6])
                messagebox.showinfo('削除不可', '指定された書籍は貸出中です。')
            else:
                delete_book(item[0])
                if self.kaesita_flag:
                    self.reset_tree2()
                else:
                    self.reset_tree()
                messagebox.showinfo('削除完了', '指定された書籍を削除しました。')
        

    # 図書編集ボタンのイベント
    def book_edit_event(self):
        if self.kaesita_flag:
            selected_item = self.tree_view2.selection()[0]
            item = self.tree_view2.item(selected_item, "values")
                        
        if self.kariteru_flag:
            selected_item = self.tree_view3.selection()[0]
            item = self.tree_view3.item(selected_item, "values")

            
        if not self.kariteru_flag and not self.kaesita_flag:
            selected_item = self.tree_view.selection()[0]     
            item = self.tree_view.item(selected_item, "values")  
                            
        self.kaesita_flag = False
        self.kariteru_flag = False  
        
        id = item[0]
        title = item[1]
        ganre = item[2]
        author = item[3]
        publisher = item[4]
        isbn = item[5]
        
        self.master.config(menu='')
        self.destroy()
        BookEdit(self.master, self.mail, id, title, ganre, author, publisher, isbn)
    
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
            self.tree_view3.place(x=self.width/2 - 570, y=150)
            # ツリービューヘッダー生成と配置
            header3 = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN', 'user-name', 'user-mail', 'rental-date')
            self.tree_view3.configure(columns=header3)
            # ツリービューヘッダーのテキスト生成と配置
            self.tree_view3.heading('book_id', text='本ID')
            self.tree_view3.heading('title', text='タイトル')
            self.tree_view3.heading('genre', text='ジャンル')
            self.tree_view3.heading('author', text='著者')
            self.tree_view3.heading('publisher', text='出版社')
            self.tree_view3.heading('ISBN', text='ISBN番号')
            self.tree_view3.heading('user-name', text='ユーザ名')
            self.tree_view3.heading('user-mail', text='メール')
            self.tree_view3.heading('rental-date', text='借りた日')
            # ツリービューヘッダーの横幅設定
            self.tree_view3.column('book_id', width=50)
            self.tree_view3.column('title', width=150)
            self.tree_view3.column('genre', width=100)
            self.tree_view3.column('author', width=150)
            self.tree_view3.column('publisher', width=150)
            self.tree_view3.column('ISBN', width=100)
            self.tree_view3.column('user-name', width=130)
            self.tree_view3.column('user-mail', width=200)
            self.tree_view3.column('rental-date', width=100)

            
            books = get_books_adomin()
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
            self.tree_view2.place(x=self.width/2 - 570, y=150)
            # ツリービューヘッダー生成と配置
            header2 = ('book_id', 'title', 'genre', 'author', 'publisher', 'ISBN','user-name', 'mail', 'rental_date', 'return_date')
            self.tree_view2.configure(columns=header2)
            # ツリービューヘッダーのテキスト生成と配置
            self.tree_view2.heading('book_id', text='本ID')
            self.tree_view2.heading('title', text='タイトル')
            self.tree_view2.heading('genre', text='ジャンル')
            self.tree_view2.heading('author', text='著者')
            self.tree_view2.heading('publisher', text='出版社')
            self.tree_view2.heading('ISBN', text='ISBN番号')
            self.tree_view2.heading('user-name', text='名前')
            self.tree_view2.heading('mail', text='メール')
            self.tree_view2.heading('rental_date', text='借りた日')
            self.tree_view2.heading('return_date', text='返した日')
            # ツリービューヘッダーの横幅設定
            self.tree_view2.column('book_id', width=50)
            self.tree_view2.column('title', width=150)
            self.tree_view2.column('genre', width=100)
            self.tree_view2.column('author', width=120)
            self.tree_view2.column('publisher', width=120)
            self.tree_view2.column('ISBN', width=100)
            self.tree_view2.column('user-name', width=100)
            self.tree_view2.column('mail', width=200)
            self.tree_view2.column('rental_date', width=100)
            self.tree_view2.column('return_date', width=100)
            # ツリービューにデータ生成と挿入
            books = get_books2_adomin()
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
            books = get_books2_adomin()
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
                
    def reset_tree2(self):
        self.title_label.configure(bg = 'white')
        if self.kariteru_flag: 
            self.tree_view3.place_forget()
            self.kariteru_flag = False
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
        books = get_books2_adomin()
        for item in self.tree_view2.get_children():
            self.tree_view2.delete(item)
        for book in books:
            self.tree_view2.insert('', index='end', values=book)
        self.kaesita_flag = True
        

    
if __name__ == '__main__':
  root = tk.Tk()
  app = AdominLibrary(root,'c.yuze.sys24@morijyobi.ac.jp')
  app.mainloop()