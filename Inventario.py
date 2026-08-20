class Inventario:
    def __init__(self):
        self.objetos ={}
    
    def agregar_objetos(Self, objeto):
        
        Self.objetos.append(objeto)

        print(f"{objeto.nombre} ha sido agregado al Inventario.")

    def mostrar_inventario(self):
        print("\n ---INVENTARIO---")

        if len(self.objetos)== 0:
            print("El Inventario esta vacio")
        else:
            for objeto in self.objetos:
                print(f"-{objeto.nombre} {{objeto.tipo}}")


        