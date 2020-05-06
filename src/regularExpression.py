import re

'''
Pencocokkan string dengan menggunakan library re
Mencari string patternInput pada textInput
Jika pattern terdapat pada text, fungsi mengembalikan inndeks 
pertama letak kemunculan pattern
Jika tidak ada pattern dalam text, fungsi mengembalikan -1
'''
def regex(textInput, patternInput):
    pattern = patternInput.upper()
    text = textInput.upper()

    if(re.search(pattern, text)):
        return ((re.search(pattern, text)).span()[0])
    else:
        return -1