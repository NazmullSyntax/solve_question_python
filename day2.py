# # # Suppose you are given the below string

# # # str = “””Email_Address,Nickname,Group_Status,Join_Year
# # # aa@aaa.com,aa,Owner,2014
# # # bb@bbb.com,bb,Member,2015
# # # cc@ccc.com,cc,Member,2017
# # # dd@ddd.com,dd,Member,2016
# # # ee@eee.com,ee,Member,2020
# # # “””

# # # In order to extract only the domain names from the email addresses from the above string (for eg. “aaa”, “bbb”..) you write the following code:

# # import re

# # str_data = """Email_Address,Nickname,Group_Status,Join_Year
# # aa@aaa.com,aa,Owner,2014
# # bb@bbb.com,bb,Member,2015
# # cc@ccc.com,cc,Member,2017
# # dd@ddd.com,dd,Member,2016
# # ee@eee.com,ee,Member,2020
# # """

# # domains = re.findall(r'@([a-zA-Z0-9]+)\.', str_data)

# # print(domains)

# # Your friend has a hypothesis – “All those people who have names ending with the sound of “y” (Eg: Hollie) are intelligent people.” Please note: The name should end with the sound of ‘y’ but not end with alphabet ‘y’.

# # Now you being a data freak, challenge the hypothesis by scraping data from your college’s website. Here’s data you have collected.

# # Name	Marks
# # Andy	0
# # Mandi	10
# # Sandy	20
# # Hollie	18
# # Molly	19
# # Dollie	15

# # You want to make a list of all people who fall in this category. You write following code do to the same:

# names = ["Andy", "Mandi", "Sandy", "Hollie", "Molly", "Dollie"]

# result = []

# for name in names:
#     if name.lower().endswith("ie"):
#         result.append(name)

# print(result)

# Assume, you are given two lists:

# a = [1,2,3,4,5]

# b = [6,7,8,9]

# The task is to create a list which has all the elements of a and b in one dimension.

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

c = a + b

print(c)