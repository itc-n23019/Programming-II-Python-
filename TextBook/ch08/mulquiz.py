import random, time

def multiplication_quiz(num_questions=10, max_attempts=3, time_limit=8):
    correct_answers = 0
    for q_num in range(num_questions):
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
        start_time = time.time()

        for attempt in range(max_attempts):
            try:
                answer = int(input(f'{q_num + 1}: {num1} x {num2} = '))
            except ValueError:
                print('整数を入力してください')
                continue

            if time.time() - start_time > time_limit:
                print('時間切れ!')
                break

            if answer == num1 * num2:
                print('正解!')
                correct_answers += 1
                break
        else:
            print('回数制限切れ!')

        time.sleep(1)

    print(f'得点: {correct_answers} / {num_questions}')

multiplication_quiz()

