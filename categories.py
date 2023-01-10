from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3



class Categories:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('774x400+100+100')

        # main title
        self.root.title('VIMMO Kategoriler')
        self.root.config(bg='#E7E1DF')
        self.root.focus_force()

        # variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # title

        label_title = Label(self.root,text='Ürün Kategori Yönetimi',font=('Biryani Light',16),bg='#97B430',fg='#0F0A0A',bd=1,relief=RIDGE)
        label_title.pack(side=TOP,fill=X,padx=4,pady=10)

        label_name = Label(self.root,text='Kategori giriniz',font=('Biryani Light',15),bg='#E7E1DF',fg='#0F0A0A')
        label_name.place(x=70,y=100)

        txt_name = Entry(self.root,textvariable=self.var_name,font=('Biryani Light',15),bg='#C6D28F',fg='#0F0A0A')
        txt_name.place(x=220,y=100,width=480)

        # buttons
        btn_add = Button(self.root,text='Ekle',command=self.add,font=('Biryani Light',13),bg='#97B430',fg='#0F0A0A')
        btn_add.place(x=600,y=130,width=98,height=25)

        btn_delete = Button(self.root,text='Sil',command=self.delete,font=('Biryani Light',13),bg='#E36363',fg='#0F0A0A')
        btn_delete.place(x=600,y=160,width=98,height=25)


        # categories frame
        
        cat_frame = Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=0,y=200,relwidth=1,height=180)

        scrolly= Scrollbar(cat_frame,orient=VERTICAL)
        scrollx= Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_list = ttk.Treeview(cat_frame,columns=('cid','isim'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.category_list.xview)
        scrolly.config(command=self.category_list.yview)

        self.category_list.heading('cid',text="C ID")
        self.category_list.heading('isim',text="Isim")

        self.category_list['show'] = 'headings'

        self.category_list.column('cid',width=40)
        self.category_list.column('isim',width=100)

        self.category_list.pack(fill=BOTH, expand=1)
        self.category_list.bind('<ButtonRelease-1>',self.get_data)

        self.show()

    def get_data(self,ev):
        f=self.category_list.focus()
        content=(self.category_list.item(f))
        row=content['values']

        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror('Hata!','Kategori ismi zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from categories where isim = ?',(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror('Hata!','Bu kategori zaten bulunuyor!',parent=self.root)
                else:
                    cur.execute('Insert into categories (isim) values(?)',(
                                self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Kategori Başarıyla Eklendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)    

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute('Select * from categories')
            rows=cur.fetchall()
            self.category_list.delete(*self.category_list.get_children())
            for row in rows:
                self.category_list.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror('Hata!','Kategori ismi zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from categories where isim=?',(self.var_name.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Kategori İsmi',parent=self.root)
                else:
                    op=messagebox.askyesno('Onayla','Silmek istediğinize emin misiniz?',parent=self.root)
                    if op == True:
                        cur.execute('delete from categories where isim=?',(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo('Başarılı','Kategori Başarıyla Silindi.',parent=self.root)
                        self.show()
                        self.var_cat_id.set('')
                        self.var_name.set('')
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)

if __name__ == '__main__':
    root = Tk()
    im = Categories(root)
    root.mainloop()