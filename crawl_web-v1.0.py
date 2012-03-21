#!/usr/bin/env python
#
import sys
import urllib
   

#  use to access the internet
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
#   ---------------- unit 4 -------------------------------------
def add_to_index(index1,keyword,url):
    for entry in index1:
      if entry[0] == keyword:
         entry[1].append(url)
         return
    index1.append([keyword,[url]])


def lookup(index1,keyword):
    for entry in index1:
      if entry[0] == keyword:
        #print entry[1]
         return entry[1]
    tmp = []
  # print 'not found'
    return tmp    # or return []


def add_page_to_index(index,url,content):
    tmp = []
    tmp = content.split()    
    count = 0
    for entry in tmp:
          if lookup(index,entry) :
             tmp1 = []
             tmp2 = []
             tmp1 = index[count]
             tmp2 = tmp1.pop()
             tmp2.append(url)
         #   print 'tmp2 --> ',tmp1[0] ,tmp2
             index[count].append(tmp2)
             count = count + 1
          else:
            #print 'NEW: append to index : count =  ',count
             add_to_index(index,entry,url)
            #print 'added --->',index
            #return index

# add max depth -------------------------
def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
               content = get_page(page)
               add_page_to_index(index,page,content)
               union(tocrawl, get_all_links(content))
               crawled.append(page)
    return index
    
 


def main():

   if len(sys.argv) == 1:
       print 'Version 1.0 purplenix.com '
       print "Usage: %s http://www.udacity.com/cs101x/index.html" % sys.argv[0]
       sys.exit(-1)
   else:
     x = []
     url = sys.argv[1]
     x = crawl_web(url,1) 
     count = 0
     for i in x:
       print i
       count =  count + 1
     print 'count = ' , count

if __name__ == '__main__':
   main()



