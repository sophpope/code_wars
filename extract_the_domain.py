# Extract the domain name from a URL
# 5 Kyu

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# from urllib.parse import urlparse

# def domain_name(url):
#     parsed_url = urlparse(url)
#     domain = parsed_url.netloc
#     domain_parts = domain.split('.')
#     if domain_parts[1] == 'com' or 'co' or 'net' or 'org' or 'ru':
#         return domain_parts[0]
#     elif domain_parts == IndexError:
#         return url[0]
#     else: 
#         return domain_parts[1]
#     print(url[0])

# print(domain_name("icann.org"))

def domain_name(url):
    domain = url.replace("http://", "").replace("https://", "").replace("www.", "")
    domain = domain.split(".") 
    return domain[0]


print(domain_name("icann.org"))