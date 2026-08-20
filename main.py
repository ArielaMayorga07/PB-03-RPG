from jugador import Jugador
from mago import  mago
from objeto import objeto


#Método principal

def main():

    # CREAR JUGADOR
    nuevo_jugador = Jugador("Ariela")

    # CREAR PJS
    magician = mago("Gandalf", 10, 100, 80)

   # ASOCIAR JUGADOR CON EL PJ
    nuevo_jugador.seleccionar_personaje(magician)
    nuevo_jugador.mostrar_personaje()

    # ATAQUE DEL MAGO
    magician.atacar()

    # CREAR OBJETOS
    pocion = objeto("pocion de vida", "consumible")
    staff = objeto("staff del Arcangel", "Arma")

    # AGREGAR AL INVENTARIO
    magician.inventario.agregar_objeto(pocion)
    magician.inventario.agregar_objeto(staff)

    # MOSTRAR INVENTARIO
    magician.inventario.mostrar_inventario()

if __name__== "__main__":
    main()