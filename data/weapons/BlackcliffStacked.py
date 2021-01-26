# Static data class for blackcliff pole with full stacks
class BlackcliffPole_Stacked:
    level = 90
    refinementLevel = 1

    name = "Blackcliff Pole (3 stacks)"

    # Base stat values
    baseATK = 510
    critDMG = 0.551

    # Passive values
    stackCount = 3
    atkPercent = 0.12 * stackCount
