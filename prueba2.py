
esc = lambda code: f'\033[{code}m'
error = lambda message: print(esc('31;1;2') + '[ERROR]' + esc(0) + f' {message}')

name = input('Hola, ¿cual es tu nombre?: ')
user_1 = input(f'\n{name} escribe el nombre del usuario 1: ')
year_user_1 = 0

while year_user_1 == 0:
    try:
        year_user_1 = int(input(f'\nPor favor indica el año de nacimiento de {user_1}: '))
    except:
        error('Escribe un número válido!!')

age_user_1 = 2020 - (year_user_1)

user_2 = input('\nAhora escribe el nombre del usuario 2: ')
year_user_2 = 0

while year_user_2 == 0:
    try:
        year_user_2 = int(input(f'\nPor favor indica el año de nacimiento de {user_2}: '))
    except:
        error('Eres un tonto, eso no es un número!!')

age_user_2 = 2020 - (year_user_2)

if age_user_1 > age_user_2:
    age1_users = age_user_1 - age_user_2
    print(f'{user_1} tiene {age_user_1} años y es mayor que {user_2} que tiene {age_user_2} años.')
    print(f'{user_1} nació {age1_users} años antes que {user_2}')

elif age_user_1 < age_user_2:
    age2_users = age_user_2 - age_user_1
    print(f'\n{user_1} tiene {age_user_1} años y es menor que {user_2} que tiene {age_user_2} años.')
    print(f'{user_2} nació {age2_users} años antes que {user_1}.')

else:
    print(f'{user_1} y {user_2} tienen la misma edad {age_user_1 or age_user_2} años.')
