from flask import render_template, request
from flask import Blueprint

from pagan_gods_site.ext.db import commands, data_dict

bp = Blueprint("site", __name__)

@bp.route("/")
@bp.route("/index")
def index():
    return render_template("pages/index.html")

@bp.route("/c_units", methods=['GET', 'POST'])
def c_units():
    if request.method == 'POST':
        card_type = list(request.form.to_dict().keys())[0]
        card_mult = card_type[1]
        card_evo = card_type[-1]
        warriors = commands.get_warriors(card_mult, card_evo)	
    else:
        card_type = 'w0EVO0'
        warriors = warriors = commands.get_warriors(0, 0)	

    return render_template("pages/cunits.html",
    warriors=warriors
    )	

@bp.route("/c_equips/<type_of_equip>")
def c_equips(type_of_equip):
    if type_of_equip == 'armors':
        equips_list = commands.get_armors()
    else:
        equips_list = commands.get_weapons()       
    return render_template("pages/cequips.html", equips_list=equips_list, type_of_equip=type_of_equip)

@bp.route("/abilities")
def abilities():
    return render_template("pages/abilities.html",
    abilities = data_dict.abilities
    )
    
@bp.route("/fur", methods=['GET', 'POST'])
def fur():
    warriors_list = commands.get_warriors_list()
    if request.method == 'POST':
        warrior = request.form.get('warrior')
        i_level = request.form.get('ilevel')
        f_level = request.form.get('flevel')
        fur = commands.get_fur(warrior, i_level, f_level)
        exp = commands.get_exp(warrior, i_level, f_level)
        runes = commands.get_runes(warrior, i_level, f_level)
        expenses_dict = {
            'warrior': warrior,
            'i_level': i_level,
            'f_level': f_level,
            'fur': fur,
            'exp': exp,
            'runes': runes,
            'wood': 1000 * runes,
            'iron': 1000 * runes
        }	
        return render_template("pages/fur.html",
        warriors_list = warriors_list, expenses_dict=expenses_dict)
    return render_template("pages/fur.html",
    warriors_list = warriors_list)

@bp.route("/flevel")
def f_level():
    i_level = int(request.args.get('ilevel'))
    max_level = max_level_to
    return render_template('flevel.html', i_level=i_level, max_level=max_level)		

# counter = 0
# warriorsteam = []
@bp.route("/strength", methods=['GET', 'POST'])
def strength():
    global counter
    global warriorsteam
    #define dropdown lists
    warriors_list = commands.get_warriors_list()
    warriors_dict = {}
    # weaponslist = db.session.query(allweapons.c.weaponp).all()
    # weaponslist = [weapons[0] for weapons in weaponslist]
    # armorslist = db.session.query(allarmors.c.armorp).all()
    # armorslist = [armors[0] for armors in armorslist]
    # totalStrength = 0
    # strengthmsg = ''
    
    if request.method == 'POST':
        if 'compareForm' in request.form:
            warrior_01 = request.form.get('warrior01')
            warrior_02 = request.form.get('warrior02')
            level_01 = request.form.get('level01')
            level_02 = request.form.get('level02')
            slug_01 = commands.get_slugs(warrior_01, warrior_02)[0]
            slug_02 = commands.get_slugs(warrior_01, warrior_02)[1]
            health_01 = commands.get_healths(warrior_01, warrior_02, level_01, level_02)[0]
            health_02 = commands.get_healths(warrior_01, warrior_02, level_01, level_02)[1]
            attack_01 = commands.get_attacks(warrior_01, warrior_02, level_01, level_02)[0]
            attack_02 = commands.get_attacks(warrior_01, warrior_02, level_01, level_02)[1]
            strength_01 = commands.get_strengths(warrior_01, warrior_02, level_01, level_02)[0]
            strength_02 = commands.get_strengths(warrior_01, warrior_02, level_01, level_02)[1]
            warriors_dict = {
                'warrior_01': warrior_01, 'slug_01': slug_01, 'level_01': level_01, 'health_01': health_01, 'attack_01': attack_01, 'strength_01': strength_01,
                'warrior_02': warrior_02,	'slug_02': slug_02, 'level_02': level_02, 'health_02': health_02,	'attack_02': attack_02, 'strength_02': strength_02,
            }
    #     elif 'addForm' in request.form:
    #         # if 'counter' in session:
    #         # 	session['counter'] += 1
    #         # else:
    #         # 	session['counter'] = 0
    #         counter+=1
    #         warrior = request.form.get('warrior')
    #         level = request.form.get('level')
    #         strength = round(float(db.session.query(warriorsdb.c.strength)\
    #             .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]),0)
    #         slug = db.session.query(allwarriors.c.slug)\
    #             .filter(allwarriors.c.warrior == warrior).first()[0]
    #         plushealth = 0
    #         plusattack = 0
    #         armor = request.form.get('armor')
    #         if armor == 'Choose armor': armor = '-' # if no armor
    #         else: 
    #             plusarmor = db.session.query(allarmors.c.percent)\
    #                 .filter(allarmors.c.armorp == armor).first()[0]
    #             health = db.session.query(warriorsdb.c.health)\
    #                 .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]
    #             plushealth = health * 0.01 * plusarmor
    #         weapon = request.form.get('weapon')
    #         if weapon == 'Choose weapon': weapon = '-' # if no weapon
    #         else:
    #             plusweapon = db.session.query(allweapons.c.percent)\
    #                 .filter(allweapons.c.weaponp == weapon).first()[0]
    #             attack = db.session.query(warriorsdb.c.attack)\
    #                 .filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]			
    #             plusattack = attack * 0.01 * plusweapon	
            
    #         strength = round((strength + plushealth + plusattack),0)
    #         selectedWarrior = {
    #             # 'id': session['counter'],
    #             'id': counter,
    #             'warrior': warrior,
    #             'level': level,
    #             'armor': armor,
    #             'weapon': weapon,
    #             'strength': strength,
    #             'slug': slug
    #         }
    #         warriorsteam.append(selectedWarrior)

    #     else: # verifyForm
    #         rating = int(request.form.get('rating'))
    #         totalStrength = sum([ warriorstrength['strength']  for warriorstrength in warriorsteam ])
    #         strengthmsg = modules.chooseMsg(rating, totalStrength)

    # stopadd = len(warriorsteam)

    # # if team empty, clear session
    # if stopadd == 0:
    #     # session.clear()
    #     counter = 0
    # # if team complete, calculate total strength
    # if stopadd == 5:
    #     warriorstrength = 0
    #     totalStrength = sum([ warriorstrength['strength']  for warriorstrength in warriorsteam ])

    return render_template("pages/strength.html",
    warriors_list = warriors_list,
    # weaponslist = weaponslist,
    # armorslist = armorslist,
    warriors_dict = warriors_dict,
    # warriors = warriorsteam,
    # stopadd = stopadd,
    # totalStrength = totalStrength,
    # strengthmsg = strengthmsg
    )

# @bp.route("/delete/<id>", methods=['GET', 'POST'])
# def delete(id):
#     global warriorsteam
#     idmatch = next((i for i, item in enumerate(warriorsteam) if item["id"] == int(id)),None)
#     warriorsteam.pop(idmatch)
#     stopadd = len(warriorsteam)
#     return redirect(url_for("strength"))

@bp.route("/level")
def level():
    warrior = request.args.get('warrior')
    max_level = commands.get_max_level(warrior)
    global max_level_to
    max_level_to = max_level
    return render_template('level.html', max_level=max_level)		

@bp.route("/levels01")
def levels_01():
    warrior_01 = request.args.get('warrior01')
    max_level_01 = commands.get_max_level(warrior_01)
    return render_template('levels01.html', max_level_01=max_level_01)

@bp.route("/levels02")
def levels_02():
    warrior_02 = request.args.get('warrior02')
    max_level_02 = commands.get_max_level(warrior_02)
    return render_template('levels02.html', max_level_02=max_level_02)

@bp.route("/m_units")
def m_units():
    m_units_list = commands.get_kuzutiks()
    return render_template("pages/munits.html", m_units_list=m_units_list)	

@bp.route("/m_tools/")
def m_tools():
    tools_list = commands.get_tools()    
    return render_template("pages/mtools.html", tools_list=tools_list)	

@bp.route("/buildings")
def buildings():
    return render_template("pages/buildings.html",
    buildings=data_dict.buildings)