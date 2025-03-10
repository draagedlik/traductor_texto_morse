def texto_morse (texto):
    """
    La funcion traduce el texto recibido, lo convierte en codigo morse y retorna el texto codificado
    Parametros:
    texto: string
    codigo_morse: string
    """
    
    #diccionario donde cada clave es una letra del abecedario y su conversion a morse
    dic_caracter_morse = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '!': '-.-.--',
        ':': '---...',
        ';': '-.-.-.',
        "'": '.----.',
        '"': '.-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '-': '-....-',
        '+': '.-.-.',
        '=': '-...-',
        '/': '-..-.',
        '@': '.--.-.',
        ' ': '/'
    }
    
    #variable string donde se guardara el codigo morse
    codigo_morse = ""
    
    #convertimos el texto en minuscula
    texto_minuscula = texto.lower()
    
    #buscamos letra por letra y si concuerda con el texto, guarda ese valor en una variables tipo string
    for letra in texto_minuscula:
        if(letra in dic_caracter_morse):
            codigo_morse += dic_caracter_morse[letra]
            
            #entre caracter y caracter morse agregamos un espacio para hacer mas legible el texto convertido
            codigo_morse += " "

    #mustra el resultado del texto en morse        
    return codigo_morse
