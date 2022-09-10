import tkinter as tk


def calcula_imc():
    peso = float(ent_peso.get())
    altura = float(ent_altura.get())
    imc = peso / altura ** 2
    if imc < 18.5: lbl_imc['text'] = f'IMC = {imc:,.1f} - Abaixo do peso normal'
    if 18.5 <= imc <= 24.9: lbl_imc['text'] = f'IMC = {imc:,.1f} - Peso normal'
    if 25 <= imc <= 29.9: lbl_imc['text'] = f'IMC = {imc:,.1f} - Sobrepeso'
    if 30 <= imc <= 34.9: lbl_imc['text'] = f'IMC = {imc:,.1f} - Obesidade I'
    if 35 <= imc <= 39.9: lbl_imc['text'] = f'IMC = {imc:,.1f} - Obesidade II'
    if imc >= 40: lbl_imc['text'] = f'IMC = {imc:,.1f} - Obesidade III'


janela = tk.Tk()
janela.title('Cálculo do IMC')
janela.geometry('300x200')

lbl_peso = tk.Label(text='Informe seu peso em Kg', pady=5)
lbl_peso.pack()
ent_peso = tk.Entry(width=10, justify='center')
ent_peso.pack()

lbl_altura = tk.Label(text='Informe sua altura', pady=5)
lbl_altura.pack()
ent_altura = tk.Entry(width=10, justify='center')
ent_altura.pack()

btn_calcula = tk.Button(text='Calcular', command=calcula_imc)
btn_calcula.pack(pady=10)

lbl_imc = tk.Label(text='', pady=10)
lbl_imc.pack()

janela.mainloop()