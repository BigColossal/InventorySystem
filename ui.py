from inventory import Inventory

class UI:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.active = True

    def display_menu(self):
        print("1. See inventory")
        print("2. Create items")
        print("3. Create equipment")
        print("4. Equip equipment")
        print("5. Unequip Equipment")
        print("6. Remove item")
        print("7. Quit")

    def menu_choices_manager(self, choice):
        match choice:
            case 1: # See inventory
                print(self.inventory.displayFullInventory())
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
                print("Goodbye!")
                self.active = False

                
    def create_items(self):
        pass

    def create_equipment(self):
        pass

    def equip_equipment(self):
        pass

    def unequip_equipment(self):
        pass

    def remove_item(self):
        pass



    def ui_loop(self):
        print("Welcome to Jeremy's inventory system!")
        print("What would you like to do?\n")

        self.display_menu()