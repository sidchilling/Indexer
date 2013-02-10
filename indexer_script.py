# Read all the stop words and store them in a list

import requests
from BeautifulSoup import BeautifulSoup
import nltk

url_title_map = {} # Mapping of url to title
word_map = {} # Mapping of word to [{'url' : 'url', 'num' : 34}]
stop_words = [] # List of stop words

def process_article(url):
    r = requests.get(url = url)
    if r.ok:
	print 'Processing for url: %s' %(url)
	body = nltk.clean_html(BeautifulSoup(r.content).find('body').renderContents()).split()
	for word in body:
	    word = word.strip().lower() # Remove leading and trailing whitespace from word and make it lower
	    if len(word) > 0: # Process the word only if it is a word
		if word not in stop_words:
		    # This word has to be considered
		    if word in word_map:
			# word is present in the word map
			url_list = word_map[word]
			inserted = False # word is inserted or not
			for url_num_map in url_list:
			    if url_num_map['url'] == url:
				url_num_map['num'] = url_num_map['num'] + 1
				inserted = True
				break
			if not inserted:
			    # url is not present in url_list
			    word_map[word].append({'url' : url, 'num' : 1})
		    else:
			# word is altogether not present
			word_map[word] = [{'url' : url, 'num' : 1}]

def get_stop_words():
    stop_words_file = open('stop_words.txt', 'r')
    words = stop_words_file.readlines()
    stop_words_file.close()
    for word in words:
	stop_words.append(word.strip())
    return stop_words

def read_feed_urls():
    f = open('feeds.txt', 'r')
    fs = f.readlines()
    f.close()
    feeds = []
    for feed in fs:
	feeds.append(feed.strip())
    return feeds

def make_url_title_map(feed_url):
    r = requests.get(url = feed_url)
    if r.ok:
	print 'Processing for feed: %s' %(feed_url)
	soup = BeautifulSoup(r.content)
	items = soup.findAll('item')
	for item in items:
	    item_str = '%s' %(item)
	    link_start_index = (item_str.find('<link />') + len('<link />'))
	    link_end_index = item_str.find('<', link_start_index)
	    if item_str[link_start_index : link_end_index].strip() not in url_title_map:
		url_title_map[item_str[link_start_index : link_end_index].strip()] = \
			item.find('title').renderContents()

def sort_word_map():
    from operator import itemgetter
    for word in word_map:
	word_map[word].sort(key = itemgetter('num'), reverse = True)

def print_result(search):
    search = search.strip().lower()
    if search in word_map:
	url_list = word_map[search]
	print 'We found %s articles with the word "%s"\n' %(len(url_list), search)
	count = 1
	for url_map in url_list[:10]: # Do only for 10
	    print '%s) "%s" [search term occurs %s times]\n%s' %(count, \
		    url_title_map[url_map['url']], url_map['num'], url_map['url'])
	    count = count + 1
    else:
	print 'Search term not found'
    print '\n\n'

if __name__ == '__main__':
    # Read the stop words
    stop_words = get_stop_words()
    # print stop_words
    feeds = read_feed_urls()
    for feed in feeds:
	make_url_title_map(feed_url = feed)
    print 'Number of urls: %s' %(len(url_title_map.keys()))
    count = 0 # Just used for printing to indicate progress 
    for url in url_title_map:
	count = count + 1
	print 'Count: %s' %(count)
	process_article(url = url)
    sort_word_map()
    # Now we will do the searching thing
    while True:
	line = raw_input('Please enter a single search term [enter to break]:')
	line = line.strip()
	if len(line) > 0:
	    print_result(search = line)
	else:
	    break
