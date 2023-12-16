import git
import json
from pathlib import Path

# Custom
from utils import Tistory


def main():
    git_root_path = Path(git.Repo(search_parent_directories=True).working_dir)
    md_file_path = Path(git_root_path / 'post' / 'Cheatsheets' / 'Docker' / '$ docker images.md')

    post_category_id = 1151033
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
