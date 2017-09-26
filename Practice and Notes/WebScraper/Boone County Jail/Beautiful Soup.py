from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, 'html.parser')
print(soup.prettify())

############################################################################

# navigate/extract specific elements of HTML
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p # first p record
soup.p['class'] # class of p record (i.e. 'title')
soup.a # first a record
soup.find_all('a') # all a records
soup.find(id="link2") # record with matching id

for link in soup.find_all('a'):
    print(link.get('href')) # print href values for a records
    
print(soup.get_text()) # print text specifically

############################################################################
     
# types of objects in HTML and XML

# Objects can be one of 4 types: Tag, NavigableString, BeautifulSoup and Comment

# 1) Tags
# Tags have names and attributes. Tags are anything between the <> brackets,
# so you can have header tags, body tags, class tags etc.
soup = bs('<b class="boldest">Extremely bold</b') # this is the full tag
tag = soup.b # find tag using its name ('b')
type(tag)

tag.name # all tags have names (this one is 'b')
tag.name = "blockquote" # tag names can be changed and will be reflected in the HTML

tag.attrs # attributes belong to tags, here it has a 'class' attribute with value 'boldest'
tag['class'] # attributes can be searched for specifically
tag['class'] = 1 # attributes can be changed
del tag['class'] # attributes can also be added and deleted
multiAttr_class = bs('<p class="body strikeout"></p>') # some specific tags can have multiple, space separated attributes
multiAttr_class.p['class'] # (class is one of them)

# 2) NavigableString
soup = bs('<b class="boldest">Extremely bold</b')
tag = soup.b

# when working on strings outside of beautiful soup, once you have extracted it from the HTML
# you should convert it to unicode, this is because navigableStrings have a bunch of features
# associated with them related to navigating and searching the tree and this takes up a lot
# of memory if you only wan't the string itself. (ALWAYS CHECK THE TYPE!)

tag.string # extracts the string element of a tag
type(tag.string)
unicode_string = unicode(tag.string) # navigableStrings are the same as unicode except they have navigating and searching
type(unicode_string) # tree features, you can convert them to unicode strings if required (e.g. if working on the string outside of beautiful soup)
tag.string.replace_with("No longer bold") # strings can't be edited in place, but they can be replaced entirely

# 3) BeautifulSoup
# The BS object itself doesn't correspond to an XML/HTML tag itself but it can be useful to check its name etc.
soup.name # it is a whole document, it can be treated like a tag (names, attrs)

# 4) Comments/Special Strings
# Comments are subclasses of navigableStrings, they add a little extra to the string (i.e. make it a comment).
# There are many other subclasses of navigableStrings including CData, ProcessingInstruction, Declaration, DocType etc.
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = bs(markup)
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>

############################################################################
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Got down to 'Navigating the tree' - this page will cover everything I need to know for BS