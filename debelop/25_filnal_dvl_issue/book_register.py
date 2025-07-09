import tkinter as tk
from function_py25 import login
from function_py25 import get_book
from function_py25 import insert_book
from PIL import Image, ImageTk
from tkinter import messagebox


class BookRegister(tk.Frame):
    def __init__(self, master, mail):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.master = master
        self.mail = mail
        master.state('zoomed')
        master.geometry('400x400')
        master.title('書籍登録画面')

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
        self.sub_title_label = tk.Label(self, text='登録内容', font=('', 10))
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
        self.title_entry = tk.Entry(self, width=30)
        self.genre_entry = tk.Entry(self, width=30)
        self.author_entry = tk.Entry(self, width=30)
        self.publisher_entry = tk.Entry(self, width=30)
        self.ISBN_entry = tk.Entry(self, width=30)
        
        self.register_btn = tk.Button(self, text='登録', font=('', 20), command=self.register_event)
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
        
        self.register_btn.place(x=self.width/2 + 45, y=500)
        self.back_btn.place(x=self.width/2 - 65, y=500)


    def register_event(self):        
        new_id = self.id_entry.get()
        new_title = self.title_entry.get()
        new_genre = self.genre_entry.get()
        new_author = self.author_entry.get()
        new_publisher = self.publisher_entry.get()
        new_isbn = self.ISBN_entry.get()

        book = get_book(new_id)
        
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
            elif book is None:
                insert_book(new_id, new_title, new_genre, new_author, new_publisher, new_isbn)
                messagebox.showinfo('登録完了', '書籍を追加しました。')
            else:
                messagebox.showinfo('登録不可', '既に同じIDが存在しています。')
        elif new_title == '' or new_genre == '' or new_author == '' or new_publisher == '' or new_isbn == '':
            messagebox.showinfo('登録不可', '空欄を埋めてください。')
        elif book is None:
            insert_book(new_id, new_title, new_genre, new_author, new_publisher, new_isbn)
            messagebox.showinfo('登録完了', '書籍を追加しました。')
        else:
            messagebox.showinfo('登録不可', '既に同じIDが存在しています。')

    
    def back_event(self):
        from adominLibrary import AdominLibrary
        self.destroy()
        AdominLibrary(self.master, self.mail)
        
    
if __name__ == '__main__':
    root = tk.Tk()
    app = BookRegister(root, 's')
    app.mainloop()
