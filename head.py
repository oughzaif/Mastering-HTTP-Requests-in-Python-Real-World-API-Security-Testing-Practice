import requests
url = "http://testphp.vulnweb.com/"
repanse = requests.head(url)
print("information : ")
for key,values in repanse.headers.items() :
    print(f"{key}:{values}")