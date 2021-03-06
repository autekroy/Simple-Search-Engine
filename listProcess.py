#-----------------------------------------
# Learning from Udacity CS 101
# Date: 12/27, 2014
#-----------------------------------------


#----------------------------------------------------------
# function usage: union 2 lists to the first list
# parameter: two lists and one integer 
# return: none
def Union(a, b):
  for p in b:
    if p not in a:
      a.append(p)


#----------------------------------------------------------
# function usage: print elements in different lines from a list
# parameter: list
# return: none
def printList(list):
  if list:
	for i in list:
		print i


#----------------------------------------------------------
# function usage: print elements in different lines in HTML formats from a list
# parameter: list
# return: none
def printHTMLList(list):
  if list:
    for i in list:
        print i + "<br>"
