from tkinter import *
from PIL import Image,ImageTk
from employee import Employee
from supplier import Supplier
from categories import Categories
from products import Product
from payment_ai import PaymentAI


class VIMMO:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('1024x540+0+0')

        # title
        self.root.title('VIMMO Inventory Management v0')
        self.root.config(bg='#E7E1DF')

        # logo
        self.icon_title=PhotoImage(file='images/vimmo-logo.png')
        title=Label(self.root,image=self.icon_title,compound=LEFT,bg='#E7E1DF',anchor='w',padx=0)
        title.place(x=5,y=0,relwidth=1,height=80)

        # logout button
        btn_logout = Button(self.root,text='Log Out',font=('Biryani Light',10),bg='#827D7C',fg='#0F0A0A',cursor='hand2')
        btn_logout.place(x=800,y=25,width=200,height=22)

        # date and time
        self.clock = Label(self.root,text='\t\t\t\t\t\t\t\t\t\t\tDate:DD-MM-YYYY    Time:HH:MM:SS',font=('Biryani Light',8),bg='#2292A4',fg='#0F0A0A',anchor='w',padx=270)
        self.clock.place(x=4,y=70,relwidth=1,height=25)

        # main left menu
        mleft_menu = Frame(self.root,highlightthickness=4,highlightbackground='#494443',relief=RIDGE,bg='#0F0A0A')
        mleft_menu.place(x=4,y=96,width=200,height=442)
        label_menu = Label(mleft_menu,highlightthickness=2,highlightbackground='#1E1919',text='Manage',font=('Biryani',15,'bold'),bg='#0F0A0A',fg='#F5EFED').pack(side=TOP,fill=X)
        self.menu_logo = Image.open('images/manage-logo.png')
        self.menu_logo = self.menu_logo.resize((130,130),Image.ANTIALIAS)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)
        lbl_menu_logo = Label(mleft_menu,image=self.menu_logo,background='#0F0A0A')
        lbl_menu_logo.pack(side=BOTTOM,fill=X)

        # buttons
        button_emp = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Personel',command=self.employee,font=('Biryani Light',15),bg='#5DA36A',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)
        button_supp = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Tedarikçi',command=self.supplier,font=('Biryani Light',15),bg='#70A957',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)
        button_category = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Kategoriler',command=self.categories,font=('Biryani Light',15),bg='#97B430',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)
        button_product = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Ürün',command=self.products,font=('Biryani Light',15),bg='#BDBF09',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)
        button_sales = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Maaş Tahmin A.I',command=self.payment_ai,font=('Biryani Light',15),bg='#C4AB09',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)
        button_exit = Button(mleft_menu,highlightthickness=4,highlightbackground='#494443',text='Çıkış',font=('Biryani Light',15),bg='#C8A109',fg='#0F0A0A',bd=1,cursor='hand2').pack(side=TOP,fill=X)

        # contents

        self.menu_img=PhotoImage(file='images/v-logo.png')
        title=Label(self.root,image=self.menu_img,bg='#E7E1DF',padx=0)
        title.place(x=305,y=130,width=300,height=380)

        self.label_emp = Label(self.root,text='Toplam Personel\n[ 0 ]',bg='#5DA36A',fg='#0F0A0A',bd=5,relief=RIDGE,font=('Biryani Light',15))
        self.label_emp.place(x=700,y=112,height=70,width=300)

        self.label_supp = Label(self.root,text='Toplam Tedarikçi\n[ 0 ]',bg='#70A957',fg='#0F0A0A',bd=5,relief=RIDGE,font=('Biryani Light',15))
        self.label_supp.place(x=700,y=192,height=70,width=300)

        self.label_category = Label(self.root,text='Kategoriler\n[ 0 ]',bg='#97B430',fg='#0F0A0A',bd=5,relief=RIDGE,font=('Biryani Light',15))
        self.label_category.place(x=700,y=272,height=70,width=300)

        self.label_product = Label(self.root,text='Toplam Ürün\n[ 0 ]',bg='#BDBF09',fg='#0F0A0A',bd=5,relief=RIDGE,font=('Biryani Light',15))
        self.label_product.place(x=700,y=352,height=70,width=300)


    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Employee(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Supplier(self.new_win)

    def categories(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Categories(self.new_win)

    def products(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Product(self.new_win)

    def payment_ai(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = PaymentAI(self.new_win)

if __name__ == '__main__':
    root = Tk()
    im = VIMMO(root)
    root.mainloop()