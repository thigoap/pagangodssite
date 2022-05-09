from flask import render_template, redirect, url_for, request
from flask import Blueprint

from pagansite.ext.db import commands
from pagansite.ext.db import datadict

bp = Blueprint("site", __name__)

@bp.route("/")
@bp.route("/index")
def index():
    return render_template("pages/index.html")

@bp.route("/cunits", methods=['GET', 'POST'])
def cunits():
    if request.method == 'POST':
        cardType = list(request.form.to_dict().keys())[0]
        cardMult = cardType[1]
        cardEVO = cardType[-1]
        warriors = commands.get_warriors(cardMult, cardEVO)	
    else:
        cardType = 'w0EVO0'
        warriors = warriors = commands.get_warriors(0, 0)	

    return render_template("pages/cunits.html",
    warriors=warriors
    )	

@bp.route("/cequips/<typeOfEquip>")
def cequips(typeOfEquip):
    if typeOfEquip == 'armors':
        equipsList = commands.get_armors()
    else:
        equipsList = commands.get_weapons()       
    return render_template("pages/cequips.html", equipsList=equipsList, typeOfEquip=typeOfEquip)

@bp.route("/abilities")
def abilities():
    return render_template("pages/abilities.html",
    abilities = datadict.abilities
    )
    
@bp.route("/fur", methods=['GET', 'POST'])
def fur():
    warriorslist = commands.get_warriors_list()
    if request.method == 'POST':
        warrior = request.form.get('warrior')
        ilevel = request.form.get('ilevel')
        flevel = request.form.get('flevel')
        fur = commands.get_fur(warrior, ilevel, flevel)
        exp = commands.get_exp(warrior, ilevel, flevel)
        runes = commands.get_runes(warrior, ilevel, flevel)
        expensesdict = {
            'warrior': warrior,
            'ilevel': ilevel,
            'flevel': flevel,
            'fur': fur,
            'exp': exp,
            'runes': runes,
            'wood': 1000 * runes,
            'iron': 1000 * runes
        }	
        return render_template("pages/fur.html",
        warriorslist = warriorslist, expensesdict=expensesdict)
    return render_template("pages/fur.html",
    warriorslist = warriorslist)

@bp.route("/flevel")
def flevel():
    ilevel = int(request.args.get('ilevel'))
    maxlevel = maxlevelto
    return render_template('flevel.html', ilevel=ilevel, maxlevel=maxlevel)		

# counter = 0
# warriorsteam = []
@bp.route("/strength", methods=['GET', 'POST'])
def strength():
    global counter
    global warriorsteam
    #define dropdown lists
    warriorslist = commands.get_warriors_list()
    warriorsdict = {}
    # weaponslist = db.session.query(allweapons.c.weaponp).all()
    # weaponslist = [weapons[0] for weapons in weaponslist]
    # armorslist = db.session.query(allarmors.c.armorp).all()
    # armorslist = [armors[0] for armors in armorslist]
    # totalStrength = 0
    # strengthmsg = ''
    
    if request.method == 'POST':
        if 'compareForm' in request.form:
            warrior01 = request.form.get('warrior01')
            warrior02 = request.form.get('warrior02')
            level01 = request.form.get('level01')
            level02 = request.form.get('level02')
            slug01 = commands.get_slugs(warrior01, warrior02)[0]
            slug02 = commands.get_slugs(warrior01, warrior02)[1]
            health01 = commands.get_healths(warrior01, warrior02, level01, level02)[0]
            health02 = commands.get_healths(warrior01, warrior02, level01, level02)[1]
            attack01 = commands.get_attacks(warrior01, warrior02, level01, level02)[0]
            attack02 = commands.get_attacks(warrior01, warrior02, level01, level02)[1]
            strength01 = commands.get_strengths(warrior01, warrior02, level01, level02)[0]
            strength02 = commands.get_strengths(warrior01, warrior02, level01, level02)[1]
            warriorsdict = {
                'warrior01': warrior01, 'slug01': slug01, 'level01': level01, 'health01': health01, 'attack01': attack01, 'strength01': strength01,
                'warrior02': warrior02,	'slug02': slug02, 'level02': level02, 'health02': health02,	'attack02': attack02, 'strength02': strength02,
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
    warriorslist = warriorslist,
    # weaponslist = weaponslist,
    # armorslist = armorslist,
    warriorsdict = warriorsdict,
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
    maxlevel = commands.get_max_level(warrior)
    global maxlevelto
    maxlevelto = maxlevel
    return render_template('level.html', maxlevel=maxlevel)		

@bp.route("/levels01")
def levels01():
    warrior01 = request.args.get('warrior01')
    maxlevel01 = commands.get_max_level(warrior01)
    return render_template('levels01.html', maxlevel01=maxlevel01)

@bp.route("/levels02")
def levels02():
    warrior02 = request.args.get('warrior02')
    maxlevel02 = commands.get_max_level(warrior02)
    return render_template('levels02.html', maxlevel02=maxlevel02)


@bp.route("/munits")
def munits():
    munitsList = commands.get_kuzutiks()
    return render_template("pages/munits.html", munitsList=munitsList)	

@bp.route("/mtools/<tool>")
def mtools(tool):
    # if tool == 'pickaxe':
    # 	tollsList = db.session.query(alltools).all()
    # else:
    # 	tollsList = db.session.query(alltools).all()
    return render_template("pages/mtools.html", tool=tool)	

@bp.route("/buildings")
def buildings():
    return render_template("pages/buildings.html",
    buildings=datadict.buildings)