import pyinputplus as pyip

PRICES = {
    '小麦パン': 100, '白パン': 110, 'サワー種': 120,
    'チキン': 200, 'ターキー': 250, 'ハム': 300, '豆腐': 280,
    'チェダー': 100, 'スイス': 150, 'モツァレラ': 180,
    'mayo': 10, 'mustard': 10, 'lettuce': 50, 'tomato': 30,
}

def sandwich_maker():
    def choose(option, prompt, add_price=True):
        choice = pyip.inputMenu(option, prompt=prompt, numbered=True)
        return choice, PRICES[choice] if add_price else 0

    bread, bread_price = choose(('小麦パン', '白パン', 'サワー種'), 'パンを選んでください\n')
    protein, protein_price = choose(('チキン', 'ターキー', 'ハム', '豆腐'), 'タンパク質を選んでください\n')
    cheese = pyip.inputYesNo('チーズは必要ですか？') == 'yes'
    cheese_choice, cheese_price = (choose(('チェダー', 'スイス', 'モツァレラ'), 'チーズを選んで下さい\n') if cheese else (None, 0))

    additions = {'mayo': 'マヨネーズ', 'mustard': 'カラシ', 'lettuce': 'レタス', 'tomato': 'トマト'}
    add_prices = sum(PRICES[add] for add, label in additions.items() if pyip.inputYesNo(f'{label}は必要ですか？') == 'yes')

    numbers = pyip.inputInt('いくつ要りますか？', min=1)
    price = bread_price + protein_price + cheese_price + add_prices

    print('-' * 10)
    print(f'パン: {bread} {bread_price}円')
    print(f'タンパク質: {protein} {protein_price}円')
    if cheese: print(f'チーズ: {cheese_choice} {cheese_price}円')
    for add, label in additions.items():
        if locals()[add]: print(f'{label}: {PRICES[add]}円')
    print(f'小計: {price}円')
    print(f'個数: {numbers}個')
    print(f'合計: {price * numbers}円')

sandwich_maker()

