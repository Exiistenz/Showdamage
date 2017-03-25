## IMPORTS

from events import Event
from messages import HintText
from messages import SayText2
from players.entity import Player

from .configs import g_configs
from .info import info
from .strings import g_hitgroups_name, g_damage_message

## GLOBALS

g_show_damage_type = {
    1: SayText2,
    2: HintText,
}

## GAME EVENT

@Event('player_hurt', 'player_death')
def player_action(event_data):
    if event_data['attacker'] in (event_data['userid'], 0):
        return

    attacker = Player.from_userid(event_data['attacker'])
    victim = Player.from_userid(event_data['userid'])
    if attacker.team == victim.team or attacker.steamid == 'BOT':
        return

    # Sometimes dmg_health key not exist
    try:
        damage = str(event_data['dmg_health'])
        armor = str(event_data['dmg_armor'])
        hitgroup = g_hitgroups_name[event_data['hitgroup']][attacker.language[:2]]
    except KeyError:
        return

    info = (
        'full' if g_configs['show_hit_member'].get_int() == 1 and 
        g_configs['show_armor_hit'].get_int() == 1 else (
            'hitgroup' if g_configs['show_hit_member'].get_int() == 1 else (
                'armor' if g_configs['show_armor_hit'].get_int() == 1 else 'damage'
            )
        )
    )

    message = g_damage_message[g_configs['display_type'].get_int()][info]

    # Display message
    g_show_damage_type[g_configs['display_type'].get_int()](message).send(attacker.index, 
        hitgroup=hitgroup, damage=damage, armor=armor)