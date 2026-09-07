# # # # # # # # # # # # Suppose you are given the below string

# # # # # # # # # # # # str = “””Email_Address,Nickname,Group_Status,Join_Year
# # # # # # # # # # # # aa@aaa.com,aa,Owner,2014
# # # # # # # # # # # # bb@bbb.com,bb,Member,2015
# # # # # # # # # # # # cc@ccc.com,cc,Member,2017
# # # # # # # # # # # # dd@ddd.com,dd,Member,2016
# # # # # # # # # # # # ee@eee.com,ee,Member,2020
# # # # # # # # # # # # “””

# # # # # # # # # # # # In order to extract only the domain names from the email addresses from the above string (for eg. “aaa”, “bbb”..) you write the following code:

# # # # # # # # # # # import re

# # # # # # # # # # # str_data = """Email_Address,Nickname,Group_Status,Join_Year
# # # # # # # # # # # aa@aaa.com,aa,Owner,2014
# # # # # # # # # # # bb@bbb.com,bb,Member,2015
# # # # # # # # # # # cc@ccc.com,cc,Member,2017
# # # # # # # # # # # dd@ddd.com,dd,Member,2016
# # # # # # # # # # # ee@eee.com,ee,Member,2020
# # # # # # # # # # # """

# # # # # # # # # # # domains = re.findall(r'@([a-zA-Z0-9]+)\.', str_data)

# # # # # # # # # # # print(domains)

# # # # # # # # # # # Your friend has a hypothesis – “All those people who have names ending with the sound of “y” (Eg: Hollie) are intelligent people.” Please note: The name should end with the sound of ‘y’ but not end with alphabet ‘y’.

# # # # # # # # # # # Now you being a data freak, challenge the hypothesis by scraping data from your college’s website. Here’s data you have collected.

# # # # # # # # # # # Name	Marks
# # # # # # # # # # # Andy	0
# # # # # # # # # # # Mandi	10
# # # # # # # # # # # Sandy	20
# # # # # # # # # # # Hollie	18
# # # # # # # # # # # Molly	19
# # # # # # # # # # # Dollie	15

# # # # # # # # # # # You want to make a list of all people who fall in this category. You write following code do to the same:

# # # # # # # # # # names = ["Andy", "Mandi", "Sandy", "Hollie", "Molly", "Dollie"]

# # # # # # # # # # result = []

# # # # # # # # # # for name in names:
# # # # # # # # # #     if name.lower().endswith("ie"):
# # # # # # # # # #         result.append(name)

# # # # # # # # # # print(result)

# # # # # # # # # # Assume, you are given two lists:

# # # # # # # # # # a = [1,2,3,4,5]

# # # # # # # # # # b = [6,7,8,9]

# # # # # # # # # # The task is to create a list which has all the elements of a and b in one dimension.

# # # # # # # # # a = [1, 2, 3, 4, 5]
# # # # # # # # # b = [6, 7, 8, 9]

# # # # # # # # # c = a + b

# # # # # # # # # print(c)

# # # # # # # # # You have built a machine learning model which you wish to freeze now and use later. Which of the following command can perform this task for you?

# # # # # # # # import joblib

# # # # # # # # joblib.dump(model, "model.pkl")

# # # # # # # # We want to convert the below string in date-time value:

# # # # # # # import pandas as pd

# # # # # # # date = "2024-01-15"

# # # # # # # date_time = pd.to_datetime(date)

# # # # # # # print(date_time)

# # # # # # # I have built a simple neural network for an image recognition problem. Now, I want to test if I have assigned the weights & biases for the hidden layer correctly. To perform this action, I am giving an identity matrix as input. Below is my identity matrix:

# # # # # # # A =  [ 1, 0, 0
# # # # # # # 0, 1, 0
# # # # # # # 0, 0, 1]7) How would you create this identity matrix in python?

# # # # # # import numpy as np

# # # # # # A = np.eye(3)

# # # # # # print(A)

# # # # # # To check whether the two arrays occupy same space, what would you do?

# # # # # # I have two numpy arrays “e” and “f”.You get the following output when you print “e” & “f”

# # # # # # print e
# # # # # # [1, 2, 3, 2, 3, 4, 4, 5, 6]
# # # # # # print f
# # # # # # [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
# # # # # # When you change the values of the first array, the values for the second array also changes. This creates a problem while processing the data.

# # # # # # For example, if you set the first 5 values of e as 0; i.e.

# # # # # import numpy as np

# # # # # e = np.array([1, 2, 3, 2, 3, 4, 4, 5, 6])

# # # # # f = e.reshape(3, 3)

# # # # e[:5] = 0

# # # # Suppose you want to join train and test dataset (both are two numpy arrays train_set and test_set) into a resulting array (resulting_set) to do data processing on it simultaneously. This is as follows:

# # # # train_set = np.array([1, 2, 3])
# # # # test_set = np.array([[0, 1, 2], [1, 2, 3]])
# # # # resulting_set --> [[1, 2, 3], [0, 1, 2], [1, 2, 3]]
# # # # 9) How would you join the two arrays?


# # # import numpy as np

# # # train_set = np.array([1, 2, 3])
# # # test_set = np.array([[0, 1, 2],
# # #                      [1, 2, 3]])

# # # resulting_set = np.vstack((train_set, test_set))

# # # print(resulting_set)


# # # Suppose you are tuning hyperparameters of a random forest classifier for the Iris dataset.

# # # Sepal_length	Sepal_width	Petal_length	Petal_width	Species
# # # 4.6	3.2	1.4	0.2	Iris-setosa
# # # 5.3	3.7	1.5	0.2	Iris-setosa
# # # 5.0	3.3	1.4	0.2	Iris-setosa
# # # 7.0	3.2	4.7	1.4	Iris-versicolor
# # # 6.4	3.2	4.5	1.5	Iris-versicolor
# # # 10) What would be the best value for “random_state (Seed value)”?

# # from sklearn.ensemble import RandomForestClassifier

# # model = RandomForestClassifier(
# #     random_state=42
# # )

# # While reading a csv file with numpy, you want to automatically fill missing values of column “Date_Of_Joining” with date “01/01/2010”.

# # Name	Age	Date_Of_Joining	Total_Experience
# # Andy	20	01/02/2013	0
# # Mandy	30	01/05/2014	10
# # Sandy	10		0
# # Bandy	40	01/10/2009	20
# # 11) Which command will be appropriate to fill missing value while reading the file with numpy? 

# np.genfromtxt('data.csv', delimiter=',', filling_values='01/01/2010')

# How would you import a decision tree classifier in sklearn?

from sklearn.tree import DecisionTreeClassifier