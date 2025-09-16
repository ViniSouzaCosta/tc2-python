from tkinter import filedialog
from tkinter import *

from PIL import Image, ImageTk
pasta_inicial =""

tela = Tk()
tela.title("open file")
tela.geometry("700x500")

def show():
    Label(tela, text=var.get()).pack()

var = StringVar()
# var = IntVar()

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