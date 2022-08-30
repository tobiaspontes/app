# sobre tkinter consulte https://realpython.com/python-gui-tkinter/
# importando a biblioteca
import tkinter as tk
from tkinter import ttk

dicionario_cotacoes = {
    'Dólar': 5.43,
    'Euro': 6.56,
    'Bitcoin': 20000
}

moedas = list(dicionario_cotacoes.keys())


def buscar_cotacao():
    moeda_preenchida = moeda.get()  # método get retorna o texto de uma entrada do usuário
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida) # busca valor no dicionário pra chave informada
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'A cotação de 1 {moeda_preenchida} é de {cotacao_moeda} Reais.'
    else:
        mensagem_cotacao['text'] = 'Cotação não encontrada!'


def buscar_cotacoes():
    texto = caixa_texto.get('1.0', tk.END) # obtém o texto desde o caracter de índice 0 da linha 1 até o fim
    lista_moedas = list(texto.split('\n')) # cria uma lista a partir do texto
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}: {cotacao}')
    texto4 = tk.Label(text='\n'.join(mensagem_cotacoes), bg='blue', fg='white')
    texto4.grid(row=6, column=1)


# criando a janela e dando um título
janela = tk.Tk()
janela.geometry('400x300') # define o tamanho da janela
janela.title('Cotação de Moedas')
# janela.rowconfigure(0, weight=1) # configura a primeira linha da janela para expandir automaticamente
janela.columnconfigure([0, 1], weight=1) # configura duas colunas para expandir automaticamente

# criando um label e utilizando o método grid para posicionar na janela
texto1 = tk.Label(text='Sistema de Busca de Cotação de Moedas', fg='white', bg='black', height=2, width=35)
texto1.grid(row=0, column=0, columnspan=2, sticky='NSEW') # columnspan expande para um número de colunas; sticky indica a direção da expansão (N=norte, S=sul, E=leste, W=oeste)
# para mais informações sobre o método grid: https://www.tutorialspoint.com/python/tk_grid.htm

# criando um label e posicionando
texto2 = tk.Label(text='Selecione a moeda desejada', pady=10)
texto2.grid(row=1, column=0)

# moeda = tk.Entry() # um campo de entrada para o usuário digitar a moeda
# moeda.grid(row=1, column=1)
moeda = ttk.Combobox(janela, values=moedas)  # informa a janela e a lista de valores do combobox
moeda.grid(row=1, column=1)

botao = tk.Button(text='Buscar Cotação', command=buscar_cotacao, pady=5) # text é o título do botão e command chama a função associada ao botão
botao.grid(row=2, column=0)

mensagem_cotacao = tk.Label(text='', pady=5, bg='blue', fg='white') # cria um label padrão para ser exibido ao usuário
mensagem_cotacao.grid(row=2, column=1)

texto3 = tk.Label(text='Caso queira mais de uma cotação, digite uma moeda em cada linha.', pady=10)
texto3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(width=10, height=5, relief=tk.RIDGE, borderwidth=5)
caixa_texto.grid(row=5, column=0, sticky='nsew')

botao_multiplas_cotacoes = tk.Button(text='Buscar cotações', command=buscar_cotacoes, pady=5)
botao_multiplas_cotacoes.grid(row=5, column=1)

# método para a janela ficar ativa em loop infinito
janela.mainloop()