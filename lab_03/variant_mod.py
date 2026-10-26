def search_component(inventory_dict, item_name):
    return inventory_dict.get(item_name)

def get_low_stock(inventory_dict, min_qty):
    low_stock_list = []
    for item in inventory_dict:
        info = inventory_dict[item]
        qty = info[0]
        if qty < min_qty:
            low_stock_list.append((item,qty))
    return low_stock_list

def get_storage_zones(inventory_dict):
    zones = set()
    for item in inventory_dict:
        info = inventory_dict[item]
        zone = info[1]
        zones.add(zone)

    return zones