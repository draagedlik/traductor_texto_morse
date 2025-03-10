from playsound3 import playsound

def morse_sonido(texto):
    """
    La funcion reproduce el codigo morse que se recibe como parametro
    Parametros:
    codigo: string
    """

    # Diccionario donde la clave es el caracter y el valor es el sonido en codigo morse

    dic_sonido_morse = {
        'a': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\a.mp3',
        'b': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\b.mp3',
        'c': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\c.mp3',
        'd': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\d.mp3',
        'e': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\e.mp3',
        'f': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\f.mp3',
        'g': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\g.mp3',
        'h': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\h.mp3',
        'i': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\i.mp3',
        'j': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\j.mp3',
        'k': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\k.mp3',
        'l': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\l.mp3',
        'm': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\m.mp3',
        'n': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\n.mp3',
        'o': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\o.mp3',
        'p': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\p.mp3',
        'q': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\q.mp3',
        'r': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\r.mp3',
        's': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\s.mp3',
        't': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\t.mp3',
        'u': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\u.mp3',
        'v': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\v.mp3',
        'w': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\w.mp3',
        'x': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\x.mp3',
        'y': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\y.mp3',
        'z': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\letras\\z.mp3',
        '0': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\0.mp3',
        '1': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\1.mp3',
        '2': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\2.mp3',
        '3': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\3.mp3',
        '4': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\4.mp3',
        '5': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\5.mp3',
        '6': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\6.mp3',
        '7': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\7.mp3',
        '8': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\8.mp3',
        '9': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\numeros\\9.mp3',
        '.': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\punto.mp3',
        ',': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\coma.mp3',
        '?': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\pregunta.mp3',
        '!': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\exclamacion.mp3',
        '-': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\guion.mp3',
        "'": 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\comilla_simple.mp3',
        '/': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\barra.mp3',
        '+': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\mas.mp3',
        '=': 'C:\\Users\\Administrador\\Documents\\GitHub\\traductor-morse\\sonidos\\signos\\igual.mp3'
    }

    for letra in texto:
        if letra in dic_sonido_morse:
            playsound(dic_sonido_morse[letra])
    
    