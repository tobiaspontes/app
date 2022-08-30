import tkinter as tk
from tkinter import filedialog


def abrir():
    print(filedialog.askopenfilename(initialdir='/', title='Abrir', filetypes=(('Python files', '*.py'), ('All files', '*.*'))))


def salvar():
    print(filedialog.asksaveasfilename(initialdir='/', title='Salvar como', filetypes=(('Python files', '*.py'), ('All files', '*.*'))))


app = tk.Tk()
app.geometry('300x200')
app.title('Barra de Menu')

menubar = tk.Menu(app)  # cria a barra de menu principal
filemenu = tk.Menu(menubar, tearoff=0) # cria o menu secundário com suas divisões
filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Salvar', command=salvar)
filemenu.add_command(label='Sair', command=app.quit)
menubar.add_cascade(label='Arquivo', menu=filemenu)  # menu secundário abre em cascata
app.config(menu=menubar)  # define a barra de menu na janela

app.mainloop()