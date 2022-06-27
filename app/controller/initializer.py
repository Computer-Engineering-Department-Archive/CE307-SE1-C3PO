from app.models import Keyword, KeywordValue
from app.model import keywordCRUD


signal_keywords = []
non_signal_keywords = []
buy_keywords = []
sell_keywords = []
category_list = []


def initializer():
    global signal_keywords, buy_keywords, sell_keywords, non_signal_keywords, category_list

    keywords = keywordCRUD.read_all_keywords_query_set()
    keyword_values = keywordCRUD.read_all_keyword_values_query_set()

    for row in keywords:
        if row.type == 'خرید' or row.type == 'فروش' or row.type == 'غیر قطعی':
            signal_keywords.append((row.key, keyword_values.filter(keyword=row).values().first()['value']))
            if row.type == 'خرید':
                buy_keywords.append((row.key, keyword_values.filter(keyword=row).values().first()['value']))
            elif row.type == 'فروش':
                sell_keywords.append((row.key, keyword_values.filter(keyword=row).values().first()['value']))
        elif row.type == 'اخبار':
            non_signal_keywords.append((row.key, keyword_values.filter(keyword=row).values().first()['value']))
        elif row.type == 'گروه سهام':
            category_list.append((row.key, keyword_values.filter(keyword=row).values().first()['value']))
