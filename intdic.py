import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# difflib / SequenceMatcher
# ratiox=SequenceMatcher(None,'rainn','rain').ratio()
# print(ratiox)


data=json.load(open('data.json'))
# print(data.keys())

# Get_close_matches
# gcm=get_close_matches('rain',data.keys(),n=7)[0]
# gcm=get_close_matches('coc',data.keys(),cutoff=0.1)
# print(gcm)

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        # return 'Did you mean %s istead?' % get_close_matches(w,data.keys())[0]
        yn=  input('Did you mean %s instad? Enter Y for yes or N fo no : ' % get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it!"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it!"

    
word=input('Plase enter your word : ')
# print(translate(word))
output = translate(word)
if type(output)==list :
    for item in output:
        print(item)
else :
    print(output)