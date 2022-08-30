# Exemplo do parâmetro sticky
#
import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=100)
window.columnconfigure([0, 1, 2, 3], minsize=100)

label1 = tk.Label(text="centro", bg="black", fg="white")
label2 = tk.Label(text="leste/oeste", bg="black", fg="white")
label3 = tk.Label(text="norte/sul", bg="black", fg="white")
label4 = tk.Label(text="todo", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()