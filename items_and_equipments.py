from enum import Enum

class equipmentTypes(Enum):
    Helmet = 1
    Chestplate = 2
    Leggings = 3
    RightGlove = 4
    LeftGlove = 5
    Boots = 6
    Sword = 7
    LongSword = 8
    DualBlades = 9
    Spear = 10
    Bow = 11
    Wand = 12
    Accessory = 13

class Item:
    def __init__(self, name):
        self.name = name

class Equipment(Item):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
        self.equipped = False

equipmentStats = {
    equipmentTypes.Helmet: {
        "WoodenHelmet": {
            "description": "A helmet made of wood, forged in the amazon forests",
            "defense": 10,
        }
    },
    equipmentTypes.Chestplate: {

    },
    equipmentTypes.RightGlove: {

    },
    equipmentTypes.LeftGlove: {

    },
    equipmentTypes.Leggings: {

    },
    equipmentTypes.Boots: {

    },
    equipmentTypes.Sword: {

    },
    equipmentTypes.DualBlades: {

    },
    equipmentTypes.Spear: {

    },
    equipmentTypes.LongSword: {

    },
    equipmentTypes.Bow: {

    },
    equipmentTypes.Wand: {

    },
    equipmentTypes.Accessory: {

    },
}

itemDescriptions = {
    
}

def getEquipmentStats(equipment):
    pass