# bar_back.py
from core.args_parser import parse_args
from interface import cli, gui

def main():
    args = parse_args()
    # If CLI has all required args and/or silent -> run CLI
    if args.silent or (args.folder and args.backend and args.output):
        cli.run(args)
    else:
        gui.launch(args)


if __name__ == "__main__":
    main()
