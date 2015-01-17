#! /usr/bin/python2.7

# Python CGI test for simple search engine
# ex: http://104.131.95.18/SSE/testCGI.py?q=is&url=http://www.udacity.com/cs101x/index.html

# Import modules for CGI handling 
from searchEngine import *
import MySQLdb
import listProcess # from listProcess.py for list processing
import cgi
import cgitb 
cgitb.enable()

# Create instance of FieldStorage 
# form = cgi.FieldStorage() 

# input_url = form.getvalue('name')

db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="SSE")
cursor = db.cursor()

cursor.execute("select * from SSE.user;")
# cursor.execute("select * from SSE.user where userID=1;");
# cursor.execute("select name from SSE.user where userID=1;");
result = cursor.fetchall()

for record in result:
  print record
  print   


