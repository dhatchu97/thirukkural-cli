#!/usr/bin/env python3

import json
import random
import argparse

# Load the JSON data
with open("thirukkural.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def get_random_kural():
    return random.choice(data["kural"])


def display_kural(kural, show_explanation, show_porul, show_transliteration):
    print(f"\nThirukkural #{kural['Number']}:")
    print(f"{kural['Line1']}\n{kural['Line2']}\n")

    if show_explanation:
        print(f"**Explanation:** {kural['explanation']}\n")

    if show_porul:
        print(f"**Porul (Tamil):** {kural['sp']}\n")

    if show_transliteration:
        print(f"**Transliteration:**\n{kural['transliteration1']}\n{kural['transliteration2']}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get a random Thirukkural with options.")
    parser.add_argument("-e", "--explanation", action="store_true", help="Show explanation in English")
    parser.add_argument("-p", "--porul", action="store_true", help="Show porul in Tamil")
    parser.add_argument("-t", "--transliteration", action="store_true", help="Show transliteration")

    args = parser.parse_args()

    kural = get_random_kural()
    display_kural(kural, args.explanation, args.porul, args.transliteration)
