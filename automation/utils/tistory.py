import re
import keyring
import sqlite3
import requests
import markdown
from pathlib import Path
from playwright.sync_api import sync_playwright

# https://tistory.github.io/document-tistory-apis/auth/authorization_code.html
# https://www.tistory.com/guide/api/manage/register


class Tistory:
    AUTH_CODE = None
    ACCESS_TOKEN = None
    BASE_URL = 'https://www.tistory.com'
    APP_ID = keyring.get_password(service_name='tistory', username='app_id')
    SECRET_KEY = keyring.get_password(service_name='tistory', username='secret_key')
    CALLBACK_URI = 'http://localhost:8000'
    BLOG_NAME = 'nno0obb'

    @classmethod
    def set_auth_code(cls):
        api_url = cls.BASE_URL + '/oauth/authorize'
        api_params = {
            'client_id': cls.APP_ID,
            'redirect_uri': cls.CALLBACK_URI,
            'response_type': "code",
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        with sync_playwright() as p:
            browser = p.webkit.launch()
            page = browser.new_page()

            page.goto(response.url)
            page.locator('#cMain > div > div > div > a.btn_login.link_kakao_id').click()

            page.locator('#loginId--1').fill('nno0obb')
            page.locator('#password--2').fill('keepRainy101!')
            page.locator('#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit').click()

            page.wait_for_load_state('networkidle')
            auth_code = re.search('code=([a-z0-9]+)', page.locator('head > script').inner_text()).group(1)
            cls.AUTH_CODE = auth_code

    @classmethod
    def set_access_token(cls):
        if cls.AUTH_CODE is None:
            cls.set_auth_code()

        api_url = cls.BASE_URL + '/oauth/access_token'
        api_params = {
            'client_id': cls.APP_ID,
            'client_secret': cls.SECRET_KEY,
            'redirect_uri': cls.CALLBACK_URI,
            'code': cls.AUTH_CODE,
            'grant_type': "authorization_code",
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        access_token = re.search('access_token=([a-z0-9_]+)', response.text).group(1)
        cls.ACCESS_TOKEN = access_token

    @classmethod
    def get_category_list(cls):
        if cls.ACCESS_TOKEN is None:
            cls.set_access_token()

        api_url = cls.BASE_URL + '/apis/category/list'
        api_params = {
            'access_token': cls.ACCESS_TOKEN,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        category_list = response_data['tistory']['item']['categories']
        return category_list

    @classmethod
    def get_post_list(cls):
        if cls.ACCESS_TOKEN is None:
            cls.set_access_token()

        api_url = cls.BASE_URL + '/apis/post/list'
        api_params = {
            'access_token': cls.ACCESS_TOKEN,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
            'page': 1,
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_list = response_data
        return post_list

    @classmethod
    def post_read(cls, pid: int):
        if cls.ACCESS_TOKEN is None:
            cls.set_access_token()

        api_url = cls.BASE_URL + '/apis/post/read'
        api_params = {
            'access_token': cls.ACCESS_TOKEN,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
            'postId': pid
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_read = response_data
        return post_read

    @classmethod
    def post_write(cls, title: str, content: str, category_id: int = None, tags: list[str] = None):
        if cls.ACCESS_TOKEN is None:
            cls.set_access_token()

        api_url = cls.BASE_URL + '/apis/post/write'
        api_params = {
            'access_token': cls.ACCESS_TOKEN,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
            'title': title,
            'content': content,
            'category': category_id or 0,
            'visibility': 3,
            'tag': ','.join(tags) if tags else '',
        }

        response = requests.post(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_write = response_data

        # DB Update
        with sqlite3.connect(Path(__file__).parent / 'tistory.db') as con:
            cur = con.cursor()
            pid = response_data['tistory']['postId']
            cur.execute(f"INSERT INTO Post VALUES(?, ?);", (pid, title))
            con.commit()
            cur.close()

        return post_write

    @classmethod
    def post_update(cls, pid: int, title: str = None, content: str = None, category_id: int = None, tags: list[str] = None):
        if cls.ACCESS_TOKEN is None:
            cls.set_access_token()

        api_url = cls.BASE_URL + '/apis/post/modify'
        api_params = {
            'access_token': cls.ACCESS_TOKEN,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
            'postId': pid,
        }

        if title:
            api_params['title'] = title
        if content:
            api_params['content'] = content
        if category_id:
            api_params['category'] = category_id
        if tags:
            api_params['tag'] = ','.join(tags)

        response = requests.post(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_update = response_data
        return post_update

    @classmethod
    def md_to_html(cls, file_path: Path):
        if not file_path.exists():
            raise RuntimeError('Given "file_path" not exists')
        with open(file_path, 'r') as f:
            html = markdown.markdown(f.read(), extensions=['nl2br', 'fenced_code'])
        return html

    @classmethod
    def get_pid_from_title(cls, title: str):
        with sqlite3.connect(Path(__file__).parent / 'tistory.db') as con:
            cur = con.cursor()
            rows = cur.execute(f"SELECT * FROM Post WHERE title = '{title}';").fetchall()
            cur.close()

            if len(rows) == 1:
                pid, title = rows.pop()
                return pid
            elif len(rows) == 0:
                return None
            else:
                raise RuntimeError("DB Integrity is broken")

    @classmethod
    def get_title_from_pid(cls, pid: int):
        with sqlite3.connect(Path(__file__).parent / 'tistory.db') as con:
            cur = con.cursor()
            rows = cur.execute(f"SELECT * FROM Post WHERE id = '{pid}';").fetchall()
            cur.close()

            if len(rows) == 1:
                pid, title = rows.pop()
                return title
            elif len(rows) == 0:
                return None
            else:
                raise RuntimeError("DB Integrity is broken")


def test():
    # category_list = Tistory.get_category_list(access_token=access_token)
    # print(category_list)
    # post_list = Tistory.get_post_list(access_token=access_token)
    # post_read = Tistory.post_read(access_token=access_token, post_id=4)
    # print(post_read)
    # md_file_path = Path('../../post/Cheatsheets/Docker/$ docker images.md')
    # html = Tistory.md_to_html(file_path=md_file_path)
    # print(html)
    # post_write = Tistory.post_write(access_token=access_token, title=md_file_path.stem, content=html, category_id=1151033)
    # print(post_write)

    # con = sqlite3.connect('./tistory.db')
    # cur = con.cursor()
    # post_id = 4
    # post_title = 'fdsa'
    # cur.execute(f"CREATE TABLE Post(id int, title text);")
    # cur.execute(f"INSERT INTO Post VALUES(?, ?);", (post_id, post_title))

    # cur.execute("SELECT * FROM Post")
    # print(cur.fetchall())
    # cur.close()
    # con.commit()
    # con.close()

    print(Tistory.get_post_id_from_title(title='$ docker images'))
    print(Tistory.get_title_from_post_id(post_id=13))


if __name__ == '__main__':
    test()

