from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import modules
import datab

app = Flask(__name__)
modules.nav.init_app(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/warriors.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://srzcpwgrdpducd:e2d91d2a7a092b77807b9d218e9bae8ef2cb1562a12513fe8577c015900e9871@ec2-52-203-118-49.compute-1.amazonaws.com:5432/dfv2ku5nod2ui'
db = SQLAlchemy(app)

allwarriors = db.Table('allwarriors', db.metadata, autoload=True, autoload_with=db.engine)
warriorsdb = db.Table('warriorsdb', db.metadata, autoload=True, autoload_with=db.engine)
allweapons = db.Table('allweapons', db.metadata, autoload=True, autoload_with=db.engine)
allarmors = db.Table('allarmors', db.metadata, autoload=True, autoload_with=db.engine)

class Warrior(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	warrior = db.Column(db.String(50))
	level = db.Column(db.Integer)
	armor = db.Column(db.String(50))
	weapon = db.Column(db.String(50))
	strength = db.Column(db.Float)
	slug = db.Column(db.String(50))
	
@app.route("/")
@app.route("/index")
def index():
	return render_template("pages/index.html")

@app.route("/cunits", methods=['GET', 'POST'])
def cunits():
	if request.method == 'POST':
		cardType = list(request.form.to_dict().keys())[0]
		print('cardType', cardType)
		cardMult = cardType[1]
		cardEVO = cardType[-1]
		print('cardMult', cardMult)
		print('cardEVO', cardEVO)
		warriors = db.session\
			.query(allwarriors.c.warrior, allwarriors.c.race, allwarriors.c.rarity, allwarriors.c.slug)\
			.filter(allwarriors.c.mult == cardMult,\
					allwarriors.c.EVO == cardEVO)\
			.all()		
	else:
		cardType = 'w0EVO0'
		warriors = db.session\
			.query(allwarriors.c.warrior, allwarriors.c.race, allwarriors.c.rarity, allwarriors.c.slug)\
			.filter(allwarriors.c.mult == 0,\
					allwarriors.c.EVO == 0)\
			.all()

	warriorparameter = warriors
	return render_template("pages/cunits.html",
	warriorparameter=warriorparameter
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
	return render_template("pages/fur.html")	

@app.route("/strength", methods=['GET', 'POST'])
def strength():
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
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.level == level01).first()[0]),0)
			health02 = round(float(db.session.query(warriorsdb.c.health)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.level == level02).first()[0]),0)
			attack01 = round(float(db.session.query(warriorsdb.c.attack)\
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.level == level01).first()[0]),0)
			attack02 = round(float(db.session.query(warriorsdb.c.attack)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.level == level02).first()[0]),0)
			strength01 = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior01, warriorsdb.c.level == level01).first()[0]),0)
			strength02 = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior02, warriorsdb.c.level == level02).first()[0]),0)		
			warriorsdict = {
				'warrior01': warrior01, 'slug01': slug01, 'level01': level01, 'health01': health01, 'attack01': attack01, 'strength01': strength01,
				'warrior02': warrior02,	'slug02': slug02, 'level02': level02, 'health02': health02,	'attack02': attack02, 'strength02': strength02,
			}
		elif 'addForm' in request.form:
			warrior = request.form.get('warrior')
			level = request.form.get('level')
			strength = round(float(db.session.query(warriorsdb.c.strength)\
				.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.level == level).first()[0]),0)
			slug = db.session.query(allwarriors.c.slug)\
				.filter(allwarriors.c.warrior == warrior).first()[0]
			plushealth = 0
			plusattack = 0
			armor = request.form.get('armor')
			if armor == 'Choose armor': armor = '-' # if no armor
			else: 
				plusarmor = db.session.query(allarmors.c.percentage)\
					.filter(allarmors.c.armorp == armor).first()[0]
				health = db.session.query(warriorsdb.c.health)\
					.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.level == level).first()[0]
				plushealth = health * 0.01 * plusarmor
			weapon = request.form.get('weapon')
			if weapon == 'Choose weapon': weapon = '-' # if no weapon
			else:
				plusweapon = db.session.query(allweapons.c.percentage)\
					.filter(allweapons.c.weaponp == weapon).first()[0]
				attack = db.session.query(warriorsdb.c.attack)\
					.filter(warriorsdb.c.warrior == warrior, warriorsdb.c.level == level).first()[0]			
				plusattack = attack * 0.01 * plusweapon	
			
			strength = round((strength + plushealth + plusattack),0)	
			selectedWarrior = Warrior(warrior=warrior, level=level, armor=armor, weapon=weapon, strength=strength, slug=slug)

			db.session.add(selectedWarrior)
			db.session.commit()
		else: # verifyForm
			rating = int(request.form.get('rating'))
			totalStrength = db.session.query(func.sum(Warrior.strength)).one()[0]
			strengthmsg = modules.chooseMsg(rating, totalStrength)

	warriors = Warrior.query.limit(5).all()
	stopadd = db.session.query(Warrior).count()

	# if team complete, calculate total strength
	if stopadd == 5:
		totalStrength = db.session.query(func.sum(Warrior.strength)).one()[0]

	return render_template("pages/strength.html",
	warriorslist = warriorslist,
	weaponslist = weaponslist,
	armorslist = armorslist,
	warriorsdict = warriorsdict,
	warriors = warriors,
	stopadd = stopadd,
	totalStrength = totalStrength,
	strengthmsg = strengthmsg
	)	

@app.route("/delete/<id>", methods=['GET', 'POST'])
def delete(id):
	warrior = Warrior.query.get(id)
	db.session.delete(warrior)
	db.session.commit()
	stopadd = db.session.query(Warrior).count()
	return redirect(url_for("strength"))	

@app.route("/level")
def level():
	warrior = request.args.get('warrior')
	maxlevel = db.session.query(allwarriors.c.maxlevel).filter(allwarriors.c.warrior == warrior).first()[0]
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
	return render_template("pages/munits.html")	

@app.route("/mtools")
def mtools():
	return render_template("pages/mtools.html")	




if __name__ == '__main__':
	app.run(debug=True)