#-----------------------------------------
# Learning from Udacity CS 101
# Date: 12/10, 2014
#-----------------------------------------
import urllib # for get html
import listProcess

def get_page(url):
  sock = urllib.urlopen(url)
  # sock = urllib.urlopen("http://www.udacity.com/cs101x/index.html")
  htmlPage = sock.read()
  sock.close()
  return htmlPage


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
# return: none
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
# return: return a finited crawled url
def crawl_web(seed, maxPages = 100):
  tocrawl = [seed] # wait for crawling
  crawled = []     # already crawled
  while tocrawl:
    page = tocrawl.pop() # get an element and remove it from list
    if page not in crawled:
      if len(crawled) < maxPages: crawled.append(page)
      else:                       break;
      listProcess.Union( tocrawl, get_all_links( get_page(page) ))
  return crawled


#---------- main funtion to run ---------- 
def main():
  # print crawl_web("http://www.udacity.com/cs101x/index.html")
  # print get_page("http://www.udacity.com/cs101x/index.html")

if __name__ == '__main__':
  main()