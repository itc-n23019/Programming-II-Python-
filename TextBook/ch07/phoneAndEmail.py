import pyperclip, re

phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

text = str(pyperclip.paste())
matches = phone_regex.findall(text) + email_regex.findall(text)

if matches:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました:')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')

