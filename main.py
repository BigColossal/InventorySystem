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
    
EQUIP_STRING_TEMPLATE = "equipped Helmet:None Chestplate:None Leggings:None RightGlove:None LeftGlove:None Boots:None Sword:None LongSword:None DualBlades:None Spear:None Bow:None Wand:None Accessory1:None Accessory2:None Accessory3:None"

class Inventory:
    """
    Inventory system that reads and edits an inventory file
    """
    equippedLineStarter = "equipped"
    inventoryLineCapacity = 8
    def __init__(self):
        self.__items = {}
        self.__equipped = {}
        self.needsUpdate = True

    def displayFullInventory(self) -> None:
        pass

    def createInventoryFile(self):
        with open("inventory.txt", "w") as f:
            f.write(EQUIP_STRING_TEMPLATE)
        
    def getItems(self) -> dict:
        """
        items getter 
        """

        if not self.needsUpdate:
            return self.__items
        else:
                try:
                    with open("inventory.txt", 'r') as f:
                        lines = f.readlines()
                except FileNotFoundError:
                    self.createInventoryFile()
                    with open("inventory.txt", "r") as f:
                        lines = f.readlines()

                for line in lines:
                    if line[0:len(Inventory.equippedLineStarter)] == Inventory.equippedLineStarter:
                        continue
                    else:
                        # line looks like this: "LargePotion 3,Iron 100,RawHide 20"
                        # So we split the line by commas and then with each item pair we make them 
                        # an array with the name being the first item and the amount being the second
                        items = list(map(lambda item: item.split(), line.split(",")))

                        # for each item (Ex: LargePotion 3), set name and their 
                        for item in items:
                            self.__items[item[0]] = item[1]
                return self.__items

    def updateItems(self, newItems: list):
        """
        Update items within inventory.txt
        """

        try:
            with open("inventory.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.createInventoryFile()
            with open("inventory.txt", "r") as f:
                lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith(Inventory.equippedLineStarter):
                continue

            items = [x for x in line.strip().split(",") if x]

            space = Inventory.inventoryLineCapacity - len(items)

            if space <= 0:
                continue

            itemsToAdd = newItems[:space]
            newItems = newItems[space:]

            items.extend(f"{x[0]} {x[1]}" for x in itemsToAdd)

            lines[i] = ",".join(items) + ",\n"

            if not newItems:
                break

        # create new lines if items still remain
        while newItems:
            itemsToAdd = newItems[:Inventory.inventoryLineCapacity]
            newItems = newItems[Inventory.inventoryLineCapacity:]

            line = ",".join(f"{x[0]} {x[1]}" for x in itemsToAdd) + ",\n"
            lines.append(line)

        with open("inventory.txt", "w") as f:
            f.writelines(lines)

    def removeItems(self, item, amt):
        pass

    def getEquipped(self):
        pass

    def updateEquipped(self, equipments):
        newEquipString, inv = self.getEquipString()
        newEquipString = list(map(lambda x: x.split(":"), newEquipString))
        for e in equipments:
            newEquipString[e.type.value][1] = e.name
        finalString = "equipped " + " ".join(list(map(lambda x: ":".join(x), newEquipString)))

        if inv[1:]:
            items = inv[1:]
        else:
            items = ""
        with open("inventory.txt", 'w') as f:
            f.write(f"{finalString}\n{items}")

    def getEquipString(self):
        try:
            with open("inventory.txt", 'r') as f:
                inventory = f.readlines()
                newEquipString = inventory[0].split()
        except FileNotFoundError:
            self.createInventoryFile()
            with open("inventory.txt", "r") as f:
                inventory = f.readlines()
                newEquipString = inventory[0].split()
        return newEquipString, inventory

    def removeEquipped(self, equipment_type):
        newEquipString, inv = self.getEquipString()

class Item:
    def __init__(self, name):
        self.name = name

class Equipment(Item):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


inv = Inventory()
TestE1 = Equipment("Drako", equipmentTypes.Bow)
TestE2 = Equipment("Blit", equipmentTypes.Spear)

def main():
    pass

if __name__ == "__main__":
    main()

                        

