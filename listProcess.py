#-----------------------------------------
# Learning from Udacity CS 101
# Date: 12/10, 2014
#-----------------------------------------


# function usage: union 2 lists to the first list
# parameter: two lists and one integer 
# return: none
def Union(a, b):
  for p in b:
    if p not in a:
      a.append(p)


def printList(list):
	for i in list:
		print i