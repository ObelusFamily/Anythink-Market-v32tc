import requests
from typing import Set

from app.api.dependencies.database import get_repository
from app.db.repositories.users import UsersRepository

USERS_GENERATOR_API = "https://random-data-api.com/api/v2/users"


def generate_random_user() -> Set(str):
    """
    Retrieve random user data in this order:
    username, email, password
    """
    json_res = requests.get(USERS_GENERATOR_API).json()

    return json_res["username"], json_res["email"], json_res["password"]


def seed_users():
    for i in range(1):
        username, email, password = generate_random_user()

    # create the user in the db


def seed_products():
    pass


def seed_comments():
    pass


if __name__ == "__main__":
    seed_users()
    seed_products()
    seed_comments()
