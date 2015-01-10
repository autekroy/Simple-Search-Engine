#! /usr/bin/python2.7

# Python CGI test for simple search engine
# ex: http://104.131.95.18/SSE/testCGI.py?q=is&url=http://www.udacity.com/cs101x/index.html

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


print url
print 
print q
print 

EngineIndex = {}
# EngineIndex = crawl_web("http://www.udacity.com/cs101x/index.html")

if len(url) != 0:
  EngineIndex = crawl_web( url )
  print "there are all the indexes"
  print EngineIndex

print "<p></p>"

if len(q) != 0:
  print "search results for " + q
  print "<p></p>" 
  listProcess.printList( lookup(EngineIndex, "to") )
