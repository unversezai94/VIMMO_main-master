from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3



class Supplier:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('774x530+100+100')

        # title
        self.root.title('VIMMO Tedarik')
        self.root.config(bg='#E7E1DF')
        self.root.focus_force()

        # variables
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        self.var_sup_inv_id = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        

        # search
        search_box = LabelFrame(self.root,text='Tedarikçi',font=('Biryani Light',8),bd=2,relief=RIDGE,bg='#E7E1DF')
        search_box.place(x=50,y=20,width=700,height=70)

        # options
        label_search = Label(search_box,textvariable=self.var_search_by,text='Fatura No Ara',font=('Biryani Light',10),background='#E7E1DF')
        label_search.place(x=30,y=9,width=180,height=30)


        txt_search = Entry(search_box,textvariable=self.var_search_txt,font=('Biryani Light',10),bg='#B3CCA2').place(x=200,y=11,width=240,height=30)
        btn_search = Button(search_box,text='Ara',command=self.search,font=('Biryani Light',10),bg='#70A957',fg='#0F0A0A').place(x=450,y=9,width=120,height=30)

        # title
        title = Label(self.root,text='Tedarik Ayrıntıları',font=('Biryani Light',10),bg='#70A957',fg='#0F0A0A').place(x=50,y=100,width=700)

        # content
        # row_1
        label_supplier_inv = Label(self.root,text='Fatura No',font=('Biryani Light',10),bg='#E7E1DF',fg='#0F0A0A').place(x=50,y=135)
        txt_supplier_inv = Entry(self.root,textvariable=self.var_sup_inv_id,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=139,y=135,width=100)

        # row_2
        label_name = Label(self.root,text='Tedarikçi Ismi',font=('Biryani Light',10),bg='#E7E1DF',fg='#0F0A0A').place(x=50,y=170)       
        txt_name = Entry(self.root,textvariable=self.var_name,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=138,y=170,width=100)

        # row_3
        label_contact = Label(self.root,text='Telefon',font=('Biryani Light',10),bg='#E7E1DF',fg='#0F0A0A').place(x=50,y=205)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=138,y=205,width=100)
           
        # row_4
        label_desc = Label(self.root,text='Notlar',font=('Biryani Light',10),bg='#E7E1DF',fg='#0F0A0A').place(x=50,y=240)
        self.txt_desc = Text(self.root,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A')
        self.txt_desc.place(x=138,y=240,width=300,height=120)

        # buttons
        btn_save = Button(self.root,text='Kaydet',command=self.add,font=('Biryani Light',8,'bold'),bg='#70A957',fg='#0F0A0A').place(x=136,y=370,width=70,height=20)
        btn_update = Button(self.root,text='Guncelle',command=self.update,font=('Biryani Light',8,'bold'),bg='#70A957',fg='#0F0A0A').place(x=214,y=370,width=70,height=20)
        btn_delete = Button(self.root,command=self.delete,text='Sil',font=('Biryani Light',8,'bold'),bg='#E36363',fg='#0F0A0A').place(x=290,y=370,width=70,height=20)
        btn_clear = Button(self.root,command=self.clear,text='Temizle',font=('Biryani Light',8,'bold'),bg='#D9D3D1',fg='#0F0A0A').place(x=366,y=370,width=70,height=20)

        # employee_list
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=450,y=130,width=300,height=350)

        scrolly= Scrollbar(emp_frame,orient=VERTICAL)
        scrollx= Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplier_list = ttk.Treeview(emp_frame,columns=('invoice','isim','telefon','notlar'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.supplier_list.xview)
        scrolly.config(command=self.supplier_list.yview)

        self.supplier_list.heading('invoice',text="Fatura No")
        self.supplier_list.heading('isim',text="Isim")
        self.supplier_list.heading('telefon',text="Telefon")
        self.supplier_list.heading('notlar',text="notlar")

        self.supplier_list['show'] = 'headings'

        self.supplier_list.column('invoice',width=80)
        self.supplier_list.column('isim',width=80)
        self.supplier_list.column('telefon',width=80)
        self.supplier_list.column('notlar',width=80)

        self.supplier_list.pack(fill=BOTH, expand=1)
        self.supplier_list.bind('<ButtonRelease-1>',self.get_data)
        self.show()
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_inv_id.get() == "":
                messagebox.showerror('Hata!','Fatura No zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from supplier where invoice = ?',(self.var_sup_inv_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror('Hata!','Bu fatura zaten bulunuyor!',parent=self.root)
                else:
                    cur.execute('Insert into supplier (invoice,isim,telefon,notlar) values(?,?,?,?)',(
                                self.var_sup_inv_id.get(),
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Fatura Başarıyla Eklendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)    
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute('Select * from supplier')
            rows=cur.fetchall()
            self.supplier_list.delete(*self.supplier_list.get_children())
            for row in rows:
                self.supplier_list.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def get_data(self,ev):
        f=self.supplier_list.focus()
        content=(self.supplier_list.item(f))
        row=content['values']

        self.var_sup_inv_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3]),
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_inv_id.get() == "":
                messagebox.showerror('Hata!','Faura No zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from supplier where invoice = ?',(self.var_sup_inv_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış fatura numarası!',parent=self.root)
                else:
                    cur.execute('Update supplier set isim=?,telefon=?,notlar=?,where invoice=?',(
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_desc.get('1.0',END),
                                self.var_sup_inv_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Fatura Başarıyla Güncellendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_inv_id.get() == "":
                messagebox.showerror('Hata!','Fatura no zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from supplier where invoice=?',(self.var_sup_inv_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Fatura numarası',parent=self.root)
                else:
                    op=messagebox.askyesno('Onayla','Silmek istediğinize emin misiniz?',parent=self.root)
                    if op == True:
                        cur.execute('delete from supplier where invoice=?',(self.var_sup_inv_id.get(),))
                        con.commit()
                        messagebox.showinfo('Başarılı','Fatura Başarıyla Silindi.',parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def clear(self):
    
        self.var_sup_inv_id.set(''),
        self.var_name.set(''),
        self.var_contact.set(''),
        self.txt_desc.delete('1.0',END)
        self.var_search_txt.set('')
        self.show()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search_txt.get()=='':
                messagebox.showerror('Hata!','Arama kutusu boş bırakılamaz.',parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_search_txt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplier_list.delete(*self.supplier_list.get_children())
                    self.supplier_list.insert('',END,values=row)
                else:
                    messagebox.showerror('Hata!','Sonuç bulunamadı.',parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
if __name__ == '__main__':
    root = Tk()
    im = Supplier(root)
    root.mainloop()