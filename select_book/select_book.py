from math import floor
import random


BUDGET = 4000 # 予算
TAX_RATE = 10 # 消費税率
wish_list = [ # 買いたい本のリスト
    {'title': '君主論', 'price': 1010, 'purpose': '戦略'},
    {'title': 'ファスト＆スロー', 'price': 840, 'purpose': '経済学'},
    {'title': 'ITコンサルティングの基本', 'price': 1800, 'purpose': '業務'},
    {'title': 'GIVE&TAKE', 'price': 1800, 'purpose': '娯楽'},
    {'title': 'ORIGINALS', 'price': 1800, 'purpose': '娯楽'},
]
cost = 0 # 買う本の合計金額
purpose_list = [] # 本を買う目的を格納するリスト 同じ目的の本は1冊まで
buy_list = [] # 買う本を格納するリスト
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
