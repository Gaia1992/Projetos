import pywhatkit

def tocar_musica(musica):
    try:
        pywhatkit.playonyt(musica)
        return f"Tocando {musica} no YouTube..."
    except:
        return "Não consegui tocar a música. Verifique sua conexão com a internet."