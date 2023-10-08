#Importamos librerias
import locale
from IPython.display import clear_output
from datetime import datetime

def RemoveLogs():
    #Si elige borarlos se reescriben los logs con un mensaje que indica la fecha de la limpieza y se limpia la consola.
    clear_output()
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogRefreshDate =  (dt.strftime("[-- Refresh Created At: %d/%m/%Y - %H:%M:%S --]"))
    
    open('Log/LogPersonajes.txt', 'w').close
    with open('Log/LogPersonajes.txt', 'w') as ArchivoLogPE:
        ArchivoLogPE.write(f"{LogRefreshDate}\nBienvenido al archivo de Log Personajes\n---------------------------------------")

    open('Log/LogPartidas.txt', 'w').close
    with open('Log/LogPartidas.txt', 'w') as ArchivoLogPA:
        ArchivoLogPA.write(f"{LogRefreshDate}\nBienvenido al archivo de Log Partidas\n-------------------------------------")

    open('Log/LogSystem.txt', 'w').close
    
    print("¡Logs Reiniciados!")

#Creamos Funciones para almacenar los Logs de la partida y los personajes.
def LogPersonajes(Personaje1, Atributos1, Personaje2, Atributos2):
    # Colocamos un timestamp
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPeDate =  (dt.strftime("[-- Characters Log Created At: %d/%m/%Y - %H:%M:%S --]"))
    LogPe = (f"\n{LogPeDate}\n{Personaje1} con los atributos: {Atributos1}\n{Personaje2} con los atributos {Atributos2}\n--------------------------------------------------------")
    with open('Log/LogPersonajes.txt', 'a') as ArchivoLogPE:
        ArchivoLogPE.write(LogPe)
    
def LogPartida(Personaje1,Personaje1Name, Personaje2, Personaje2Name,opcion, TurnosElejidos, TurnosJugados, Resultado):
    #Comprobamos el metodo de asignacion de valores.
    Metodo = ""
    if opcion == "1":
        Metodo = "Automático"
    elif opcion == "2":
        Metodo = "Manual"
        
    # Colocamos un timestamp
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPaDate = (dt.strftime("[-- Game Log Created At: %d/%m/%Y - %H:%M:%S --]"))    
    LogPa = (f"\n{LogPaDate}\nPersonaje 1 | {Personaje1Name}:{Personaje1}\nPersonaje 2 | {Personaje2Name}:{Personaje2}\nMétodo de elección = {Metodo}\nTurnos [Elejidos/Jugados] = {TurnosElejidos}/{TurnosJugados}\nResultado:{Resultado}\n--------------------------------------------------")
    #Cargamos el .excel que registra los datos, los cargamos y lo cerramos
    with open('Log/LogPartidas.txt', 'a') as ArchivoLogPA:
        ArchivoLogPA.write(LogPa)

def SystemLog(ListaDatos):
    # Colocamos un timestamp
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogSysDate =  (dt.strftime("%d/%m/%Y - %H:%M:%S"))
    ListaDatos.append = LogSysDate
    with open('Log/LogSystem.txt', 'a') as ArchivoLogSys:
        ArchivoLogSys.write(LogSysDate)

