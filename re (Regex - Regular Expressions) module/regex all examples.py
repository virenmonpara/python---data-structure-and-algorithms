import re
# regex example i have learned from youtube link below
# https://youtu.be/K8L6KVGG-7o
text_to_search = ''' 
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

metaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
354*564*6843
800-595-4321
900-655-4321

Mr. Viren
Mr Smith
Ms Davis
Mrs. Robinson0945
Mr. T

cat
pat
bat
mat
'''
sentence = 'Hello Mr. Viren, how are you'


# print('\t viren')  #print viren after tab
# print(r'\t viren')  # with raw string it will print \t viren
# pattern=re.compile(r'\.') # r'\.' is used to escape the dot
# pattern=re.compile(r'\d') # \d for finding a digit in data
# pattern=re.compile(r'[^b]at') # ^ is used to exclude the character
# pattern = re.compile(r'\bHa') # \b is word boundary
# pattern = re.compile(r'^Hello')  # ^ is used to find at beginning of the string
# pattern = re.compile(r'you$') # $ is used to find at end of the string
# pattern=re.compile(r'\d\d\d') # to find three digit number in row
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # to find mentioned(number of \d) digit number in row
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') #above mentioned pattern is also do the same
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') #finding numbers with .or- in row it will not show with *
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') #finding number starting with 800 or 900 and then followed by .or-
# pattern=re.compile(r'[a-zA-Z0-9]') # to find all the characters in row
# pattern=re.compile(r'Mr\.?\s[A-Z]\w*') # matching Mr. or Mr and then followed by capital letter and then followed by any character
# pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+') # matching Mr. or Ms or Mrs and then followed by capital letter and then followed by 1 or more characters here Mr. T will excluded
# matching Mr. or Ms or Mrs and then followed by capital letter and then followed by 0 or more characters here Mr. T will included
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# matches = pattern.finditer(sentence)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

###############################################


# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') #finding number starting with 800 or 900 and then followed by .or-
pattern = re.compile(r'[a-z]')

with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)

####################################################

# matching all email address
pattern = re.compile(r'[a-zA-Z0-9_.-+]+@[a-zA-Z0-9-]+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,3}') # to match first email address

with open('emails.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)

#################################

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # matching all urls


with open('urls.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        # print(match)
        print(match.group(1))  # we can use group(1) to get first group

######################################

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # matching all urls


with open('urls.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        # print(match)
        print(match.group(1))  # we can use group(1) to get first group
