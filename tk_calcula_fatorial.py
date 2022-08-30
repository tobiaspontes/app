import tkinter as tk

def fatorial():
    n = int(ent_nro.get())
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    lbl_resultado['text'] = f'{fatorial:,.0f}'.replace(',','.')

janela = tk.Tk()
janela.title('Calcula Fatorial')
janela.resizable(width=True, height=False)
janela.geometry('400x50')

ent_nro = tk.Entry(master=janela, justify='center', width=10)
btn_fatorial = tk.Button(text='!', command=fatorial, padx=20)
lbl_resultado = tk.Label()

ent_nro.grid(row=0, column=0, padx=10, pady=10)
btn_fatorial.grid(row=0, column=1, padx=10)
lbl_resultado.grid(row=0, column=2, padx=10)

janela.mainloop()