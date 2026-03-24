from enum import Enum
from items_and_equipments import equipmentTypes, Item, Equipment, getEquipmentStats
from inventory import Inventory
from ui import UI


inv = Inventory()
ui = UI(inv)

def main():
    ui.ui_loop()

if __name__ == "__main__":
    main()