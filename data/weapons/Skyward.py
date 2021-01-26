# Static data class for skyward spine
class SkywardSpine:
    level = 90
    refinementLevel = 1

    name = "Skyward Spine"

    # Base stat values
    baseATK = 674

    # Passive values
    critRATE = 0.08
    normalATKSpeed = 0.12
    chance = 0.5
    mvAdditive = 0.4 * chance
    cooldown = 2 * 60
