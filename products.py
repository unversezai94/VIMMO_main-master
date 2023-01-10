from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3



class Product:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('974x530+100+100')

        # title
        self.root.title('VIMMO Ürün')
        self.root.config(bg='#E5E7DB')
        self.root.focus_force()

        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        self.var_pid = StringVar()
        self.var_cat=StringVar()
        self.var_supp=StringVar()
        self.cat_list = list()
        self.supp_list = list()
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        product_frame = Frame(self.root,bd=3,relief=RIDGE,bg='#E5E7DB')
        product_frame.place(x=10,y=10,width=450,height=480)

        title = Label(product_frame,text='Ürün Ayrıntıları',font=('Biryani Light',11),bg='#BDBF09',fg='#0F0A0A').pack(side=TOP,fill=X)

        lbl_categories = Label(product_frame,text='Kategori',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=60)
        lbl_supplier = Label(product_frame,text='Tedarikçi',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=110)
        lbl_prod_name = Label(product_frame,text='Ürün İsmi',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=160)
        lbl_price = Label(product_frame,text='Fiyat',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=210)
        lbl_quantity = Label(product_frame,text='Miktar',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=260)
        lbl_status = Label(product_frame,text='Durum',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=310)

        lbl_categories = Label(product_frame,text='Ürün Kategorisi',font=('Biryani Light',11),bg='#E5E7DB',fg='#0F0A0A').place(x=30,y=60)

        cmb_search = ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=('Biryani Light',10),background='#5DA36A')
        cmb_search.place(x=150,y=60,width=200)
        cmb_search.current(0)

        cmb_supp = ttk.Combobox(product_frame,textvariable=self.var_supp,values=self.supp_list,state='readonly',justify=CENTER,font=('Biryani Light',10),background='#5DA36A')
        cmb_supp.place(x=150,y=110,width=200)
        cmb_supp.current(0)

        txt_name = Entry(product_frame,textvariable=self.var_name,font=('Biryani Light',10),background='#F1F529').place(x=150,y=160,width=200)
        txt_price = Entry(product_frame,textvariable=self.var_price,font=('Biryani Light',10),background='#F1F529').place(x=150,y=210,width=200)
        txt_quantity = Entry(product_frame,textvariable=self.var_quantity,font=('Biryani Light',10),background='#F1F529').place(x=150,y=260,width=200)
        
        cmb_status = ttk.Combobox(product_frame,textvariable=self.var_status,values=("Seçiniz","Aktif","İnaktif"),state='readonly',justify=CENTER,font=('Biryani Light',10),background='#5DA36A')
        cmb_status.place(x=150,y=310,width=200)
        cmb_supp.current(0)


        btn_save = Button(product_frame,text='Kaydet',command=self.add,font=('Biryani Light',8,'bold'),bg='#5DA36A',fg='#0F0A0A').place(x=15,y=450,width=100,height=20)
        btn_update = Button(product_frame,text='Guncelle',command=self.update,font=('Biryani Light',8,'bold'),bg='#5DA36A',fg='#0F0A0A').place(x=120,y=450,width=100,height=20)
        btn_delete = Button(product_frame,command=self.delete,text='Sil',font=('Biryani Light',8,'bold'),bg='#E36363',fg='#0F0A0A').place(x=225,y=450,width=100,height=20)
        btn_clear = Button(product_frame,command=self.clear,text='Temizle',font=('Biryani Light',8,'bold'),bg='#D9D3D1',fg='#0F0A0A').place(x=330,y=450,width=100,height=20)

        search_box = LabelFrame(self.root,text='Ürün Ara',font=('Biryani Light',8),bd=2,relief=RIDGE,bg='#E5E7DB')
        search_box.place(x=30,y=370,width=415,height=70)

        # options
        cmb_search = ttk.Combobox(search_box,textvariable=self.var_search_by,values=('Lütfen Seçiniz','Kategori','Tedarikçi'),state='readonly',justify=CENTER,font=('Biryani Light',8),background='#5DA36A')
        cmb_search.place(x=10,y=10,width=100,height=30)
        cmb_search.current(0)

        txt_search = Entry(search_box,textvariable=self.var_search_txt,font=('Biryani Light',10),bg='#F1F529').place(x=120,y=10,width=175,height=30)
        btn_search = Button(search_box,text='Ara',command=self.search,font=('Biryani Light',10),bg='#BDBF09',fg='#0F0A0A').place(x=300,y=8.5,width=100,height=30)

        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=460,y=10,width=500,height=480)

        scrolly= Scrollbar(p_frame,orient=VERTICAL)
        scrollx= Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_list = ttk.Treeview(p_frame,columns=('pid','Tedarikci','Kategori','isim','fiyat','miktar','durum'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.product_list.xview)
        scrolly.config(command=self.product_list.yview)

        self.product_list.heading('pid',text="ID")
        self.product_list.heading('Kategori',text="Kategori")
        self.product_list.heading('Tedarikci',text="Tedarikci")
        self.product_list.heading('isim',text="Ürün İsmi")
        self.product_list.heading('fiyat',text="Fiyat")
        self.product_list.heading('miktar',text="Miktar")
        self.product_list.heading('durum',text="Durum")
        

        self.product_list['show'] = 'headings'

        self.product_list.column('pid',width=40)
        self.product_list.column('Kategori',width=100)
        self.product_list.column('Tedarikci',width=80)
        self.product_list.column('isim',width=40)
        self.product_list.column('fiyat',width=80)
        self.product_list.column('miktar',width=80)
        self.product_list.column('durum',width=80)
        self.product_list.pack(fill=BOTH, expand=1)
        self.product_list.bind('<ButtonRelease-1>',self.get_data)
        self.show()
        

    def fetch_cat_sup(self):
        self.cat_list.append("Kategori Yok")
        self.supp_list.append("Kategori Yok")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute('Select isim from categories')
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Seçiniz")
            for i in cat:
                self.cat_list.append(i[0])
            
            cur.execute('Select isim from supplier')
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.supp_list[:]
                self.supp_list.append("Seçiniz")
            for i in sup:
                self.supp_list.append(i[0])
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)    

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Seçiniz" or self.var_cat.get() == "Kategori Yok" or self.var_supp.get() == "Seçiniz" or self.var_supp.get() == "Kategori Yok" or self.var_name.get() == "":
                messagebox.showerror('Hata!','Alanlar boş bırakılamaz',parent=self.root)
            else:
                cur.execute('Select * from products where urunismi = ?',(self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror('Hata!','Bu ürün bulunmakta. Farklı bir ürün deneyin!',parent=self.root)
                else:
                    cur.execute('Insert into products (Kategori,Tedarikci,urunismi,fiyat,miktar,durum) values(?,?,?,?,?,?)',(
                                self.var_cat.get(),
                                self.var_supp.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_quantity.get(),
                                self.var_status.get(),
    
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Ürün Başarıyla Eklendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)    
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute('Select * from products')
            rows=cur.fetchall()
            self.product_list.delete(*self.product_list.get_children())
            for row in rows:
                self.product_list.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def get_data(self,ev):
        f=self.product_list.focus()
        content=(self.product_list.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_supp.set(row[1])
        self.var_cat.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror('Hata!','Lütfen listeden ürün seçiniz.',parent=self.root)
            else:
                cur.execute('Select * from products where pid = ?',(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Ürün!',parent=self.root)
                else:
                    cur.execute('Update products set Tedarikci=?,Kategori=?,urunismi=?,fiyat=?,miktar=?,durum=? where pid=?',(
                                self.var_supp.get(),
                                self.var_cat.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_quantity.get(),
                                self.var_status.get(),
                                self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Ürün Başarıyla Güncellendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror('Hata!','Lütfen listeden ürün seçiniz.',parent=self.root)
            else:
                cur.execute('Select * from products where pid=?',(self.var_pid.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Ürün!',parent=self.root)
                else:
                    op=messagebox.askyesno('Onayla','Silmek istediğinize emin misiniz?',parent=self.root)
                    if op == True:
                        cur.execute('delete from products where pid=?',(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo('Başarılı','Ürün Başarıyla Silindi.',parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def clear(self):
    
        self.var_cat.set("Seçiniz")
        self.var_supp.set("Seçiniz")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("")
        self.var_search_txt.set("")
        self.var_pid.set("")
        self.var_search_by.set('Lütfen Seçiniz')
        self.show()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search_by.get()=='Lütfen Seçiniz':
                messagebox.showerror('Hata!','Lütfen seçim yapınız.',parent=self.root)
            elif self.var_search_by.get()=='':
                messagebox.showerror('Hata!','Arama kutusu boş bırakılamaz.',parent=self.root)
            else:
                cur.execute("select * from products where "+self.var_search_by.get()+" LIKE '%"+self.var_search_txt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_list.delete(*self.product_list.get_children())
                    for row in rows:
                        self.product_list.insert('',END,values=row)
                else:
                    messagebox.showerror('Hataa!','Sonuç bulunamadı.',parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)

if __name__ == '__main__':
    root = Tk()
    im = Product(root)
    root.mainloop()