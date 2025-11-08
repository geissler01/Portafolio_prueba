"""
contador = input('Insert anything: ')
print(f'{contador.count('.')}')

variable = 'Hello world'
print(variable)
print(f'{variable.replace('world','family')}')

variable = '   Hello world '
print(variable)
print(f'{variable.strip()}')



print("2. Comparison Operators")
NUMBER1 = 20
NUMBER2 = "20"
NUMBER3 = 30
print(f"10 == 10 => {10 == 10}")
print(f"10 == 14 => {10 == 14}")
print(f"2 == '2' => {2 == '2'}")
print(f"2 == int('2') => {2 == int('2')}")
print(f"NUMBER1 == int(NUMBER2) => {NUMBER1 == int(NUMBER2)}")
print(f"NUMBER1 == NUMBER3 => {NUMBER1 == NUMBER3}")

print(f"10 != 10 => {10 != 10}")
print(f"10 != 14 => {10 != 14}")
print(f"2 != '2' => {2 != '2'}")
print(f"2 != int('2') => {2 != int('2')}")

PASSWORD = "Abc123"
PASSWORD_CONFIRMATION = "ABC123"
print(f"Passwords match? => {PASSWORD != PASSWORD_CONFIRMATION}")

print(f"{NUMBER1} > {NUMBER3} => {NUMBER1 > NUMBER3}")
print(f"{NUMBER1} < {NUMBER3} => {NUMBER1 < NUMBER3}")
print(f"{NUMBER1} >= {NUMBER2} => {NUMBER1 >= int(NUMBER2)}")
print(f"{NUMBER1} <= {NUMBER3} => {NUMBER1 <= NUMBER3}")
print()

# 3. Logical Operators
print("3. Logical Operators")
height = 4.0
print(f"height >= 1.71 and type(height) == float => {height >= 1.71 and type(height) == float}")
print(f"height >= 1.71 and isinstance(height, int) => {height >= 1.71 and isinstance(height, int)}")

print(f"height >= 1.71 or isinstance(height, float) => {height >= 1.71 or isinstance(height, float)}")

variable = True
print(f"Original variable: {variable}")
print(f"Not variable: {not variable}")



elementos_mixtos = [1, "manzana", 3.14, {'a': 1}]

for elemento in elementos_mixtos:
    if isinstance(elemento, int):
        print(f"Entero encontrado: {elemento * 2}")
    elif isinstance(elemento, str):
        print(f"Cadena encontrada: {elemento.upper()}")
    else:
        print(f"Otro tipo: {type(elemento)}")

"""

# Creating a dictionary
print("2. Creating a dictionary")
person = {
    "name": "Alice",
    "age": 30,
    "city": "Medellín"
}
print(f"Person: {person}")
print()

# Accessing items
print("3. Accessing values by keys")
print(f"Name: {person['name']}")
print(f"City: {person.get('city')}")
print(f"Name: {person['age']}")
print(f"Name: {person.get('age')}")
print()

# Adding and modifying items
print("4. Adding or modifying entries")
person["profession"] = "Engineer"
person["age"] = 31
person["sex"] = 'female'
print(f"Updated person: {person}")
print()