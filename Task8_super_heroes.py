from pprint import pprint
import requests

names_heroeus = {"Captain America":None ,  "Hulk":None , "Thanos":None}

def main(name):
    url = 'https://superheroapi.com/api/2619421814940190/'
    response = requests.get(url + 'search/'+ name)
    answer = (response.json())
    id = (answer ['results'] [0] ['id'])
    response = requests.get(url + id)
    answer = (response.json())
    intellect = (answer ['powerstats'] ['intelligence'])
    return intellect
 
for i in names_heroeus:
   names_heroeus [i] = int(main(i))
print (max(names_heroeus, key=names_heroeus.get))