import random
import math 
import csv

trabajadores=["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos={}

def asignar_sueldos():
    global sueldos
    sueldos={}
    for trabajador in trabajadores:
        sueldos["trabajador"]={"sueldo":random.randint(300000,2500000)}
    print("sueldos asignados aleatoriamente")

def clasificar_sueldos():
    clasificacion={"menor":[],"medianos":[],"mayores":[]}
    for trabajadores,datos in trabajadores.items():
        sueldo=datos["sueldo"]
        if sueldo < 800000:
            clasificacion["menor"].append(trabajador)
        elif sueldo >= 800000 or sueldo < 2000000:
            clasificacion["medianos"].append(trabajador)
        else:
            clasificacion["mayores"].append(trabajador)
    print("Clasificacion ")
    for categoria,lista in clasificacion.items():
        print(f"{categoria}: {', '.join(lista)}")
    print()

def estadisticas_3():
    sueldos=[datos["sueldo"] for datos in trabajadores.values()]

    estadisticas={
        "sueldo mas alto":max(trabajadores, key=lambda k:trabajadores [k]["sueldo"]),
        "sueldo mas bajo":min(trabajadores, key=lambda k:trabajadores [k]["sueldo"]),
        "promedio de sueldos":sum(sueldos)/ len(sueldos),
        "media geometrica":math.exp(sum(math.log))
        }
    
            






def menu():
    while True:
        print("""
        1)asignar sueldos aleatorios
        2)clasificar sueldos
        3)ver estadisticas
        4)reporte de sueldos
        5)salir
              
                """)
        opc=input("ingrese una opcion: ")

        while not opc.isnumeric():
            print("eso no es un numero")
            opc=input("ingrese una opcion: ")
        opc=int(opc)

        if opc==1:
            asignar_sueldos()
        
        elif opc==2:
            clasificar_sueldos()
        
        elif opc==3:
            estadisticas_3()
        elif opc==4:
            break


if __name__=="__main__":
    menu()