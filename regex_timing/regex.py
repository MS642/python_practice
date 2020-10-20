import re

text = "The agent's phone number is 408*555*1234. call soon!"
print('phone' in text)
pattern = 'phone'

print(re.search(pattern, text))
match = re.search(pattern, text)
print(match.start())
print(match.end())

text = 'my phone is the best phone '
match = re.search(pattern, text)
print(match)
matches = re.findall(pattern, text)
print(matches)
print(len(matches))

for match in re.finditer(pattern, text):
    print(match.span())
    print(match.group())
print(text[3:8])
print("=======================")
text = 'my phone number is 408-555-1234'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{3})')
print("=======================")
phone = re.search(phone_pattern, text)
print(phone)
print(phone.group())
print(phone.group(1))
print(phone.group(2))
print(phone.group(3))
# re.search(r'cat|')
"""
^ starts with
$ ends with
| or
[^\d] excludes all digits
"""
pattern = r'[^\d]'
pattern2 = r'[^\d]+'
phrase = '1Find all 3 the chars excluding numbers 1813'
print(re.findall(pattern, phrase))
print(re.findall(r'\d$', phrase))
print(re.findall(r'^\d', phrase))
print(re.findall(pattern2, phrase))
phrase = 'This is a string! But it has a punctuation. How can we remove them?'
print(re.findall(r'[^?.! ]+', phrase))
clean = re.findall(r'[^?.! ]+', phrase)
print(' '.join(clean))

phrase = 'Find the hypen-words. the trick is that Idk how long-ish they are'
print(re.findall(r'[\w]*-[\w]*', phrase))
print(re.findall(r'[\w]+-[\w]+', phrase))