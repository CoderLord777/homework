import hashlib


def hash_password(password: str) -> int:
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return int(hashed_password, 16)


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash_password(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'
