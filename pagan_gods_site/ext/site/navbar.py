from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link

# navbar
nav_bar_01 = Navbar('',
    View('Combat Units', 'site.c_units'),
    View('Combat Equipments', 'site.c_equips', type_of_equip='armors'),
	View('Abilities', 'site.abilities'),
    View('FUR and XP', 'site.fur'),
	View('Stats and Strength', 'site.strength')

)
nav_bar_02 = Navbar('',
    View('Mining Units', 'site.m_units'),
    View('Mining Tools', 'site.m_tools'),
    View('House of Voivode', 'site.buildings')    
)

nav_bar_03 = Navbar('',
    Link('Official Site', 'https://pagangods.io'),
    Link('Game App', 'https://app.pagangods.io'),
    Link('Medium', 'https://inoworlds.medium.com')
)


nav = Nav()
nav.register_element('nav_bar_01', nav_bar_01)
nav.register_element('nav_bar_02', nav_bar_02)
nav.register_element('nav_bar_03', nav_bar_03)


# def chooseMsg(rating, totalStrength):
#     percent = int(100*(rating * 50) / totalStrength)
#     if percent > 0 and percent < 100:
#         message = f'Your team is beating enemies {100 - percent}% weaker than you. You can do better!'
#     elif percent >=100 and percent < 200:
#         message = f'Great! You are beating enemies {percent}% stronger!' 
#     elif percent >=200 and percent < 250:
#         message = f'Awesome! You are beating enemies {percent}% stronger!' 
#     else:
#         message = f'Impressive! You are beating enemies {percent}% stronger!'                       
#     return message