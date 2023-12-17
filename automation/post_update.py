import json
import argparse
from pathlib import Path

# Custom
from utils import Tistory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', required=True, type=Path)
    args = parser.parse_args()

    md_file_path = args.file_path.absolute()

    post_title = md_file_path.stem
    pid = Tistory.get_pid_from_title(title=post_title)
    post_content = Tistory.md_to_html(file_path=md_file_path)

    post = Tistory.post_update(pid=pid, content=post_content)
    print(json.dumps(post, ensure_ascii=False, indent=4))
    # {
    #     "tistory": {
    #         "status": "200",
    #         "postId": "13",
    #         "url": "https://nno0obb.tistory.com/13"
    #     }
    # }


if __name__ == '__main__':
    main()
