from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


conn = sqlite3.connect('C:\sistema_salao\DataBase\my_database.db')
c = conn.cursor()
result = c.execute('SELECT MAX (id) from agend')
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


        self.label1 = Label(master, text='Agendamento', font=('arial', 25, 'bold'))
        self.label1.place(x=30, y=60)

        self.e_pesq = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_pesq.place(x=600, y=80)
        self.la_pesq = Label(master, text='Pesquisa:(Cliente)', font=('arial', 9, 'bold'))
        self.la_pesq.place(x=485, y=80)


        self.line = Label(master, width=60, height=1, bg='#222125')
        self.line.place(x=30, y=180)

        self.e_cliente = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cliente.place(x=30, y=230)
        self.la_cliente = Label(master,text='Cliente:', font=('arial 9 bold'))
        self.la_cliente.place(x=30, y=209)

        self.e_email = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_email.place(x=30, y=280)
        self.la_email = Label(master, text='Email:', font=('arial 9 bold'))
        self.la_email.place(x=30, y=259)

        self.e_tel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_tel.place(x=450, y=230)
        self.la_tel = Label(master, text='Telefone:', font=('arial 9 bold'))
        self.la_tel.place(x=450, y=209)

        self.e_cel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cel.place(x=620, y=230)
        self.la_cel = Label(master, text='Celular:', font=('arial 9 bold'))
        self.la_cel.place(x=620, y=209)

        self.e_func = Entry(master, width=25, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_func.place(x=30, y=330)
        self.la_func = Label(master, text='Funcionário:', font=('arial 9 bold'))
        self.la_func.place(x=30, y=309)

        self.e_serv = Entry(master, width=25, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_serv.place(x=300, y=330)
        self.la_serv = Label(master, text='Serviço:', font=('arial 9 bold'))
        self.la_serv.place(x=300, y=309)

        self.e_hora = Entry(master, width=6, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_hora.place(x=30, y=380)
        self.la_hora = Label(master, text='Horário:', font=('arial 9 bold'))
        self.la_hora.place(x=30, y=359)

        self.e_data = Entry(master, width=10, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_data.place(x=120, y=380)
        self.la_data = Label(master, text='Data:', font=('arial 9 bold'))
        self.la_data.place(x=120, y=359)



        self.tbox = ttk.Treeview(master,  selectmode='browse')
        self.tbox["columns"] =  ["#1", "#2", "#3", "#4", "#5","#6","#7","#8" ]
        self.tbox.bind('<<TreeviewSelect>>', self.entry_tree)
        self.tbox.place(x=30, y=430)
        self.tbox.column("#0", stretch=False, width=60)
        self.tbox.column("#1", stretch=False, width=90)
        self.tbox.column("#2", stretch=False, width=100)
        self.tbox.column("#3", stretch=False, width=100)
        self.tbox.column("#4", stretch=False, width=150)
        self.tbox.column("#5", stretch=False, width=100)
        self.tbox.column("#6", stretch=False, width=100)
        self.tbox.column("#7", stretch=False, width=80)
        self.tbox.column("#8", stretch=False, width=80)
        self.tbox.heading("#0", text="Código")
        self.tbox.heading("#1", text="Nome")
        self.tbox.heading("#2", text="Telefone")
        self.tbox.heading("#3", text="Celular")
        self.tbox.heading("#4", text="Email")
        self.tbox.heading("#5", text="Funcionário")
        self.tbox.heading("#6", text="Serviço")
        self.tbox.heading("#7", text="Hora")
        self.tbox.heading("#8", text="Data")
        for row in self.consultar_registros():
            self.tbox.insert('', 'end', text=row[1], values=(row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9]))


        self.tbox.insert("",0, END)
        self.tree = ttk.Scrollbar( orient=HORIZONTAL)
        self.tree.configure(command=self.tbox.xview)
        self.tbox.configure(xscrollcommand=self.tree.set)
        self.tree.place(x=30, y=658, width=863)

        self.tbox.insert("", END, 0)
        self.tree = ttk.Scrollbar(orient=VERTICAL)
        self.tree.configure(command=self.tbox.yview)
        self.tbox.configure(yscrollcommand=self.tree.set)
        self.tree.place(x=895, y=430, height=243)




        self.novo = Button(master, text='Novo', bg='#f17215',
                               bd=2, relief='raise', width=15, height=2, command=self.novo)
        self.novo.place(x=80, y=700)
        self.salvar = Button(master, text='Salvar/Editar', bg='#f17215',
                               bd=2, relief='raise', width=15, height=2, command=self.salvar)# and self.up_tree)
        self.salvar.place(x=220, y=700)
        self.deletar = Button(master, text='Deletar', bg='#f17215',
                               bd=2, relief='raise', width=15, height=2 , command=self.delete)
        self.deletar.place(x=360, y=700)
        self.atualiza = Button(master, text='Atualizar', bg='#f17215',
                                bd=2, relief='raise', width=15, height=2, command=self.atualizar)
        self.atualiza.place(x=500, y=700)
        self.pesquisa = Button(master, text='Pesquisar', bg='#222',fg='#fff',
                               bd=2, relief='raise', width=15, height=2, command=self.search)
        self.pesquisa.place(x=640, y=700)



    def salvar(self, *args, **kwargs):
        self.cliente = self.e_cliente.get()
        self.tel = self.e_tel.get()
        self.cel = self.e_cel.get()
        self.email = self.e_email.get()
        self.func = self.e_func.get()
        self.serv = self.e_serv.get()
        self.hora = self.e_hora.get()
        self.data = self.e_data.get()

        if self.e_cliente == "" or self.e_cel == "" or self.e_serv == "" or self.e_hora == "" or self.e_data =="":
                messagebox.showinfo(' Barber Shop', 'CAMPO OBRIGATÓRIO!')

        else:
            sql = "INSERT INTO agend(Nome, Telefone, Celular, Email, Funcionario, Serviço, Hora, Data)VALUES (?,?,?,?,?,?,?,?) "
            c.execute(sql, (self.cliente , self.tel , self.cel ,self.email , self.func , self.serv ,self.hora , self.data) )
            conn.commit()
            messagebox.showinfo('Barber Shop', 'CADASTRO RALIZADO COM SUCESSO!')

    def novo(self, *args, **kwargs):
        self.e_pesq.delete(0, END)
        self.e_cliente.delete(0, END)
        self.e_tel.delete(0, END)
        self.e_cel.delete(0, END)
        self.e_email.delete(0, END)
        self.e_func.delete(0, END)
        self.e_serv.delete(0, END)
        self.e_hora.delete(0, END)
        self.e_data.delete(0, END)

    def search(self,*args, **kwargs):
        sql = "SELECT * FROM agend WHERE nome=?"
        result = c.execute(sql, (self.e_pesq.get(),))

        for r in result:
            self.nome = r[1]
            self.telefone = r[2]
            self.celular = r[3]
            self.email = r[4]
            self.funcionario = r[5]
            self.servico = r[6]
            self.hora = r[7]
            self.data = r[8]



        conn.commit()
        self.e_cliente.delete(0, END)
        self.e_cliente.insert(0, str(self.nome))
        self.e_tel.delete(0, END)
        self.e_tel.insert(0, str(self.telefone))
        self.e_cel.delete(0, END)
        self.e_cel.insert(0, str(self.celular))
        self.e_email.delete(0, END)
        self.e_email.insert(0, str(self.email))
        self.e_func.delete(0, END)
        self.e_func.insert(0, str(self.funcionario))
        self.e_serv.delete(0, END)
        self.e_serv.insert(0, str(self.servico))
        self.e_hora.delete(0, END)
        self.e_hora.insert(0, str(self.hora))
        self.e_data.delete(0, END)
        self.e_data.insert(0, str(self.data))

    def consultar_registros(self):
        return c.execute("SELECT id, * FROM agend")

    def up_tree(self):
        for i in self.tbox.get_children():
            self.tbox.update(i)

    def atualizar(self, *args, **Kwargs):
        self.up_1 = self.e_cliente.get()
        self.up_2 = self.e_tel.get()
        self.up_3 = self.e_cel.get()
        self.up_4 = self.e_email.get()
        self.up_5 = self.e_func.get()
        self.up_6 = self.e_serv.get()
        self.up_7 = self.e_hora.get()
        self.up_8 = self.e_data.get()

        query = "UPDATE agend SET nome=?, telefone=?, celular=?, email=?, funcionario=?, serviço=?, hora=?, data=? WHERE nome=?"
        c.execute(query, (self.up_1, self.up_2, self.up_3, self.up_4, self.up_5, self.up_6,self.up_7, self.up_8, self.e_pesq.get()  ))
        conn.commit()
        messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')

    def delete(self, *args, **kwargs):
        c.execute('DELETE FROM agend WHERE id = ?', (id,) )
        conn.commit()
        self.tbox.delete()
        messagebox.showinfo('Barber Shop', 'CLIENTE APAGADO COM SUCESSO!')


    def entry_tree(self, *args, **kwargs):
        print(self.tbox.selection())



        nome = self.tbox.item(self.tbox.selection())["values"][0]
        tel = self.tbox.item(self.tbox.selection())["values"][1]
        cel = self.tbox.item(self.tbox.selection())["values"][2]
        email = self.tbox.item(self.tbox.selection())["values"][3]
        func = self.tbox.item(self.tbox.selection())["values"][4]
        serv = self.tbox.item(self.tbox.selection())["values"][5]
        hora = self.tbox.item(self.tbox.selection())["values"][6]
        data = self.tbox.item(self.tbox.selection())["values"][7]

        self.e_pesq.delete(0, END)
        self.e_pesq.insert(END, str(nome))

        self.e_cliente.delete(0, END)
        self.e_cliente.insert(END, str(nome))
        self.e_tel.delete(0, END)
        self.e_tel.insert(END, str(tel))
        self.e_cel.delete(0, END)
        self.e_cel.insert(END, str(cel))
        self.e_email.delete(0, END)
        self.e_email.insert(END, str(email))
        self.e_func.delete(0, END)
        self.e_func.insert(END, str(func))
        self.e_serv.delete(0, END)
        self.e_serv.insert(END, str(serv))
        self.e_hora.delete(0, END)
        self.e_hora.insert(END, str(hora))
        self.e_data.delete(0, END)
        self.e_data.insert(END, str(data))




janela = Tk()
main = DataBase(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0,0)
janela.config()
janela.title()

janela.mainloop()