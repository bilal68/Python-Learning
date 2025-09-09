# file: app.py
from __future__ import annotations
import argparse
import csv
from pathlib import Path

BOOK_FILE = Path("address_book.txt")

# ---------- Shared helpers ----------
def file_exists(path: str | Path) -> bool:
    return Path(path).exists()

# ---------- Mode 1: Grades from CSV ----------
def calculate_student_averages(csv_path: str) -> dict[str, float]:
    averages: dict[str, float] = {}
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row_num, row in enumerate(reader, start=1):
            if not row:
                continue
            name = row[0].strip()
            if not name:
                print(f"Skipping row {row_num}: no name.")
                continue
            grades = []
            for cell in row[1:]:
                cell = cell.strip()
                if not cell:
                    continue
                try:
                    grades.append(float(cell))
                except ValueError:
                    # ignore non-numeric cells
                    pass
            averages[name] = (sum(grades) / len(grades)) if grades else float("nan")
    return averages

def run_grades(csv_path: str) -> None:
    if not file_exists(csv_path):
        print(f"Error: '{csv_path}' not found.")
        return
    avgs = calculate_student_averages(csv_path)
    for name, avg in avgs.items():
        if avg == avg:  # NaN check
            print(f"{name}: {avg:.2f}")
        else:
            print(f"{name}: No numeric grades")

# ---------- Mode 2: Text-based Address Book ----------
def add_contact(name: str, phone: str) -> None:
    with open(BOOK_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name}\t{phone}\n")
    print(f"Saved: {name} -> {phone}")

def search_contacts(query: str) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    if not file_exists(BOOK_FILE):
        return results
    with open(BOOK_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t", maxsplit=1)
            if len(parts) != 2:
                continue
            name, phone = parts
            if query.lower() in name.lower() or query.lower() in phone.lower():
                results.append((name, phone))
    return results

def run_addressbook() -> None:
    while True:
        print("\nAddress Book")
        print("1) Add contact")
        print("2) Search contacts")
        print("3) Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                add_contact(name, phone)
            else:
                print("Name and phone are required.")
        elif choice == "2":
            q = input("Search query: ").strip()
            hits = search_contacts(q)
            if not hits:
                print("No matches found.")
            else:
                print("\nMatches:")
                for n, p in hits:
                    print(f"- {n}: {p}")
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try 1, 2, or 3.")

# ---------- CLI ----------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Grades & Address Book utility")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_grades = sub.add_parser("grades", help="Read CSV and print average grades")
    p_grades.add_argument("csv_path", help="Path to students CSV file")

    sub.add_parser("addressbook", help="Interactive address book (add/search)")
    return p

def main() -> int:
    args = build_parser().parse_args()
    if args.cmd == "grades":
        run_grades(args.csv_path)
    elif args.cmd == "addressbook":
        run_addressbook()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
