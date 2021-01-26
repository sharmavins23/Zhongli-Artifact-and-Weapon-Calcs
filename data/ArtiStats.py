# Data class for artifact stats
class ArtifactStats:
    level = 20

    # TODO: Sanity check lists for sum values or somehow otherwise refactor

    def __init__(self):
        self.sandsChoice = [1, 0]
        self.cupChoice = [1, 0, 0, 0]
        self.helmChoice = [1, 0, 0, 0]
        self.sandsHP = 0
        self.sandsATK = 0
        self.cupHP = 0
        self.cupATK = 0
        self.cupPHYS = 0
        self.cupGEO = 0
        self.helmHP = 0
        self.helmATK = 0
        self.helmCritRATE = 0
        self.helmCritDMG = 0

    # Setters for sands, cup, and helm choice
    def setSands(self, choice):
        self.sandsChoice = [0] * 2
        self.sandsChoice[choice] = 1

        self.sandsHP = 0.4660 * self.sandsChoice[0]
        self.sandsATK = 0.4660 * self.sandsChoice[1]

    def setCup(self, choice):
        self.cupChoice = [0] * 4
        self.cupChoice[choice] = 1

        self.cupHP = 0.4660 * self.cupChoice[0]
        self.cupATK = 0.4660 * self.cupChoice[1]
        self.cupPHYS = 0.5830 * self.cupChoice[2]
        self.cupGEO = 0.4660 * self.cupChoice[3]

    def setHelm(self, choice):
        self.helmChoice = [0] * 4
        self.helmChoice[choice] = 1

        self.helmHP = 0.4660 * self.helmChoice[0]
        self.helmATK = 0.4660 * self.helmChoice[1]
        self.helmCritRATE = 0.3110 * self.helmChoice[2]
        self.helmCritDMG = 0.6220 * self.helmChoice[3]

    # Static stat configurations
    flowerHP = 4780
    featherATK = 311
