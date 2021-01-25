# Data imports
from data.ZLData import Zhongli
from data.ArtiStats import ArtifactStats
from data.weapons.CPikeData import CrescentPike


# Functional damage calculation
def doDamageCalc(weapon, artiset):
    # HP stat calculations =====================================================
    totalHPPercent = ArtifactStats.sandsHP + \
        ArtifactStats.cupHP + ArtifactStats.helmHP

    if hasattr(weapon, hpPercent):
        totalHPPercent += weapon.HPPercent

    totalHP = (Zhongli.baseHP * (1 + totalHPPercent)) + ArtifactStats.flowerHP

    # ATK stat calculations ====================================================
    totalATKPercent = ArtifactStats.sandsATK + \
        ArtifactStats.cupATK + ArtifactStats.helmATK

    if hasattr(weapon, atkPercent):
        totalATKPercent += weapon.ATKPercent

    totalATK = (Zhongli.baseATK + weapon.baseATK) * \
        (1+totalATKPercent) + ArtifactStats.featherATK

    # CRIT stat calculations ===================================================
    totalCritRATE = ArtifactStats.helmCritRATE

    if hasattr(weapon, critRATE):
        totalCritRate += weapon.critRATE

    totalCritDMG = ArtifactStats.helmCritDMG

    if hasattr(weapon, critDMG):
        totalCritDMG += weapon.critDMG

    critMulti = totalCritRATE * (1+totalCritDMG) + 1

    # PHYS stat calculations ===================================================
    totalPHYSDMG = ArtifactStats.cupPHYS

    if hasattr(weapon, physDMG):
        totalPHYSDMG += weapon.physDMG

    physMulti = totalPHYSDMG + 1

    # GEO stat calculations ====================================================
    totalGEODMG = ArtifactStats.cupGEO

    geoMulti = totalGEODMG + 1

# * Movement Calculations ======================================================
    # Normal attack calculations ===============================================
    comboTotal = Zhongli.Normal.mv

    if hasattr(weapon, mvAdditive):
        comboTotal += (weapon.mvAdditive * Zhongli.Normal.hits)

    # Buff additional damage
    normalBuffAddlDMG = Zhongli.Normal.hpConv * totalHP * Zhongli.Normal.hits

    normalAttackDamage = ((totalATK * comboTotal) + normalBuffAddlDMG) * \
        physMulti * critMulti * Zhongli.Normal.rotations

    # Dominus Lapidis calculations =============================================
    eBuffAddlDMG = Zhongli.HoldE.hpConv * totalHP

    holdEDMG = ((totalATK * Zhongli.HoldE.mv) +
                (2*eBuffAddlDMG)) * critMulti * geoMulti

    eResoDamage = ((totalATK * Zhongli.EResonate.mv) +
                   eBuffAddlDMG) * critMulti * geoMulti

    eDamage = holdEDMG + (6 * eResoDamage)

    # Planet Befall calculations ===============================================
    qConversionDMG = totalHP * Zhongli.Q.hpConv

    qDamage = ((totalATK * Zhongli.q.mv) + qConversionDMG) * \
        critMulti * geoMulti

# * Outputs ====================================================================
    return {
        "ATK": totalATK,
        "HP": totalHP,
        "normalDMG": normalAttackDamage,
        "eDMG": eDamage,
        "qDMG": qDamage
    }
