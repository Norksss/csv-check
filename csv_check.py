"""Report CSV structure problems without changing the source file."""
import argparse
import csv
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    args = parser.parse_args()
    problems = 0
    try:
        with open(args.file, newline="", encoding="utf-8-sig") as source:
            rows = csv.reader(source, strict=True)
            header = next(rows, None)
            if not header:
                print("File is empty or has no header.")
                return 1
            names = [name.strip().casefold() for name in header]
            if any(not name for name in names):
                print("Header contains unnamed columns.")
                problems += 1
            if len(names) != len(set(names)):
                print("Header contains duplicate column names.")
                problems += 1
            count = 0
            for count, row in enumerate(rows, 1):
                if len(row) != len(header):
                    print(f"Record {count + 1}: expected {len(header)} fields, got {len(row)}.")
                    problems += 1
            print(f"Checked {count} data records; found {problems} problems.")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Cannot check file: {error}", file=sys.stderr)
        return 2
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
