import os
from ship_types import SHIP_TYPES


def clear_screen():
    os.system("cls")


def get_ship_type_description(type_code):
    return SHIP_TYPES.get(type_code, "Ukjent typekode")


def print_ship_table(ships):
    clear_screen()
    print("What is that ship?")
    print(f"{'SHIPNAME':<15} | {'TYPE':<15} | {'DESTINATION':<15}")
    for _, details in ships.items():
        print(
            f"{details['Name']:<15} | {details['Type']:<15} | {details['Destination']:<15}"
        )
