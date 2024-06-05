import random

capitals = {
    '北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市', 
    '宮城県': '仙台市', '秋田県': '秋田市', '山形県': '山形市', '福島県': '福島市',
    '茨城県': '水戸市', '栃木県': '宇都宮市', '群馬県': '前橋市',
    '埼玉県': 'さいたま市', '千葉県': '千葉市', '東京都': '東京',
    '神奈川県': '横浜市', '新潟県': '新潟市', '富山県': '富山市', '石川県': '金沢市',
    '福井県': '福井市', '山梨県': '甲府市', '長野県': '長野市', '岐阜県': '岐阜市',
    '静岡県': '静岡市', '愛知県': '名古屋市', '三重県': '津市', '滋賀県': '大津市',
    '京都府': '京都市', '大阪府': '大阪市', '兵庫県': '神戸市', '奈良県': '奈良市',
    '和歌山県': '和歌山市', '鳥取県': '鳥取市', '島根県': '松江市',
    '岡山県': '岡山市', '広島県': '広島市', '山口県': '山口市', '徳島県': '徳島市',
    '香川県': '高松市', '愛媛県': '松山市', '高知県': '高知市', '福岡県': '福岡市',
    '佐賀県': '佐賀市', '長崎県': '長崎市', '熊本県': '熊本市', '大分県': '大分市',
    '宮崎県': '宮崎市', '鹿児島県': '鹿児島市', '沖縄県': '那覇市'
}

for quiz_num in range(35):
    with open(f'capitalsquiz{quiz_num + 1}.txt', 'w') as quiz_file, \
         open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w') as answer_key_file:
        
        quiz_file.write('名前:\n\n日付:\n\n')
        quiz_file.write((' ' * 20) + f'都道府県庁所在地クイズ (問題番号 {quiz_num + 1})\n\n')

        prefectures = list(capitals.keys())
        random.shuffle(prefectures)

        for question_num, prefecture in enumerate(prefectures):
            correct_answer = capitals[prefecture]
            wrong_answers = random.sample([ans for ans in capitals.values() if ans != correct_answer], 3)
            answer_options = random.sample(wrong_answers + [correct_answer], 4)
            
            quiz_file.write(f'{question_num + 1}. {prefecture}の都道府県庁所在地は?\n')
            for i, option in enumerate(answer_options):
                quiz_file.write(f' {"ABCD"[i]}. {option}\n')
            quiz_file.write('\n')
            
            answer_key_file.write(f'{question_num + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n')