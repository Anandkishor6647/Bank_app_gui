import hashlib
import bcrypt
import database


def hashed(data):
    hashed_password = bcrypt.hashpw(data.encode("utf-8"), bcrypt.gensalt())
    hashed_password_str = hashed_password.decode("utf-8")
    return hashed_password_str


def authenticate(stored, provided):
    return bcrypt.checkpw(provided.encode("utf-8"), stored.encode("utf-8"))


# print(authenticate(database.show_db()[0][4], "qwerty"))
