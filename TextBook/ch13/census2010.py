import os

import census2010

# アンカレッジの人口を取得
anchorage_data = census2010.all_data['AK']['Anchorage']
anchorage_pop = anchorage_data['pop']

# 2010年のアンカレッジの人口を表示
print('2010年のアンカレッジの人口は {} です。'.format(anchorage_pop))

