import random

def get_input():
    while True:
        print('コインの表裏を当ててください。表か裏を入力してください：')
        guess = input().strip()
        if guess == '裏':
            return 0
        elif guess == '表':
            return 1
        else:
            print('無効な入力です。もう一度入力してください。')

toss = random.randint(0, 1)  # 0は裏、1は表

guess = get_input()
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = get_input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')

