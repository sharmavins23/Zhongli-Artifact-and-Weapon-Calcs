# Static data class for lithic spear, with one liyue character
class LithicSpear_Base:
    level = 90
    refinementLevel = 1

    name = "Lithic Spear (1 Liyue Comp)"

    # Base stat values
    baseATK = 565
    atkPercent = 0.276

    # Passive values
    stackCount = 1
    atkPercent += 0.07 * stackCount
    critRATE = 0.03 * stackCount
