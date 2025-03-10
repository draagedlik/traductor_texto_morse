def  datos_personales(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')



#llamada de la funcion
datos_personales(nombre='Juan', apellido='Kildegaard', edad=37)