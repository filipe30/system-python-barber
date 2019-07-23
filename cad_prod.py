from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


conn = sqlite3.connect('C:\sistema_salao\DataBase\my_database.db')
c = conn.cursor()
result = c.execute('SELECT MAX (id) from product')
for r in result:
    id = r[0]






class DataBase:
    def __init__(self, master, * args, **kw):
        self.master = master

        self.frame1 = Frame(master, width=1000, height=50,
                            bg='#222125', bd=1, relief='raise')
        self.frame1.pack(side=TOP)
        self.frame1 = Frame(master, width=1000, height=50,
                            bg='#222125', bd=1, relief='raise')
        self.frame1.pack(side=BOTTOM)



        self.label1 = Label(master, text='CADASTRO DE PRODUTO', font=('arial', 25, 'bold'))
        self.label1.place(x=30, y=70)

        self.img = PhotoImage(file='img.gif')
        self.la_img = Label(master, image=self.img)
        self.la_img.place(x=550, y=100)


        self.e_produto = Entry(master, width=40, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_produto.place(x=30, y=230)
        self.la_produto = Label(master,text='Produto:', font=('arial 15 bold'))
        self.la_produto.place(x=30, y=199)

        self.e_fornecedor = Entry(master, width=40, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_fornecedor.place(x=30, y=300)
        self.la_fornecedor = Label(master, text='Fornecedor:', font=('arial 15 bold'))
        self.la_fornecedor.place(x=30, y=269)



        self.e_vlr_custo = Entry(master, width=17, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_vlr_custo.place(x=30, y=370)
        self.la_vlr_custo = Label(master, text='Preço de Custo:', font=('arial 15 bold'))
        self.la_vlr_custo.place(x=30, y=339)

        self.e_vlr_venda = Entry(master, width=17, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_vlr_venda.place(x=284, y=370)
        self.la_vlr_venda = Label(master, text='Preço de Venda:', font=('arial 15 bold'))
        self.la_vlr_venda.place(x=284, y=339)

        self.e_estoque = Entry(master, width=8, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_estoque.place(x=30, y=440)
        self.la_estoque = Label(master, text='Estoque:', font=('arial 15 bold'))
        self.la_estoque.place(x=30, y=409)

        self.e_lote = Entry(master, width=10, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_lote.place(x=155, y=440)
        self.la_lote = Label(master, text='Lote:', font=('arial 15 bold'))
        self.la_lote.place(x=155, y=409)

        self.e_venc = Entry(master, width=15, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_venc.place(x=306, y=440)
        self.la_venc = Label(master, text='Vencimento:', font=('arial 15 bold'))
        self.la_venc.place(x=306, y=409)

        self.salvar = Button(master, text='Salvar', bg='#f17215',
                           bd=2, relief='raise', width=20, height=3, command=self.salvar)
        self.salvar.place(x=30, y=520)

        self.deletar = Button(master, text='Novo', bg='#f17215',
                              bd=2, relief='raise', width=20, height=3, command=self.novo)
        self.deletar.place(x=300, y=520)

    def salvar(self, *args, **kwargs):
        self.produto = self.e_produto.get()
        self.fornecedor = self.e_fornecedor.get()
        self.vlr_custo = self.e_vlr_custo.get()
        self.vlr_venda = self.e_vlr_venda.get()
        self.estoque = self.e_estoque.get()
        self.lote = self.e_lote.get()
        self.venc = self.e_venc.get()


        if self.produto == "" or self.fornecedor == "" or self.vlr_custo == "" or self.vlr_venda == "" or self.estoque == "" or self.lote =="" or self.venc =="":
            messagebox.showinfo(' Barber Shop', 'CAMPO OBRIGATÓRIO!')

        else:
            sql = "INSERT INTO product(produto, fornecedor, vlr_custo, vlr_venda, estoque, lote, vencimento)VALUES (?,?,?,?,?,?,?) "
            c.execute(sql, (self.produto, self.fornecedor, self.vlr_custo, self.vlr_venda, self.estoque, self.lote, self.venc))
            conn.commit()

            messagebox.showinfo('Barber Shop', 'CADASTRO RALIZADO COM SUCESSO!')



    def novo(self, *args, **kwargs):
        self.e_produto.delete(0, END)
        self.e_fornecedor.delete(0, END)
        self.e_vlr_custo.delete(0, END)
        self.e_vlr_venda.delete(0, END)
        self.e_estoque.delete(0, END)
        self.e_lote.delete(0, END)
        self.e_venc.delete(0, END)



janela = Tk()
main = DataBase(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0,0)
janela.config()
janela.title()

janela.mainloop()