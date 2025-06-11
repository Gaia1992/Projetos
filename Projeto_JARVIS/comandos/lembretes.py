from datetime import datetime

# Função para adicionar lembrete
def adicionar_lembrete(comando, hora=None, data=None):
    if data and hora:  # Se tanto a data quanto a hora foram passadas
        # Unir data e hora em um único datetime
        data_hora = f"{data} {hora}"
        try:
            lembrete_data = datetime.strptime(data_hora, "%d/%m/%Y %Hh%M")  # Formato de data + hora
            print(f"Lembrete agendado para: {lembrete_data}")
        except ValueError:
            print("Formato de data e hora inválido. Use: 'dd/mm/aaaa hh:mm'. Exemplo: 25/04/2025 10h30.")
    elif hora:  # Se só a hora for passada
        try:
            lembrete_hora = datetime.strptime(hora, "%Hh%M")
            print(f"Lembrete agendado para: {lembrete_hora}")
        except ValueError:
            print("Formato de hora inválido. Use: 'hh:mm'. Exemplo: 10h30.")
    else:  # Se apenas a tarefa foi dada, sem data ou hora
        print(f"Lembrete agendado: {comando}")