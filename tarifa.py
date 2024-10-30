from datetime import datetime
import time 


def calculo_tarifa():
    
  
    tarifa_por_intervalo = 500  # Costo cada 15 minutos
    intervalo = 15 * 60  # Intervalo en segundos
    total_a_pagar = 0

    while True:
        time.sleep(intervalo)
        total_a_pagar += tarifa_por_intervalo
        print(f"Tarifa acumulada: ${total_a_pagar}")
    
    
    
