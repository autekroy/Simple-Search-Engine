#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

input_url = form.getvalue('input_url')


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title></title>"
print "</head>"
print "<body>"
print input_url
print "</body>"
print "</html>"