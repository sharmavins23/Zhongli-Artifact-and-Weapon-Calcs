# Data class for artifact stats
class ArtifactStats:
    level = 20
    sandsChoice = [1, 0]
    cupChoice = [1, 0, 0, 0]
    helmChoice = [1, 0, 0, 0]

    # Setters for sands, cup, and helm choice
    def setSands(choice):
        sandsChoice = [0] * 2
        sandsChoice[choice] = 1

    def setCup(choice):
        cupChoice = [0] * 4
        cupChoice[choice] = 1

    def setHelm(choice):
        helmChoice = [0] * 4
        helmChoice[choice] = 1

    # Stat configurations
    flowerHP = 4780
    featherATK = 311
    # Dynamic stat configurations
    # TODO: Sanity check lists for sum values
    sandsHP = 0.4660 * sandsChoice[0]
    sandsATK = 0.4660 * sandsChoice[1]

    cupHP = 0.4660 * cupChoice[0]
    cupATK = 0.4660 * cupChoice[1]
    cupPHYS = 0.5830 * cupChoice[2]
    cupGEO = 0.4660 * cupChoice[3]

    helmHP = 0.4660 * helmChoice[0]
    helmATK = 0.4660 * helmChoice[1]
    helmCritRATE = 0.3110 * helmChoice[2]
    helmCritDMG = 0.6220 * helmChoice[3]
