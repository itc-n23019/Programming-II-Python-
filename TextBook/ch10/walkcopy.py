import os
import shutil

def walk_copy(folder, ext, dst):
    os.makedirs(dst, exist_ok=True)
    for foldername, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(ext.lower()):
                shutil.copy(os.path.join(foldername, filename), dst)

if __name__ == "__main__":
    for ext in ['.jpg', '.txt']:
        walk_copy('delicious', ext, ext[1:] + 's')

