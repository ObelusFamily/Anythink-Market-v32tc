from os import environ
import string
import requests
import random
import asyncio
from typing import Set, List

from asyncpg import connect

from app.api.dependencies.database import get_repository
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository
from app.models.domain.users import User, UserInDB
from app.models.domain.items import Item
from app.models.domain.comments import Comment

# USERS_GENERATOR_API = "https://random-data-api.com/api/v2/users"
DB_CONNECTION_STRING = environ.get("DATABASE_URL")


def generate_string(length=8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def generate_random_user(suffix=None) -> Set[str]:
    """
    Retrieve random user data in this order:
    username, email, password
    """
    # json_res = requests.get(USERS_GENERATOR_API).json()
    json_res = {
        "username": "user" + str(suffix),
        "email": "user" + str(suffix) + "@gmail.com",
        "password": "user" + str(suffix) + "password",
    }

    return json_res["username"], json_res["email"], json_res["password"]


async def seed_users(conn, amount=1) -> List[UserInDB]:
    users = []
    users_repo: UsersRepository = get_repository(UsersRepository)(conn)
    for i in range(amount):
        username, email, password = generate_random_user(i)
        users.append(
            await users_repo.create_user(
                username=username, email=email, password=password
            )
        )
    return users


async def seed_products(conn, user: UserInDB, amount=1):
    items_repo: ItemsRepository = get_repository(ItemsRepository)(conn)
    return await items_repo.create_item(
        slug=generate_string(4),
        title=generate_string(),
        description=generate_string(),
        seller=User(username=user.username, email=user.email),
    )


async def seed_comments(conn, user: UserInDB, product: Item, amount=1):
    comments_repo: CommentsRepository = get_repository(CommentsRepository)(conn)
    return await comments_repo.create_comment_for_item(
        body=generate_string(),
        item=Item(**product.dict()),
        user=User(username=user.username, email=user.email),
    )


async def main():
    db_connection = await connect(DB_CONNECTION_STRING)
    users_created = await seed_users(db_connection, amount=100)

    for user in users_created:
        product_created = await seed_products(db_connection, user)
        await seed_comments(db_connection, user, product_created)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
