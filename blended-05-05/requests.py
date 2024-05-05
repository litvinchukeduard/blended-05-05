from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from models import Zoo, Animal, Bird, Mamal

engine = create_engine("postgresql+psycopg2://postgres:example@localhost:5432/zoo")

with Session(engine) as session:
    # Знайти середній розмах крил для птах
    # SELECT AVG(wings_span) AS AVG_WINGS_SPAN
    # FROM animals
    # WHERE species='Bird'
    print(session.query(func.avg(Bird.wings_span)).scalar())

    # Знайти найчастіший колір хутра для ссавців
    # SELECT fur_color, COUNT(*) as fur_color_count
    # FROM animals
    # where fur_color is not null
    # GROUP BY fur_color
    # order by fur_color_count desc
    # limit 1;
    print(session\
          .query(Mamal.fur_color, func.count(Mamal.fur_color))\
          .filter(Mamal.fur_color.is_not(None))\
          .group_by(Mamal.fur_color)\
          .order_by(func.count(Mamal.fur_color).desc())\
          .limit(1)\
          .first())
    
    # Знайти зоопарк з найбільшою кількістю звірів
    # SELECT z.name, COUNT(*) as animal_count
    # FROM zoos AS z
    # JOIN animals AS a ON a.zoo_id=z.id
    # group by z.name
    # order by animal_count DESC
    # limit 1;
    print(session\
        .query(Zoo.name, func.count(Zoo.name))\
        .join(Zoo.animals)\
        .group_by(Zoo.name)\
        .order_by(func.count(Zoo.name).desc())\
        .limit(1)\
        .first())


