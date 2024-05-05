# Користувач (юзернейм, пошта, пости, коментарі, друзі),
# Пост (контент, автор, дата створення, коментарі, лайки),
# Коментар (користувач, пост, текст, дата створення)
# Лайк (користувач, пост) # (1, 2)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from typing import List

Base = declarative_base()

user_friend_association_table = Table(
    "user_friend_association_table",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("friend_id", ForeignKey("users.id"), nullable=False),
)


class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    friends: Mapped[List['User']] = relationship(secondary=user_friend_association_table,
                                                 primaryjoin= (user_friend_association_table.c.user_id == id),
                                                 secondaryjoin= (user_friend_association_table.c.friend_id == id))
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

    def __str__(self):
        return f'User {self.username}:{self.email}'


# Пост (контент, автор, дата створення, коментарі, лайки),
# One to Many
class Post(Base):
    __tablename__='posts'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    creation_date = Column(Date)

    comments = relationship("Comment", back_populates="post")

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    def __str__(self):
        return f'Post {self.id} {self.content} : {self.creation_date}'

# Коментар (користувач, пост, текст, дата створення)
# One to Many
class Comment(Base):
    __tablename__='comments'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    creation_date = Column(Date)

    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="comments")


# Лайк (користувач, пост)
class Like(Base):
    __tablename__='likes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))


# like.user = user
# like.user_id = user.id