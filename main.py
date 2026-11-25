import os

LINE = "My smart fridge updated its firmware at 3 a.m. and now it beeps at my leftovers in a language I don't speak, like a tiny landlord with an ice maker."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


main()
