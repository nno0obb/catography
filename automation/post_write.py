import argparse

import git
import json
from pathlib import Path

# Custom
from utils import Tistory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', required=True, type=Path)
    parser.add_argument('-c', '--category-id', required=True, type=int)
    args = parser.parse_args()

    md_file_path = args.file_path.absolute()
    post_category_id = args.category_id

    post_title = md_file_path.stem
    post_content = Tistory.md_to_html(file_path=md_file_path)

    post = Tistory.post_write(title=post_title, content=post_content, category_id=post_category_id)
    print(json.dumps(post, ensure_ascii=False, indent=4))
    # {
    #     "tistory": {
    #         "status": "200",
    #         "postId": "11",
    #         "url": "https://nno0obb.tistory.com/11"
    #     }
    # }


if __name__ == '__main__':
    main()
