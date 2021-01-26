# Static data class for Prototype Starglitter
class Starglitter:
    level = 90
    refinementLevel = 1

    name = "Prototype Starglitter"

    # Base stat values
    baseATK = 510

    # Passive values
    stackCount = 1  # Since we can only E every 12s, we only ever have 1 stack
    normalDMG = 0.08 * stackCount
