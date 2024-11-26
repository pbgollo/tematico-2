from database.db import engine, Base
from models import *
import tkinter as tk
from views.LoginGui import LoginView
from views.ConvidadoGui import ConvidadoView
from views.EventoGui import EventoView
from views.PrincipalGui import PrincipalView

Base.metadata.create_all(bind=engine)

def iniciar_app():
    root = tk.Tk()  
    app = LoginView(root)  
    root.mainloop()

if __name__ == "__main__":
    iniciar_app()