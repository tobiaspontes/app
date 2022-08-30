import tkinter as tk

def fahrenheit_to_celsius():
    # Converte o valor de Fahrenheit para Celsius e insere o resultado em  lbl_resultado.
    fahrenheit = ent_temperatura_f.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_resultado_f['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

def celsius_to_fahrenheit():
    # Converte o valor de Celsius para Fahrenheit e insere o resultado em  lbl_resultado.
    celsius = ent_temperatura_c.get()
    fahrenheit = ((float(celsius)) * (9 / 5)) + 32
    lbl_resultado_c['text'] = f'{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}'


janela = tk.Tk()
janela.title('Conversor de Temperatura')
janela.resizable(width=False, height=False)
janela.geometry('320x100')

# Layout para conversão de Fahrenheit em Celsius
frm_entrada_f = tk.Frame(master=janela, padx=20)
ent_temperatura_f = tk.Entry(master=frm_entrada_f, width=10, justify='center')
lbl_temperatura_f = tk.Label(master=frm_entrada_f, text='\N{DEGREE FAHRENHEIT}')

ent_temperatura_f.grid(row=0, column=0, sticky='e')
lbl_temperatura_f.grid(row=0, column=1, sticky='w')

btn_converte_f = tk.Button(master=janela, text='\N{RIGHTWARDS BLACK ARROW}', command=fahrenheit_to_celsius, padx=20)
lbl_resultado_f = tk.Label(master=janela, text='\N{DEGREE CELSIUS}', padx=20)

frm_entrada_f.grid(row=0, column=0, padx=10)
btn_converte_f.grid(row=0, column=1, pady=10)
lbl_resultado_f.grid(row=0, column=2, padx=10)

# Layout para conversão de Celsius em Fahrenheit
frm_entrada_c = tk.Frame(master=janela, padx=20)
ent_temperatura_c = tk.Entry(master=frm_entrada_c, width=10, justify='center')
lbl_temperatura_c = tk.Label(master=frm_entrada_c, text='\N{DEGREE CELSIUS}')

ent_temperatura_c.grid(row=0, column=0, sticky='e')
lbl_temperatura_c.grid(row=0, column=1, sticky='w')

btn_converte_c = tk.Button(master=janela, text='\N{RIGHTWARDS BLACK ARROW}', command=celsius_to_fahrenheit, padx=20)
lbl_resultado_c = tk.Label(master=janela, text='\N{DEGREE FAHRENHEIT}', padx=20)

frm_entrada_c.grid(row=1, column=0, padx=10)
btn_converte_c.grid(row=1, column=1, pady=10)
lbl_resultado_c.grid(row=1, column=2, padx=10)

janela.mainloop()
