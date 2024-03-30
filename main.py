import math

multiplier = 4

lvl = 1
exp = 0
neededExp = math.floor(math.log2(lvl ** multiplier) + lvl)
skillPoints = 0

def levelUp():
    global exp, neededExp, lvl
    neededExp = math.floor(math.log2(lvl ** multiplier) + lvl)
    previous_lvl = lvl
    gotten_vl = lvl
    did_level_up = False
    while exp >= neededExp:
        lvl += 1
        gotten_vl = lvl
        exp -= neededExp
        did_level_up = True

        neededExp = math.floor(math.log2(lvl ** multiplier) + lvl)

    if did_level_up:
        print(f"===== Level UP! ===== ")
        print(f"Level Up! {previous_lvl} -> {gotten_vl}")
        print(f"Exp: {exp}/{neededExp}")
        print(f"===================== ")

def addExp(amount):
    global exp
    exp += amount

while True:
    levelUp()
    print(f"Level: {lvl}, Exp: {exp}/{neededExp}")
    addExp(int(input("Add Exp: ")))


