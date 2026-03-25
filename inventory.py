class Inventory:
    """
    Inventory system that reads and edits an inventory file
    """
    equippedLineStarter = "equipped"
    inventoryLineCapacity = 8
    EQUIP_STRING_TEMPLATE = "equipped Helmet:None Chestplate:None Leggings:None RightGlove:None LeftGlove:None Boots:None Sword:None LongSword:None DualBlades:None Spear:None Bow:None Wand:None Accessory1:None Accessory2:None Accessory3:None\n"

    def __init__(self):
        self.__items = {}
        self.__equipped = {}
        self.needsUpdate = True

    def displayFullInventory(self):
        items = self.getItems()
        equipped = self.getEquipped()

        result = "Inventory:\n"
        for name, amt in items.items():
            result += f"{name}: {amt}\n"

        result += "\nEquipped:\n"
        for slot, item in equipped.items():
            result += f"{slot}: {item}\n"

        return result

    def createInventoryFile(self):
        with open("inventory.txt", "w") as f:
            f.write(Inventory.EQUIP_STRING_TEMPLATE)

    def getItems(self) -> dict:
        if not self.needsUpdate:
            return self.__items

        self.__items = {}

        lines = self.readInventoryContents()

        for line in lines:
            if line.startswith(Inventory.equippedLineStarter):
                continue

            items = [x for x in line.strip().split(",") if x]

            for item in items:
                name, amount = item.split()
                self.__items[name] = int(amount)

        self.needsUpdate = False
        return self.__items

    def updateItems(self, newItems: list):
        lines = self.readInventoryContents()

        for i, line in enumerate(lines):
            if line.startswith(Inventory.equippedLineStarter):
                continue

            items = [x for x in line.strip().split(",") if x]
            updated_items = []

            for item in items:
                name, amount = item.split()
                amount = int(amount)

                match = next((x for x in newItems if x[0].name == name), None)

                if match:
                    amount += match[1]
                    newItems.remove(match)

                updated_items.append(f"{name} {amount}")

            items = updated_items

            space = Inventory.inventoryLineCapacity - len(items)

            if space <= 0:
                continue

            itemsToAdd = newItems[:space]
            newItems = newItems[space:]

            items.extend(f"{x[0].name} {x[1]}" for x in itemsToAdd)

            lines[i] = ",".join(items) + ",\n"

            if not newItems:
                break

        while newItems:
            itemsToAdd = newItems[:Inventory.inventoryLineCapacity]
            newItems = newItems[Inventory.inventoryLineCapacity:]

            line = ",".join(f"{x[0].name} {x[1]}" for x in itemsToAdd) + ",\n"
            lines.append(line)

        with open("inventory.txt", "w") as f:
            f.writelines(lines)

        self.needsUpdate = True

    def removeItems(self, item, amt):
        lines = self.readInventoryContents()

        for i, line in enumerate(lines):
            if line.startswith(Inventory.equippedLineStarter):
                continue

            items = [x for x in line.strip().split(",") if x]
            updated = []

            for entry in items:
                name, amount = entry.split()
                amount = int(amount)

                if name == item:
                    amount -= amt
                    if amount <= 0:
                        continue

                updated.append(f"{name} {amount}")

            lines[i] = ",".join(updated) + ",\n"

        with open("inventory.txt", "w") as f:
            f.writelines(lines)

        self.needsUpdate = True

    def readInventoryContents(self):
        try:
            with open("inventory.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.createInventoryFile()
            with open("inventory.txt", "r") as f:
                lines = f.readlines()

        return lines

    def getEquipped(self):
        if not self.needsUpdate:
            return self.__equipped

        equipString, _ = self.getEquipString()

        self.__equipped = {}

        for pair in equipString[1:]:  # skip "equipped"
            slot, item = pair.split(":")
            self.__equipped[slot] = item

        return self.__equipped

    def updateEquipped(self, equipments):
        newEquipString, inv = self.getEquipString()
        newEquipString = [x.split(":") for x in newEquipString]

        for e in equipments:
            if not e.equipped:
                index = e.type.value
                newEquipString[index][1] = e.name
                e.equipped = True

        finalString = " ".join(":".join(x) for x in newEquipString)

        items = "".join(inv[1:]) if len(inv) > 1 else ""

        with open("inventory.txt", "w") as f:
            f.write(finalString + "\n")
            f.write(items)

        self.needsUpdate = True

    def getEquipString(self):
        try:
            with open("inventory.txt", "r") as f:
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
        newEquipString = [x.split(":") for x in newEquipString]

        index = equipment_type.value
        newEquipString[index][1] = "None"

        finalString = " ".join(":".join(x) for x in newEquipString)
        inv[0] = finalString + "\n"

        with open("inventory.txt", "w") as f:
            f.writelines(inv)

        self.needsUpdate = True