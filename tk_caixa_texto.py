# Exemplo de Label, Entry, Button e Text
#
import tkinter as tk

def trata_entrada():
    nome = ent_entrada.get()  # acessa o que o usuário digitou
    txt_caixa_texto.insert(tk.END, nome) # insere a entrada do usuário na caixa de texto
    ent_entrada.delete(0, tk.END) # deleta o que o usuário digitou
    ent_entrada.insert(0, 'Outro Nome') # apresenta outro texto na entrada do usuário
    entrada_cx_texto = txt_caixa_texto.get('1.0', tk.END) # obtém todo o texto da caixa de texto
    print(entrada_cx_texto) # imprime no terminal o texto da caixa de texto
    txt_caixa_texto.delete('1.0', '1.5') # deleta desde o primeiro caracter até o quinto caracter da caixa de texto
    txt_caixa_texto.insert('1.0', 'Agora eu digo')
    txt_caixa_texto.insert('2.0', 'Mais um texto\n')
    txt_caixa_texto.insert(tk.END, '\nInserindo texto na última linha')


janela = tk.Tk()

lbl_nome = tk.Label(text='Nome')
ent_entrada = tk.Entry()
btn_botao = tk.Button(text='Click me!', command=trata_entrada)
txt_caixa_texto = tk.Text()

lbl_nome.pack()
ent_entrada.pack()
btn_botao.pack()
txt_caixa_texto.pack()


janela.mainloop()
