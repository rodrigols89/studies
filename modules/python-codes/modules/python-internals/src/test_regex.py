import re

regex = r".rigo"
string = "Rodrigo Leite da Silva"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
