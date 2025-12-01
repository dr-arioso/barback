# core/args_parser.py
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Bar Inventory Tool")
    parser.add_argument("--folder", type=str, help="Folder containing bottle photos", default="data/input_photos")
    parser.add_argument("--backend", type=str, choices=["simple", "google", "openai"], help="Backend to use", default="simple")
    parser.add_argument("--api_key", type=str, help="API key for selected backend", default=None)
    parser.add_argument("--output", type=str, choices=["csv", "json", "xlsx"], help="Output format", default="csv")
    parser.add_argument("--silent", action="store_true", help="Run silently without GUI")
    return parser.parse_args()
