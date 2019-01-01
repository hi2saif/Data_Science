#Regular Expression to check for email strings


s= 'richie@cc.gatech.edu'
pattern = '''
       ^
       (?P<user>[a-zA-Z][\w.\-+]*)
       @
       (?P<domain>[\w.\-]*[a-zA-Z])
       $
    '''
matcher = re.compile(pattern)
matches = matcher.match(s)
if matches:
    print('true')
else:
    print('false')
	
	
	
#Regular Expression to check for US phone  number (040) 555-1234

import re
s= '(404) 121-2121'
pattern = '''\s*\((\d{3})\)\s*(\d{3})-(\d{4})
    '''
matcher = re.compile(pattern,re.VERBOSE)
matches = matcher.match(s)
if matches:
    print('true')
else:
    print('false')
	
	
#enhanced code for Regular expression for US phone number

pattern = '''
        ^\s*               # Leading spaces
        (?P<areacode>
           \d{3}-?         # "xxx" or "xxx-"
           | \(\d{3}\)\s*  # OR "(xxx) "
        )
        (?P<prefix>\d{3})  # xxx
        -?                 # Dash (optional)
        (?P<suffix>\d{4})  # xxxx
        \s*$               # Trailing spaces
    '''
    matcher = re.compile(pattern, re.VERBOSE)
    matches = matcher.match(s)

#Processing an HTML file	
Write some Python code to create a variable named rankings, which is a list of dictionaries set up as follows:

rankings[i] is a dictionary corresponding to the restaurant whose rank is i+1. For example, from the screenshot above, rankings[0] should be a dictionary with information about Gus's World Famous Fried Chicken.
Each dictionary, rankings[i], should have these keys:
rankings[i]['name']: The name of the restaurant, a string.
rankings[i]['stars']: The star rating, as a string, e.g., '4.5', '4.0'
rankings[i]['numrevs']: The number of reviews, as an integer.
rankings[i]['price']: The price range, as dollar signs, e.g., '$', '$$', '$$$', or '$$$$'.

matchers = {
    'name': '''<a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="[^"]*" data-hovercard-id="[^"]*"><span>(.+)</span></a>''',
    'stars': '''title="([0-9.]+) star rating"''',
    'numrevs': '''(\d+) reviews''',
    'price': '''<span class="business-attribute price-range">(\$+)</span>'''
}

def get_field(s, key):
    from re import search
    assert key in matchers
    match = search(matchers[key], s)
    if match is not None:
        return match.groups()[0]
    return None

sections = yelp_html.split('<span class="indexed-biz-name">')
rankings = []
for i, section in enumerate(sections[1:]):
    rankings.append({})
    for key in matchers.keys():
        rankings[i][key] = get_field(section, key)
    
for r in rankings:
    r['numrevs'] = int(r['numrevs'])
	
	
	
#----------------------------------------------------------------------------------------------------------------------------------------------#

#Mining the web:

#The Requests module
#Python's Requests module to download a web page.
#For instance, here is a code fragment to download the Georgia Tech home page and print the first 250 characters. You might also want to view the source of Georgia Tech's home page to get a nicely formatted view, and compare its output to what you see above.

import requests

response = requests.get('http://www.gatech.edu/')
webpage = response.text  # or response.content for raw bytes

print(webpage[0:250]) 
import re # Maybe you want to use a regular expression?

def get_gt_top_stories(webpage_text):
    """Given the HTML text for the GT front page, returns a list
    of the URLs of the top stories or an empty list if none are
    found.
    """
    pattern = '''<a class="slide-link" href="(?P<url>[^"]+)"'''
    return re.findall(pattern, webpage_text)

top_stories = get_gt_top_stories(webpage)
print("Links to GT's top stories:", top_stories)

#let's see how to build a "get request" with the requests module

url_command = 'http://yelp.com/search'
url_args = {'find_desc': "ramen",
            'find_loc': "atlanta, ga"}
response = requests.get (url_command, params=url_args)

print ("==> Downloading from: '%s'" % response.url) # confirm URL
print ("\n==> Excerpt from this URL:\n\n%s\n" % response.text[0:100])


#Given a search topic, location, and a rank k, return the name of the k-th item of a Yelp! search. If there is no k-th item, return None.
def find_yelp_item (topic, location, k):
    """Returns the k-th suggested item from Yelp! in Atlanta for the given topic."""
    import re
    if k < 1: return None
        
    # Download page
    url_command = 'http://yelp.com/search'
    url_args = {'find_desc': topic,
                'find_loc': location,
                'start': k-1
               }
    
    response = requests.get (url_command, params=url_args)
    if not response: return None
    
    # Split page into lines
    lines = response.text.split ('\n')
    
    # Look for the line containing the name of the k-th item
    item_pattern = re.compile ('<span class="indexed-biz-name">{}\..*<span >(?P<item_name>.*)</span></a>'.format (k))
    for l in lines:
        item_match = item_pattern.search (l)
        if item_match:
            return item_match.group ('item_name')

    # No matches, evidently
    return None

	
#Tools to process the HTML data
#Parsing HTML: The Beautiful Soup module
#The Beautiful Soup package gives you a data structure for traversing this tree
some_page = """
<html>
  <body>
    <p>First paragraph.</p>
    <p>Second paragraph, which links to the <a href="http://www.gatech.edu">Georgia Tech website</a>.</p>
    <p>Third paragraph.</p>
  </body>
</html>
"""
print(some_page)

from bs4 import BeautifulSoup

soup = BeautifulSoup(some_page, "lxml")

print('1. soup ==', soup) # Print the HTML contents
print('\n2. soup.html ==', soup.html) # Root of the tree
print('\n3. soup.html.body ==', soup.html.body) # A child tag
print('\n4. soup.html.body.p ==', soup.html.body.p) # Another child tag
print('\n5. soup.html.body.contents ==', type(soup.html.body.contents), '::', soup.html.body.contents)

#Mining the web in JSON

import requests

response = requests.get ('https://api.github.com/repos/cse6040/labs-fa17/events')

print ("==> .headers:", response.headers, "\n")
print (response.headers['Content-Type'])

import json
print(type(response.json ()))
print(json.dumps(response.json()[:3], sort_keys=True, indent=2))
	