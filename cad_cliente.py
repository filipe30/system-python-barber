from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


conn = sqlite3.connect('C:\sistema_salao\DataBase\my_database.db')
c = conn.cursor()
result = c.execute('SELECT MAX (id) from client')
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


        self.label1 = Label(master, text='Cadastro de Clientes', font=('arial', 25, 'bold'))
        self.label1.place(x=30, y=60)





        self.e_cliente = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cliente.place(x=30, y=130)
        self.la_cliente = Label(master,text='Cliente:', font=('arial 9 bold'))
        self.la_cliente.place(x=30, y=109)

        self.e_email = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_email.place(x=30, y=180)
        self.la_email = Label(master, text='Email:', font=('arial 9 bold'))
        self.la_email.place(x=30, y=159)

        self.e_tel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_tel.place(x=430, y=130)
        self.la_tel = Label(master, text='Telefone:', font=('arial 9 bold'))
        self.la_tel.place(x=430, y=109)

        self.e_cel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cel.place(x=620, y=130)
        self.la_cel = Label(master, text='Celular:', font=('arial 9 bold'))
        self.la_cel.place(x=620, y=109)

        self.e_cpf = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cpf.place(x=430, y=180)
        self.la_cpf = Label(master, text='CPF:', font=('arial 9 bold'))
        self.la_cpf.place(x=430, y=159)

        self.e_id = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_id.place(x=620, y=180)
        self.la_id = Label(master, text='IDENTIDADE:', font=('arial 9 bold'))
        self.la_id.place(x=620, y=159)

        self.e_ender = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_ender.place(x=30, y=230)
        self.la_ender = Label(master, text='Endereço:', font=('arial 9 bold'))
        self.la_ender.place(x=30, y=209)

        self.e_bairro = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_bairro.place(x=430, y=230)
        self.la_bairro = Label(master, text='Bairro:', font=('arial 9 bold'))
        self.la_bairro.place(x=430, y=209)

        self.e_cidade = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_cidade.place(x=620, y=230)
        self.la_cidade = Label(master, text='Cidade:', font=('arial 9 bold'))
        self.la_cidade.place(x=620, y=209)

        self.e_data = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
        self.e_data.place(x=800, y=130)
        self.la_data = Label(master, text='Nascimento:', font=('arial 9 bold'))
        self.la_data.place(x=800, y=109)



        self.tbox = ttk.Treeview(master, height=19,  selectmode='browse')
        self.tbox["columns"] =  ["#1", "#2", "#3", "#4", "#5","#6","#7","#8","#9","#10" ]
        self.tbox.bind('<<TreeviewSelect>>', self.entry_tree)
        self.tbox.place(x=30, y=260)
        self.tbox.column("#0", stretch=False, width=60)
        self.tbox.column("#1", stretch=False, width=90)
        self.tbox.column("#2", stretch=False, width=100)
        self.tbox.column("#3", stretch=False, width=100)
        self.tbox.column("#4", stretch=False, width=135)
        self.tbox.column("#5", stretch=False, width=135)
        self.tbox.column("#6", stretch=False, width=0)
        self.tbox.column("#7", stretch=False, width=0)
        self.tbox.column("#8", stretch=False, width=100)
        self.tbox.column("#9", stretch=False, width=100)
        self.tbox.column("#10", stretch=False, width=100)
        self.tbox.heading("#0", text="Código")
        self.tbox.heading("#1", text="Nome")
        self.tbox.heading("#2", text="Telefone")
        self.tbox.heading("#3", text="Celular")
        self.tbox.heading("#4", text="Email")
        self.tbox.heading("#5", text="Endereço")
        self.tbox.heading("#6", text="Bairro")
        self.tbox.heading("#7", text="Cidade")
        self.tbox.heading("#8", text="Identidade")
        self.tbox.heading("#9", text="Cpf")
        self.tbox.heading("#10", text="Nascimento")
        for row in self.consultar_registros():
            self.tbox.insert('', 'end', text=row[1], values=(row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))



        self.treex = ttk.Scrollbar(orient=HORIZONTAL)
        self.treex.configure(command=self.tbox.xview)
        self.tbox.configure(xscrollcommand=self.treex.set)

        self.tbox.insert("", END)
        self.treex.place(x=30, y=670, width=925)


        self.tree = ttk.Scrollbar(orient=VERTICAL)
        self.tree.configure(command=self.tbox.yview)
        self.tbox.configure(yscrollcommand=self.tree.set)
        self.tbox.insert("", END)
        self.tree.place(x=955, y=260, height=425)




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
                               bd=2, relief='raise', width=15, height=2)
        self.pesquisa.place(x=640, y=700)



    def salvar(self, *args, **kwargs):
        self.cliente = self.e_cliente.get()
        self.email = self.e_email.get()
        self.tel = self.e_tel.get()
        self.cel = self.e_cel.get()
        self.cpf = self.e_cpf.get()
        self.id = self.e_id.get()
        self.ender = self.e_ender.get()
        self.bairro = self.e_bairro.get()
        self.cidade = self.e_cidade.get()
        self.data = self.e_data.get()
        #continuar configurando
        if self.e_cliente == "" or self.e_email == "" or self.e_cel == "" or self.e_ender == "" or self.e_bairro =="" or self.e_cidade =="" or self.e_data =="":
                messagebox.showinfo(' Barber Shop', 'CAMPO OBRIGATÓRIO!')

        else:
            sql = "INSERT INTO client(nome,  telefone, celular, email,endereço, bairro, cidade, identidade,   cpf,   nascimento)VALUES (?,?,?,?,?,?,?,?,?,?) "
            c.execute(sql, (self.cliente , self.tel , self.cel, self.email,self.ender , self.bairro, self.cidade, self.id ,  self.cpf , self.data) )
            conn.commit()
            messagebox.showinfo('Barber Shop', 'CADASTRO RALIZADO COM SUCESSO!')

    def novo(self, *args, **kwargs):
        self.e_cliente.delete(0, END)
        self.e_tel.delete(0, END)
        self.e_cel.delete(0, END)
        self.e_email.delete(0, END)
        self.e_ender.delete(0, END)
        self.e_bairro.delete(0, END)
        self.e_cidade.delete(0, END)
        self.e_id.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_data.delete(0, END)


    def consultar_registros(self):
        return c.execute("SELECT id, * FROM client")


    def atualizar(self, *args, **Kwargs):
        self.up_1 = self.e_cliente.get()
        self.up_2 = self.e_tel.get()
        self.up_3 = self.e_cel.get()
        self.up_4 = self.e_email.get()
        self.up_5 = self.e_ender.get()
        self.up_6 = self.e_bairro.get()
        self.up_7 = self.e_cidade.get()
        self.up_8 = self.e_id.get()
        self.up_9 = self.e_cpf.get()
        self.up_10 = self.e_data.get()

        query = "UPDATE client SET nome=?, telefone=?, celular=?, email=? endereço=?, bairro=?, cidade=?, identidade=?,  cpf=?,  nascimento=?"
        c.execute(query, (self.up_1, self.up_2, self.up_3, self.up_4, self.up_5, self.up_6,self.up_7, self.up_8,self.up_9,self.up_10) )
        conn.commit()
        messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')

    def delete(self, *args, **kwargs):
        c.execute('DELETE FROM client WHERE id = ?', (id,) )
        conn.commit()
        self.tbox.delete()
        messagebox.showinfo('Barber Shop', 'CLIENTE APAGADO COM SUCESSO!')


    def entry_tree(self, *args, **kwargs):
        print(self.tbox.selection())



        nome = self.tbox.item(self.tbox.selection())["values"][0]
        tel = self.tbox.item(self.tbox.selection())["values"][1]
        cel = self.tbox.item(self.tbox.selection())["values"][2]
        email = self.tbox.item(self.tbox.selection())["values"][3]
        ender = self.tbox.item(self.tbox.selection())["values"][4]
        bairro = self.tbox.item(self.tbox.selection())["values"][5]
        cidade = self.tbox.item(self.tbox.selection())["values"][6]
        identidade = self.tbox.item(self.tbox.selection())["values"][7]
        cpf = self.tbox.item(self.tbox.selection())["values"][8]
        nascimento = self.tbox.item(self.tbox.selection())["values"][9]


        self.e_cliente.delete(0, END)
        self.e_cliente.insert(END, str(nome))
        self.e_tel.delete(0, END)
        self.e_tel.insert(END, str(tel))
        self.e_cel.delete(0, END)
        self.e_cel.insert(END, str(cel))
        self.e_email.delete(0, END)
        self.e_email.insert(END, str(email))
        self.e_ender.delete(0, END)
        self.e_ender.insert(END, str(ender))
        self.e_bairro.delete(0, END)
        self.e_bairro.insert(END, str(bairro))
        self.e_cidade.delete(0, END)
        self.e_cidade.insert(END, str(cidade))
        self.e_id.delete(0, END)
        self.e_id.insert(END, str(identidade))
        self.e_cpf.delete(0, END)
        self.e_cpf.insert(END, str(cpf))
        self.e_data.delete(0, END)
        self.e_data.insert(END, str(nascimento))




janela = Tk()
main = DataBase(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0,0)
janela.config()
janela.title()

janela.mainloop()