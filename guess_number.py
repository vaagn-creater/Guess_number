import random


secret_number = random.randint(1, 100)

print("Угадайте число от 1 до 100")

while True:
    # Вводим предположение пользователя
    guess = int(input("Ваше предположение: "))

    # Проверяем предположение пользователя
    if guess < secret_number:
        print("Ваше число меньше загаданного.")

    if guess > secret_number:
        print("Ваше число больше загаданного.")
        
    if guess == secret_number:
        break
    
print('Отличная интуиция! Вы угадали число :)') 