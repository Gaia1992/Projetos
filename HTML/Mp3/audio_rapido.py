from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup

texto = """
Sequencia Rj45

Vizualizando a parte de tras, a ordem e:

1-branco/verde
2-verde
3-branco/laranja
4-azul
5-branco/azul
6-laranja
7-branco/marrom
8-marrom

Jhonata Cuzãooooooooooooooooooo
"""  # Aqui você pode colar todo o texto que quiser

# Gera o áudio original
tts = gTTS(text=texto, lang='pt', slow=False)
tts.save("audio_original.mp3")

# Acelera o áudio
som = AudioSegment.from_file("audio_original.mp3")
som_rapido = speedup(som, playback_speed=1.25)

# Salva o novo arquivo
som_rapido.export("audio_rapido.mp3", format="mp3")
print("Áudio pronto: audio_rapido.mp3")
