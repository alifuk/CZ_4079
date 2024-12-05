import re

if __name__ == "__main__":
    text = "Nájezd automobilu je- 100000 km jelikož je 5 let starý."
    pattern = r"-|\."
    match = re.findall(pattern, text)
    print(match)