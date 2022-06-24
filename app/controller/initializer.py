from app.models import Keyword, KeywordValue
from app.model import keywordCRUD


sell_keywords = []
buy_keywords = []
signal_keywords = []
non_signal_keywords = []
category_list = []


def initializer():
    keywords = keywordCRUD.read_all_keywords_query_set()
    keyword_values = keywordCRUD.read_all_keyword_values_query_set()

    for row in keywords:
        if row.type is 'خرید' or row.type is 'فروش' or row.type is 'غیر قطعی':
            signal_keywords.append((row.key, keyword_values.filter(keyword=row)))
            if row.type is 'خرید':
                buy_keywords.append((row.key, keyword_values.filter(keyword=row)))
            elif row.type is 'فروش':
                sell_keywords.append((row.key, keyword_values.filter(keyword=row)))
        elif row.type is 'اخبار':
            non_signal_keywords.append((row.key, keyword_values.filter(keyword=row)))
        elif row.type is 'گروه سهام':
            category_list.append((row.key, keyword_values.filter(keyword=row)))
