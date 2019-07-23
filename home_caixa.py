from tkinter import *
from tkinter import  PhotoImage
import sqlite3
from tkinter import messagebox
import datetime
from subprocess import call
from tkinter.ttk import Combobox


class Aplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.img = PhotoImage(file ='img.gif')
        self.la_img = Label(master, image = self.img)
        self.la_img.place(x=1170, y=100)

        self.la_title = Label(master, text='BarberShop', font=('arial', 25, 'bold'))
        self.la_title.place(x=5, y=5)

        self.pagmt_type = Combobox(master, width=25)
        self.pagmt_type.place(x=820, y=35)

        self.e_updesc = Entry(master, width=7, font=('arial 18 bold'), bd=1, relief="solid")
        self.e_updesc.place(x=700, y=30)
        self.la_updesc = Label(master, text='Desconto', font=('arial 8 bold'),fg='red')
        self.la_updesc.place(x=700, y=10)

        self.e_upqtd = Entry(master, width=7, font=('arial 18 bold'), bd=1, relief="solid")
        self.e_upqtd.place(x=550, y=30)
        self.la_upqtd = Label(master, text='Qtd Item', font=('arial 8 bold'), fg='red')
        self.la_upqtd.place(x=550, y=10)

        self.e_cb = Entry(master, width=35, font=('arial 15 bold'), bd=1, relief="solid")
        self.e_cb.place(x=30, y=80)

        self.e_nop = Entry(master, width=55, font=('arial 15 bold'), bd=1, relief="solid")
        self.e_nop.place(x=440, y=80)

        self.e_qtd = Entry(master, width=5, font=('arial 40 bold') ,bd=1, relief="solid")
        self.e_qtd.place(x=30, y=150)
        self.la_qtd = Label(master, text='Quantidade', font=('arial 10 bold'))
        self.la_qtd.place(x=30, y=125)

        self.cb_func = Combobox(master, width=25)
        self.cb_func.place(x=220, y=150)
        self.la_func = Label(master, text='Funcionário', font=('arial 10 bold'))
        self.la_func.place(x=220, y=125)

        self.e_vup = Entry(master, width=6, font=('arial 40 bold'), bd=1, relief="solid")
        self.e_vup.place(x=470, y=150)
        self.la_vup = Label(master, text='Valor Unitário Produtos', font=('arial 10 bold'))
        self.la_vup.place(x=470, y=125)

        self.e_desc = Entry(master, width=6, font=('arial 40 bold'), bd=1, relief="solid")
        self.e_desc.place(x=670, y=150)
        self.la_vup = Label(master, text='Desconto', font=('arial 10 bold'))
        self.la_vup.place(x=670, y=125)

        self.e_prc = Entry(master, width=6, font=('arial 40 bold'), bd=1, relief="solid")
        self.e_prc.place(x=870, y=150)
        self.la_vup = Label(master, text='Valor Total Produtos', font=('arial 10 bold'))
        self.la_vup.place(x=870, y=125)

        self.tbox = Text(master, width=127, height=25, bd=2, relief="solid")
        self.tbox.place(x=30, y=220)


        self.new_vend = Button(master, text='Nova Venda', bg='#f17215',
                               bd=2, relief='raise', width=15, height=2)
        self.new_vend.place(x=30, y=650)
        self.vend = Button(master, text='Vendas', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.vend.place(x=170, y=650)
        self.init = Button(master, text='Iniciar Caixa', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.init.place(x=310, y=650)
        self.cad_prod = Button(master, text='Cadastro/Produtos', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.cad_prod.place(x=450, y=650)
        self.cad_client = Button(master, text='Cadastro/Clientes', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.cad_client.place(x=590, y=650)
        self.final_vend = Button(master, text='Finalizar Venda', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.final_vend.place(x=730, y=650)
        self.print = Button(master, text='Imprimir Relatório', bg='#f17215',
                                 bd=2, relief='raise', width=15, height=2, )
        self.print.place(x=870, y=650)

        self.la_total = Label(master, width=160, height=6, bg='#aff9d7')
        self.la_total.place(x=50, y=720)




janela = Tk()
app = Aplication(janela)
janela.title('Sistema Salão')
janela.state('zoomed')
janela.config()
janela.geometry('900x600')
janela.mainloop()