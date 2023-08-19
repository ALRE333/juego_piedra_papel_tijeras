# -*- coding: utf-8 -*-
#Piedra papel o tijeras
import random
print('INSTRUCCIONES: Esta una versión resumida del típico juego "piedra, papel o',
      'tijeras" contra la maquina. Para jugar, el usuario deberá escoger primero',
      'una de las tres opciones: PIEDRA (1), PAPEL (2) o TIJERAS (3), para ello',
      'tecleará uno de los tres números (encerrados en parentecis) y, posteriormente,'
      'dará la tecla "ENTER".')
Dic_opciones = {1:'Piedra', 2:'Papel', 3:'tijera'}
opciones = [1, 2, 3]
while True:
    print()
    eleccionUsuario = int(input('¿Cuál es tu elección? '))
    print()
    while eleccionUsuario<1 or 3<eleccionUsuario: #(Con esta primera condición nos aseguramos que el usuario escoja algo valido
        eleccionUsuario = int(input('Esa elección no es valida, \
        por favor vuelva a introducir desición: '))
        print()
    eleccionMaquina = random.choice(opciones)
    #Inicia el juego
    if eleccionMaquina == eleccionUsuario: #condición de EMPATE
        print('Maquina: ' + str(Dic_opciones[eleccionMaquina]) + ' vs ' + ' Usuario: ' +
            str((Dic_opciones[eleccionUsuario])))
        print()
        print('¡EMPATE!')
        print()
    elif (eleccionMaquina == 1 and eleccionUsuario == 2 or  #condición de victoria
      eleccionMaquina == 2 and eleccionUsuario == 3 or
      eleccionMaquina == 3 and eleccionUsuario == 1):
        print('Maquina: ' + str(Dic_opciones[eleccionMaquina]) + ' vs ' + ' Usuario: ' +
            str((Dic_opciones[eleccionUsuario])))
        print()
        print('¡GANASTE!')
        print()
    else: #condición de derrota
        print('Maquina: ' + str(Dic_opciones[eleccionMaquina]) + ' vs ' + ' Usuario: ' +
            str((Dic_opciones[eleccionUsuario])))
        print()
        print('¡PERDISTE!')
        print()
    volverAJugar = int(input('¿Otra partida? (1: Sí; 2: No) '))
    if volverAJugar == 2:
        break
print()
print('FIN DEL JUEGO')
