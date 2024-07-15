# Python3 code to demonstrate working of
# Unique Keys Values
# Using list comprehension + any() + count()

# initializing dictionary
test_dict = {'Gfg' : [6, 5], 'is' : [6, 10, 5], 'best' : [12, 6, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Unique Keys Values
# Using list comprehension + any() + count()
res = [key for key, vals in test_dict.items() if any([ele for sub in test_dict.values()
	for ele in set(sub)].count(idx) == 1 for idx in vals)]

# printing result
print("The unique values keys are : " + str(res))
