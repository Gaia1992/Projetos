import os

def abrir_aplicativo(nome):
    nome = nome.lower()

    if "chrome" in nome:
        os.system("start chrome")
        return "Abrindo Google Chrome."
    elif "whatsapp" in nome:
        os.system("start https://web.whatsapp.com/")
        return "Abrindo WhatsApp Web."
    elif "word" in nome:
        os.system("start winword")
        return "Abrindo Microsoft Word."
    else:
        return "Não conheço esse aplicativo ainda."