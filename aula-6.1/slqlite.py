from tkinter import filedialog
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox

pasta_inicial =""

tela = Tk()
tela.title("Controle de Pessoas")
var = StringVar()
var.set("m")
tela.geometry("700x500")

# Cria database
conn = sqlite3.connect("MyDB.db")

# Criar cursor
cur = conn.cursor()

# Criar Tabela
cur.execute("CREATE TABLE IF NOT EXISTS pessoas(codigo INT primary key, nome TEXT, altura REAL, peso REAL, cidade TEXT, datanasc TEXT, dataAtual TEXT, dataCadastro TEXT, descricao TEXT)")

# Close connection
conn.close()

def insercao():
    # conecta ao database
    conn = sqlite3.connect("MyDB.db")

    cur = conn.cursor()

    # Insere dados na tabela
    cur.execute('INSERT INTO pessoas VALUES (:codigo, :nome, :idade, :sexo, :altura, :peso, :cidade, :datanasc, :dataatual, :dataCadastro, :descricao),'
    {'codigo': txt_codigo.get(), 'nome': txt_nome.get(), 'idade':txt_idade.get(), 'sexo': var.get(), 'altura': txt_altura.get(), 'peso': txt_peso.get(), 'cidade': cmb_cidade.get(), 'datanasc': txt_data_nascimento.get(),'dataatual'; txt_data_atualizacao.get(),'dataCadastro': txt_data_cadastro.get(), 'descricao': txt_descricao.get()})

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear Text Boxes
    txt_nome.delete(0, END)
    txt_idade.delete(0,END)
    txt_altura.delete(0, END)
    txt_descricao.delete(0, END)

def consulta():

    conn = sqlite3.connect("MyDB.db")

    # Create Cursor
    cur conn.cursor()

    # faz consulta da tabela 
    cur.execute('SELECT *, oid FROM pessoas')

    records = cur.fetchall()

    #mostra resultados encontrados
    print_records = ""
    for rec in records:
        print_records += 'Codigo' + str(rec[0])

def show():
    Label(tela, text=var.get()).pack()


chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="off")
chk_button.deselect()
chk_button.pack()

Button(tela, text="Show me", command=show).pack()

def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial,title="Escolha uma imagem", 
                                            filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                                                        ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10, y=50)
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excluir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

btn_salvar = Button(tela, text="Salvar", image= foto_salvar, compound=TOP).place(x=130, y=310)
btn_excluir = Button(tela, text="Excluir", image= foto_excluir, compound=TOP).place(x=200, y=310)
btn_alterar = Button(tela, text="Alterar", image= foto_alterar, compound=TOP).place(x=270,y=310)
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP).place(x=340,y=310)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT).place(x=620,y=340)


tela.mainloop()