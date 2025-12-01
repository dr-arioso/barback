import json
from pathlib import Path
from typing import Optional

BRANDS_FILE = Path("data/brands.json")

def load_brands() -> list:
    if BRANDS_FILE.exists():
        try:
            with open(BRANDS_FILE,"r",encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_brands(brand_list: list):
    BRANDS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(BRANDS_FILE,"w",encoding="utf-8") as f:
        json.dump(sorted(set(brand_list)), f, indent=2)

def fuzzy_match(input_text:str, brand_list:list, threshold:float=80.0)->Optional[str]:
    try:
        from rapidfuzz import process
    except ImportError:
        return None
    if not brand_list:
        return None
    match = process.extractOne(input_text, brand_list)
    if match and match[1]>=threshold:
        return match[0]
    return None

def resolve_brand(text:str, silent:bool=False)->Optional[str]:
    brand_list = load_brands()
    candidate = fuzzy_match(text, brand_list)
    if candidate:
        return candidate
    if not silent:
        print(f"Could not confidently match brand from text: '{text}'")
        print("Select a brand from known list or enter new:")
        for idx,b in enumerate(brand_list,start=1):
            print(f"{idx}: {b}")
        print("0: Enter new brand")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            choice = 0
        if choice==0:
            new_brand = input("Enter new brand name: ").strip()
            if new_brand:
                brand_list.append(new_brand)
                save_brands(brand_list)
                return new_brand
            return None
        elif 1<=choice<=len(brand_list):
            return brand_list[choice-1]
        return None
    else:
        new_brand = text.strip()
        if new_brand:
            brand_list.append(new_brand)
            save_brands(brand_list)
            return new_brand
        return None
