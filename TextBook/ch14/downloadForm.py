import ezsheets

# ユーザーにスプレッドシートのIDを入力させる
SPREADSHEET_ID = input("Enter the Google Spreadsheet ID: ")

# スプレッドシートにアクセス
ss = ezsheets.Spreadsheet(SPREADSHEET_ID)
sheet = ss[0]

# スプレッドシートの内容を行ごとに取得して表示
for row in range(1, sheet.rowCount + 1):
    data = sheet.getRow(row)
    print(data)

