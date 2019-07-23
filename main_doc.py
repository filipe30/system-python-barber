from tkinter import *
from tkinter import  PhotoImage
import sqlite3
from tkinter import messagebox
import datetime
from subprocess import call



date = datetime.datetime.now().date().strftime('%d/%m/%Y')
hour = datetime.datetime.now().time().strftime('%H:%M')




class Aplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.frame1 = Frame(master, width=200, height=1500,
                            bg='#222125',bd=5, relief='raise')
        self.frame1.pack(side=LEFT)

        self.label1 = Label(master, text='Barber Shop', font=('arial', 55, 'bold'))
        self.label1.pack()



        self.caixa = Button(self.frame1, text='Caixa', fg='#f97303',bg='#505157',
                            bd=10, relief='raise', width=12, height=2,
                            font=('comic sans ms', 15, 'bold'), command=self.home_caixa ).place(x=10, y=5)

        self.agenda = Button(self.frame1, text='Agenda', fg='#f97303',bg='#505157',
                            bd=10, relief='raise', width=12, height=2,
                            font=('comic sans ms', 15, 'bold'),command=self.agenda ).place(x=10, y=125)

        self.cadprod = Button(self.frame1, text='Cadastro\nProduto', fg='#f97303',bg='#505157',
                            bd=10, relief='raise', width=12, height=2,
                            font=('comic sans ms',15, 'bold'),command=self.cadprod ).place(x=10, y=245)

        self.cadclient = Button(self.frame1, text='Cadastro\nCliente', fg='#f97303',bg='#505157',
                            bd=10, relief='raise', width=12, height=2,
                            font=('comic sans ms', 15, 'bold'),command=self.cadcliente ).place(x=10, y=365)

        self.cadfornec = Button(self.frame1, text='Cadastro\nFornecedor', fg='#f97303', bg='#505157',
                                bd=10, relief='raise', width=12, height=2,
                                font=('comic sans ms', 15, 'bold'), ).place(x=10, y=490)

        self.aniversario = Button(self.frame1, text='Aniversários', fg='#f97303', bg='#505157',
                                bd=10, relief='raise', width=12, height=2,
                                font=('comic sans ms', 15, 'bold'), ).place(x=10, y=610)

        self.modelo = Button(self.frame1, text='Modelos', fg='#f97303', bg='#505157',
                                bd=10, relief='raise', width=12, height=2,
                                font=('comic sans ms', 15, 'bold'), ).place(x=10, y=730)

        self.foto = PhotoImage(file='img.gif')
        self.foto = self.foto.subsample(1, 1)
        self.label = Label(master, image=self.foto)
        self.label.pack()

    def home_caixa(self):
        call(['python','home_caixa.py'])

    def agenda(self):
        call(['python','agendar.py'])

    def cadprod(self):
        call(['python','cad_prod.py'])

    def cadcliente(self):
        call(['python','cad_cliente.py'])

janela = Tk()
app = Aplication(janela)
janela.title('Sistema Salão')
janela.state('zoomed')
janela.config()
janela.geometry('900x600')
janela.mainloop()