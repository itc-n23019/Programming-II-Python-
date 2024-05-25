











import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')


if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':  
        if sys.argv[2].lower() == 'all':
           mcb_shelf.clear()          
        else:
           del mcb_shelf[sys.argv[2]] 
elif len(sys.argv) == 2:
    
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
else:
    print("""使い方：
py.exe mcb2.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
py.exe mcb2.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
py.exe mcb2.pyw list - 全キーワードをクリップボードにコピー
py.exe mcb2.pyw delete <keyword> - キーワードに紐づけられたテキストを削除
py.exe mcb2.pyw delete all - すべてのテキストを削除
""")

mcb_shelf.close()
