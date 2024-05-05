from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

# Створити моделі для 
# Зоопарку (назва, локація, звірі), 
# Тварини (імʼя, вид, вік, зоопарк)

# Ссавець (колір хутра)
# Птаха (розмах крил)

# One-to-Many

Base = declarative_base()

class Zoo(Base):
    __tablename__ = 'zoos'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    animals = relationship("Animal", back_populates="zoo")


class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)

    zoo_id = Column(Integer, ForeignKey("zoos.id"))
    zoo = relationship("Zoo", back_populates="animals")


# fur_color, wings_span
class Mamal(Animal):
    fur_color = Column(String)


class Bird(Animal):
    wings_span = Column(Integer)
