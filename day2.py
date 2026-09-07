# Suppose you are given the below string

# str = “””Email_Address,Nickname,Group_Status,Join_Year
# aa@aaa.com,aa,Owner,2014
# bb@bbb.com,bb,Member,2015
# cc@ccc.com,cc,Member,2017
# dd@ddd.com,dd,Member,2016
# ee@eee.com,ee,Member,2020
# “””

# In order to extract only the domain names from the email addresses from the above string (for eg. “aaa”, “bbb”..) you write the following code:

import re

str_data = """Email_Address,Nickname,Group_Status,Join_Year
aa@aaa.com,aa,Owner,2014
bb@bbb.com,bb,Member,2015
cc@ccc.com,cc,Member,2017
dd@ddd.com,dd,Member,2016
ee@eee.com,ee,Member,2020
"""

domains = re.findall(r'@([a-zA-Z0-9]+)\.', str_data)

print(domains)