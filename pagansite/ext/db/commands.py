from pagansite.ext.db import db
from pagansite.ext.db import models


# warriors
def get_warriors(cardMult, cardEVO):
    allwarriors = models.all_wariors()
    warriors = db.session.query(
                allwarriors.c.warrior,
                allwarriors.c.race,
                allwarriors.c.rarity,
                allwarriors.c.slug).filter(
                        allwarriors.c.mult == cardMult,
                        allwarriors.c.evo == cardEVO).all()
    return warriors

def get_warriors_list():
    warriorslist = models.all_wariors()
    warriorslist = db.session.query(warriorslist).all()
    warriors = [warriors[1] for warriors in warriorslist]
    return warriors


# equipments
def get_armors():
    allarmors = models.all_armors()
    allarmors = db.session.query(allarmors).all()
    return allarmors 

def get_weapons():
    allweapons = models.all_weapons()
    allweapons = db.session.query(allweapons).all()
    return allweapons 


# fur and xp
def get_fur(warrior, ilevel, flevel):
    warriorsdb = models.wariors_db()
    fur = db.session\
        .query(db.func.sum(warriorsdb.c.fur))\
        .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
    return fur[0][0]

def get_exp(warrior, ilevel, flevel):
    warriorsdb = models.wariors_db()
    exp = db.session\
        .query(db.func.sum(warriorsdb.c.xp))\
        .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
    return exp[0][0]

def get_runes(warrior, ilevel, flevel):
    warriorsdb = models.wariors_db()
    runes = db.session\
        .query(db.func.sum(warriorsdb.c.runes))\
        .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
    return runes[0][0]

def get_max_level(warrior):
    allwarriors = models.all_wariors()
    max_level = db.session.query(allwarriors.c.maxlevel).filter(allwarriors.c.warrior == warrior).first()[0]
    return max_level


# stats and strength
def get_slugs(warrior01, warrior02):
    allwarriors = models.all_wariors()
    slug01 = db.session.query(allwarriors.c.slug)\
            .filter(allwarriors.c.warrior == warrior01).first()[0]
    slug02 = db.session.query(allwarriors.c.slug)\
            .filter(allwarriors.c.warrior == warrior02).first()[0]
    return (slug01, slug02)

def get_healths(warrior01, warrior02, level01, level02):
    warriorsdb = models.wariors_db()   
    health01 = round(float(db.session.query(warriorsdb.c.health)\
        .filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
    health02 = round(float(db.session.query(warriorsdb.c.health)\
        .filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)
    return (health01, health02)

def get_attacks(warrior01, warrior02, level01, level02):
    warriorsdb = models.wariors_db()  
    attack01 = round(float(db.session.query(warriorsdb.c.attack)\
        .filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
    attack02 = round(float(db.session.query(warriorsdb.c.attack)\
        .filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)
    return (attack01, attack02)        

def get_strengths(warrior01, warrior02, level01, level02):
    warriorsdb = models.wariors_db()  
    strength01 = round(float(db.session.query(warriorsdb.c.strength)\
        .filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
    strength02 = round(float(db.session.query(warriorsdb.c.strength)\
        .filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)	
    return (strength01, strength02)


# workers
def get_kuzutiks():
    allkuzutiks = models.all_kuzutiks()
    allkuzutiks = db.session.query(allkuzutiks).all()
    return allkuzutiks