# Python3 code to demonstrate working of
# Unique Keys Values
# Using loop + count()

# initializing dictionary
test_dict = {'Gfg' : [6, 5], 'is' : [6, 10, 5], 'best' : [12, 6, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Unique Keys Values
# Using loop + count()
temp = [sub for ele in test_dict.values() for sub in ele]
res = []
for key, vals in test_dict.items():
	for val in vals:
		if temp.count(val) == 1:
			res.append(key)
			break

# printing result
print("The unique values keys are : " + str(res))
