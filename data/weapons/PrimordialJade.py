# Static data calss for primordial jade winged spear
class PrimordialJadeWingedSpear:
    level = 90
    refinementLevel = 1

    name = "Primordial Jade Winged Spear"

    # Base stat values
    baseATK = 674
    critRATE = 0.221

    # Passive values
    stackCount = 7
    atkPercent = 0.032 * stackCount
    normalDMG = 0.12  # ! Modelling as normal damage, even though this is a full multiplier
