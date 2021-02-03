# Static data class for crescent pike
class CrescentPike:
    level = 90
    refinementLevel = 5

    name = "Crescent Pike"

    # Base stat values
    baseATK = 565
    physDMG = 0.345

    # Passive values
    mvAdditive = 0.2 + ((refinementLevel-1)*0.05)
