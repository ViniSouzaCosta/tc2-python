from tkinter import *
#criação da variavel
tela = Tk()

#Titulo na barra de tarefas
tela.title("Fatec Registro")
#Configuração da cor da tela (opcional)
tela.configure(background= '#1e3743')
#Configuração do tamanho da tela
tela.geometry("700x600")

tela.resizable(True, True)
#Tamanho maximo que a tela pode chegar
tela.maxsize(width=800, height=700)
#Tamanho minimo que a tela pode chegar
tela.minsize(width=500, height=300)


lbl_nome = Label(tela, text="NOME").place (x=10, y=10)
lbl_cpf = Label(tela, text="CPF").place(x=10, y=50)
#lbl_nome e o nome de indentificação interno da label
#Label e o tipo do componente
#tela a variavel que a label está ligado
#text="" e o texto a ser exibido na tela
#place o posicionamento da tela
tela.mainloop()