# Data imports
from data.ZLData import Zhongli
from data.ArtiStats import ArtifactStats
# Weapon imports
from data.weapons.CPikeData import CrescentPike
# Artifact set imports
from data.artisets.BloodstainedGlad import BloodstainedGlad
from data.artisets.BloodstainedNoblesse import BloodstainedNoblesse
from data.artisets.Bolide import Bolide
from data.artisets.Glad import Glad
from data.artisets.GladNoblesse import GladNoblesse
from data.artisets.PetraGlad import PetraGlad
from data.artisets.PetraNoblesse import PetraNoblesse


# Functional damage calculation
def doDamageCalc(weapon, artiset):
    # HP stat calculations =====================================================
    totalHPPercent = ArtifactStats.sandsHP + \
        ArtifactStats.cupHP + ArtifactStats.helmHP

    if hasattr(weapon, "hpPercent"):
        totalHPPercent += weapon.hpPercent

    totalHP = (Zhongli.baseHP * (1 + totalHPPercent)) + ArtifactStats.flowerHP

    # ATK stat calculations ====================================================
    totalATKPercent = ArtifactStats.sandsATK + \
        ArtifactStats.cupATK + ArtifactStats.helmATK

    if hasattr(weapon, "atkPercent"):
        totalATKPercent += weapon.atkPercent

    if hasattr(artiset, "atkPercent"):
        totalATKPercent += artiset.atkPercent

    totalATK = (Zhongli.baseATK + weapon.baseATK) * \
        (1+totalATKPercent) + ArtifactStats.featherATK

    # CRIT stat calculations ===================================================
    totalCritRATE = ArtifactStats.helmCritRATE

    if hasattr(weapon, "critRATE"):
        totalCritRate += weapon.critRATE

    totalCritDMG = ArtifactStats.helmCritDMG

    if hasattr(weapon, "critDMG"):
        totalCritDMG += weapon.critDMG

    critMulti = totalCritRATE * (1+totalCritDMG) + 1

    # PHYS stat calculations ===================================================
    totalPHYSDMG = ArtifactStats.cupPHYS

    if hasattr(weapon, "physDMG"):
        totalPHYSDMG += weapon.physDMG

    physMulti = totalPHYSDMG + 1

    # GEO stat calculations ====================================================
    totalGEODMG = ArtifactStats.cupGEO

    if hasattr(artiset, "geoDMG"):
        totalGEODMG += artiset.geoDMG

    geoMulti = totalGEODMG + 1

# * Movement Calculations ======================================================
    # Normal attack calculations ===============================================
    comboTotal = Zhongli.Normal.mv

    if hasattr(weapon, "mvAdditive"):
        comboTotal += (weapon.mvAdditive * Zhongli.Normal.hits)

    # Buff additional damage
    normalBuffAddlDMG = Zhongli.Normal.hpConv * totalHP * Zhongli.Normal.hits

    normalDMG = 0
    if hasattr(artiset, "normalDMG"):
        normalDMG += artiset.normalDMG

    normalAttackDamage = ((totalATK * comboTotal) + normalBuffAddlDMG) * \
        (physMulti + normalDMG) * critMulti * Zhongli.Normal.rotations

    # Dominus Lapidis calculations =============================================
    eBuffAddlDMG = Zhongli.HoldE.hpConv * totalHP

    holdEDMG = ((totalATK * Zhongli.HoldE.mv) +
                (2*eBuffAddlDMG)) * critMulti * geoMulti

    eResoDamage = ((totalATK * Zhongli.EResonate.mv) +
                   eBuffAddlDMG) * critMulti * geoMulti

    eDamage = holdEDMG + (6 * eResoDamage)

    # Planet Befall calculations ===============================================
    qConversionDMG = totalHP * Zhongli.Q.hpConv

    burstDMG = 0
    if hasattr(artiset, "burstDMG"):
        burstDMG += artiset.burstDMG
    burstDMGMulti = burstDMG + 1

    qDamage = ((totalATK * Zhongli.Q.mv) + qConversionDMG) * \
        critMulti * geoMulti * burstDMGMulti

# * Outputs ====================================================================
    return {
        "ATK": totalATK,
        "HP": totalHP,
        "normalDMG": normalAttackDamage,
        "eDMG": eDamage,
        "qDMG": qDamage,
        "totalDMG": normalAttackDamage + eDamage + qDamage
    }


# Calling code
if __name__ == "__main__":
    artisets = [BloodstainedGlad, BloodstainedNoblesse,
                Bolide, Glad, GladNoblesse, PetraGlad, PetraNoblesse]

    weapons = [CrescentPike]

    artistats = {
        "sands": ["hp", "atk"],
        "cup": ["hp", "atk", "phys", "geo"],
        "helm": ["hp", "atk", "critRATE", "critDMG"]
    }

    for weapon in weapons:
        for artiset in artisets:
            for sandsIndex, sands in enumerate(artistats["sands"]):
                ArtifactStats.setSands(sandsIndex)
                for cupIndex, cup in enumerate(artistats["cup"]):
                    ArtifactStats.setCup(cupIndex)
                    for helmIndex, helm in enumerate(artistats["helm"]):
                        ArtifactStats.setHelm(helmIndex)

                        # Run calculations
                        damageData = doDamageCalc(weapon, artiset)
                        damageData["meta"] = {
                            "weapon": type(weapon).__name__,
                            "artifact set": type(artiset).__name__,
                            "sands": sands,
                            "cup": cup,
                            "helm": helm
                        }

                    print(damageData)

# ! Artifacts are never changed
# ! Need to add dunder methods for name or str
