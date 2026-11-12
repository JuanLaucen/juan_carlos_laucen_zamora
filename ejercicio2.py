equipos_disponibles=20
salir=0
equipos_asignados=0
print("Bienvenida ¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Inves-tigación!")

try:
    while (salir==0):
        print("=== MENÚ PRINCIPAL ===")
        print("1.- Equipos disponibles.")
        print("2.- Asignar equipo.")
        print("3.- Liberar equipo.")
        print("4.- Historial de usos.")
        print("5.- Salir.")
        opcion=int(input("Ingrese \n"))

        match opcion:
            case 1:
                print(equipos_disponibles)
            case 2:
                equipos_solicitud=int(input("ingrese numero de equipos que desea asignar \n"))
                if equipos_solicitud <0 or equipos_solicitud> equipos_disponibles:
                    print("ingrese una cantidad Valida a ingresar")
                else:
                    equipos_asignados+=equipos_solicitud 
                    equipos_disponibles-=equipos_solicitud
            case 3:
                equipos_liberar=int(input("ingrese la cantidad de equipos que quiere liberar \n"))
                if equipos_liberar>0 and equipos_liberar<=20:
                    equipos_disponibles+=equipos_liberar
                    equipos_asignados-=equipos_liberar
            case 4:
                print("estos son los equipos asignados durante la sesion \n ", equipos_asignados)
            case 5:
                salir+=1
                print("Gracias por utilizar nuestro software, hasta la próxima.")     
except:
    print("valor invalido")