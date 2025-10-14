from tkinter import *
from tkinter import messagebox
import subprocess
import subprocess
from PIL import Image, ImageTk

tela = Tk()
tela.title("Menu")
tela.geometry("800x600")

largura = 1000
altura = 700

caminho_imagem = "icones\imagem_fundo.png"

imagem_pil = Image.open(caminho_imagem)
largura, altura = imagem_pil.size
if largura > 2078:
    proporcao = largura / 2078
    nova_altura = int(altura / proporcao)
    imagem_pil = imagem_pil.resize((1024, nova_altura))
imagem_tk = ImageTk.PhotoImage(imagem_pil)
lbl_imagem = Label(tela, image=imagem_tk)
lbl_imagem.image = imagem_tk
lbl_imagem.place(x=0, y=0)    

def abrir_tela_clientes():
    subprocess.run(["python", "clientes.py"])

def abrir_tela_animais():
    subprocess.run(["python", "animais.py"])

def abrir_tela_servicos():
    subprocess.run(["python", "servico.py"])    

def logout():
    tela.destroy()
    subprocess.run(["python", "login.py"])  

barra_menus = Menu(tela)

opcoes_menus_arquivos = Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)
opcoes_novo = Menu(opcoes_menus_arquivos)

barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)
opcoes_novo.add_command(label="cadastrar")
opcoes_menus_arquivos.add_command(label="Abrir")
opcoes_menus_arquivos.add_command(label="Salvar")
opcoes_menus_arquivos.add_command(label="Salvar como...")
opcoes_menus_arquivos.add_separator()
opcoes_menus_arquivos.add_command(label="Sair", command=tela.quit)
barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)
opcoes_menus_gestao.add_command(label="Animais", command=abrir_tela_animais)
opcoes_menus_gestao.add_command(label="Clientes", command=abrir_tela_clientes)

       

tela.config(menu=barra_menus)

foto_sair = PhotoImage(file = r"icones\logo_animais.png")
foto_animais = PhotoImage(file = r"icones\logo_animais.png")
foto_usuarios = PhotoImage(file = r"icones\logo_usuarios.png")
foto_servicos = PhotoImage(file = r"icones\logo_servicos.png")
foto_logout = PhotoImage(file = r"icones\logout.png")
#opcoes_novo.add_command(label="Salvar Imagem")
#opcoes_novo.add_command(label="Pasta")

lbl_logo = Label(tela, text="PET SHOP DOG´S", compound= TOP, image=foto_sair).place(x=890, y=580)
btn_animais = Button(tela, text="Animais", image=foto_animais, compound= TOP, command=abrir_tela_animais).place(x=100, y=200)
btn_clientes = Button(tela, text="Clientes",image=foto_usuarios, compound= TOP, command=abrir_tela_clientes).place(x=350, y=200)
btn_servicos = Button(tela, text="Serviços",image=foto_servicos, compound= TOP, command=abrir_tela_servicos).place(x=550, y=200)
btn_logout = Button(tela, text="Logout", image=foto_sair, compound= TOP, command=logout).place(x=800, y=200)

tela.mainloop()