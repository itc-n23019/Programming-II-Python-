import shelve, pyperclip, sys

def show_usage():
    print("""Usage:
py mcb2.pyw save <keyword> - Save clipboard to keyword
py mcb2.pyw <keyword> - Load keyword to clipboard
py mcb2.pyw list - Copy all keywords to clipboard
py mcb2.pyw delete <keyword> - Delete keyword
py mcb2.pyw delete all - Delete all keywords
""")

with shelve.open('mcb') as mcb_shelf:
    if len(sys.argv) == 3 and sys.argv[1].lower() in ('save', 'delete'):
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[2].lower() == 'all':
            mcb_shelf.clear()
        else:
            mcb_shelf.pop(sys.argv[2], None)
    elif len(sys.argv) == 2:
        pyperclip.copy(str(list(mcb_shelf.keys())) if sys.argv[1].lower() == 'list' else mcb_shelf.get(sys.argv[1], ''))
    else:
        show_usage()
