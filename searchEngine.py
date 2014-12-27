#-----------------------------------------
# Learning from Udacity CS 101
# Date: 12/10, 2014
#-----------------------------------------
import sys
import listProcess

#=============================== about crawler ====================================#

def get_page(url):
  try:
    import urllib # for get html
    sock = urllib.urlopen(url)
    htmlPage = sock.read()
    sock.close()
    return htmlPage
  except:
    return ""

#----------------------------------------------------------
# function usage: get the next url
# parameter: the page html information
# return:  url and the next position of page
def get_next_target(page):
    start_link = page.find('<a href=')
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
def crawl_web(seed, maxPages = 100):
  tocrawl = [seed] # wait for crawling
  crawled = []     # already crawled
  index = []       # index for every webpage
  while tocrawl:
    page = tocrawl.pop() # get an element and remove it from list
    if page not in crawled:
      # restrict the page whithin maxPages
      if len(crawled) > maxPages:
        break
      
      content = get_page(page)
      add_page_to_index(index, page, content)
      listProcess.Union( tocrawl, get_all_links( content ))
      crawled.append(page)      
  return index

#=============================== about index ====================================#

def add_page_to_index(index, url, content):
  words = content.split() #split words
  for word in words:
    add_to_index(index, word, url)


def add_to_index(index, keyword, url):
  for entry in index:
    if entry[0] == keyword: # find the previous keyword
      for urlEntry in entry[1]: # find the count number of this url in this keyword
        if urlEntry[0] == url:
          urlEntry[1] = urlEntry[1] + 1
          return # alreay find so we can terminate this function
      entry[1].append( [url, 1] )
      return
      
  # not found. It's a new keyword
  index.append( [keyword, [ [url, 1] ] ] )


def lookup(index, keyword):
  for entry in index:
    if entry[0] == keyword:
      return entry[1] # find keyword
  return [] # didn't find keyword


#---------- main funtion to run ---------- 
def main():
  EngineIndex = crawl_web( sys.argv[1] )
  listProcess.printList( EngineIndex )
  print lookup(EngineIndex, "to")
  # print crawl_web("http://www.udacity.com/cs101x/index.html")
  # print get_page("http://www.udacity.com/cs101x/index.html")

if __name__ == '__main__':
  main()