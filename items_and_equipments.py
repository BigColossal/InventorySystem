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

class itemTypes(Enum):
    Mineral = 1
    Crop = 2
    Potion = 3


class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Equipment(Item):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.equipped = False

equipmentStats = {
    equipmentTypes.Helmet: {
        "WoodenHelmet": {
            "description": "A helmet made of wood, forged in the amazon forests",
            "defense": 10,
        },
        "StoneHelmet": {
            "description": "A helmet carved from dense stone",
            "defense": 16,
        },
        "IronHelmet": {
            "description": "A sturdy helmet forged from iron",
            "defense": 24,
        },
        "SteelHelmet": {
            "description": "A reinforced steel helmet used by seasoned warriors",
            "defense": 34,
        },
        "MythrilHelmet": {
            "description": "A lightweight yet powerful helmet made of mythril",
            "defense": 48,
        },
    },

    equipmentTypes.Chestplate: {
        "WoodenChestPlate": {
            "description": "A chestplate made of wood, forged in the amazon forests",
            "defense": 24,
        },
        "StoneChestplate": {
            "description": "A heavy chestplate carved from solid stone",
            "defense": 36,
        },
        "IronChestplate": {
            "description": "A durable chestplate forged from iron",
            "defense": 52,
        },
        "SteelChestplate": {
            "description": "A battle-hardened steel chestplate",
            "defense": 70,
        },
        "MythrilChestplate": {
            "description": "A legendary mythril chestplate that feels light as air",
            "defense": 95,
        },
    },

    equipmentTypes.RightGlove: {
        "WoodenRightGlove": {
            "description": "A glove made of wood, designed for the right hand",
            "defense": 4,
        },
        "StoneRightGlove": {
            "description": "A rough stone glove for the right hand",
            "defense": 7,
        },
        "IronRightGlove": {
            "description": "An iron glove crafted for the right hand",
            "defense": 11,
        },
        "SteelRightGlove": {
            "description": "A steel glove built for combat",
            "defense": 16,
        },
        "MythrilRightGlove": {
            "description": "A mythril glove that enhances dexterity",
            "defense": 22,
        },
    },

    equipmentTypes.LeftGlove: {
        "WoodenLeftGlove": {
            "description": "A glove made of wood, designed for the left hand",
            "defense": 4,
        },
        "StoneLeftGlove": {
            "description": "A rough stone glove for the left hand",
            "defense": 7,
        },
        "IronLeftGlove": {
            "description": "An iron glove crafted for the left hand",
            "defense": 11,
        },
        "SteelLeftGlove": {
            "description": "A steel glove built for combat",
            "defense": 16,
        },
        "MythrilLeftGlove": {
            "description": "A mythril glove that enhances dexterity",
            "defense": 22,
        },
    },

    equipmentTypes.Leggings: {
        "WoodenLeggings": {
            "description": "Leggings made of wood, forged in the amazon forests",
            "defense": 18,
        },
        "StoneLeggings": {
            "description": "Heavy leggings carved from stone",
            "defense": 26,
        },
        "IronLeggings": {
            "description": "Iron leggings designed for battle",
            "defense": 38,
        },
        "SteelLeggings": {
            "description": "Steel leggings worn by elite soldiers",
            "defense": 52,
        },
        "MythrilLeggings": {
            "description": "Light mythril leggings with incredible protection",
            "defense": 70,
        },
    },

    equipmentTypes.Boots: {
        "WoodenBoots": {
            "description": "Boots made of wood, forged in the amazon forests",
            "defense": 6,
        },
        "StoneBoots": {
            "description": "Boots reinforced with stone plates",
            "defense": 10,
        },
        "IronBoots": {
            "description": "Iron boots made for endurance",
            "defense": 15,
        },
        "SteelBoots": {
            "description": "Steel boots worn by hardened adventurers",
            "defense": 22,
        },
        "MythrilBoots": {
            "description": "Mythril boots that allow swift movement",
            "defense": 30,
        },
    },

    equipmentTypes.Sword: {
        "WoodenSword": {
            "description": "A sword made of wood, forged in the amazon forests",
            "damage": 5,
            "attack speed": 10,
            "debuffs": "n/a"
        },
        "StoneSword": {
            "description": "A crude sword carved from stone",
            "damage": 8,
            "attack speed": 8,
            "debuffs": "n/a"
        },
        "IronSword": {
            "description": "A reliable sword forged from iron",
            "damage": 14,
            "attack speed": 9,
            "debuffs": "n/a"
        },
        "SteelSword": {
            "description": "A razor sharp steel sword",
            "damage": 20,
            "attack speed": 10,
            "debuffs": "bleed"
        },
        "MythrilSword": {
            "description": "A mystical sword made from mythril",
            "damage": 30,
            "attack speed": 12,
            "debuffs": "bleed"
        },
    },

    equipmentTypes.DualBlades: {
        "WoodenDualblades": {
            "description": "Dualblades made of wood",
            "damage": 3,
            "attack speed": 20,
            "debuffs": "n/a"
        },
        "IronDualblades": {
            "description": "Fast iron dual blades",
            "damage": 8,
            "attack speed": 24,
            "debuffs": "bleed"
        },
        "SteelDualblades": {
            "description": "Deadly steel dual blades",
            "damage": 12,
            "attack speed": 28,
            "debuffs": "bleed"
        },
    },

    equipmentTypes.Spear: {
        "WoodenSpear": {
            "description": "A spear made of wood",
            "damage": 7,
            "attack speed": 7,
            "debuffs": "n/a"
        },
        "IronSpear": {
            "description": "A sharp iron spear",
            "damage": 15,
            "attack speed": 8,
            "debuffs": "pierce"
        },
        "SteelSpear": {
            "description": "A deadly steel spear",
            "damage": 22,
            "attack speed": 9,
            "debuffs": "pierce"
        },
    },

    equipmentTypes.LongSword: {
        "WoodenLongSword": {
            "description": "A longsword made of wood",
            "damage": 10,
            "attack speed": 5,
            "debuffs": "n/a"
        },
        "IronLongSword": {
            "description": "A powerful iron longsword",
            "damage": 20,
            "attack speed": 6,
            "debuffs": "bleed"
        },
        "SteelLongSword": {
            "description": "A massive steel longsword",
            "damage": 30,
            "attack speed": 7,
            "debuffs": "bleed"
        },
    },

    equipmentTypes.Bow: {
        "WoodenBow": {
            "description": "A bow made of wood",
            "damage": 5,
            "attack speed": 10,
            "debuffs": "n/a"
        },
        "IronBow": {
            "description": "A reinforced iron bow",
            "damage": 12,
            "attack speed": 11,
            "debuffs": "pierce"
        },
        "SteelBow": {
            "description": "A powerful steel bow",
            "damage": 18,
            "attack speed": 12,
            "debuffs": "pierce"
        },
    },

    equipmentTypes.Wand: {
        "WoodenWand": {
            "description": "A wand carved from enchanted wood",
            "damage": 12,
            "attack speed": 4,
            "debuffs": "n/a"
        },
        "CrystalWand": {
            "description": "A wand with a glowing crystal core",
            "damage": 20,
            "attack speed": 5,
            "debuffs": "burn"
        },
        "ArcaneWand": {
            "description": "A wand infused with arcane energy",
            "damage": 32,
            "attack speed": 6,
            "debuffs": "burn"
        },
    },

    equipmentTypes.Accessory: {
        "Silver Ring": {
            "description": "A finely crafted silver ring",
            "defense": 10,
            "buffs": "n/a"
        },
        "Warrior Ring": {
            "description": "A ring that enhances strength",
            "defense": 4,
            "buffs": "attack+5"
        },
        "Guardian Amulet": {
            "description": "An amulet that increases protection",
            "defense": 15,
            "buffs": "defense+10"
        },
        "Swift Charm": {
            "description": "A charm that increases attack speed",
            "defense": 2,
            "buffs": "attack_speed+5"
        },
    },
}

itemDescriptions = {
    itemTypes.Mineral: {
        "Stone": {
            "description": "A common chunk of rough stone used in basic crafting."
        },
        "Coal": {
            "description": "A combustible black mineral often used as fuel."
        },
        "CopperOre": {
            "description": "A reddish ore that can be smelted into copper bars."
        },
        "IronOre": {
            "description": "A strong metal ore commonly used in weapons and armor."
        },
        "SilverOre": {
            "description": "A shiny ore prized for both crafting and trade."
        },
        "GoldOre": {
            "description": "A rare and valuable ore often used for high tier items."
        },
        "MythrilOre": {
            "description": "A legendary lightweight metal with incredible strength."
        },
        "Obsidian": {
            "description": "A dark volcanic glass known for its sharp edges."
        },
        "CrystalShard": {
            "description": "A magical fragment that radiates faint energy."
        },
        "Diamond": {
            "description": "An extremely rare gemstone known for its durability."
        }
    },

    itemTypes.Crop: {
        "Wheat": {
            "description": "A basic grain used to produce flour and bread."
        },
        "Corn": {
            "description": "A tall crop that produces sweet golden kernels."
        },
        "Potato": {
            "description": "A hearty root vegetable commonly used in many meals."
        },
        "Carrot": {
            "description": "A bright orange vegetable known for its sweetness."
        },
        "Tomato": {
            "description": "A juicy red fruit often used in cooking."
        },
        "Blueberry": {
            "description": "A small sweet berry packed with flavor."
        },
        "Pumpkin": {
            "description": "A large orange crop often harvested in autumn."
        },
        "Herbs": {
            "description": "A bundle of fragrant plants used in potions and cooking."
        },
        "MagicHerb": {
            "description": "A rare herb infused with natural magical properties."
        },
        "GoldenApple": {
            "description": "A mysterious fruit rumored to have restorative powers."
        }
    },

    itemTypes.Potion: {
        "HealthPotion": {
            "description": "A potion that restores a small amount of health."
        },
        "GreaterHealthPotion": {
            "description": "A stronger potion that restores more health."
        },
        "ManaPotion": {
            "description": "A potion that restores magical energy."
        },
        "StaminaPotion": {
            "description": "A potion that refreshes physical endurance."
        },
        "SpeedPotion": {
            "description": "A potion that temporarily increases movement speed."
        },
        "StrengthPotion": {
            "description": "A potion that temporarily increases attack power."
        },
        "DefensePotion": {
            "description": "A potion that temporarily boosts defense."
        },
        "RegenerationPotion": {
            "description": "A potion that slowly restores health over time."
        },
        "InvisibilityPotion": {
            "description": "A rare potion that briefly makes the drinker invisible."
        },
        "Antidote": {
            "description": "A potion that cures poison and negative toxins."
        }
    }
}

def getEquipmentStats(equipment):
    return equipmentStats[equipment.type][equipment.name]

def getItemDescription(item):
    return itemDescriptions[item.type][item.name]["description"]