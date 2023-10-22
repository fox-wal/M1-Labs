import os

FILENAME = "pride-and-prejudice.txt"
PATH = os.path.dirname(os.path.abspath(FILENAME))

try:
    file = open(FILENAME, "r", encoding="UTF-8")
    chapter_count = 0
    for line in file.readlines():
        if line.lower().__contains__("chapter"):
            chapter_count += 1

    print("Chapters:", chapter_count)
except OSError:
    print("File not found.")