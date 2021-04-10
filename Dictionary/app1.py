import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print(type(data))


def translate(myWord):
    if myWord in data:
        print(type(data[myWord]))
        return data[myWord]
    elif len(get_close_matches(myWord, data.keys())) > 0:
        yn = input("Did you mean %s"  %get_close_matches(myWord, data.keys())[0] + "Press Y or N")
        if yn == "Y":
            return data[get_close_matches(myWord, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist , please double check it!"
        else:
            return "We did not understand your query !"
    else:
        return "No Such word!"


word = input("Enter a word:")
output = translate(word.lower())
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        
        
        