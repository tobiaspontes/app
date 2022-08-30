import tkinter as tk

# Cria uma nova janela com um título
janela = tk.Tk()
janela.title("Formulário para Endereço")

# Cria um frame para conter os labels e entradas do usuário
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

# Cria uma lista com os labels e largura das entradas (lista de tuplas)
labels = [
    ("Primeiro Nome:", 50),
    ("Último Nome:", 20),
    ("Endereço (linha 1):", 50),
    ("Endereço (linha 2):", 50),
    ("Cidade:", 30),
    ("Estado:", 10),
    ("Código Postal:", 20),
    ("País:", 20)
]

# Loop para preencher o frame com os labels e as entradas
for idx, (texto, largura) in enumerate(labels):
    label = tk.Label(master=frm_form, text=texto)
    entry = tk.Entry(master=frm_form, width=largura)
    label.grid(row=idx, column=0, sticky="e", pady=5)
    entry.grid(row=idx, column=1, sticky='w', pady=5)

# Cria novo frame para conter os botões de "Processar" e "Limpar"
# Esse frame ocupará a janela toda na direção horizontal
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipady=10)

# Cria o botão "Processar" e o empacota no lado direito do frame
btn_enter = tk.Button(master=frm_buttons, text="Enter")
btn_enter.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Cria o botão "Limpar" e o empacota no lado direito do frame
btn_limpa = tk.Button(master=frm_buttons, text="Limpar")
btn_limpa.pack(side=tk.RIGHT, ipadx=10)

# Inicia o app
janela.mainloop()