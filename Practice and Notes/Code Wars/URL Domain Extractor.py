import re
from urlparse import urlparse
#import tldextract

#def domain_name1(url):
#    match = re.match(r'(.\:\/\/*)(.*)(\.*)', url).group(1)
#    output = match.replace('www.','')
#    output = output.replace('.com','')
#    return output
    
def domain_name2(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain.replace('http://','')
    
#def domain_name3(url):
#    extract = tldextract.extract(url)
#    return "{}.{}".format(extract.domain, extract.suffix)

url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"
url3 = "https://www.cnet.com"

#print domain_name1(url1)
print domain_name2(url1)
#print domain_name3(url1)