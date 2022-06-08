import re
# regex example learned from youtube link below
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

Mr.Viren
Mr.Urvish
Mr.Ruchit
Mr.Hasmukh
Mr. T

cat
pat
bat
mat
'''
sentence = 'Start a sentence and then bring it to an end'


# print('\t Tab')   # \t is tab
# print(r'\t Tab')  # Raw String
# pattern=re.compile(r'\.') # r'\.' is used to escape the dot
# pattern=re.compile(r'\d') # \d is digit
# pattern=re.compile(r'[^b]at') # ^ is used to exclude the character
# pattern = re.compile(r'\bHa') # \b is word boundary
# pattern = re.compile(r'^Start')  # ^ is used to find at beginning of the string
# pattern = re.compile(r'end$') # $ is used to find at end of the string
# pattern=re.compile(r'\d\d\d') # to find three digit number in row
# to find mentioned(number of \d) digit number in row
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# matches = pattern.finditer(sentence)
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
with open('re (Regex - Regular Expressions) module\data.txt','r',encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
