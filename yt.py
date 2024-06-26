import csv
import random
nombre=""
apellido=""
cargo=""
lista_trabajadores=[]
opc=0
sueldo_afp=0
sueldo_salud=0






def grabarArchivo(lista_trabajadores):
    archivo_csv="datos.csv"
    with open(archivo_csv,"w", newline="")as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["nombre","apellido","cargo","sueldo_bruto","sueldo_liquido"])
        escritor.writerows(lista_trabajadores)

def cargarAchivo():
    try:
        archivo_csv="datos.csv"
        with open(archivo_csv,"r")as archivo:
            lector=csv.reader(archivo)
            for fila in lector:
                lista_trabajadores.append(fila)
    except:
        print("Error al cargar el archivo")


def registar():
    try:
        print("Registro de Trabajadores")
        nombre=input("Ingrese su nombre: ")

        apellido=input("Ingrese su apellido: ")

        cargo=input("Ingrese su cargo Mesero/Cocinero/Cajero: ")
      
        sueldo_bruto=input("Ingrese su sueldo bruto: ")
        while not sueldo_bruto.isnumeric():
            print("ingrese solo numero")
            sueldo_bruto=input("Ingrese su sueldo bruto: ")
        sueldo_bruto=int(sueldo_bruto)
        sueldo_afp=sueldo_bruto*0.1
        sueldo_salud=sueldo_bruto*00.7
        
        sueldo_liquido=sueldo_bruto-(sueldo_afp+sueldo_salud)
        

        
        lista_trabajadores.append([nombre,apellido,cargo,sueldo_bruto,sueldo_liquido])
        grabarArchivo(lista_trabajadores)
    except:
        print("Error al Registar")

def mostrar_todo():
        print("Mostrando Todos los Trabajadores")
        for items in lista_trabajadores:
            print(f"Nombre: {items[0]}")
            print(f"Apellido: {items[1]}")
            print(f"Cargo: {items[2]}")
            print(f"Sueldo Bruto: {items[3]}")
            print(f"Sueldo Liquido: {items[4]}")
            print("----------------------------")





def imprimir_sueldos():
        cargo=input("Ingrese su cargo: ")
        encontrado=False
        if cargo=="mesero":
            for items in lista_trabajadores:
                if items[2]==cargo:
                    print(f"Nombre: {items[0]}")
                print(f"Apellido: {items[1]}")
                print(f"Cargo: {items[2]}")
                print(f"Sueldo Bruto: {items[3]}")
                print(f"Sueldo Liquido: {items[4]}")
                print("----------------------------")
                encontrado=True
                
        elif cargo=="cajero":
            for items in lista_trabajadores:
                if items[2]==cargo:
                    print(f"Nombre: {items[0]}")
                    print(f"Apellido: {items[1]}")
                    print(f"Cargo: {items[2]}")
                    print(f"Sueldo Bruto: {items[3]}")
                    print(f"Sueldo Liquido: {items[4]}")
                    print("----------------------------")
                    encontrado=True
                    
        elif cargo=="cocinero":
            for items in lista_trabajadores:
                if items[2]==cargo:
                    print(f"Nombre: {items[0]}")
                    print(f"Apellido: {items[1]}")
                    print(f"Cargo: {items[2]}")
                    print(f"Sueldo Bruto: {items[3]}")
                    print(f"Sueldo Liquido: {items[4]}")
                    print("----------------------------")
                    encontrado=True
                    


def menu():
    cargarAchivo()
    while True:
        print("""

        1)Registar Trabajador
        2)Listar trabajadores
        3)Imprimir sueldos por cargo
        4)Salir 

            """)
        opc=input("Ingrese una opcion: ")
        
        while not opc.isnumeric():
            print("eso no es numero")
            opc=input("Ingrese una opcion: ")
        opc=int(opc)

        if opc==1:
            registar()   
        elif opc==2:
            mostrar_todo()
        elif opc==3:
            imprimir_sueldos()
        elif opc==4:
            print("Saliendo del Programa.......")
            break
    
    



if __name__=="__main__":
    menu()