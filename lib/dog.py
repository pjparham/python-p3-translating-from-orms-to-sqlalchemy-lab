from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog)
    # dogs = session.query(Dog)
    # return [dog for dog in dogs]

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    # query = session.query(Dog).filter(Dog.name.like(name)).all()
    # print(query)
    # for record in query:
    #     return record

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()
    # query = session.query(Dog).filter(Dog.id == id).all()
    # for record in query: 
    #     return record

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(name), Dog.breed == breed).first()
    # query = session.query(Dog).filter(Dog.name.like(name),
    #     Dog.breed == breed).all()
    # for record in query:
    #     return record

def update_breed(session, dog, breed):
    dog_to_update = session.query(Dog).filter(Dog.name.like(dog.name)).first()
    dog_to_update.breed = breed
    session.commit()