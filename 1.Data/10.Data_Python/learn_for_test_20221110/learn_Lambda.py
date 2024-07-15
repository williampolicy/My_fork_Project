str1 = 'GeeksforGeeks'
 
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))



format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
 
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))



def cube(y):
    return y*y*y
 
 
lambda_cube = lambda y: y*y*y
 
 
# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))
 
# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))




List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)



# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
 
adults = list(filter(lambda age: age > 18, ages))
 
print(adults)




# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)



# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))
 
print(uppered_animals)