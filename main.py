from random import randint

secret_number = randint(1,50)

while True:
        user_input = input("Введи свій варіант: ")

        if user_input.isdigit():  # перевірка, чи це число
            guess = int(user_input)

            if guess < secret_number:
                print("число більше!")
            elif guess > secret_number:
                print("число менше!")
            else:
                print(f"Молодець,! Ти вгадав число {secret_number}")
                break
        else:
            print("Випив ? - За гру не сідай. Пиши тільки цифри)")
