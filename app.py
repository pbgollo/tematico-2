from database.db import engine, Base
from models import *
import tkinter as tk
from views.LoginGui import LoginView
from views.ConvidadoGui import ConvidadoView
from views.FormEventoGui import FormEventoView

Base.metadata.create_all(bind=engine)

def iniciar_app():
    root = tk.Tk()  
    app = FormEventoView(root)  
    root.mainloop()

if __name__ == "__main__":
    iniciar_app()