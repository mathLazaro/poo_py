from tkinter import messagebox



class ShowView:
    def __init__(self, titulo:str, mensagem:str, tipo:str):
        if tipo == 'erro':
            messagebox.showerror(titulo,mensagem)
        elif tipo == 'info':
            messagebox.showinfo(titulo,mensagem)