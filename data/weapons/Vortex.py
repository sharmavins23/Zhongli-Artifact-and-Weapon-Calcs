# Static data class for vortex vanquisher
class VortexVanquisher:
    level = 90
    refinementLevel = 1

    name = "Vortex Vanquisher"

    # Base stat values
    baseATK = 608
    atkPercent = 0.496

    # Passive values
    stackCount = 5
    atkPercent = 2 * 0.04 * stackCount  # Assuming shield is up at all times
