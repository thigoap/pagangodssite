from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link

# navbar
navbar1 = Navbar('',
    View('Combat Units', 'cunits'),
    View('Combat Equipments', 'cequips', typeOfEquip='armors'),
	View('Abilities', 'abilities'),
    View('FUR and XP', 'fur'),
	View('Stats and Strength', 'strength')

)
navbar2 = Navbar('',
    View('Mining Units', 'munits'),
    View('Mining Tools', 'mtools', tool = 'axe')
)

navbar3 = Navbar('',
    Link('Official Site', 'https://pagangods.io'),
    Link('Game App', 'https://app.pagangods.io'),
    Link('Medium', 'https://inoworlds.medium.com')
)


nav = Nav()
nav.register_element('navbar1', navbar1)
nav.register_element('navbar2', navbar2)
nav.register_element('navbar3', navbar3)


def chooseMsg(rating, totalStrength):
    percent = int(100*(rating * 50) / totalStrength)
    if percent > 0 and percent < 100:
        message = f'Your team is beating enemies {100 - percent}% weaker than you. You can do better!'
    elif percent >=100 and percent < 200:
        message = f'Great! You are beating enemies {percent}% stronger!' 
    elif percent >=200 and percent < 250:
        message = f'Awesome! You are beating enemies {percent}% stronger!' 
    else:
        message = f'Impressive! You are beating enemies {percent}% stronger!'                       
    return message
