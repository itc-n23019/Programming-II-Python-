import re

def check_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password)
    )

if __name__ == "__main__":
    passwords = [
        'abcdehA1', 'abcdeA1', '', '        ',
        'abcdefgh', 'abcdefgA', 'abcdefg1',
        'ABCDEFGH', 'ABCDEFGa', 'ABCDEFG1',
        '12345678', '1234567a', '1234567A'
    ]
    for p in passwords:
        print(f"{p}: {check_password(p)}")

