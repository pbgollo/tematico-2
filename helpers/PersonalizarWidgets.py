class PersonalizarWidgets:
    def __init__(self, small_font=("Arial", 9), medium_font=("Arial", 11, "bold"), big_font=("Arial", 18, "bold"), giant_font=("Arial", 22, "bold"), cor_primaria='#70cfff', cor_secundaria='#ffc400', cor_terciaria='#21b3ed', cor_vermelha='#ff4d4d'):
        self.small_font = small_font 
        self.medium_font = medium_font
        self.big_font = big_font
        self.cor_primaria = cor_primaria
        self.cor_secundaria = cor_secundaria
        self.cor_terciaria = cor_terciaria
        self.cor_vermelha = cor_vermelha
        self.giant_font = giant_font

    def configurar_small_label(self, widget, fg="white", bg=None):
        widget.config(font=self.medium_font, fg=fg, bg=bg or self.cor_primaria)

    def configurar_big_label(self, widget, fg="white", bg=None):
        widget.config(font=self.big_font, fg=fg, bg=bg or self.cor_primaria)

    def configurar_giant_label(self, widget, fg="white", bg=None):
        widget.config(font=self.giant_font, fg=fg, bg=bg or self.cor_primaria)

    def configurar_entry(self, widget, fg="black", bg="#fafafa"):
        widget.config(font=self.small_font, fg=fg, bg=bg, relief="flat")

    def configurar_button_amarelo(self, widget, fg="white", bg=None):
        widget.config(font=self.medium_font, fg=fg, bg=bg or self.cor_secundaria, bd=0)

    def configurar_button_azul(self, widget, fg="white", bg=None):
        widget.config(font=self.medium_font, fg=fg, bg=bg or self.cor_terciaria, bd=0)
        
    def configurar_button_vermelho(self, widget, fg="white", bg=None):
        widget.config(font=self.medium_font, fg=fg, bg=bg or self.cor_vermelha, bd=0)
        

