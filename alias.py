from hero import Hero

heroes_aliases = {
    "naga": "Naga Siren",
    "kotl": "Keeper of the Light",
}


class NotFoundError(Exception):
    pass


def find_hero(heroes: list[Hero], value: str) -> Hero:
    value_lower = value.lower()
    if value_lower in heroes_aliases:
        value_lower = heroes_aliases[value_lower].lower()
    for hero in heroes:
        if value_lower == hero.name.lower():
            return hero
    raise NotFoundError(value)
