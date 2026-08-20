class objeto:
    def __init__(self,nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def mostrar_informacion(self):
        print(f"objeto: {self.nombre}")
        print(f"tipo: {self.tipo}")

    