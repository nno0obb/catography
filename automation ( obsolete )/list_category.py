import json
from tabulate import tabulate

# Custom
from utils import Tistory


def main():
    category_list = Tistory.get_category_list()
    print(json.dumps(category_list, ensure_ascii=False, indent=4))

    headers = ['category_id', 'label']
    rows = []
    for category in category_list:
        cid = category['id']
        clabel = ' > '.join(category['label'].split('/'))
        row = [cid, clabel]
        rows.append(row)

    rows.sort(key=lambda x: x[1])
    print(tabulate(rows, headers=headers))
    #   category_id  label
    # -------------  --------------------------------
    #       1150978  Book ( CSE )
    #       1150979  Book ( CSE ) > 앤서블로 시작하는 인프라 자동화
    #       1162163  Book ( Non-CSE )
    #       1150977  Cheatsheet
    #       1151033  Cheatsheet > Docker
    #       1162159  Insight
    #       1162160  Insight > 인문∕사회∕심리
    #       1151034  PS
    #       1151035  PS > 백준


if __name__ == '__main__':
    main()
