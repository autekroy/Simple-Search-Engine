#! /usr/bin/python2.7

# Import modules for CGI handling 
from searchEngine import *
import listProcess # from listProcess.py for list processing
import cgi
import cgitb 
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

input_url = form.getvalue('url')

print "Content-type:text/html\r\n\r\n"

url = ""
if form.getvalue('url'):
  url = form.getvalue('url')

q = ""
if form.getvalue('q'):
  q = form.getvalue('q')


EngineIndex = crawl_web("http://www.udacity.com/cs101x/index.html")

if len(url) != 0:
  EngineIndex = crawl_web( url )
  print EngineIndex
elif len(q) != 0:
  print "search results for " + q
  print "<p></p>" 
  listProcess.printList( lookup(EngineIndex, "to") )
