from pagan_gods_site.ext.db import db

def all_warriors():
    all_warriors = db.Table('allwarriors', db.metadata, autoload=True, autoload_with=db.engine)
    return all_warriors

def warriors_db():
    warriors_db = db.Table('warriorsdb', db.metadata, autoload=True, autoload_with=db.engine)
    return warriors_db

def all_armors():
    all_armors = db.Table('allarmors', db.metadata, autoload=True, autoload_with=db.engine)
    return all_armors

def all_weapons():
    all_weapons = db.Table('allweapons', db.metadata, autoload=True, autoload_with=db.engine)
    return all_weapons

def all_kuzutiks():
    all_kuzutiks = db.Table('allkuzutiks', db.metadata, autoload=True, autoload_with=db.engine)
    return all_kuzutiks

def all_tools():
    all_tools = db.Table('alltools', db.metadata, autoload=True, autoload_with=db.engine)
    return all_tools