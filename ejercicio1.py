investigadores_principales=0
investigadores_asistentes=0
registro_cientifico=0
try:
    while(registro_cientifico==0):
        ingreso_cientificos=int(input("ingrese cantidad de cientificos a registrar"))
        if ingreso_cientificos>0:
            registro_cientifico+=ingreso_cientificos
        else:
            print("“¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.”")
    for id in range(registro_cientifico):
        id=input("ingrese la Id de los cientificos").replace("","")
        if len(id)<5:
            print("ingrese un valor valido")
    for publicaciones in range(registro_cientifico):
        publicaciones=int(input("Ingrese cantidad de publicacion de los cientificos"))
        if publicaciones<10 and publicaciones<=0:
            investigadores_asistentes+=1
        elif publicaciones>10:
            investigadores_principales+=1
        else:
            print("“¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.”")
    print("¡El instituto cuenta con ",investigadores_principales)
    print("y con ", investigadores_asistentes)        
except:
    print("ingrese un valor valido")