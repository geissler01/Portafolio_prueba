print('*' *30)
print('     |   La granja  |     ')
print('*' *30 +'\n')

animals = []
new_animal = input('Ingrese el nombre de un animal: ')
animals.append(new_animal)

while True:

    print('*** Seleccione la opcion que desee realizar ***\n')
    print('1. Añadir nuevo animal')
    print('2. Listar animales listados')
    print('3. Borrar un animal por ID (posicion)')
    print('4. Borrar todos los animales listados')
    print('5. Listar un animal por ID (posicion)\n')

    selection = int(input('Ingrese el número de su elección: '))

    if selection == 1:
        new_animal = input('Ingrese el nombre de un animal: ')
        animals.append(new_animal)
    elif selection == 2:
        print(f'\nLista de animales: {animals}\n')
    elif selection == 3:
        position = int(input('Ingrese la posición del animal que desea eliminar: '))
        animals.pop(position)
    elif selection == 4:
        animals.clear()
    elif selection == 5:
        id = int(input('Ingrese la posicion de la lista que desea ver: '))
        print(f'El animal seleccionado es: {animals[id]}')
    else: 
        print('Error: ingrese una opcion valida')
        break
    