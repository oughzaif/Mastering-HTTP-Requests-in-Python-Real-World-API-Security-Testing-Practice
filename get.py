import requests
from bs4 import BeautifulSoup

r = requests.get("https://jsonplaceholder.typicode.com/posts")
# is for know what is status code
print(r.status_code)
# r is for get requests and o is get a text with r 
"""o = r.text
print(o)"""
# m to get header detaill
m = r.text
s = BeautifulSoup(m, "lxml")
print(s)
f= open("D:\Cyber Security\web-scrapping\\test.txt", "w")
z = f.write(m)


