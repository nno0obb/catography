import json
from tabulate import tabulate
from collections import defaultdict

# Custom
from utils import Tistory


def main():
    category_list = Tistory.get_category_list()
    print(json.dumps(category_list, ensure_ascii=False, indent=4))

    headers = ['category_id', 'label']
    rows = []
    for category in category_list:
        row = [category['id'], category['label']]
        rows.append(row)

    rows.sort(key=lambda x: x[1])
    print(tabulate(rows, headers=headers))
    #   category_id  label
    # -------------  -----------------------
    #       1150978  Books
    #       1150979  Books/앤서블로 시작하는 인프라 자동화
    #       1150977  Cheatsheets
    #       1151033  Cheatsheets/Docker
    #       1151034  PS
    #       1151035  PS/백준


if __name__ == '__main__':
    main()
