import re
text = "The quick brown fox jumps over the lazy dog."
match = re.search(r"fox", text)
if match:
    print(f"Match found: {match.group()}"
    