# pypi_name_check.py
import requests

CANDIDATES = [
    "Curio", "Trinket", "ThingKit", "Squirrel", "Magpie", 
    "Packrat", "Magpy", "Sqrrl", "Sqyrrl", "StashKit", 
    "StashThing", "StashBot"
]

PYPI_SEARCH_URL = "https://pypi.org/pypi"

def check_name(name: str):
    """Check if name exists exactly or partially on PyPI."""
    results = {"exact": False, "partial": []}
    
    # Exact check
    exact_url = f"{PYPI_SEARCH_URL}/{name}/json"
    resp = requests.get(exact_url)
    if resp.status_code == 200:
        results["exact"] = True
    
    # Partial search
    search_url = f"https://pypi.org/search/?q={name}"
    try:
        r = requests.get(search_url, timeout=5)
        if r.ok:
            text = r.text.lower()
            # crude partial check: look for the candidate in returned page
            matches = [line for line in text.splitlines() if name.lower() in line]
            results["partial"] = matches[:5]  # show first 5 hits
    except Exception:
        results["partial"] = []
    
    return results

def main():
    for candidate in CANDIDATES:
        res = check_name(candidate)
        print(f"--- {candidate} ---")
        print("Exact match on PyPI:", res["exact"])
        if res["partial"]:
            print(f"Partial matches (first 5): {res['partial']}")
        else:
            print("No obvious partial matches found.")
        print()

if __name__ == "__main__":
    main()
