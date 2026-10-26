#main.py
import sys
from variant_mod import(get_storage_zones,get_low_stock)

def main():
    if len(sys.argv) > 1:
        min_qty = int(sys.argv[1])
    else:
        min_qty = 50

    inventory = {'Resistor 10k': (120, 'Zone-A'),
                 'Capacitor 100uF': (30, 'Zone-B'),
                 'Microcontroller': (15, 'Zone-A'),
                 'Relay 12V': (80, 'Zone-C')
    }

    deficite_items = get_low_stock(inventory, min_qty)
    storage_zones = get_storage_zones(inventory)

    print("=== УЧЕТ АВТОМАТИЗИРОВАННОГО СКЛАДА ===")
    print("Дефицитные детали (< " + str(min_qty) +" шт):", deficite_items)
    print("Буквенные зоны хранения (set):", storage_zones)

if __name__ == "__main__":
    main()