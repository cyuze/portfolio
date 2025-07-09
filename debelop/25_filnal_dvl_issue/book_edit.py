import tkinter as tk
from function_py25 import login
from PIL import Image, ImageTk
from function_py25 import get_book
from function_py25 import update_book
from function_py25 import update_book2
from tkinter import messagebox


class BookEdit(tk.Frame):
    def __init__(self, master, mail, id, book_title, genre, author, publisher, isbn):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.master = master
        self.mail = mail
        self.id = id
        self.book_title = book_title
        self.genre = genre
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        master.state('zoomed')
        master.geometry('400x400')
        master.title('書籍編集画面')

        self.create_widgets()

    # ウィジェットを配置して画面作るメソッド
    def create_widgets(self):
        # ウィンドウの縦横幅を入手
        self.master.update_idletasks()
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()
        # 生成
        # 画像読み込み
        cimg1 = Image.open('C:/Users/yuze/Pictures/図書管理アプリ/本棚.png')
        cimg1 = cimg1.resize((self.width, self.height), Image.Resampling.LANCZOS)
        # 画像ファイルオブジェクトの生成
        self.img1 = ImageTk.PhotoImage(cimg1)
        # 画像オブジェクトをラベルに張り付けて表示
        self.bg_img_label = tk.Label(self, image=self.img1)
        self.bg_img_label.place(x=0, y=0)
        self.bg_img_label.lower()

        self.big_title_label = tk.Label(self, text='図書管理アプリ', font=('', 20))
        self.sub_title_label = tk.Label(self, text='編集内容', font=('', 10))
        self.back_label = tk.Label(self, width=60, height=40)
                # self.back_labelの四隅ラベル
        self.corner_label1 = tk.Label(self, bg='tomato', width=2,height=1)
        self.corner_label2 = tk.Label(self, bg='palegreen', width=2,height=1)
        self.corner_label3 = tk.Label(self, bg='palegreen', width=2,height=1)
        self.corner_label4 = tk.Label(self, bg='tomato', width=2,height=1)

        self.id_label = tk.Label(self, text='ID:')
        self.title_label = tk.Label(self, text='タイトル:')
        self.genre_label = tk.Label(self, text='ジャンル:')
        self.author_label = tk.Label(self, text='著者:')
        self.publisher_label = tk.Label(self, text='出版社:')
        self.ISBN_label = tk.Label(self, text='ISBN番号:')

        self.id_entry = tk.Entry(self, width=30)
        self.id_entry.insert(0, self.id)
        self.title_entry = tk.Entry(self, width=30)
        self.title_entry.insert(0, self.book_title)
        self.genre_entry = tk.Entry(self, width=30)
        self.genre_entry.insert(0, self.genre)
        self.author_entry = tk.Entry(self, width=30)
        self.author_entry.insert(0, self.author)
        self.publisher_entry = tk.Entry(self, width=30)
        self.publisher_entry.insert(0, self.publisher)
        self.ISBN_entry = tk.Entry(self, width=30)
        self.ISBN_entry.insert(0, self.isbn)
        
        self.edit_btn = tk.Button(self, text='保存', font=('', 20), command=self.edit_event)
        self.back_btn = tk.Button(self, text='戻る', font=('', 20), command=self.back_event)

        # 配置
        self.back_label.place(x=self.width/2 - 220, y=20)
        self.back_label.lower(self.big_title_label)
                # ラベルの位置を取得して四隅に配置
        self.update_idletasks()  # ウィジェットを更新して最新の位置情報を取得
        back_label_x = self.back_label.winfo_x()
        back_label_y = self.back_label.winfo_y()
        back_label_width = self.back_label.winfo_width()
        back_label_height = self.back_label.winfo_height()

        self.corner_label1.place(x=back_label_x, y=back_label_y)
        self.corner_label2.place(x=back_label_x+ back_label_width - 20, y=back_label_y)
        self.corner_label3.place(x=back_label_x, y=back_label_y + back_label_height - 21)
        self.corner_label4.place(x=back_label_x + back_label_width - 20, y=back_label_y + back_label_height - 21)

        self.big_title_label.place(x=self.width/2 - 100, y=40)
        self.sub_title_label.place(x=self.width/2 - 35, y=125)

        self.id_label.place(x=self.width/2 - 90, y=160)
        self.id_entry.place(x=self.width/2 - 65, y=160)
        self.title_label.place(x=self.width/2 - 115, y=210)
        self.title_entry.place(x=self.width/2 - 65, y=210)
        self.genre_label.place(x=self.width/2 - 115, y=260)
        self.genre_entry.place(x=self.width/2 - 65, y=260)
        self.author_label.place(x=self.width/2 - 103, y=310)
        self.author_entry.place(x=self.width/2 - 65, y=310)
        self.publisher_label.place(x=self.width/2 - 115, y=360)
        self.publisher_entry.place(x=self.width/2 - 65, y=360)
        self.ISBN_label.place(x=self.width/2 - 128, y=410)
        self.ISBN_entry.place(x=self.width/2 - 65, y=410)
        
        self.edit_btn.place(x=self.width/2 + 45, y=500)
        self.back_btn.place(x=self.width/2 - 65, y=500)
        
    def edit_event(self):
        new_title = self.title_entry.get()
        new_genre = self.genre_entry.get()
        new_author = self.author_entry.get()
        new_publisher = self.publisher_entry.get()
        new_isbn = self.ISBN_entry.get()
        new_id = self.id_entry.get()
        book = get_book(self.id)
        book_exist = get_book(new_id)
        book_exist2 = get_book(self.id)
        
        if new_id != '':
            try:
                new_id = int(self.id_entry.get())  # IDを整数に変換
                if new_id <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showinfo('登録不可', 'IDは正の整数でお願いします')
                return
            if new_title == '' or new_genre == '' or new_author == '' or new_publisher == '' or new_isbn == '':
                messagebox.showinfo('登録不可', '空欄を埋めてください。')
            elif book[6] == '可能' and book_exist is None:
                update_book(self.id, new_id,new_title,new_genre,new_author,new_publisher,new_isbn)
                messagebox.showinfo('保存終了', '書籍のデータを更新しました')
                self.destroy()
                BookEdit(self.master, self.mail, new_id, new_title, new_genre, new_author, new_publisher, new_isbn)
            elif book[6] == '可能' and book_exist2[0] == new_id:
                update_book2(new_id, new_title,new_genre,new_author,new_publisher,new_isbn)
                messagebox.showinfo('保存終了', '書籍のデータを更新しました')
                self.destroy()
                BookEdit(self.master, self.mail, new_id, new_title, new_genre, new_author, new_publisher, new_isbn)
            else:
                messagebox.showinfo('保存不可', 'その書籍は貸出中もしくは、同じIDが既に存在しています。')
                print('edit2')
                print(book_exist[0])
                print(new_id)
        elif new_title == '' or new_genre == '' or new_author == '' or new_publisher == '' or new_isbn == '':
            messagebox.showinfo('登録不可', '空欄を埋めてください。')         
        elif book[6] == '可能' and book_exist is None:
            update_book(self.id, new_id,new_title,new_genre,new_author,new_publisher,new_isbn)
            messagebox.showinfo('保存終了', '書籍のデータを更新しました')
            self.destroy()
            BookEdit(self.master, self.mail, new_id, new_title, new_genre, new_author, new_publisher, new_isbn)
        elif book[6] == '可能' and book_exist[0] == new_id:
            update_book2(new_id, new_title,new_genre,new_author,new_publisher,new_isbn)
            messagebox.showinfo('保存終了', '書籍のデータを更新しました')
            self.destroy()
            BookEdit(self.master, self.mail, new_id, new_title, new_genre, new_author, new_publisher, new_isbn)   
        else:
            messagebox.showinfo('保存不可', 'その書籍は貸出中もしくは、同じIDが既に存在しています。')
            print('edit1')
        


    
    def back_event(self):
        from adominLibrary import AdominLibrary
        self.destroy()
        AdominLibrary(self.master, self.mail)