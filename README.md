Indexer
=======

This is a python script which I had written for reading from RSS feeds, extracting article urls, indexing all the
words in the URL and giving a search on those.

The problem statement for this script can be described as below -


Given a file containing a list of RSS feeds. Write a script that indexes articles from these feeds.
Indexing an article means storing how many times each word appears in each article. This is how search engines 
determine which documents match a query, and in what ranking. After all articles have been indexed, the 
script should loop asking the user for a word, and display the title and URL of articles that contain the word, 
and in the order of the number of times that work appears in each article. Limit the output to 10 articles 
with the most occurrences of the word. Use the feeds.txt file as the list of RSS feeds.

Some words are very common and should not be indexed. A list of such words are present in stop_words.txt file.

Example program run:
Please enter a single search term [enter to break]: India
We found 86 articles with the word "India".
       1.) "Holiest day at India's Kumbh Mela" [search term occurs 26 times]
"http://www.bbc.co.uk/news/world-asia-india-21395425"
       2.) "Delhi parliament plotter hanged" [search term occurs 20 times]
   "http://www.bbc.co.uk/news/world-south-asia-21392156"
       3.) "Sharp end of Indian politics" [search term occurs 19 times]
   "http://www.bbc.co.uk/news/magazine-21384169"
and so on for 10 articles.

