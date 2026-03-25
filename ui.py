from inventory import Inventory
from items_and_equipments import (
    itemTypes,
    equipmentTypes,
    createItem,
    createEquipment,
    getEquipmentStats,
    getItemDescription
)


class UI:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.active = True

    def display_menu(self):
        print("\nWhat would you like to do?\n")
        print("1. See inventory")
        print("2. Create items")
        print("3. Create equipment")
        print("4. Equip equipment")
        print("5. Unequip equipment")
        print("6. Remove item")
        print("7. Inspect Item/Equipment")
        print("8. Quit")

    def menu_choices_manager(self, choice):
        match choice:
            case 1:
                self.see_inventory()

            case 2:
                self.create_items()

            case 3:
                self.create_equipment()

            case 4:
                self.equip_equipment()

            case 5:
                self.unequip_equipment()

            case 6:
                self.remove_item()

            case 7:
                self.inspect_item()

            case 8:
                print("Goodbye!")
                self.active = False

            case _:
                print("Invalid choice.")

    # ---------------------

    def see_inventory(self):
        items = self.inventory.getItems()
        equipped = self.inventory.getEquipString()[0]

        print("\n===== INVENTORY =====")
        for name, amt in items.items():
            print(f"{name}: {amt}")

        print("\n===== EQUIPPED =====")
        for e in equipped:
            print(e)

    # ---------------------

    def create_items(self):
        print("\nWhat type of item would you like to create?")
        print("1. Mineral")
        print("2. Crop")
        print("3. Potion")

        choice = int(input("> "))

        type_map = {
            1: itemTypes.Mineral,
            2: itemTypes.Crop,
            3: itemTypes.Potion
        }

        if choice not in type_map:
            print("Invalid type.")
            return

        item_type = type_map[choice]

        from items_and_equipments import itemDescriptions
        available = itemDescriptions[item_type]

        print("\nAvailable items:")
        for name in available:
            print("-", name)

        name = input("\nItem name: ")
        amount = int(input("Amount: "))

        try:
            item = createItem(name)
            self.inventory.updateItems([(item, amount)])
            print("Item added to inventory.")
        except ValueError as e:
            print(e)

    # ---------------------

    def create_equipment(self):
        print("\nSelect equipment type:\n")

        for e in equipmentTypes:
            print(f"{e.value}. {e.name}")

        choice = int(input("> "))

        try:
            equip_type = equipmentTypes(choice)
        except ValueError:
            print("Invalid type.")
            return

        from items_and_equipments import equipmentStats

        print("\nAvailable equipment:\n")

        for name in equipmentStats[equip_type]:
            print("-", name)

        name = input("\nEquipment name: ")

        try:
            equipment = createEquipment(name)
            self.inventory.updateItems([(equipment, 1)])
            print("Equipment created and added to inventory.")
        except ValueError as e:
            print(e)

    # ---------------------

    def equip_equipment(self):
        name = input("Equipment name to equip: ")

        try:
            equipment = createEquipment(name)
            self.inventory.updateEquipped([equipment])
            print("Equipped successfully.")
        except ValueError:
            print("Invalid equipment.")

    # ---------------------

    def unequip_equipment(self):
        print("\nSelect equipment slot to remove:\n")

        for e in equipmentTypes:
            print(f"{e.value}. {e.name}")

        try:
            choice = int(input("> "))
            equip_type = equipmentTypes(choice)

            self.inventory.removeEquipped(equip_type)

            print("Equipment removed.")

        except ValueError:
            print("Invalid slot.")

    # ---------------------

    def remove_item(self):
        name = input("Item name to remove: ")
        amount = int(input("Amount: "))

        from items_and_equipments import createItem

        try:
            item = createItem(name)
            self.inventory.removeItems(item, amount)
            print("Item removed.")
        except:
            print("Invalid item.")

    # ---------------------

    def inspect_item(self):
        name = input("Item/equipment name: ")

        from items_and_equipments import createItem, createEquipment

        try:
            item = createItem(name)
            desc = getItemDescription(item)
            print(f"\n{name}")
            print(desc)
            return
        except:
            pass

        try:
            equip = createEquipment(name)
            stats = getEquipmentStats(equip)

            print(f"\n{name}")
            for k, v in stats.items():
                print(f"{k}: {v}")

        except:
            print("Item not found.")

    # ---------------------

    def ui_loop(self):
        print("Welcome to Jeremy's inventory system!")

        while self.active:
            self.display_menu()

            try:
                choice = int(input("\n> "))
                self.menu_choices_manager(choice)
            except:
                print("Invalid input.")