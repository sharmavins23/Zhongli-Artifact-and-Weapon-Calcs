# Static data class for character stats
class Zhongli:
    level = 90
    talentLevel = 6
    # Base stat values
    baseHP = 14695
    baseATK = 251
    baseCritRATE = 0.05
    baseCritDMG = 0.5

    # Ability MVs and frame counts

    class Normal:  # Normal attack spear kick hop combo
        frames = 140
        mv = 2.7090
        hits = 8
        rotations = (720 - 100 - 140) / 140  # Removing time for hold E and Q
        hpConv = 0.0139

    class HoldE:  # Hold E initial hit
        frames = 720
        mv = 1.3440
        hits = 2  # Damage from pillar pop-up and hold E shockwave
        hpConv = 0.0190

    class EResonate:  # Pillar resonance
        frames = 120
        mv = 0.4480
        rotations = 6
        hpConv = 0.0190

    class Q:  # I WILL HAVE ORDER
        frames = 140
        mv = 6.3956
        hpConv = 0.33
