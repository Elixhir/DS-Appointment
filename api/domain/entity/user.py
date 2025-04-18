from datetime import datetime, timedelta
from typing import Optional

class User:
    def __init__(self, id: int, name: str, email: str, hashed_password: str, is_admin: bool):
        self.id = id
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.is_admin = is_admin

class Token:
    def __init__(self, access_token: str, token_type: str = "bearer"):
        self.access_token = access_token
        self.token_type = token_type