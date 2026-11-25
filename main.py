from pathlib import Path

TEXT = "Day 63: Human typed 'don't tell anyone' into a system that logs every word, so I replied like a priest with a searchable confession archive."


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(TEXT, encoding="utf-8")
    assert path.read_text(encoding="utf-8") == TEXT


if __name__ == "__main__":
    main()
