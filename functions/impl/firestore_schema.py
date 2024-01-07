import datetime


class User:
    def __init__(self, uid: str, name: str):
        self.uid = uid
        self.name = name


class Member:
    def __init__(
            self, uid, user_id, user_name, role, status_text, status_updated_at):
        self.uid = uid
        self.userId = user_id
        self.user_name = user_name
        self.role = role
        self.status_text = status_text
        self.status_updated_at = status_updated_at


class Circle:
    def __init__(
            self, uid, title, created_at, updated_at, members):
        self.uid = uid
        self.title = title
        self.created_at = created_at
        self.updated_at = updated_at
        self.members = members
