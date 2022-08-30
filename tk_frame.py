# Exemplo de Frame
#
import tkinter as tk

dic_efeitos_borda = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

janela = tk.Tk()

for nome_efeito, efeito in dic_efeitos_borda.items():
    frm_quadro = tk.Frame(master=janela, relief=efeito, borderwidth=5)
    frm_quadro.pack(side=tk.TOP, pady=10, padx=10, fill='both')
    lbl_texto = tk.Label(master=frm_quadro, text=nome_efeito)
    lbl_texto.pack()

janela.mainloop()