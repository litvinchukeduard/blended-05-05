import random
from datetime import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from faker import Faker

from models import User, Post, Comment, Like, user_friend_association_table

fake = Faker()

engine = create_engine("postgresql+psycopg2://postgres:example@localhost:5432/social-media")
# Створити нового користувача
# Увійти як цей користувач
# Створити пост як цей користувач
# Переглянути усі пости як цей користувач
# Лайкнути пост як цей користувач
# Додати коментар як цей користувач
# Переглянути усіх користувачів
# Додати користувача у друзі

with Session(engine) as session:
    # Створити нового користувача
    # Увійти як цей користувач
    user = None
    while True:
        print()
        print("Commands:")
        print("1. Add user")
        print("2. Authorize user")
        print("3. Log out")
        print("4. Current user info")
        print("5. Create post")
        print("6. View all posts for current user")
        print("7. View all posts")
        print("8. Like a post")
        print("exit to exit application")
        print()
        user_input = input("Enter number: ").strip()

        if user_input == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            user = User(username=username, email=email)
            session.add(user)
            session.commit()
            print("User added")
        elif user_input == "2":
            email = input("Enter email: ")
            user = session.query(User).filter(User.email==email).first()
            if user is None:
                print("User is not registered")
            else:
                print("Logged in successfully")
        elif user_input == "3":
            user = None
            print("Logged out successfully")
        elif user_input == "4":
            print(user)
        elif user_input == "5":
            if user is not None:
                content = input("Enter post content: ")
                post = Post(content=content, creation_date=datetime.now())
                post.author = user
                session.add(post)
                session.commit()
                print("Post saved successfully")
            else:
                print("Log in to create a post")
        elif user_input == "6":
            if user is not None:
                posts = session.query(Post).filter(Post.author==user).all()
                for post in posts:
                    likes_count = session.query(func.count(Like.id)).filter(Like.post_id == post.id).scalar()
                    print(post)
                    print(f'Number of likes: {likes_count}')
                    print()
            else:
                print("Log in to view your posts")
        elif user_input == "7":
            posts = session.query(Post).all()
            for post in posts:
                print(post)
        elif user_input == "8":
            if user is not None:
                post_id = input("Enter post id: ")
                post = session.query(Post).filter(Post.id==post_id).first()
                print(post)
                like = Like(user_id=user.id, post_id=int(post_id))
                session.add(like)
                session.commit()
                print("Like added!")
            else:
                print("Log in to view your posts")
        elif user_input == 'exit':
            print('Good bye!')
            break
