import requests
import yaml


with open("testdata.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_auth_and_user_data():
    # Авторизация
    response_auth = requests.post(data['url_login'], data={"username": data['login'], "password": data['password']})
    assert response_auth.status_code == 200
    auth = response_auth.json()
    # Получаем токен и id из json ответа
    user_id = response_auth.json().get("id")
    user_token = response_auth.json().get("token")

    headers = {"X-Auth-Token": user_token}

    user_url = data['user_url']
    profile_url = f"{user_url}{user_id}"

    # Получение данных о пользователе
    response_user = requests.get(profile_url, headers=headers)
    assert response_user.status_code == 200
    user_data = response_user.json()


    # Проверяем, что username в ответе совпадает с ожидаемым
    expected_username = auth.get('username')
    actual_username = user_data.get('username')

    assert actual_username == expected_username



