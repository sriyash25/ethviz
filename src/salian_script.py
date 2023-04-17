import json

# define the alphabet
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

# dump the alphabet to a JSON file
with open('alphabet.json', 'w') as f:
    json.dump(alphabet, f)