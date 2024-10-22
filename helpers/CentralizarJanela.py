import tkinter as tk

class CentralizarJanela:
    @staticmethod
    def centralizar(root, largura_janela, altura_janela):
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)

        root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")