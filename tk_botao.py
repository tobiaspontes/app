from tkinter import Tk, Label, Button

def fui_clicado():
    print('\nFui clicado!')
    botao.config(text='Fui clicado!')

janela = Tk()

texto = Label(text='Olá Live de Python!', font=(14))
texto.pack()

botao = Button(
    text='Clica ni mim!',
    font=(14),
    command=fui_clicado
)
botao.pack()

janela.mainloop()