#! /usr/bin/python2.7

# Python CGI test for simple search engine
# ex: http://104.131.95.18/SSE/testCGI.py?q=is&url=http://www.udacity.com/cs101x/index.html

# Import modules for CGI handling 
import MySQLdb
import listProcess # from listProcess.py for list processing
import cgi
import cgitb 
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

user = form.getvalue('username')
pw =   form.getvalue('password')

print "Content-type:text/html\r\n\r\n"

print "input user: " + user + " input password:  " + pw + "<br>"

db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="SSE")
cursor = db.cursor()

# print all the information
cursor.execute("select * from SSE.user;")
result = cursor.fetchall()

print "<p>all the users: <br>"
for record in result:
  print record
  print

if "@" in user: # mean user input a email
  sqlcmd = "select * from SSE.user where email=\"" + user + "\";"
else:
  sqlcmd = "select * from SSE.user where name=\"" + user + "\";"

cursor.execute(sqlcmd);
result = cursor.fetchall()


# edit information in table
# update SSE.user set email = 'autek-roy@hotmail.com' where name = "autekroy";

if result:
  print "<p>print the search result: <br>"
  record = result[0] # result should be only one list
  print record[3] + "<br>"
  #print record[3] # it's password
  if record[3] == pw:
    print "<p> you sign in successfully!"
  else:
    print "<p>wrong user name or password"
  #print result[0]
else: # can't find useri
  print "<p>wrong user name or password"

db.close()
