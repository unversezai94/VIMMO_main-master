import sqlite3

def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur = con.cursor()

    # employee db
    cur.execute('CREATE TABLE IF NOT EXISTS employee(ID INTEGER PRIMARY KEY AUTOINCREMENT,isim text,email text,cinsiyet text,telefon text,dogumtarihi text,firmayagiris text,sifre text,tip text,adres text,maas text)')
    con.commit()

    # supplier db
    cur.execute('CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,isim text,telefon text,notlar text)')
    con.commit()

    # category db
    cur.execute('CREATE TABLE IF NOT EXISTS categories(cid INTEGER PRIMARY KEY AUTOINCREMENT,isim text)')
    con.commit()
    
    # product db
    cur.execute('CREATE TABLE IF NOT EXISTS products(pid INTEGER PRIMARY KEY AUTOINCREMENT,Tedarikci text,Kategori text,urunismi text,fiyat text,miktar text,durum text)')
    con.commit()
create_db()