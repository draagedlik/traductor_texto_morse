from playsound3 import playsound

def morse_sonido(texto):
    """
    La funcion reproduce el codigo morse que se recibe como parametro
    Parametros:
    codigo: string
    """

    # Diccionario donde la clave es el caracter y el valor es el sonido en codigo morse

    dic_sonido_morse = {
        'a': 'sonidos\\letras\\a.mp3',
        'b': 'sonidos\\letras\\b.mp3',
        'c': 'sonidos\\letras\\c.mp3',
        'd': 'sonidos\\letras\\d.mp3',
        'e': 'sonidos\\letras\\e.mp3',
        'f': 'sonidos\\letras\\f.mp3',
        'g': 'sonidos\\letras\\g.mp3',
        'h': 'sonidos\\letras\\h.mp3',
        'i': 'sonidos\\letras\\i.mp3',
        'j': 'sonidos\\letras\\j.mp3',
        'k': 'sonidos\\letras\\k.mp3',
        'l': 'sonidos\\letras\\l.mp3',
        'm': 'sonidos\\letras\\m.mp3',
        'n': 'sonidos\\letras\\n.mp3',
        'o': 'sonidos\\letras\\o.mp3',
        'p': 'sonidos\\letras\\p.mp3',
        'q': 'sonidos\\letras\\q.mp3',
        'r': 'sonidos\\letras\\r.mp3',
        's': 'sonidos\\letras\\s.mp3',
        't': 'sonidos\\letras\\t.mp3',
        'u': 'sonidos\\letras\\u.mp3',
        'v': 'sonidos\\letras\\v.mp3',
        'w': 'sonidos\\letras\\w.mp3',
        'x': 'sonidos\\letras\\x.mp3',
        'y': 'sonidos\\letras\\y.mp3',
        'z': 'sonidos\\letras\\z.mp3',
        '0': 'sonidos\\numeros\\0.mp3',
        '1': 'sonidos\\numeros\\1.mp3',
        '2': 'sonidos\\numeros\\2.mp3',
        '3': 'sonidos\\numeros\\3.mp3',
        '4': 'sonidos\\numeros\\4.mp3',
        '5': 'sonidos\\numeros\\5.mp3',
        '6': 'sonidos\\numeros\\6.mp3',
        '7': 'sonidos\\numeros\\7.mp3',
        '8': 'sonidos\\numeros\\8.mp3',
        '9': 'sonidos\\numeros\\9.mp3',
        '.': 'sonidos\\signos\\punto.mp3',
        ',': 'sonidos\\signos\\coma.mp3',
        '?': 'sonidos\\signos\\pregunta.mp3',
        '!': 'sonidos\\signos\\exclamacion.mp3',
        '-': 'sonidos\\signos\\guion.mp3',
        "'": 'sonidos\\signos\\comilla_simple.mp3',
        '/': 'sonidos\\signos\\barra.mp3',
        '+': 'sonidos\\signos\\mas.mp3',
        '=': 'sonidos\\signos\\igual.mp3'
    }

    for letra in texto:
        if letra in dic_sonido_morse:
            playsound(dic_sonido_morse[letra])
    
    