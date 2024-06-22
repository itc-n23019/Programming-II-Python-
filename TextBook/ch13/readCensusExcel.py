import openpyxl, pprint  # ❶
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')  # ❷
sheet = wb['Population by Census Tract']  # ❸
county_data = {}

print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):  # ❹
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    county_data.setdefault(state, {})  # ❶
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})  # ❷

    county_data[state][county]['tracts'] += 1  # ❸
    county_data[state][county]['pop'] += int(pop)  # ❹

print('結果を書き込み中...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('完了')


