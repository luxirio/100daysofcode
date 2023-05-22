import re

text_strings = [
    "$2,799+ 1 bd",
    "$945",
    "$2,960/mo",
    "$2,395+/mo",
    "$1,995+/mo",
    "$2,416+ 1 bd",
    "$2,295+ 1 bd",
    "$2,509+ 1 bd",
    "$2,633+ 1 bd",
    "$2,942/mo"
]

for text in text_strings:
    match = re.search(r'\$([\d,]+)', text)
    if match:
        dollar_amount = match.group(1)
        print(dollar_amount)