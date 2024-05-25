import re

def detect_date(s):
    match = re.search(r'(\d{2})/(\d{2})/(\d{4})', s)
    if not match:
        return None

    day, month, year = map(int, match.groups())
    if not (1000 <= year <= 2999) or not (1 <= month <= 12):
        return None
    
    
    max_days = [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= day <= max_days[month - 1]):
        return None
    
    return day, month, year

if __name__ == '__main__':
    
    assert detect_date('Today is 15/08/1945.') == (15, 8, 1945)
    assert detect_date('There is no 31/02/2020.') == None
    assert detect_date('There is no 31/04/2021.') == None
    assert detect_date('There is no 15/00/1945.') == None
    assert detect_date('There is no 15/13/1945.') == None
    assert detect_date('There is no 00/08/1945.') == None
    assert detect_date('There is no 32/18/1945.') == None
    assert detect_date('There is no 01/08/9999.') == None
    assert detect_date('Bad format: 1945/08/15.') == None

