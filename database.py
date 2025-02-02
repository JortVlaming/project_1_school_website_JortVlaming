import base64, time
from datetime import datetime


# dummy class until i get around to implementing mysql

class Database:
    def __init__(self):
        self.userManager = UserManager(self)
        pass

    def generate_token(self, username: str, password: str) -> str:
        now = str(time.time())
        now_bytes = now.encode("ascii")
        now_b64 = base64.b64encode(now_bytes)

        username_b64 = base64.b64encode(username.encode("ascii"))
        password_b64 = base64.b64encode(password.encode("ascii"))

        token = now_b64 + b"." + username_b64 + b"." + password_b64

        return token.decode("ascii")

    def verify_token(self, token: str|None) -> bool:
        if token is None:
            return False
        split = token.split(".")

        gen_b64 = split[0]
        un_b64 = split[1]
        pwd_b64 = split[2]

        gen = base64.b64decode(gen_b64.encode("ascii")).decode("ascii")
        un = base64.b64decode(un_b64.encode("ascii")).decode("ascii")
        pwd = base64.b64decode(pwd_b64.encode("ascii")).decode("ascii")

        # TODO: verify token integrity

        return True

class UserManager:
    def __init__(self, db:Database):
        self.db = db
        pass

class User:
    def __init__(self, id:int, username: str, naam: str, opleiding: str, aboutme: str):
        self.id = id
        self.username = username
        self.naam = naam
        self.opleiding = opleiding
        self.aboutme = aboutme

class Post:
    def __init__(self, poster: str, post_id:int, content: str, posted: datetime=datetime.now(), deleted: bool=False):
        self.poster = poster
        self.post_id = post_id
        self.content = content
        self.posted = posted
        self.deleted = deleted
