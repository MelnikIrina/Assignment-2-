user_input = input("Введи свій варіант: ")
if user_input.isdigit():
# Якщо рядок складається тільки з цифр, сміливо
перетворюємо його на число
guess = int(user_input)
# Тут буде ваша логіка порівняння числа (if/elif/else)
if guess < secret_number:
                print("- число більше!")
            elif guess > secret_number:
                print("- число менше!")
            else:
                print(f"Молодець,! Ти вгадав число {secret_number}")

print("Помилка! Потрібно вводити тільки цілі числа.")
