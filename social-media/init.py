import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from faker import Faker

from models import User, Post, Comment, Like, user_friend_association_table

fake = Faker()

engine = create_engine("postgresql+psycopg2://postgres:example@localhost:5432/social-media")

def create_users(n: int):
    for _ in range(n):
        user = User(username=fake.user_name(), email=fake.email())
        create_posts(user, random.randint(1, 10))
        session.add(user)
    session.commit()

def create_posts(user: User, n: int):
    for _ in range(n):
        post = Post(content=fake.sentence(nb_words=20), creation_date=fake.date_this_year())
        post.user = user
        create_comments(post, user, random.randint(1, 10))
        session.add(post)

def create_comments(post: Post, user: User, n: int):
    for _ in range(n):
        comment = Comment(content=fake.sentence(nb_words=10), creation_date=fake.date_this_year())
        comment.author = user
        comment.post = post
        session.add(comment)

def create_likes(n: int):
    for _ in range(n):
        like = Like(user_id=random.randint(1, n), post_id=random.randint(1, n))
        session.add(like)
    session.commit()

def create_friends(n: int):
    for _ in range(n):
        session.execute(user_friend_association_table.insert()
                        .values(user_id=random.randint(1, n), friend_id=random.randint(1, n)))
    session.commit()


with Session(engine) as session:
    # create_users(10)
    # create_likes(10)
    create_friends(3)
