import os, re

date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$""", re.VERBOSE)

for amer_filename in os.listdir('.'):
    if mo = date_pattern.search(amer_filename):
        before_part, month_part, day_part, _, year_part, after_part = mo.groups()
        euro_filename = f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"
        print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
        # os.rename(amer_filename, euro_filename)

