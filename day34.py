'''REGULAR EXPRESSION(Reg Ex)
--------------------------
---> This regular Expressions or RedEx is a sequence of characters that forms a searching pattern.
---> To use this we have to import re, which will unlock the package

Functions
-----------
1)Findall
----------
---> by using this function, it will find all sequence in the string
syntax --> re.findall(metachar, variable_name)

2)Search
---------
---> by using this function, it will only find first sequence in the string
syntax --> re.search("metachar", variable_name)

---> Metacharacters are special characters in RegEx that have a specific meaning (not treated as normal characters).
They help you define search patterns more powerfully.


import re

text = "apple bag dog egg fan hat"
result1 = re.findall(r'[a-g]', text)
result2 = re.findall(r'[aeh]', text)

print(result1)
print(result2)  


import re

text = "Apple BAG dog Egg FAN hat"
result = re.findall(r'[A-Z]', text)

print(result) 

import re

text = "My number is 9515825824"
result = re.search(r'\d+', text)

print(result.group())
'''



























 




         
