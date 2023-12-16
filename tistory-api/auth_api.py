import re
import keyring
import requests
from playwright.sync_api import sync_playwright

# https://tistory.github.io/document-tistory-apis/auth/authorization_code.html
# https://www.tistory.com/guide/api/manage/register


class Tistory:
    BASE_URL = 'https://www.tistory.com'
    APP_ID = keyring.get_password(service_name='tistory', username='app_id')
    SECRET_KEY = keyring.get_password(service_name='tistory', username='secret_key')
    CALLBACK_URI = 'http://localhost:8000'
    BLOG_NAME = 'nno0obb'

    @classmethod
    def get_auth_code(cls):
        api_url = cls.BASE_URL + f'/oauth/authorize'
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
            return auth_code

    @classmethod
    def get_access_token(cls, auth_code: str):
        api_url = cls.BASE_URL + f'/oauth/access_token'
        api_params = {
            'client_id': cls.APP_ID,
            'client_secret': cls.SECRET_KEY,
            'redirect_uri': cls.CALLBACK_URI,
            'code': auth_code,
            'grant_type': "authorization_code",
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        access_token = re.search('access_token=([a-z0-9_]+)', response.text).group(1)
        return access_token

    @classmethod
    def get_post_list(cls, access_token: str):
        api_url = cls.BASE_URL + '/apis/post/list'
        api_params = {
            'access_token': access_token,
            'output': 'json',
            'blogName': cls.BLOG_NAME,
            'page': 1
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_list = response_data
        return post_list

    @classmethod
    def get_post_read(cls, access_token: str, post_id: int):
        api_url = cls.BASE_URL + '/apis/post/read'
        api_params = {
            'access_token': access_token,
            'blogName': cls.BLOG_NAME,
            'output': 'json',
            'postId': post_id
        }

        response = requests.get(url=api_url, params=api_params)
        response.raise_for_status()

        response_data = response.json()
        post_read = response_data
        return post_read


def test():
    auth_code = Tistory.get_auth_code()
    access_token = Tistory.get_access_token(auth_code=auth_code)
    post_list = Tistory.get_post_list(access_token=access_token)
    post_read = Tistory.get_post_read(access_token=access_token, post_id=3)
    print(post_read)


if __name__ == '__main__':
    test()

