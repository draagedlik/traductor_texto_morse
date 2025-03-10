from pydub import AudioSegment
from pydub.playback import play

# Crear un sonido vacío de 1 segundo para poder poner entre cada palabra del codigo morse
vacío = AudioSegment.silent(duration=1000)  # duración en milisegundos (1000 ms = 1 segundo)

# Reproducir el sonido vacío
play(vacío)

# Exportar el archivo vacío como MP3
vacío.export("sonido_vacío.mp3", format="mp3")
