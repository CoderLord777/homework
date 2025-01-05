import requests

url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(url)

    response.raise_for_status()  # Генерирует исключение для ошибок HTTP

    data = response.json()

    print("Список пользователей:\n")
    for user in data:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        print(f"Company: {user['company']['name']}, City: {user['address']['city']}\n")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка: {http_err}")
except Exception as err:
    print(f"Другие ошибки: {err}")
