#-----------------------------------------
# Learning from Udacity CS 101
# Date: 12/10, 2014
#-----------------------------------------

import listProcess

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
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

#----------------------------------------------------------
# function usage: crawl urls from a seed (a link)
# parameter: a link, and max number of links
# return: return a finited crawled url
def crawl_web(seed, maxPages):
  tocrawl = [seed] # wait for crawling
  crawled = []     # already crawled
  while tocrawl:
    page = tocrawl.pop() # get an element and remove it from list
    if page not in crawled:
      if len(crawled) < maxPages: crawled.append(page)
      else:                       break;
      listProcess.Union( tocrawl, get_all_links( get_page(page) ))
  return crawled

def main():
  print crawl_web("http://www.udacity.com/cs101x/index.html", 2)

if __name__ == '__main__':
  main()