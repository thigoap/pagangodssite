from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

import modules
import datab

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SESSION_SECRET_KEY')
modules.nav.init_app(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://srzcpwgrdpducd:e2d91d2a7a092b77807b9d218e9bae8ef2cb1562a12513fe8577c015900e9871@ec2-52-203-118-49.compute-1.amazonaws.com:5432/dfv2ku5nod2ui'

db = SQLAlchemy(app)

allwarriors = db.Table('allwarriors', db.metadata, autoload=True, autoload_with=db.engine)
warriorsdb = db.Table('warriorsdb', db.metadata, autoload=True, autoload_with=db.engine)
allweapons = db.Table('allweapons', db.metadata, autoload=True, autoload_with=db.engine)
allarmors = db.Table('allarmors', db.metadata, autoload=True, autoload_with=db.engine)
allkuzutiks = db.Table('allkuzutiks', db.metadata, autoload=True, autoload_with=db.engine)
# alltools = db.Table('alltools', db.metadata, autoload=True, autoload_with=db.engine)

	
@app.route("/")
@app.route("/index")
def index():
	return render_template("pages/index.html")

@app.route("/cunits", methods=['GET', 'POST'])
def cunits():
	if request.method == 'POST':
		cardType = list(request.form.to_dict().keys())[0]
		cardMult = cardType[1]
		cardEVO = cardType[-1]
		warriors = db.session\
			.query(allwarriors.c.warrior, allwarriors.c.race, allwarriors.c.rarity, allwarriors.c.slug)\
			.filter(allwarriors.c.mult == cardMult,\
					allwarriors.c.evo == cardEVO)\
			.all()		
	else:
		cardType = 'w0EVO0'
		warriors = db.session\
			.query(allwarriors.c.warrior, allwarriors.c.race, allwarriors.c.rarity, allwarriors.c.slug)\
			.filter(allwarriors.c.mult == 0,\
					allwarriors.c.evo == 0)\
			.all()			

	return render_template("pages/cunits.html",
	warriors=warriors
	)	

@app.route("/cequips/<typeOfEquip>")
def cequips(typeOfEquip):
	if typeOfEquip == 'armors':
		equipsList = db.session.query(allarmors).all()
	else:
		equipsList = db.session.query(allweapons).all()
	return render_template("pages/cequips.html", equipsList=equipsList, typeOfEquip=typeOfEquip)

@app.route("/abilities")
def abilities():
	return render_template("pages/abilities.html",
	abilities = datab.abilities
	)
	
@app.route("/fur", methods=['GET', 'POST'])
def fur():
	warriorslist = db.session.query(allwarriors.c.warrior).all()
	warriorslist = [warriors[0] for warriors in warriorslist]
	if request.method == 'POST':
		warrior = request.form.get('warrior')
		ilevel = request.form.get('ilevel')
		flevel = request.form.get('flevel')
		fur = db.session\
		.query(db.func.sum(warriorsdb.c.fur))\
		.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
		fur = fur[0][0]	
		exp = db.session\
		.query(db.func.sum(warriorsdb.c.xp))\
		.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
		exp = exp[0][0]	
		runes = db.session\
		.query(db.func.sum(warriorsdb.c.runes))\
		.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl > int(ilevel), warriorsdb.c.lvl <= int(flevel)).all()
		runes = runes[0][0]	
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

@app.route("/flevel")
def flevel():
	ilevel = int(request.args.get('ilevel'))
	maxlevel = maxlevelto
	return render_template('flevel.html', ilevel=ilevel, maxlevel=maxlevel)		

counter = 0
warriorsteam = []
@app.route("/strength", methods=['GET', 'POST'])
def strength():
	global counter
	global warriorsteam
	#define dropdown lists
	warriorslist = db.session.query(allwarriors.c.warrior).all()
	warriorslist = [warriors[0] for warriors in warriorslist]
	weaponslist = db.session.query(allweapons.c.weaponp).all()
	weaponslist = [weapons[0] for weapons in weaponslist]
	armorslist = db.session.query(allarmors.c.armorp).all()
	armorslist = [armors[0] for armors in armorslist]
	warriorsdict = {}
	totalStrength = 0
	strengthmsg = ''
	
	if request.method == 'POST':
		if 'compareForm' in request.form:
			warrior01 = request.form.get('warrior01')
			warrior02 = request.form.get('warrior02')
			level01 = request.form.get('level01')
			level02 = request.form.get('level02')
			# eval(variavel) pega uma tabela usando variável
			slug01 = db.session.query(allwarriors.c.slug)\
				.filter(allwarriors.c.warrior == warrior01).first()[0]
			slug02 = db.session.query(allwarriors.c.slug)\
				.filter(allwarriors.c.warrior == warrior02).first()[0]
			health01 = round(float(db.session.query(warriorsdb.c.health)\
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
			health02 = round(float(db.session.query(warriorsdb.c.health)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)
			attack01 = round(float(db.session.query(warriorsdb.c.attack)\
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
			attack02 = round(float(db.session.query(warriorsdb.c.attack)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)
			strength01 = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.lvl == level01).first()[0]),0)
			strength02 = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.lvl == level02).first()[0]),0)		
			warriorsdict = {
				'warrior01': warrior01, 'slug01': slug01, 'level01': level01, 'health01': health01, 'attack01': attack01, 'strength01': strength01,
				'warrior02': warrior02,	'slug02': slug02, 'level02': level02, 'health02': health02,	'attack02': attack02, 'strength02': strength02,
			}
		elif 'addForm' in request.form:
			# if 'counter' in session:
			# 	session['counter'] += 1
			# else:
			# 	session['counter'] = 0
			counter+=1
			warrior = request.form.get('warrior')
			level = request.form.get('level')
			strength = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]),0)
			slug = db.session.query(allwarriors.c.slug)\
				.filter(allwarriors.c.warrior == warrior).first()[0]
			plushealth = 0
			plusattack = 0
			armor = request.form.get('armor')
			if armor == 'Choose armor': armor = '-' # if no armor
			else: 
				plusarmor = db.session.query(allarmors.c.percent)\
					.filter(allarmors.c.armorp == armor).first()[0]
				health = db.session.query(warriorsdb.c.health)\
					.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]
				plushealth = health * 0.01 * plusarmor
			weapon = request.form.get('weapon')
			if weapon == 'Choose weapon': weapon = '-' # if no weapon
			else:
				plusweapon = db.session.query(allweapons.c.percent)\
					.filter(allweapons.c.weaponp == weapon).first()[0]
				attack = db.session.query(warriorsdb.c.attack)\
					.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.lvl == level).first()[0]			
				plusattack = attack * 0.01 * plusweapon	
			
			strength = round((strength + plushealth + plusattack),0)
			selectedWarrior = {
				# 'id': session['counter'],
				'id': counter,
				'warrior': warrior,
				'level': level,
				'armor': armor,
				'weapon': weapon,
				'strength': strength,
				'slug': slug
			}
			warriorsteam.append(selectedWarrior)

		else: # verifyForm
			rating = int(request.form.get('rating'))
			totalStrength = sum([ warriorstrength['strength']  for warriorstrength in warriorsteam ])
			strengthmsg = modules.chooseMsg(rating, totalStrength)

	stopadd = len(warriorsteam)

	# if team empty, clear session
	if stopadd == 0:
		# session.clear()
		counter = 0
	# if team complete, calculate total strength
	if stopadd == 5:
		warriorstrength = 0
		totalStrength = sum([ warriorstrength['strength']  for warriorstrength in warriorsteam ])

	return render_template("pages/strength.html",
	warriorslist = warriorslist,
	weaponslist = weaponslist,
	armorslist = armorslist,
	warriorsdict = warriorsdict,
	warriors = warriorsteam,
	stopadd = stopadd,
	totalStrength = totalStrength,
	strengthmsg = strengthmsg
	)

@app.route("/delete/<id>", methods=['GET', 'POST'])
def delete(id):
	global warriorsteam
	idmatch = next((i for i, item in enumerate(warriorsteam) if item["id"] == int(id)),None)
	warriorsteam.pop(idmatch)
	stopadd = len(warriorsteam)
	return redirect(url_for("strength"))

@app.route("/level")
def level():
	warrior = request.args.get('warrior')
	maxlevel = db.session.query(allwarriors.c.maxlevel).filter(allwarriors.c.warrior == warrior).first()[0]
	global maxlevelto
	maxlevelto = maxlevel
	return render_template('level.html', maxlevel=maxlevel)		

@app.route("/levels01")
def levels01():
	warrior01 = request.args.get('warrior01')
	maxlevel01 = db.session.query(allwarriors.c.maxlevel).filter(allwarriors.c.warrior == warrior01).first()[0]
	return render_template('levels01.html', maxlevel01=maxlevel01)

@app.route("/levels02")
def levels02():
	warrior02 = request.args.get('warrior02')
	maxlevel02 = db.session.query(allwarriors.c.maxlevel).filter(allwarriors.c.warrior == warrior02).first()[0]
	return render_template('levels02.html', maxlevel02=maxlevel02)


@app.route("/munits")
def munits():
	munitsList = db.session.query(allkuzutiks).all()
	return render_template("pages/munits.html", munitsList=munitsList)	

@app.route("/mtools/<tool>")
def mtools(tool):
	# if tool == 'pickaxe':
	# 	tollsList = db.session.query(alltools).all()
	# else:
	# 	tollsList = db.session.query(alltools).all()
	return render_template("pages/mtools.html", tool=tool)	




if __name__ == '__main__':
	app.run(debug=True)