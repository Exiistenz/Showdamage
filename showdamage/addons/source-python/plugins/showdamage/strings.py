## IMPORTS

from messages import SayText2
from translations.strings import LangStrings

## ALL DECLARATION

__all__ = (
	'g_hitgroups_name',
	'g_damage_message'
)

## GLOBALS

strings = LangStrings('showdamage')

## MESSAGE DEFINITION

g_hitgroups_name = [
    strings['Generic'],
    strings['Head'],
    strings['Chest'],
    strings['Stomach'],
    strings['Left Arm'],
    strings['Right Arm'],
    strings['Left Leg'],
    strings['Right Leg']
]

g_damage_message = {
	1 : {
		'full' : strings['Show Damage Chat Full'],
		'hitgroup' : strings['Show Damage Chat Hitgroup'],
		'armor' : strings['Show Damage Chat Armor'],
		'damage' : strings['Show Damage Chat Damage']
	},
	2 : {
		'full' : strings['Show Damage Hint Full'],
		'hitgroup' : strings['Show Damage Hint Hitgroup'],
		'armor' : strings['Show Damage Hint Armor'],
		'damage' : strings['Show Damage Hint Damage']
	}
}
