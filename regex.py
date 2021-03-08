# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import re

message1="Hi my number is 123-456-7892"
pattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
obj = pattern.search(message1)
print(obj.group())
print(obj.group(1))
print(obj.group(2))

print("------------------------")
# ? = 0 or 1 occurence (option pattern)
message2="Hi my number is 456-7892"
pattern = re.compile(r'(\d{3}-)?(\d{3}-\d{4})') #made first 3 digits as optional
obj = pattern.search(message1)
print(obj.group())

obj1 = pattern.search(message2,re.I|re.M)
print(obj1.group())

print("------------------------")
# ? = 0 or 1 occurence (option pattern)
pattern = re.compile(r'bat(wo)?man', re.I|re.M) # (wo) is optional either batman and batwoman bot will work
obj3 = re.search(pattern,"hi i am Batman")
print(obj3.group())
print(pattern.search("hi i'm batwomAN").group())

print("++++++++++++++++++++++++++++++++++++")
#(?i) for ignorecase
#* for 0 or more repeatitions
print(re.search("(?i)bat(wo)*man","""i am a human
and below is
BATwoWoWowoman""").group())
print(re.search("(?i)bat(wo)+man","batwoman").group())

pattern = re.compile(r'bat(wo)+man', re.IGNORECASE)
obj = pattern.search("I m a batman")
print(obj.group()) if obj else print(None)

print("-----------------------------------------------")
# | for or type of searches
pattern = re.compile(r'cherries|strawberries|blueberries|berries', re.I|re.M)
print(pattern.findall("i love cherries, strawberries and feel blueberries are expensive"))
print("*************************************************")
print(re.findall("(?i)\d+\s?\w+","123 asd, 15lemons"))
#imp. groups finall gives tuples
print(re.findall("(\d{3})-(\d{3})-(\d{4})", "my numbers are 913-031-3301, 836-876-1552")) , print("-- imp!!")

print("-------------- IMP. -------------------------")
# ^: inside [] act as negate where []:sets
print("All vowels: ",re.findall("(?i)[aeiou]", "An Old man was working in a Station"))
print("All consonants: ",re.findall("(?i)[^aeiou\s]", "An Old man was working in a Station"))

# ^ is used for start of sentence
print(re.findall("(?i)^hello", "Hello World! and hello to my friends!"))

# $ end of sentence
print(re.findall("(?i)friends!$", "Hello World! and hello to my friends!"))

print("---------------------------------------")
#finditer
# \w = [a-zA-Z_]
# find . in pattern use = "\."
pattern = re.compile(r"abc", re.IGNORECASE|re.MULTILINE)
matches = re.finditer(pattern, "123abc123ABC12345ABc")

for match in matches:
    print(match, match.span(), match.start(), match.end(), match.group())
    
print("################### IMP. ####################")

dates = """
2020-04-21
2020/04/21
04/21/2020
04-21-2020
"""
pattern = re.compile(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]\d{4}')

matches = re.finditer(pattern, dates)

for match in matches:
    print(match.group())
    
print("~~~~~~~~~~~~~~~~~ IMP. ~~~~~~~~~~~~~~~~~~~")
names = """
Mr Simpson
Mrs Simpson
Mrs. Brown
Mr. Brown
Mr Smith
Ms. Mary
Ms Mariam
"""

pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s\w+')

matches = re.finditer(pattern, names)

for match in matches:
    print(match.group())

print("%%%%% IMP - Positive and Negative Lookahead %%%%%%%%%%%")
print(re.search("Iraq(?!i).*","Iraqu").group())
print(re.search("Iraq(?!i).*","Iraqi")) # i should not follow q
print(re.search("Iraq(?=i).*","Iraqi").group())
print(re.search("Iraq(?=i).*","Iraqu")) #i should follow after q

print("$$$$$ IMP - Positive and Negative Lookbehind $$$$$$$$$$")
print(re.search(".*(?<=text)book.*","textbook").group())# book should  follow text
print(re.search(".*(?<!text)book.*","textbook")) # book should not follow text
print(re.search(".*(?<!text)book.*","cookbook").group()) # book should not follow text

# Extract text between two words
sent = "subject: hello users hope u doing great <eom>"
print(re.search("(?<=subject:)(.*)(?=(?=\<eom\>))", sent))
