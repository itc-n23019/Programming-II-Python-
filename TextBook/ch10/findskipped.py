import os, re, shutil

def find_skipped_files(folder, prefix, rename=False):
    files, max_digit_len, rest = {}, 0, ''

    pattern = re.compile(f'^{prefix}(\\d+)(.*)')
    for filename in os.listdir(folder):
        if mo := pattern.search(filename):
            files[int(mo.group(1))] = filename
            max_digit_len = max(max_digit_len, len(mo.group(1)))
            rest = mo.group(2)

    if not files:
        return

    org_index = sorted(files)
    for n in range(org_index[0], org_index[-1] + 1):
        if n not in files:
            print(f'Missing {prefix}{str(n).zfill(max_digit_len)}{rest}')

    if rename:
        for n, ind in enumerate(org_index):
            new_filename = f'{prefix}{str(org_index[0] + n).zfill(max_digit_len)}{rest}'
            if new_filename != files[ind]:
                print(f'Rename {os.path.join(folder, files[ind])} -> {os.path.join(folder, new_filename)}')
                shutil.move(os.path.join(folder, files[ind]), os.path.join(folder, new_filename))

if __name__ == "__main__":
    find_skipped_files('seqfiles', 'spam')

