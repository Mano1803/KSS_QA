import re
import os


with open("regex_check.txt", "r", encoding="utf-8") as f:
    content = f.read()


data_dict = {}
pattern = re.compile(r"^([\w\s()/\-]+):\s+(.+)$", re.MULTILINE)

for match in pattern.finditer(content):
    key = match.group(1).strip()
    value = match.group(2).strip()
    data_dict[key] = value


filename = None
file_pattern = re.compile(r'System image file is\s+"?(.+?)"?$', re.IGNORECASE | re.MULTILINE)

match = file_pattern.search(content)
if match:
    full_path = match.group(1).strip()
    filename = os.path.basename(full_path)


print("Parsed Dictionary:")
for k, v in data_dict.items():
    print(f"{k}: {v}")

print("\nFilename from system image file:", filename)
