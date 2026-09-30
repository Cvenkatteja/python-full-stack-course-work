'''import re

text= "myname is veknakt teja and my phone no is 6302568815"

pattern = r'\d+'

matches= re.search(pattern,text)

print(matches)
'''

'''
import re

text = "my name is venkateja my phone number is 9966674144 i have the income of the progress is dtill wating unnder the program is going"

pattern = r'\d+'

match = re.findall(pattern , text)

if match:
    
    print("match found:",match)
else:
    
    print("maatch is not found")
'''
import re

text =''' A small business generated a revenue of $50,000 in the first
month while its total cost, including rent, salaries, and materials was $30,000.
This resulted ins a profit of $20,000, showing a positive startfor the company
In the second month, revenue increased to $70,000 due to higher sales
but costs also rose to $40,000. Even with increased expenses
the business earned a profit of $30,000, indicating steady growth
By carefully managing costs and improving'''

pattern = r"\$?\s?\d{1,3}(?:,\d{3})+"

matches = re.findall(pattern,text)

print(matches)






















