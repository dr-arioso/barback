
def select_from_list(prompt: str, options: list):
    """
    Simple terminal-based selection for interactive prompts.
    Returns selected value or None if canceled.
    """
    print(prompt)
    for idx, opt in enumerate(options, start=1):
        print(f"{idx}: {opt}")
    print("0: Cancel / Enter manually")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        return None
    if choice == 0:
        return None
    if 1 <= choice <= len(options):
        return options[choice - 1]
    return None
