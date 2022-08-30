import tkinter as tk


def enviar():
    if var_promocoes.get(): # 0 = False   1 = True
        print('Usuário deseja receber promoções.')
    else:
        print('Usuário NÃO deseja receber promoções.')
    if var_politicas.get():
        print('Usuário concordou com Termos de Uso e Políticas de Privacidade.')
    else:
        print('Usuário NÃO concordou com Termos de Uso e Políticas de Privacidade.')


janela = tk.Tk()

var_promocoes = tk.IntVar() # variável que vai receber o resultado do checkbox (0 = não marcado ou 1 = marcado)
checkbox_promocoes = tk.Checkbutton(text='Deseja receber e-mails promocionais?', variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text='Aceitar Termos de Uso e Políticas e Privacidade', variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()