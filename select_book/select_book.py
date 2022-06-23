from math import floor
import random


BUDGET = 20000  # 予算
TAX_RATE = 10  # 消費税率
wish_list = [  # 買いたい本のリスト
    {'title': '君主論',                     'price': 1010,  'purpose': '戦略'},
    {'title': '菊と刀',                     'price': 1310,  'purpose': '日本'},
    {'title': 'OPEN',                       'price': 2400,  'purpose': '戦略'},
    {'title': '失敗の本質',                 'price': 762,  'purpose': '日本'},
    {'title': '戦略の本質',                 'price': 900,  'purpose': '日本'},
    {'title': 'サイロ・エフェクト',         'price': 1018,  'purpose': '娯楽'},
    {'title': 'アマゾンの倉庫で絶望し、ウーバーの車で発狂した',
     'price': 1100,  'purpose': '戦略'},
    {'title': 'RANGE',                      'price': 1900,   'purpose': '教養'},
    {'title': 'ファスト＆スロー',           'price': 840,   'purpose': '経済学'},
    {'title': '空気の研究',                 'price': 650,   'purpose': '日本'},
    {'title': '新1分間マネジャー',          'price': 1300,   'purpose': 'マネジメント'},
    {'title': 'コンサルタントの道具箱',     'price': 2200,   'purpose': '業務'},
    {'title': 'コンサルタントの秘密',       'price': 2900,   'purpose': '業務'},
    {'title': 'ITコンサルティングの基本',   'price': 1800,  'purpose': '業務'},
    {'title': 'GIVE&TAKE',                  'price': 1800,  'purpose': 'アダム・グラント'},
    {'title': 'ORIGINALS',                  'price': 1800,  'purpose': 'アダム・グラント2'},
]
cost = 0  # 買う本の合計金額
purpose_list = []  # 本を買う目的を格納するリスト 同じ目的の本は1冊まで
buy_list = []  # 買う本を格納するリスト
# シャッフル
random.shuffle(wish_list)
for book in wish_list:
    tax_included = book['price'] + book['price'] / 100 * TAX_RATE
    if (not book['purpose'] in purpose_list
            and cost + tax_included < BUDGET):
        purpose_list.append(book['purpose'])
        buy_list.append(book['title'])
        cost += tax_included
print(buy_list)
print(floor(cost), '円')
