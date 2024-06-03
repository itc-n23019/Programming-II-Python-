import shelve, pyperclip, sys  

with shelve.open('mcb') as mcb_shelf:
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':  
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        pyperclip.copy(str(list(mcb_shelf.keys())) if sys.argv[1].lower() == 'list' else mcb_shelf.get(sys.argv[1], ''))
