# ej 1 - caja del kiosko
nombre_cliente = input("Ingresa tu nombre: ")

while not nombre_cliente.isalpha():
    nombre_cliente = input("Ingresa tu nombre: ")

cantidad_productos = input("Cuantos productos desea comprar: ")



while not cantidad_productos.isdigit():
    cantidad_productos = input("Cuantos productos desea comprar: ")

cantidad_productos = int(cantidad_productos)

total_sin_descuento = 0
total_con_descuento = 0


for i in range(cantidad_productos):
    precio_productos = input(f"Producto {i+1} - Precio: ")
    while not precio_productos.isdigit():
        precio_productos = input(f"Producto {i+1} - Precio: ")
    precio_productos = int(precio_productos)

    descuento = input("S/N: ")
    while not descuento == "S" or descuento == "s" or descuento == "n" or descuento == "N":
        print("Tienes descuento?")
        descuento = input("S/N: ")

    total_sin_descuento += precio_productos

    if descuento == "s" or descuento == "S":
        precio_productos = precio_productos - (precio_productos * 0.10)

    total_con_descuento += precio_productos

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# ej 2 - acceso al campus y menu seguro

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales invalidas.")

if not acceso:
    print("Cuenta bloqueada")
else:
    while True:
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")
        opcion = input("Opcion: ")

        if not opcion.isdigit():
            print("error: ingrese un numero valido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opcion fuera de rango.")
            continue

        if opcion == 1:
            print("inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: minimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave actualizada.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("¡Vos podes con todo lo que te propongas!")
        elif opcion == 4:
            print("Saliendo...")
            break

# ej 3 - agenda de turnos con nombres

nombre_operador = input("Nombre del operador: ")
while not nombre_operador.isalpha():
    nombre_operador = input("Nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

opcion = 0

while opcion != 5:
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    opcion = input("Opcion:")

    while not opcion.isdigit():
        opcion = input("Opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("ya tiene turno el lunes")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno guardado en Lunes 1")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno guardado en Lunes 2")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno guardado en Lunes 3")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno guardado en Lunes 4")
            else:
                print("no hay turnos el lunes")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(" ya tiene turno el martes")
            elif martes1 == "":
                martes1 = paciente
                print("Turno guardado en Martes 1")
            elif martes2 == "":
                martes2 = paciente
                print("Turno guardado en Martes 2")
            elif martes3 == "":
                martes3 = paciente
                print("Turno guardado en Martes 3")
            else:
                print("No hay turnos el martes")

    elif opcion == 2:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado")
            else:
                print("No se encontro ese paciente el lunes")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado")
            else:
                print("No se encontro ese paciente el martes")

    elif opcion == 3:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)

        if dia == 1:
            print("--- Agenda Lunes ---")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)
        else:
            print("--- Agenda Martes ---")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1
        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes = ocupados_martes + 1
        if martes2 != "":
            ocupados_martes = ocupados_martes + 1
        if martes3 != "":
            ocupados_martes = ocupados_martes + 1
        libres_martes = 3 - ocupados_martes

        print("--- Resumen ---")
        print("Lunes: ocupados", ocupados_lunes, "- libres", libres_lunes)
        print("Martes: ocupados", ocupados_martes, "- libres", libres_martes)

        if ocupados_lunes > ocupados_martes:
            print("El dia con mas turnos es Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("El dia con mas turnos es Martes")
        else:
            print("Hay un empate entre Lunes y Martes")

    elif opcion == 5:
        print("Cerrando sistema...")

    else:
        print("Opcion invalida")

# ej 4 - escape room la boveda

nombre_agente = input("Nombre: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Nombre: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0
resultado = ""

while True:
    if cerraduras_abiertas == 3:
        resultado = "VICTORIA"
        break
    if energia <= 0 or tiempo <= 0:
        resultado = "DERROTA"
        break
    if alarma == True and tiempo <= 3:
        resultado = "DERROTA (bloqueo)"
        break

    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1 Forzar cerradura")
    print("2 Hackear panel")
    print("3 Descansar")
    opcion = input("Opcion: ")

    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        opcion = input("Opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            racha_forzar = 0
            print("La cerradura se trabo. Alarma activada.")
        elif energia < 40:
            print("Riesgo de alarma detectado.")
            numero = input("Elegi un numero entre 1-3: ")
            while not numero.isdigit() or numero not in ("1", "2", "3"):
                numero = input("Elegi un numero entre 1-3: ")
            numero = int(numero)
            if numero == 3:
                alarma = True
                print("Fallaste. Alarma activada.")
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con exito.")
        else:
            cerraduras_abiertas += 1
            print("Cerradura forzada con exito.")

    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Codigo completo. Se abrio una cerradura.")

    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma == True:
            energia -= 10
        print("Descansaste y recuperaste energia.")

print(f"\nResultado final: {resultado}")


# escape room gladiador

print("--- BIENVENIDO A LA ARENA ---")
nombre_jugador = input("Nombre del Gladiador: ")
while not nombre_jugador.isalpha():
    print("Error: Solo se letras.")
    nombre_jugador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_jugador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_jugador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("elegi una accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Opcion: ")
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Error: Ingrese un numero valido.")
        opcion = input("Opcion: ")
    opcion = int(opcion)

    turno_jugador = True

    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5
            print("Golpe critico")
        else:
            danio_final = danio_pesado
        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño")

    elif opcion == 2:
        print("rafaga de golpes")
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print("Usaste una pocion y recuperaste 30 de vida.")
        else:
            print("No quedan pociones")

    turno_jugador = False

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigoataco por {danio_enemigo} puntos de daño")

    print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
