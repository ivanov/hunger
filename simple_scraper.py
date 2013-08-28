import urllib2


url_instance= urllib2.urlopen('https://twitter.com/search?q=%23pyboot&mode=realtime')
content = url_instance.read()
url_instance.close()

def scrape_usernames_quick_and_dirty(content):
    "extract @ usernames from content of a twitter search page" 
    # you can do this more elegantly with regular expressions (import re), but
    # we don't have time to go over them, and as Jamie Zawinski once said:
    #
    #    Some people, when confronted with a problem, think: "I know, I'll use
    #    regular expressions." Now they have two problems.
    #
    # Also, we should note that there are better ways of parsing out html
    # pages in Python. Have a look at 
    at_marker = '<s>@</s><b>'
    end_marker = '</b>'
    start = 0
    usernames = []
    while True:
        # find the first index of an @ marker
        hit = content.find(at_marker, start) 
        if hit == -1:
            # we hit the end and nothing was found, break out of the while
            # loop, and return what we have
            break;
        hit += len(at_marker) 
        end = content.find(end_marker, hit) 
        if hit != end:
            # twitter has some @ signs with no usernames on that page
            username = content[hit:end]
            usernames.append(username)
        start = end

#def scrape_usernames_using_etree
