import json

# Custom
from utils import Tistory


def main():
    category_list = Tistory.get_category_list()
    print(json.dumps(category_list, ensure_ascii=False, indent=4))
    # [
    #     {
    #         "id": "1150977",
    #         "name": "Commands",
    #         "parent": "",
    #         "label": "Commands",
    #         "entries": "4",
    #         "entriesInLogin": "5"
    #     },
    #     {
    #         "id": "1150979",
    #         "name": "앤서블로 시작하는 인프라 자동화",
    #         "parent": "1150978",
    #         "label": "Books/앤서블로 시작하는 인프라 자동화",
    #         "entries": "0",
    #         "entriesInLogin": "0"
    #     },
    #     {
    #         "id": "1151033",
    #         "name": "docker",
    #         "parent": "1150977",
    #         "label": "Commands/docker",
    #         "entries": "4",
    #         "entriesInLogin": "4"
    #     },
    #     {
    #         "id": "1151035",
    #         "name": "백준",
    #         "parent": "1151034",
    #         "label": "PS/백준",
    #         "entries": "0",
    #         "entriesInLogin": "0"
    #     },
    #     {
    #         "id": "1150978",
    #         "name": "Books",
    #         "parent": "",
    #         "label": "Books",
    #         "entries": "0",
    #         "entriesInLogin": "0"
    #     },
    #     {
    #         "id": "1151034",
    #         "name": "PS",
    #         "parent": "",
    #         "label": "PS",
    #         "entries": "0",
    #         "entriesInLogin": "0"
    #     }
    # ]


if __name__ == '__main__':
    main()
