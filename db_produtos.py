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

        self.e_produto = Entry(master, width=25, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_produto.place(x=20, y=100)
        self.la_produto = Label(master, text='Produto', font=('arial 15 bold'))
        self.la_produto.place(x=115, y=70)

        self.e_vlr_custo = Entry(master, width=15, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_vlr_custo.place(x=380, y=100)
        self.la_vlr_custo = Label(master, text='Preço/Custo', font=('arial 15 bold'))
        self.la_vlr_custo.place(x=405, y=70)

        self.e_vlr_venda = Entry(master, width=15, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_vlr_venda.place(x=620, y=100)
        self.la_vlr_venda = Label(master, text='Preço/Venda', font=('arial 15 bold'))
        self.la_vlr_venda.place(x=640, y=70)

        self.e_estoque = Entry(master, width=10, font=('arial 14 bold'), bd=1, relief="solid")
        self.e_estoque.place(x=850, y=100)
        self.la_estoque = Label(master, text='Estoque', font=('arial 15 bold'))
        self.la_estoque.place(x=865, y=70)




        self.tbox = ttk.Treeview(master, selectmode='browse',height=25)
        self.tbox["columns"] = ["#1", "#2", "#3", "#4", "#5", "#6", "#7"]
        self.tbox.bind('<<TreeviewSelect>>', self.entry_tree)
        self.tbox.place(x=20, y=150)
        self.tbox.column("#0", stretch=False, width=100)
        self.tbox.column("#1", stretch=False, width=120)
        self.tbox.column("#2", stretch=False, width=128)
        self.tbox.column("#3", stretch=False, width=128)
        self.tbox.column("#4", stretch=False, width=120)
        self.tbox.column("#5", stretch=False, width=120)
        self.tbox.column("#6", stretch=False, width=120)
        self.tbox.column("#7", stretch=False, width=120)
        self.tbox.heading("#0", text="Código")
        self.tbox.heading("#1", text="Produto")
        self.tbox.heading("#2", text="Fornecedor")
        self.tbox.heading("#3", text="Preço de Custo")
        self.tbox.heading("#4", text="Preço de Venda")
        self.tbox.heading("#5", text="Estoque")
        self.tbox.heading("#6", text="Lote")
        self.tbox.heading("#7", text="Vencimento")
        for row in self.consultar_registros():
            self.tbox.insert('','end', text=row[1],
                             values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

        self.deletar = Button(master, text='Deletar', bg='#f17215',
                              bd=2, relief='raise', width=15, height=2, command=self.delete)
        self.deletar.place(x=380, y=700)
        self.atualiza = Button(master, text='Atualizar', bg='#f17215',
                                bd=2, relief='raise', width=15, height=2, command=self.atualizar)
        self.atualiza.place(x=520, y=700)




        self.tbox.insert("", 0, END)
        self.tree = ttk.Scrollbar(orient=HORIZONTAL)
        self.tree.configure(command=self.tbox.xview)
        self.tbox.configure(xscrollcommand=self.tree.set)
        self.tree.place(x=20, y=678, width=980)

        self.tbox.insert("", END, 0)
        self.tree = ttk.Scrollbar(orient=VERTICAL)
        self.tree.configure(command=self.tbox.yview)
        self.tbox.configure(yscrollcommand=self.tree.set)
        self.tree.place(x=980, y=150, height=527)


    def consultar_registros(self):
        return c.execute("SELECT id, * FROM product")




    def entry_tree(self, *args, **kwargs):
        print(self.tbox.selection())



        produto = self.tbox.item(self.tbox.selection())["values"][0]
        vlr_custo = self.tbox.item(self.tbox.selection())["values"][2]
        vlr_venda = self.tbox.item(self.tbox.selection())["values"][3]
        estoque = self.tbox.item(self.tbox.selection())["values"][4]

        self.e_produto.delete(0, END)
        self.e_produto.insert(END, str(produto))

        self.e_vlr_custo.delete(0, END)
        self.e_vlr_custo.insert(END, str(vlr_custo))
        self.e_vlr_venda.delete(0, END)
        self.e_vlr_venda.insert(END, str(vlr_venda))
        self.e_estoque.delete(0, END)
        self.e_estoque.insert(END, str(estoque))



    def atualizar(self, *args, **Kwargs):
        self.up_1 = self.e_produto.get()
        self.up_2 = self.e_vlr_custo.get()
        self.up_3 = self.e_vlr_venda.get()
        self.up_4 = self.e_estoque.get()



        query = "UPDATE product SET produto=?, vlr_custo=?, vlr_venda=? WHERE estoque=?"
        c.execute(query, (self.up_1, self.up_2, self.up_3, self.up_4, ))
        conn.commit()
        messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')

    def delete(self, *args, **kwargs):
        c.execute('DELETE FROM product WHERE id = ?', (id,) )
        conn.commit()
        self.tbox.delete()
        messagebox.showinfo('Barber Shop', 'PRODUTO APAGADO COM SUCESSO!')



janela = Tk()
main = DataBase(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0,0)
janela.config()
janela.title()

janela.mainloop()
