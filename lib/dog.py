from sqlalchemy import create_engine
from models import Dog

engine = create_engine('sqlite:///:memory:', future=True)

def create_table(base):
    '''contains function "create_table()" that takes a declarative_base, creates table "dogs" if it does not exist, and returns the engine.'''
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    '''
        contains function "save()" that takes a Dog instance and session as arguments, 
        saves the dog to the database, and returns the session.
    '''
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
     '''contains function "new_from_db()" that takes a database row and returns a Dog instance.'''
     
     row = session.query(Dog).filter_by(id=row.id).first()
     return row

def get_all(session):
    '''
        contains function "get_all()" that takes a session 
        and returns a list of Dog instances for every record in the database.
    '''
    all = session.query(Dog).all()
    return [dog for dog in all]

def find_by_name(session, name):
    '''
        contains function "find_by_name()" that takes a session and name 
        and returns a Dog instance corresponding to its database record retrieved by name.
    '''
    row = session.query(Dog).filter_by(name=name).first()
    return row

def find_by_id(session, id):
    '''
        contains function "find_by_id()" that takes a session and id 
        and returns a Dog instance corresponding to its database record retrieved by id.
    '''
    row = session.query(Dog).filter_by(id=id).first()
    return row

def find_by_name_and_breed(session, name, breed):
    '''
        contains function "find_by_name_and_breed()" that takes a session, a name, 
        and a breed as arguments and returns a Dog instance matching that record.
    '''
    row = session.query(Dog).filter_by(name=name, breed=breed).first()
    return row

def update_breed(session, dog, breed):
    '''
        contains function "update_breed()" that takes a session instance, 
        and breed as arguments and updates the instance's breed.
    '''
    dog.breed = breed
    session.commit()
    return session
    pass