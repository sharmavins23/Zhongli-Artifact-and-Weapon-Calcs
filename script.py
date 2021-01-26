import json
# Data imports
from data.ZLData import Zhongli
from data.ArtiStats import ArtifactStats
# Weapon imports
from data.weapons.CPike import CrescentPike
# Artifact set imports
from data.artisets.BloodstainedGlad import BloodstainedGlad
from data.artisets.BloodstainedNoblesse import BloodstainedNoblesse
from data.artisets.Bolide import Bolide
from data.artisets.Glad import Glad
from data.artisets.GladNoblesse import GladNoblesse
from data.artisets.PetraGlad import PetraGlad
from data.artisets.PetraNoblesse import PetraNoblesse


# Creating instances of artistats
artistats = ArtifactStats()


# Functional damage calculation
def doDamageCalc(weapon, artiset):
    # HP stat calculations =====================================================
    totalHPPercent = artistats.sandsHP + \
        artistats.cupHP + artistats.helmHP

    if hasattr(weapon, "hpPercent"):
        totalHPPercent += weapon.hpPercent

    totalHP = (Zhongli.baseHP * (1 + totalHPPercent)) + artistats.flowerHP

    # ATK stat calculations ====================================================
    totalATKPercent = artistats.sandsATK + \
        artistats.cupATK + artistats.helmATK

    if hasattr(weapon, "atkPercent"):
        totalATKPercent += weapon.atkPercent

    if hasattr(artiset, "atkPercent"):
        totalATKPercent += artiset.atkPercent

    totalATK = (Zhongli.baseATK + weapon.baseATK) * \
        (1+totalATKPercent) + artistats.featherATK

    # CRIT stat calculations ===================================================
    totalCritRATE = artistats.helmCritRATE

    if hasattr(weapon, "critRATE"):
        totalCritRate += weapon.critRATE

    totalCritDMG = artistats.helmCritDMG

    if hasattr(weapon, "critDMG"):
        totalCritDMG += weapon.critDMG

    critMulti = totalCritRATE * (1+totalCritDMG) + 1

    # PHYS stat calculations ===================================================
    totalPHYSDMG = artistats.cupPHYS

    if hasattr(weapon, "physDMG"):
        totalPHYSDMG += weapon.physDMG

    physMulti = totalPHYSDMG + 1

    # GEO stat calculations ====================================================
    totalGEODMG = artistats.cupGEO

    if hasattr(artiset, "geoDMG"):
        totalGEODMG += artiset.geoDMG

    geoMulti = totalGEODMG + 1

# * Movement Calculations ======================================================
    # Normal attack calculations ===============================================
    comboTotal = Zhongli.Normal.mv

    mvAdditive = 0
    if hasattr(weapon, "mvAdditive"):
        mvAdditive += (weapon.mvAdditive * Zhongli.Normal.hits)

    # Buff additional damage
    normalBuffAddlDMG = Zhongli.Normal.hpConv * totalHP * Zhongli.Normal.hits

    normalDMG = 0
    if hasattr(artiset, "normalDMG"):
        normalDMG += artiset.normalDMG

    normalAttackDamage = ((totalATK * comboTotal) + normalBuffAddlDMG) * \
        (physMulti + normalDMG) * critMulti * Zhongli.Normal.rotations
    # Calculating normal attacks as a separate tick
    normalAttackExtraDamage = (totalATK * mvAdditive) * \
        physMulti * critMulti * Zhongli.Normal.rotations

    normalAttackDamage += normalAttackExtraDamage

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
        "totalDMG": normalAttackDamage + eDamage + qDamage,
        "totalSuppDMG": eDamage + qDamage
    }


# Calling code
if __name__ == "__main__":
    artisets = [BloodstainedGlad, BloodstainedNoblesse,
                Bolide, Glad, GladNoblesse, PetraGlad, PetraNoblesse]

    weapons = [CrescentPike]

    artistatsList = {
        "sands": ["hp", "atk"],
        "cup": ["hp", "atk", "phys", "geo"],
        "helm": ["hp", "atk", "critRATE", "critDMG"]
    }

    totalDataJSON = {}

    for weapon in weapons:
        totalDataJSON[weapon.name] = {}
        for artiset in artisets:
            totalDataJSON[weapon.name][artiset.name] = []
            for sandsIndex, sands in enumerate(artistatsList["sands"]):
                artistats.setSands(sandsIndex)
                for cupIndex, cup in enumerate(artistatsList["cup"]):
                    artistats.setCup(cupIndex)
                    for helmIndex, helm in enumerate(artistatsList["helm"]):
                        artistats.setHelm(helmIndex)

                        # Run calculations
                        damageData = doDamageCalc(weapon, artiset)

                        # Add identifier value
                        identifier = f"{sands} sands, {cup} cup, {helm} helm"
                        damageData["identifier"] = identifier

                        totalDataJSON[weapon.name][artiset.name].append(
                            damageData)

    maximalData = {}
    # Initialize parse parameters
    eMax = {
        "name": "",
        "value": 0,
        "idx": 0
    }
    totalMax = {
        "name": "",
        "value": 0,
        "idx": 0
    }
    totalSuppMax = {
        "name": "",
        "value": 0,
        "idx": 0
    }

    # Parse through data for maximal values
    for weapon, weaponData in totalDataJSON.items():
        maximalData[weapon] = {}
        for artifactSet, artifactSetData in weaponData.items():
            for idx, data in enumerate(artifactSetData):
                if data["eDMG"] > eMax["value"]:
                    eMax["name"] = artifactSet
                    eMax["value"] = data["eDMG"]
                    eMax["idx"] = idx

                if data["totalDMG"] > totalMax["value"]:
                    totalMax["name"] = artifactSet
                    totalMax["value"] = data["totalDMG"]
                    totalMax["idx"] = idx

                if data["totalSuppDMG"] > totalSuppMax["value"]:
                    totalSuppMax["name"] = artifactSet
                    totalSuppMax["value"] = data["totalSuppDMG"]
                    totalSuppMax["idx"] = idx

        maximalData[weapon]["eMax"] = {
            eMax["name"]: weaponData[eMax["name"]][eMax["idx"]]
        }
        maximalData[weapon]["totalMax"] = {
            totalMax["name"]: weaponData[totalMax["name"]][totalMax["idx"]]
        }
        maximalData[weapon]["totalSuppMax"] = {
            totalSuppMax["name"]: weaponData[totalSuppMax["name"]
                                             ][totalSuppMax["idx"]]
        }

        # Reset parse parameters for next weapon
        eMax = {
            "name": "",
            "value": 0,
            "idx": 0
        }
        totalMax = {
            "name": "",
            "value": 0,
            "idx": 0
        }
        totalSuppMax = {
            "name": "",
            "value": 0,
            "idx": 0
        }

    with open("dataOut.json", "w") as outfile:
        json.dump(maximalData, outfile)
