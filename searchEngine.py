#----------------------------------------
# Learning from Udacity CS 101
# Date: 01/12, 2015
# Email: autekwing@ucla.edu
#-----------------------------------------
import sys
import listProcess # from listProcess.py for list processing
import time # python library
import cgi
import cgitb 

#=============================== about crawler ====================================#

#----------------------------------------------------------
# function usage: return a webpage content
# parameter: a url link
# return: html page content
def get_page(url):
  try:
    import urllib # for get html
    sock = urllib.urlopen(url)
    htmlPage = sock.read()
    sock.close()
    return htmlPage
  except:
    return ""


# def get_page(url):
#     try:
#         if url == "http://www.udacity.com/cs101x/index.html":
#             return '''<html> <body> This is a test page for learning to crawl!
# <p> It is a good idea to
# <a href="http://www.udacity.com/cs101x/crawling.html">
# learn to crawl</a> before you try to
# <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
# <a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''

#         elif url == "http://www.udacity.com/cs101x/crawling.html":
#             return '''<html> <body> I have not learned to crawl yet, but I am
# quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
# </body> </html>'''

#         elif url == "http://www.udacity.com/cs101x/walking.html":
#             return '''<html> <body> I cant get enough
# <a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''

#         elif url == "http://www.udacity.com/cs101x/flying.html":
#             return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
#     except:
#         return ""
#     return ""

#----------------------------------------------------------
# function usage: get the next url
# parameter: the page html information
# return:  url and the next position of page
def get_next_target(page):
    start_link = page.find('href=')
    if start_link == -1:
    	return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote # return as tuple, which can't be modified


#----------------------------------------------------------
# function usage: print all the url, need function get_next_target
# paramete: the whole html page
# return: links
def get_all_links(page):
  links = []
  while True:
    url, endpos = get_next_target(page)
    if url:
      # print url
      links.append(url)
      page = page[endpos:]
    else:
      break
  return links

#----------------------------------------------------------
# for future regular expression practice
# import re
# pat = re.compile('<DT><a href="[^"]+">(.+?)</a>')
# url = 'http://www.infolanka.com/miyuru_gee/art/art.html'
# sock = urllib.urlopen(url)
# li = pat.findall(sock.read())
# sock.close()
# print li


#----------------------------------------------------------
# function usage: crawl urls from a seed (a link)
# parameter: a link, and max number of links
# return: return a finited crawled url with index
def crawl_web(seed, maxPages = 10):
  tocrawl = [seed] # wait for crawling
  crawled = []     # already crawled
  index = {}       # index(dictionary) for every webpage
  graph = {}       # <url>, [list of pages it links to]
  while tocrawl:
    page = tocrawl.pop() # get an element and remove it from list
    if page not in crawled:
      # restrict the page whithin maxPages
      if len(crawled) > maxPages:
        break
      
      content = get_page(page) # no content for this webpage. url is invalid or empty page
      if content == "":
        continue

      add_page_to_index(index, page, content)
      outLinks = get_all_links( content )
      graph[page] = outLinks
      listProcess.Union( tocrawl, outLinks)
      crawled.append(page)      
  return index, graph

#=============================== about index ====================================#

#----------------------------------------------------------
# function usage: add indexes from a webpage
# parameter: whole index list, url link, and webpage content
# return: none
def add_page_to_index(index, url, content):
  words = content.lower().split() #split words
  for word in words:
    add_to_index(index, word, url)


#----------------------------------------------------------
# function usage: add indexes with source url
# parameter: whole index list, index keyword
# return: none
def add_to_index(index, keyword, url):
  if keyword in index: # find the previous keyword
    for urlEntry in index[keyword]: # find the count number of this url in this keyword
      if urlEntry[0] == url:
        urlEntry[1] = urlEntry[1] + 1
        return # alreay find so we can terminate this function
    index[keyword].append( [url, 1] )
    return
  # not found. It's a new keyword
  index[keyword] = [ [url, 1] ]


#----------------------------------------------------------
# function usage: lookup a keyword from index list
# parameter: whole index list and keyword
# return: keyword in index list
def lookup(index, keyword):
  keyword = keyword.lower() # use lower alphabet to search
  if index and keyword in index:
    return index[keyword] # find keyword
  return None # didn't find keyword

#----------------------------------------------------------
# function usage: 
# parameter:
# return:
def popularity(t, p):
  if t == 0:
    return 1
  else:
    score = 0
    for f in firends(p):
      score = score + popularity(t-1, f) # recursive to find the socres
    return score


#----------------------------------------------------------
# function usage: 
# parameter:
# return:
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages

            #Insert Code Here

            newranks[page] = newrank
        ranks = newranks
    return ranks

#----------------------------------------------------------
# function usage: 
# parameter:
# return:
def lookup_best(index, graph, keyword):
 return None 

#=============================== about time ====================================#
def time_execution(code):
  start = time.clock()  # start clock
  result = eval(code)   # evaluate any string as if it is a Python command
  run_time = time.clock() - start
  return resutl, run_time



#========================== main funtion to run =====================
def main():
  # EngineIndex = crawl_web( sys.argv[1] )
  #cgitb.enable()
  #form = cgi.FieldStorage() 
  #crawlStr = form.getvalue('q')
  #EngineIndex = crawl_web( crawlStr )
  #print EngineIndex
  #print "test search"
  # listProcess.printList( EngineIndex )
  # listProcess.printList( lookup(EngineIndex, "google") )
  index, graph = crawl_web("http://www.udacity.com/cs101x/index.html")
  print index
  print 
  print graph
  listProcess.printList( lookup(index, "to") )
  # listProcess.printHTMLList( lookup_best(index, graph, "to") )
  #i print get_page("http://www.udacity.com/cs101x/index.html")

if __name__ == '__main__':
  main()
