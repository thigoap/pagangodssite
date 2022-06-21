from pagan_gods_site.ext.db import db
from pagan_gods_site.ext.db import models


# warriors
def get_warriors(card_mult, card_evo):
    all_warriors = models.all_warriors()
    warriors = db.session.query(
                all_warriors.c.warrior,
                all_warriors.c.race,
                all_warriors.c.rarity,
                all_warriors.c.slug).filter(
                        all_warriors.c.mult == card_mult,
                        all_warriors.c.evo == card_evo).all()
    return warriors

def get_warriors_list():
    warriors_list = models.all_warriors()
    warriors_list = db.session.query(warriors_list).all()
    warriors = [warriors[1] for warriors in warriors_list]
    return warriors


# equipments
def get_armors():
    all_armors = models.all_armors()
    all_armors = db.session.query(all_armors).all()
    return all_armors 

def get_weapons():
    all_weapons = models.all_weapons()
    all_weapons = db.session.query(all_weapons).all()
    return all_weapons 


# fur and xp
def get_fur(warrior, i_level, f_level):
    warriors_db = models.warriors_db()
    fur = db.session\
        .query(db.func.sum(warriors_db.c.fur))\
        .filter(warriors_db.c.warrior == warrior, warriors_db.c.lvl > int(i_level), warriors_db.c.lvl <= int(f_level)).all()
    return fur[0][0]

def get_exp(warrior, i_level, f_level):
    warriors_db = models.warriors_db()
    exp = db.session\
        .query(db.func.sum(warriors_db.c.xp))\
        .filter(warriors_db.c.warrior == warrior, warriors_db.c.lvl > int(i_level), warriors_db.c.lvl <= int(f_level)).all()
    return exp[0][0]

def get_runes(warrior, i_level, f_level):
    warriors_db = models.warriors_db()
    runes = db.session\
        .query(db.func.sum(warriors_db.c.runes))\
        .filter(warriors_db.c.warrior == warrior, warriors_db.c.lvl > int(i_level), warriors_db.c.lvl <= int(f_level)).all()
    return runes[0][0]

def get_max_level(warrior):
    all_warriors = models.all_warriors()
    max_level = db.session.query(all_warriors.c.maxlevel).filter(all_warriors.c.warrior == warrior).first()[0]
    return max_level


# stats and strength
def get_slugs(warrior_01, warrior_02):
    all_warriors = models.all_warriors()
    slug_01 = db.session.query(all_warriors.c.slug)\
            .filter(all_warriors.c.warrior == warrior_01).first()[0]
    slug_02 = db.session.query(all_warriors.c.slug)\
            .filter(all_warriors.c.warrior == warrior_02).first()[0]
    return (slug_01, slug_02)

def get_healths(warrior_01, warrior_02, level_01, level_02):
    warriors_db = models.warriors_db()   
    health_01 = round(float(db.session.query(warriors_db.c.health)\
        .filter(warriors_db.c.warrior == warrior_01, warriors_db.c.lvl == level_01).first()[0]),0)
    health_02 = round(float(db.session.query(warriors_db.c.health)\
        .filter(warriors_db.c.warrior == warrior_02, warriors_db.c.lvl == level_02).first()[0]),0)
    return (health_01, health_02)

def get_attacks(warrior_01, warrior_02, level_01, level_02):
    warriors_db = models.warriors_db()  
    attack_01 = round(float(db.session.query(warriors_db.c.attack)\
        .filter(warriors_db.c.warrior == warrior_01, warriors_db.c.lvl == level_01).first()[0]),0)
    attack_02 = round(float(db.session.query(warriors_db.c.attack)\
        .filter(warriors_db.c.warrior == warrior_02, warriors_db.c.lvl == level_02).first()[0]),0)
    return (attack_01, attack_02)        

def get_strengths(warrior_01, warrior_02, level_01, level_02):
    warriors_db = models.warriors_db()  
    strength_01 = round(float(db.session.query(warriors_db.c.strength)\
        .filter(warriors_db.c.warrior == warrior_01, warriors_db.c.lvl == level_01).first()[0]),0)
    strength_02 = round(float(db.session.query(warriors_db.c.strength)\
        .filter(warriors_db.c.warrior == warrior_02, warriors_db.c.lvl == level_02).first()[0]),0)	
    return (strength_01, strength_02)


# workers
def get_kuzutiks():
    all_kuzutiks = models.all_kuzutiks()
    all_kuzutiks = db.session.query(all_kuzutiks).all()
    return all_kuzutiks


# tools
def get_tools():
    all_tools = models.all_tools()
    all_tools = db.session.query(all_tools).all()
    return all_tools 


