import pyttsx3
import speech_recognition as sr
from comandos.abrir_apps import abrir_aplicativo
from comandos.previsao_tempo import obter_previsao
from comandos.tocar_musica import tocar_musica
from comandos.lembretes import adicionar_lembrete

# Inicializa o motor de voz
voz = pyttsx3.init()
voz.setProperty('rate', 150)

def falar(texto):
    print("Jarvis:", texto)
    voz.say(texto)
    voz.runAndWait()

def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print("Você:", comando)
        return comando
    except:
        return "Não entendi, repete por favor."

def processar_comando(comando):
    comando = comando.lower()

    if "hora" in comando:
        from datetime import datetime
        agora = datetime.now().strftime("%H:%M")
        return f"Agora são {agora}"
    
    elif "sair" in comando:
        return "Encerrando, até a próxima!"
    
    elif "abrir" in comando:
        return abrir_aplicativo(comando)
    
    elif "previsão" in comando or "tempo" in comando or "clima" in comando:
        cidade = comando.replace("previsão", "").replace("tempo", "").replace ("clima", "").strip()
        print(f'buscando previsão para: {cidade}')  # debug
        return obter_previsao(cidade)

    elif "toca" in comando or "tocar" in comando or "música" in comando:
        musica = comando.replace("toca", "").replace("tocar", "").replace("música", "").strip()
        return tocar_musica(musica)

    elif "lembre-me" in comando or "lembrar" in comando:
        comando = comando.replace("lembre-me", "").replace("lembrar", "").strip()

        if "no dia" in comando and "às" in comando:
            partes = comando.split("no dia")
            tarefa = partes[0].strip()
            data_e_hora = partes[1].strip()
            data, hora = data_e_hora.split("às")
            adicionar_lembrete(tarefa, hora.strip(), data.strip())
            return f"Lembrete agendado: {tarefa} no dia {data.strip()} às {hora.strip()}."

        elif "às" in comando:
            partes = comando.split("às")
            tarefa = partes[0].strip()
            hora = partes[1].strip()
            adicionar_lembrete(tarefa, hora)
            return f"Lembrete agendado: {tarefa} às {hora}."

        else:
            return f"Lembrete agendado: {comando}."

    else:
        return "Ainda estou aprendendo esse comando."

def modo_texto():
    while True:
        entrada = input("Você: ")
        resposta = processar_comando(entrada)
        falar(resposta)
        if "sair" in entrada.lower():
            break

def modo_voz():
    while True:
        comando = ouvir()
        resposta = processar_comando(comando)
        falar(resposta)
        if "sair" in comando.lower():
            break

# Escolha o modo
if __name__ == "__main__":
    print("Escolha o modo: (1) Texto ou (2) Voz")
    escolha = input("Modo: ")
    if escolha == "1":
        modo_texto()
    elif escolha == "2":
        modo_voz()
    else:
        print("Escolha inválida.")

import os
import shutil


# Função para salvar o código atual
def save_code(file_path):
    # Verifica se o arquivo de código existe
    if os.path.exists(file_path):
        # Cria uma pasta de backup se não existir
        backup_folder = "backup_codes"
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # Caminho do arquivo de backup (sempre com o mesmo nome)
        backup_file_path = os.path.join(backup_folder, "backup.py")

        # Faz a cópia do código atual
        shutil.copy(file_path, backup_file_path)
        print(f"Código salvo com sucesso: {backup_file_path}")
    else:
        print("O arquivo não foi encontrado.")


# Função para reescrever o código com novo conteúdo
def rewrite_code(file_path, new_code):
    # Primeiro, salva o código atual antes de reescrever
    save_code(file_path)

    # Reescreve o código com o novo conteúdo
    with open(file_path, "w") as file:
        file.write(new_code)
    print(f"Código reescrito com sucesso: {file_path}")