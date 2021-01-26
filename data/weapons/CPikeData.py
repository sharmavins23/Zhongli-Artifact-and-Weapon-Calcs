# Static data class for crescent pike
class CrescentPike:
    level = 90

    def __init__(self):
        self.refinementLevel = 1
        self.mvAdditive = 0.2

    def __name__(self):
        return "Crescent Pike"

    def setRefinement(self, value):
        self.refinementLevel = value
        self.mvAdditive = 0.2 + (0.05 * (value-1))

    # Base stat values
    baseATK = 565
    physDMG = 0.345
