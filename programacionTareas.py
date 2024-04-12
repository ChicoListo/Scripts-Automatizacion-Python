#en este script usamos schedule para ejecutar funciones cada diez segundos.
import schedule
import time

def job():
    print("Ejecutando tarea programada.")

# Programación cada 10 segundos
schedule.every(10).seconds.do(job)

# Bucle para ejecutar programaciones pendientes
while True:
    schedule.run_pending()
    time.sleep(1)  # Esto ayuda a reducir el consumo de CPU al dormir el proceso durante 1 segundo
