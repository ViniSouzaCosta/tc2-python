from tkinter import *

tela = Tk()
tela.title("open file")
tela.geometry("300x300")

def show():
    Label(tela, text=var.get()).pack()

var = StringVar()
# var = IntVar()

chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="off")
chk_button.deselect()
chk_button.pack()

Button(tela, text="Show me", command=show).pack()

tela.mainloop()