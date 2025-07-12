import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
"userId": 1,
"title" : "afina",
"body": "scrap" 
}
pos = requests.post(url,data)
mam = pos.json()
print(mam)