import re

names_file = open("name.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

first_name = r'Love' # r'...' means a raw text
# print(re.match(first_name, data)) # MATCH matches the first word
# print(re.search(r'Kenneth', data)) # SEARCH searches everywhere in the text


# New Terms
# > open() - Opens a file in Python. This won't contain the content of the file, it just points to it in memory.
# > .read() - Reads the entire contents of the file object it's called on.

# > .close() - Closes the file object it's called on. This clears the file out of Python's memory.
# > r'string' - A raw string that makes writing regular expressions easier.
# > re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.
# > re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.

# A better way to read files
# If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

# with open("some_file.txt") as open_file:
#     data = open_file.read()

# CHAPTER 2 ESCAPE CHARACTERS
# New terms
# @ \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
# @ \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", @ \W would only match the hyphens.
# @ \s - matches whitespace, so spaces, tabs, newlines, etc.
# @ \S - matches everything that isn't whitespace.
# @ \d - is how we match any number from 0 to 9
# @ \D - matches anything that isn't a number.
# @ \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# @ \B - matches anything that isn't the edges of a word.

# Two other escape characters that we didn't cover in the video are \A and \Z. These match the beginning and the end of the string, respectively. As we'll learn later, though, ^ and $ are more commonly used and usually what you actually want.

# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)) # (555) 555-5555
# OR BETTER
# print(re.search(r'\(?\d{3}\)?-?\s? \d{3}-\d{4}', data)) # ? shows that perenthesis could be optional in the text
# OR WITH FINDALL
# print(re.findall(r'\(?\d{3}\)?-?\s? \d{3}-\d{4}', data))

# Exercise
import re

def first_number(str):
    return re.search(r'\d', str)

def numbers(count, str):
    return re.search(r'\w' * count, str)

# print(numbers(3, 'string73'))

# CHAPTER 3 Exact match
# New terms
# > \w{3} - matches any three word characters in a row.
# > \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# > \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# > \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# > \w? - matches 0 or 1 word characters.
# > \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# > \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.

# print(re.search(r'\w+, \w+', data))
# Or WE CAN DO THIS AND CHECK THE DIFFERENCE
# print(re.findall(r'\w*, \w+', data))

# CHALLENGE
# Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.
# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']
# def find_words(count, str):
#     # count = r'(?=\w)" + re.escape(count)'
#     count = r'\w\{\{0},\}'.format(count)
#     return re.findall(count, str)

# print(find_words(4, "dog, cat, baby, balloon, me"))

# CHAPTER 3 SETs

# Sets let us combine explicit characters and escape patterns into pieces that can be repeated multiple times. They also let us specify pieces that should be left out of any matches.
# New terms
# @ [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
# @ [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
# @ [0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

# EXAMPLE FOR EMAIL

# print(re.findall(r'[-\w\d+,.?]+@[-\w\d.]+', data))

# print(re.findall(r'\b[trehous]+\b', data, re.IGNORECASE)) # \b to get only treehouse not words with the letters. IGNORECASE or just I
# print(re.findall(r'\b[trehous]{9}\b', data, re.I)) #{9} says return if the words are also 9

string = '1234567890'
good_numbers = re.findall(r'[^567]+', string)
# print(good_numbers)

# Multiple line
# print((r'''
# \b[-\w]+,   #Find a word boundary, 1+ hyphens or characters and a comma
# \s         # Find 1 whitespace
# [-\w ]+    # 1+ hyphens and characters and explicit spaces
# [^\t\n]    # Ignore tabs and newlines
# ''', data, re.X))

#EXAMPLE 2
# print(re.findall(r'''
# ^([-\w]*,\s[-\w ]+)\t #Last and first names. Everything in() belongs to a group
# ([-\w\d.+]+@[-\w\d.]+)\t #Email 
# (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone number. Here * means some words are optinal
# ([\w\s]+,\s[\w\s.]+)\t? # Job and company
# (@[\w\d]+)?$ #Twitter. Here $ means the end of the string while ^ means the start of a string
# ''', data, re.X|re.M))

# EXAMPLE 3 SAME AS @ BUTGIVEN THEM NAMES
line = re.search(r'''
^(?P<name>[-\w]*,\s[-\w ]+)\t 
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t 
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t 
(?P<job>[\w\s]+,\s[\w\s.]+)\t?
(?P<twitter>@[\w\d]+)?$
''', data, re.X|re.M)
# print(line)
# print(line.groupdict())

# CHALLENGE
# Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.
string = 'Perotto, Pier Giorgio'
names = re.match(r'(?P<lastname>\b[-\w]+\b)(?P<firstname>[,\s\w ]+)', string, re.X)
# (?P<name>,\s[-\w ]+[-\w]*)
print(names.groupdict())

string2 = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
(?P<email>[-\w\d.+]+@[-\w\d.]+)?\t 
# (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t 
''', string2, re.X)
# print(contacts.groupdict())

# EXAMPLE 4 COMPILING RGEX IN PYTHON MAKES IT READY FOR ANY KIND OF FUNCTION

line2 = re.compile(r'''
^(?P<name>[-\w]*,\s[-\w ]+)\t 
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t 
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t 
(?P<job>[\w\s]+,\s[\w\s.]+)\t?
(?P<twitter>@[\w\d]+)?$
''',re.X|re.M)
print(re.search(line2, data).groupdict()) # SAME AS THIS BELOW
print(line2.search(data).groupdict())

# EXAMPLE 5 FINDITER REGEX METHOD THAT RETURNS A LIST LIKE OBJECT
for match in line2.finditer(data):
    print(match.group('name'))

# CREATING SUBGROUP
line3 = re.compile(r'''
^(?P<name>(?P<last>[-\w]*),\s(?P<first>[-\w ]+))\t 
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t 
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t 
(?P<job>[\w\s]+,\s[\w\s.]+)\t?
(?P<twitter>@[\w\d]+)?$
''',re.X|re.M)

for match in line3.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))


# CHALLENGE
# Create a variable named players that is an re.search() or re.match() to capture three groups: last_name, first_name, and score. It should include re.MULTILINE.
string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'^(?P<last_name>[-\w\s?]*),\s(?P<first_name>[-\w\s? ]*):\s(?P<score>[-\d ]+)$', string,re.M)
print(players.groupdict())

# Thankfully, there is a flag to modify this behavior as well. The re.MULTILINE flag tells python to make the ‘^’ and ‘$’ special characters match the start or end of any line within a string. Using this flag: Newlines are treated as individual strings
# re.X helps us write our patterns over multiple lines

class Player:
  def __init__(self, last_name, first_name, score):
    self.last_name last_name
    self.first_name = first_name
    self.score = score