import random

secret_number = random.randint(1, 20)

for guesses_taken in range(1, 7):
    guess = int(input('1から20までの数を当ててください：'))

    if guess == secret_number:
        print(f'当たり！{guesses_taken}回で当たりました！')
        break
    elif guess < secret_number:
        print('小さいです。')
    else:
        print('大きいです。')
else:
    print(f'残念。正解は{secret_number}でした。')

