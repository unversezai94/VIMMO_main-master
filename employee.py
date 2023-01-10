from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3



class Employee:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('774x530+100+100')

        # title
        self.root.title('VIMMO Personel')
        self.root.config(bg='#E5E7DB')
        self.root.focus_force()

        # variables
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_birth = StringVar()
        self.var_joining = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # search
        search_box = LabelFrame(self.root,text='Personel Ara',font=('Biryani Light',8),bd=2,relief=RIDGE,bg='#E5E7DB')
        search_box.place(x=50,y=20,width=600,height=70)

        # options
        cmb_search = ttk.Combobox(search_box,textvariable=self.var_search_by,values=('Lütfen Seçiniz','Eposta','Isim','Telefon'),state='readonly',justify=CENTER,font=('Biryani Light',10),background='#5DA36A')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        txt_search = Entry(search_box,textvariable=self.var_search_txt,font=('Biryani Light',10),bg='#B3CCA2').place(x=200,y=10,height=30)
        btn_search = Button(search_box,text='Ara',command=self.search,font=('Biryani Light',10),bg='#5DA36A',fg='#0F0A0A').place(x=350,y=9,width=120,height=30)

        # title
        title = Label(self.root,text='Personel Ayrıntıları',font=('Biryani Light',10),bg='#5DA36A',fg='#0F0A0A').place(x=50,y=100,width=600)

        # content
        # row_1
        label_emp_id = Label(self.root,text='Personel ID',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=130)
        label_gender = Label(self.root,text='Cinsiyet',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=130)
        label_contact = Label(self.root,text='Telefon',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=130)

        txt_emp_id = Entry(self.root,textvariable=self.var_emp_id,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=139,y=130,width=100)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=('Lütfen Seçiniz','Erkek','Kadın'),state='readonly',justify=CENTER,font=('Biryani Light',10),background='#DBE4E4')
        cmb_gender.place(x=335,y=130,width=100)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=540,y=130,width=100)

        # row_2
        label_name = Label(self.root,text='Personel Ismi',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=160)
        label_birth = Label(self.root,text='Dogum Tarihi',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=160)
        label_joining = Label(self.root,text='Firmaya Girisi',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=160)

        txt_name = Entry(self.root,textvariable=self.var_name,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=138,y=160,width=100)
        txt_birth = Entry(self.root,textvariable=self.var_birth,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=335,y=160,width=100)
        txt_joining = Entry(self.root,textvariable=self.var_joining,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=540,y=160,width=100)

        # row_3
        label_email = Label(self.root,text='E-mail',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=190)
        label_pass = Label(self.root,text='Sifre',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=190)
        label_utype = Label(self.root,text='Tip',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=190)

        txt_email = Entry(self.root,textvariable=self.var_email,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=138,y=190,width=100)
        txt_pass = Entry(self.root,textvariable=self.var_pass,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=335,y=190,width=100)

        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype,values=('Lütfen Seçiniz','Yönetici','Personel'),state='readonly',justify=CENTER,font=('Biryani Light',10),background='#DBE4E4')
        cmb_utype.place(x=540,y=190,width=100)
        cmb_utype.current(0)
        
        # row_4
        label_adress = Label(self.root,text='Adres',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=230)
        label_salary = Label(self.root,text='Maas',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=230)

        self.txt_adress = Text(self.root,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A')
        self.txt_adress.place(x=138,y=230,width=300,height=40)
        txt_salary = Entry(self.root,textvariable=self.var_salary,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=540,y=230,width=100)

        # buttons
        btn_save = Button(self.root,text='Kaydet',command=self.add,font=('Biryani Light',8,'bold'),bg='#5DA36A',fg='#0F0A0A').place(x=538,y=260,width=100,height=20)
        btn_update = Button(self.root,text='Guncelle',command=self.update,font=('Biryani Light',8,'bold'),bg='#5DA36A',fg='#0F0A0A').place(x=538,y=285,width=100,height=20)
        btn_delete = Button(self.root,command=self.delete,text='Sil',font=('Biryani Light',8,'bold'),bg='#E36363',fg='#0F0A0A').place(x=538,y=310,width=100,height=20)
        btn_clear = Button(self.root,command=self.clear,text='Temizle',font=('Biryani Light',8,'bold'),bg='#D9D3D1',fg='#0F0A0A').place(x=538,y=335,width=100,height=20)

        # employee_list
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=380,relwidth=1,height=150)

        scrolly= Scrollbar(emp_frame,orient=VERTICAL)
        scrollx= Scrollbar(emp_frame,orient=HORIZONTAL)

        self.employee_list = ttk.Treeview(emp_frame,columns=('ID','isim','email','cinsiyet','telefon','dogumtarihi','firmayagiris','sifre','tip','adres','maas'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.employee_list.xview)
        scrolly.config(command=self.employee_list.yview)

        self.employee_list.heading('ID',text="ID")
        self.employee_list.heading('isim',text="Isim")
        self.employee_list.heading('email',text="Email")
        self.employee_list.heading('cinsiyet',text="Cinsiyet")
        self.employee_list.heading('telefon',text="Telefon")
        self.employee_list.heading('dogumtarihi',text="Dogum Tarihi")
        self.employee_list.heading('firmayagiris',text="Firmaya Giris")
        self.employee_list.heading('sifre',text="Sifre")
        self.employee_list.heading('tip',text="Tip")
        self.employee_list.heading('adres',text="Adres")
        self.employee_list.heading('maas',text="Maas")

        self.employee_list['show'] = 'headings'

        self.employee_list.column('ID',width=40)
        self.employee_list.column('isim',width=100)
        self.employee_list.column('email',width=80)
        self.employee_list.column('cinsiyet',width=40)
        self.employee_list.column('telefon',width=80)
        self.employee_list.column('dogumtarihi',width=80)
        self.employee_list.column('firmayagiris',width=80)
        self.employee_list.column('sifre',width=80)
        self.employee_list.column('tip',width=40)
        self.employee_list.column('adres',width=80)
        self.employee_list.column('maas',width=80)

        self.employee_list.pack(fill=BOTH, expand=1)
        self.employee_list.bind('<ButtonRelease-1>',self.get_data)
        self.show()
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror('Hata!','Personel ID zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from employee where ID = ?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror('Hata!','Bu Personel ID zaten bulunuyor!',parent=self.root)
                else:
                    cur.execute('Insert into employee (ID,isim,email,cinsiyet,telefon,dogumtarihi,firmayagiris,sifre,tip,adres,maas) values(?,?,?,?,?,?,?,?,?,?,?)',(
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_birth.get(),
                                self.var_joining.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_adress.get('1.0',END),
                                self.var_salary.get() 
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Personel Başarıyla Eklendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)    
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute('Select * from employee')
            rows=cur.fetchall()
            self.employee_list.delete(*self.employee_list.get_children())
            for row in rows:
                self.employee_list.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def get_data(self,ev):
        f=self.employee_list.focus()
        content=(self.employee_list.item(f))
        row=content['values']

        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_birth.set(row[5]),
        self.var_joining.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_adress.delete('1.0',END)
        self.txt_adress.insert(END,row[9]),
        self.var_salary.set(row[10]) 
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror('Hata!','Personel ID zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from employee where ID = ?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Personel ID!',parent=self.root)
                else:
                    cur.execute('Update employee set isim=?,email=?,cinsiyet=?,telefon=?,dogumtarihi=?,firmayagiris=?,sifre=?,tip=?,adres=?,maas=? where ID=?',(
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_birth.get(),
                                self.var_joining.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_adress.get('1.0',END),
                                self.var_salary.get(),
                                self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Başarılı','Personel Başarıyla Güncellendi.')
                    self.show()

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror('Hata!','Personel ID zorunludur.',parent=self.root)
            else:
                cur.execute('Select * from employee where ID=?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Hata!','Yanlış Personel ID!',parent=self.root)
                else:
                    op=messagebox.askyesno('Onayla','Silmek istediğinize emin misiniz?',parent=self.root)
                    if op == True:
                        cur.execute('delete from employee where ID=?',(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo('Başarılı','Personel Başarıyla Silindi.',parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
    def clear(self):
    
        self.var_emp_id.set(''),
        self.var_name.set(''),
        self.var_email.set(''),
        self.var_gender.set('Lütfen Seçiniz'),
        self.var_contact.set(''),
        self.var_birth.set(''),
        self.var_joining.set(''),
        self.var_pass.set(''),
        self.var_utype.set('Lütfen Seçiniz'),
        self.txt_adress.delete('1.0',END)
        self.var_salary.set('')
        self.var_search_txt.set('')
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
                cur.execute("select * from employee where "+self.var_search_by.get()+" LIKE '%"+self.var_search_txt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employee_list.delete(*self.employee_list.get_children())
                    for row in rows:
                        self.employee_list.insert('',END,values=row)
                else:
                    messagebox.showerror('Hataa!','Sonuç bulunamadı.',parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}',parent=self.root)
if __name__ == '__main__':
    root = Tk()
    im = Employee(root)
    root.mainloop()