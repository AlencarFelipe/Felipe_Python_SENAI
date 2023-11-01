class Locadora:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []

    def adicionar_filme(self,  filme):
        self.catalogo.append(filme)
    
    def listar_catalogo(self):
        print(f"Catalogo da locadora{self.nome}:")
        for filme in self.catalogo:
            print(filme)