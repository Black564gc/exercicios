import json
import os

cabeleleiro = "data.json"

def carregar_dados():
    if os.path.exists(cabeleleiro):
        with open("data", "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return [] 
    
def obter_dados():
    nome_cliente = input("infome o nome do cliente"),
    serviço_desejado = input("informe o serviço desejado"),
    data_agendamento = input(int("informe a data deb agendamento")),
    horario_agendamento = input(int("informe horario agendado ")),
    observaçoes = input("informe a obeservaçoes ")

    
    cabeleleiro = {
        "nome": "nome_cliente", 
        "serviço_desejado": "serviço_desejado",
        "data de agendamento": "data_agendamento",
        "horario de agendamento": "horario_agendamento",
        "observaçoes": "observaçoes"
    }

    return cabeleleiro


    
  