'''
Find the list of url's which are duplicate
Set Removes the list of duplicates from the list
'''

#app01
import requests


url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
# print(response.json())

url_list = []
for key in response.json():
    url_list.append(key['url'])

print("url_list", url_list)

print(len(url_list))

#find unique url_list values

url_list_Set = set(url_list)
print(len(url_list_Set))
