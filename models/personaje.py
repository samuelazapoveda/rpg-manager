class Personaje:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.nivel = 1
        self.vida = 100

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "clase": self.clase,
            "nivel": self.nivel,
            "vida": self.vida
        }