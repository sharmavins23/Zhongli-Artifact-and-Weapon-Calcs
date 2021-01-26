# Static data class for lithic spear, with four liyue characters
class LithicSpear_Stacked:
    level = 90
    refinementLevel = 1

    name = "Lithic Spear (Full Liyue Comp)"

    # Base stat values
    baseATK = 565
    atkPercent = 0.276

    # Passive values
    stackCount = 4
    atkPercent += 0.07 * stackCount
    critRATE = 0.03 * stackCount
