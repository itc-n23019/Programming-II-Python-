import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    zip_filename = f"{os.path.basename(folder)}_{sum(1 for f in os.listdir('.') if f.startswith(os.path.basename(folder)) and f.endswith('.zip')) + 1}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for foldername, _, filenames in os.walk(folder):
            backup_zip.write(foldername)
            for filename in filenames:
                if not filename.startswith(os.path.basename(folder) + '_') or not filename.endswith('.zip'):
                    backup_zip.write(os.path.join(foldername, filename))

    print('Done.')

backup_to_zip('C:\\delicious')

