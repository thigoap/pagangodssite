from pagansite.ext.db import db

def all_wariors():
    allwarriors = db.Table('allwarriors', db.metadata, autoload=True, autoload_with=db.engine)
    return allwarriors

def wariors_db():
    warriorsdb = db.Table('warriorsdb', db.metadata, autoload=True, autoload_with=db.engine)
    return warriorsdb

def all_armors():
    allarmors = db.Table('allarmors', db.metadata, autoload=True, autoload_with=db.engine)
    return allarmors

def all_weapons():
    allweapons = db.Table('allweapons', db.metadata, autoload=True, autoload_with=db.engine)
    return allweapons

def all_kuzutiks():
    allkuzutiks = db.Table('allkuzutiks', db.metadata, autoload=True, autoload_with=db.engine)
    return allkuzutiks

# def all_tools():
#     alltools = db.Table('alltools', db.metadata, autoload=True, autoload_with=db.engine)
#     return alltools