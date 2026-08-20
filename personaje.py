from Inventario import Inventario

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = Inventario()

    def atacar(self):
        print (f"{self.nombre} realiza un ataque.")

    def recibir_danio(self, danio):
        
        self.vida -= danio
        # self.vida = self.vida - danio
        
        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibe {danio} punto de daño")
        print(f"vida actual: {self.vida}")

    def mostrar_informacion(self):
        print("INFORMACION DEL P3---")
        print(f"nombre: {self.nombre}")
        print(f"vida: {self.vida}")
        print/f"nivel: {self.nivel}"
