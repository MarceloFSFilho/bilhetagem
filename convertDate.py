#Mudaca de Estado de Servico
from datetime import date, timedelta, datetime
import time

estadoServico = {1: 'fechado',
                 2:'liberado',
                 3: 'ocioso',
                 4:'placa',
                 5: 'comercial'
                 }

def converte_juliana_bil002(data):
    curr_date = "31/12/2002"
    curr_date_temp = datetime.strptime(curr_date, "%d/%m/%Y")
    new_date = curr_date_temp + timedelta(days=int(data))
    format_date = new_date.strftime("%d/%m/%Y")
    return format_date
def convert_hora(segundos):
    return time.strftime("%H:%M:%S", time.gmtime(segundos))

print(converte_juliana_bil002(7596))
print(convert_hora(80436))

print(estadoServico[2])

