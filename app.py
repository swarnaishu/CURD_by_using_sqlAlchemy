import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///table.db',echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class City(Base):
    __tablename__='city'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    province = Column(String)
    country = Column(String)

    def __init__(self, id, name, province, country):
        self.id = id
        self.name = name
        self.province = province
        self.country = country

    def dic(self):
        return {
            'id': self.id,
            'name': self.name,
            'province': self.province,
            'country': self.country
        }
    
    def save_to_db(self):
        session.add(self)
        session.commit()

    def remove(self):
        session.delete(self)
        session.commit()
    


Base.metadata.create_all(engine)

#insert
obj = City(1,'chennai','TamilNadu','India')
obj.save_to_db()
obj = City(2,'Mumbai','Maharastra','India')
obj.save_to_db()
obj = City(3,'kolkata','westBengal','India')
obj.save_to_db()

objs = session.query(City).all()
for obj in objs:
    print(obj.dic())

#update
obj = session.query(City).filter_by(id=2).first()
obj.id=4
obj.save_to_db()

objs = session.query(City).all()
for obj in objs:
    print(obj.dic())

#delete
obj = session.query(City).filter_by(id=4).first()
obj.remove()