class Cidade:
    def __init__(self, name = "Tangamandápio"):
        self.id = None
        self.nome = name
    def __str__(self):
        return "id: " + str(self.id) + " - " + self.nome
