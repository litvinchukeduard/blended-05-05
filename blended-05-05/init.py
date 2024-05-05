import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from faker import Faker

from models import Zoo, Animal, Bird, Mamal

fake = Faker()

engine = create_engine("postgresql+psycopg2://postgres:example@localhost:5432/zoo")

zoos = []

def create_zoos():
    zoo_names = ('Central zoo', 'Small zoo', 'Bird zoo')
    for name in zoo_names:
        zoo = Zoo(name=name, location=fake.city())
        zoos.append(zoo)
        session.add(zoo)
    session.commit()

def create_animals(n: int):
    species_list = ('Lion', 'Panther', 'Elephant', 'Penguin')
    for i in range(n):
        species = random.choice(species_list)
        animal = Animal(name=fake.name(), species=species, age=fake.random_int(0, 20))
        # animal.zoo_id = 
        animal.zoo = random.choice(zoos)
        session.add(animal)
    session.commit()

def create_birds(n: int):
    for i in range(n):
        species = 'Bird'
        bird = Bird(name=fake.name(), species=species, age=fake.random_int(0, 20), wings_span=fake.random_int(1, 20))
        bird.zoo_id = 2
        session.add(bird)
    session.commit()

def create_mamals(n: int):
    for i in range(n):
        species = 'Mamal'
        mamal = Mamal(name=fake.name(), species=species, age=fake.random_int(0, 20), fur_color=fake.color())
        mamal.zoo_id = 3
        session.add(mamal)
    session.commit()

with Session(engine) as session:
    # create_zoos()
    # create_animals(50)
    # create_birds(5)
    create_mamals(20)
