import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb 


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Login de usuario")
        self.geometry("250x150")
        self.resizable(False, False)
        self.attributes("-toolwindow", True)
        

        # Ingresa usuario
        tb.Label(self, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_user = tb.Entry(self)
        self.entry_user.grid(row=0, column=1, padx=10, pady=10)

        # Ingresa contraseña
        tb.Label(self, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_pass = tb.Entry(self, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=10)

        frame_botones = tb.Frame(self)
        frame_botones.grid(row=2, column=1, columnspan=2, pady=10)
        btn_login = tb.Button(frame_botones, text="Entrar")  # command=self.login
        btn_login.pack(side="left", padx=5)
        btn_cerrar = tb.Button(frame_botones, text="Cerrar", command=self.destroy)  # Sin paréntesis
        btn_cerrar.pack(side="left", padx=5)

