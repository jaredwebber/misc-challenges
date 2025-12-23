from pathlib import Path
import math
import operator

PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / "test.txt"
file_content = path.read_text()
lines = file_content.splitlines()

def part_one() -> None:
    coords = []

    for line in lines:
        x, y, z = line.split(",")
        coords.append([int(x), int(y), int(z)])
        
    link_map: dict[list, list] = {}

    for i in coords:
        link_map[i] = []

    # link up to 1000 pairs (or 10 for test file)

    

    



