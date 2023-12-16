import git
import json
from pathlib import Path

# Custom
from utils import Tistory


def main():
    git_root_path = Path(git.Repo(search_parent_directories=True).working_dir)
    md_file_path = Path(git_root_path / 'post' / 'Cheatsheets' / 'Docker' / '$ docker images.md')

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
