from modulo_morse import texto_morse
from modulo_sonidos import morse_sonido

def menu():
    numero = int(input("\n1.Traducir texto a codigo morse \n2.Reproducir codigo morse del texto codificado\n3.Salir del programa \n\nSeleccione una opción: "))
    
    return numero

opcion = menu()

texto = ''

while 0 < opcion < 5:
    match opcion:
        case 1:
            texto = input("Ingrese un texto: ")
            texto_codificado = texto_morse(texto)
            print("Texto codificaco a morse: ", texto_codificado)

        case 2:
            if len(texto) > 0:
                morse_sonido(texto)
            else:
                print("ERROR. Primero debe ingrsar un texto con la opcion 1")

        case 3:
            print("Adios, fin del programa")
            exit()
        
    opcion = menu()







