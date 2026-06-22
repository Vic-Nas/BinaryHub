from pathlib import Path

ENGINES_DIR = Path(__file__).resolve().parent / "engines"
REQUIRED_ENGINES = ("BitCrack.exe", "hashcat.exe")


def missing_engines() -> list[str]:
    return [name for name in REQUIRED_ENGINES if not (ENGINES_DIR / name).is_file()]


def main() -> int:
    missing = missing_engines()
    if missing:
        print("Missing engine files:", ", ".join(missing))
        return 1

    print("All required engine files are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
