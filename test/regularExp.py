import re

test = 'abdeDebdEger'
print(re.findall('[A-Z]',test)) # ['D','E']
print(re.findall('[A-Z]*',test) ) #['', '', '', '', 'D', '', '', '', 'E', '', '', '', '']
print(re.findall('[^A-Z]*',test) ) # ['abde', '', 'ebd', '', 'ger', '']
print(re.findall('[A-Z][^A-Z]*',test) ) #['Debd', 'Eger']
print(re.findall('[A-Z]*[^A-Z]*',test) )


