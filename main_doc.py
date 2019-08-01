from tkinter import *
from tkinter import  PhotoImage
import sqlite3
from tkinter import messagebox
from time import strftime
from datetime import date
from subprocess import call

hj = date.today()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
mes = {1:'janeiro', 2:'fevereiro', 3:'março',  4:'abril', 5:'maio', 6:'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'desembro'}
janela = Tk()
dia_la = Label(janela,text=(dias[hj.weekday()]+','+ ' '+ str(hj.day)+' '+'de'+' '+str(mes[hj.month])+' '+'de'+' '+str(hj.year)), font='Helvita 50 bold', fg='blue')
dia_la.place(x=200, y=750)


rel = Label(janela,font= 'Helvita 50 bold', fg= 'blue')
rel.place(x=1325,y=750)
def contador(): # funcao contador
        agora =  strftime('%H:%M:%S')
        if rel['text'] != agora:
                rel['text'] = agora
        rel.after(100, contador)
contador()

welcome = Label(janela,text=['text'], font= 'Helvita 60 bold', fg= 'blue')
welcome.place(x=230, y=200)
def upwel():
    agora = strftime('%H:%M:%S')
    if agora <= str(12):
        welcome['text'] = ('Bom Dia !')
    elif agora <= str(18):
        welcome['text'] = ('Boa Tarde !')
    else:
        welcome['text'] = ('Boa Noite !')
    welcome.after(100, upwel)
upwel()

janela.title('Sistema Salão')
janela.state('zoomed')
janela.config()
janela.geometry('900x600')


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
                                font=('comic sans ms', 15, 'bold'),command=self.cadfornecedor ).place(x=10, y=490)

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

    def cadfornecedor(self):
        call(['python','cad_fornecedor.py'])



app = Aplication(janela)
janela.mainloop()