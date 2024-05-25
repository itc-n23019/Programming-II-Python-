import re

def is_phone_number(text):
    return bool(re.fullmatch(r'\d{3}-\d{3}-\d{4}', text))

print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi は電話番号:')
print(is_phone_number('Moshi moshi'))

message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
for i in range(len(message) - 11):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('電話番号が見つかりました: ' + chunk)
print('完了')

