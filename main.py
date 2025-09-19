from random import randint

nickname = input("Ти увімкнув гру <Вгадай число>. Тож тепер придумай собі ім'я: ")
print(f"Супер, {nickname}! Я загадав число від 1 до 50. Спробуй вгадати!")

secret_number = randint(1,50)

game = True
while game:
        user_input = input("Введи свій варіант: ")

        if user_input.isdigit():  # перевірка, чи це число
            guess = int(user_input)

            if guess < secret_number:
                print("- число більше!")
            elif guess > secret_number:
                print("- число менше!")
            else:
                print(f"Молодець,! Ти вгадав число {secret_number}")
        else:
            print("Випив ? - За гру не сідай. Пиши тільки цифри)")
print(f"{nickname}, дякую за гру!")
