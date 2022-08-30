import tkinter as tk
import random

def rola_dado():
    valor_dado = random.randint(1, 6)
    label['text'] = str(valor_dado)

janela = tk.Tk()
janela.columnconfigure(0, minsize=150)
janela.rowconfigure([0, 1], minsize=50)

botao = tk.Button(text='Roll', command=rola_dado)
label = tk.Label()

botao.grid(row=0, column=0, sticky="nsew")
label.grid(row=1, column=0)

janela.mainloop()