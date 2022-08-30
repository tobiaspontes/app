import tkinter as tk


def escolha_1():
    print(f'Classe escolhida: {var_opcao.get()}')


def escolha_2():
    print(f'Classe: {var_opcao.get()}')


def escolha_3():
    print(f'Escolha: {var_opcao.get()}')


janela = tk.Tk()

var_opcao = tk.StringVar(value='Nenhuma opção selecionada')

rbtn_economica = tk.Radiobutton(text='Classe Econômica', variable=var_opcao, value='Classe Econômica', command=escolha_1, padx=10, pady=10)
rbtn_executiva = tk.Radiobutton(text='Classe Executiva', variable=var_opcao, value='Classe Executiva', command=escolha_2, padx=10, pady=10)
rbtn_primeira_classe  = tk.Radiobutton(text='Primeira Classe', variable=var_opcao, value='Primeira Classe', command=escolha_3, padx=10, pady=10)

rbtn_economica.grid(row=0, column=0)
rbtn_executiva.grid(row=0, column=1)
rbtn_primeira_classe.grid(row=0, column=2)

janela.mainloop()