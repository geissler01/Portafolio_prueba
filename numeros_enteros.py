"""
# Opcion simple
user_input = input("Enter a number => ")
if user_input.isdigit():
    number = int(user_input)
    print(f"You entered the integer: {number}")
    print(f"Is it even? => {number % 2 == 0}")
else:
    print("That is not a valid integer!")

"""
# opcion interable si se desea.
while True:
    num = input('Enter a number => ')
    if num.isdigit():
        number = int(num)
        print(f'You entered the integer number: {number}')
        print(f'Is not it even? => {number % 2 == 1}')
        break
    else:
        print('¡That is not valid integer!')
        continue
    