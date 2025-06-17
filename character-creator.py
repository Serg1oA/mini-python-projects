# The total height of the character (in terms of text lines)
# A one-character string, to use for the hair
# A one-character string, to use for the eyes
# A one-character string, to use for the hands
# A four-character string, to use for the feet

height = 0
while not isinstance(height, int) or height < 13:
    height = int(input("Enter your character's height (13+): "))

hair = ""
while len(hair) != 1:
    hair = input("Letter/symbol for the hair (just 1): ")

eyes = ""
while len(eyes) != 1:
    eyes = input("Letter/symbol for the eyes (just 1): ")

hands = ""
while len(hands) != 1:
    hands = input("Letter/symbol for the hands (just 1): ")

feet = ""
while len(feet) != 4:
    feet = input("Four letters/symbols for the feet (just 4): ")


print(f"""
{hair * 12}
{hair}|        |{hair}
{hair}|  {eyes}  {eyes}  |{hair}
 |   /\   |
 |        |
 \  '--'  /
   ------
     XX
{hands}----XX----{hands}
{"    XXXX\n" * int((height-11)/2)}    ====
{"   ||  ||\n" * int((height-11)/2)} {feet}  {feet}
""")