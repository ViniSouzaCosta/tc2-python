from tkinter import *
tela = Tk()

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue",bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome")

def meu_click():
    lbl_hello = Label(tela, text="Bem Vindo " + txt_nome.get())
    lbl_hello.pack()

btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()


tela.title("Fatec Registro")
tela.geometry("700x600")
tela.resizable(True,True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

lbl_nome = Label(tela, text="Nome", font="Arial 20 bold italic", fg="#FF8C00").place(x=10 , y=10)
lbl_cpf = Label(tela, text="CPF", font="Times 15 italic", fg="#7CFC00").place(x=10, y=50)
tela.mainloop()
