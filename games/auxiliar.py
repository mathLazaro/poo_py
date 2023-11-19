from tkinter import messagebox



class ShowView:
    def __init__(self, titulo:str, mensagem:str):
        messagebox.showinfo(titulo,mensagem)