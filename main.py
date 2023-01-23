from tkinter import *
from tkinter import ttk #biblioteca de elementos de arqvore.
from tkinter import messagebox #biblioteca de mensagens

#importando o script do Banco de Dados.
from db import Database

# Definição das caracteristicas
db = Database("BancoSuperMagico.db")
root = Tk()
root.title("Aplicação com Inserção e Alteração")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

nome = StringVar()
cpf = StringVar()
oculos = StringVar()

# Carcteristicas do Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Sistema de Gestão de Pessoas", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblNome = Label(entries_frame, text="NOME", font=("Calibri", 16), bg="#535c68", fg="white")
lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtNome = Entry(entries_frame, textvariable=nome, font=("Calibri", 16), width=30)
txtNome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblCPF = Label(entries_frame, text="CPF", font=("Calibri", 16), bg="#535c68", fg="white")
lblCPF.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtCPF = Entry(entries_frame, textvariable=cpf, font=("Calibri", 16), width=30)
txtCPF.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblOculos = Label(entries_frame, text="OCULOS", font=("Calibri", 16), bg="#535c68", fg="white")
lblOculos.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtOculos = Entry(entries_frame, textvariable=oculos, font=("Calibri", 16), width=30)
txtOculos.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# COMEÇO DOS TRABALHOS DOS EVENTOS.
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)

    global row
    row = data["values"]

    #print(row)
    nome.set(row[1])
    cpf.set(row[2])
    oculos.set(row[3])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_bd():
    #verificação do que está sendo inserido.
    if txtNome.get() == "" or txtCPF.get() == "" or txtOculos.get() == "":
        messagebox.showerror("ERRO NA INSERÇÃO", "OLHE OS DETALHES")
        return

    #função vindo do banco.
    db.inserir(txtNome.get(), txtCPF.get(), txtOculos.get())

    messagebox.showinfo("SUCESSO", "REGISTRO INSERIDO")
    clearAll()
    dispalyAll()

def update_bd():
    #verificação do que está sendo inserido.
    if txtNome.get() == "" or txtCPF.get() == "" or txtOculos.get() == "":
        messagebox.showerror("ERRO NA INSERÇÃO", "OLHE OS DETALHES")
        return

    #função vindo do banco.
    db.update(row[0], txtNome.get(), txtCPF.get(), txtOculos.get())

    messagebox.showinfo("SUCESSO", "REGISTRO INSERIDO")
    clearAll()
    dispalyAll()

def delete_bd():
    #função vindo do banco.
    db.remover(row[0])
    clearAll()
    dispalyAll()

def clearAll():
    nome.set("")
    cpf.set("")
    oculos.set("")

#TRABALHO COM OS BOTÕES
btn_frame = Frame(entries_frame, bg="#535c68")

btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

btnAdicionar = Button(btn_frame, command=add_bd, text="Adicionar Registro", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#16a085", bd=0).grid(row=0, column=0)

btnEditar = Button(btn_frame, command=update_bd, text="Update do Registro", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)

btnDelete = Button(btn_frame, command=delete_bd, text="Deletar Registro", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)

btnLimpar = Button(btn_frame, command=clearAll, text="Limpar Campos", width=15, font=("Calibri", 16, "bold"), fg="white",
                   bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

# TABELA DO FRAME
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=1320)

style = ttk.Style()

style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  #Modifica da fonte do Body.
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  #Modifica a fonte dos lables

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")

tv.heading("1", text="ID")
tv.column("1", width=5)

tv.heading("2", text="Nome")

tv.heading("3", text="CPF")
tv.column("3", width=5)

tv.heading("4", text="Oculos")
tv.column("4", width=5)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
