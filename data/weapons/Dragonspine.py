# Static data class for dragonspine spear
class DragonspineSpear:
    level = 90
    refinementLevel = 1

    name = "Dragonspine Spear"

    # Base stat values
    baseATK = 454
    physDMG = 0.69

    # Passive values
    chance = 0.6
    mvAdditive = 0.8 * chance  # Assuming enemies aren't affected by cryo
    cooldown = 10 * 60
