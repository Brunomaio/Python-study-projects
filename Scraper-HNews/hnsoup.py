import requests
import pprint
from bs4 import BeautifulSoup
import csv

page = 1
res = requests.get(f'https://news.ycombinator.com/news?p={page}')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        if points > 50:
            hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


hnfeed = create_custom_hn(links, subtext)

# Exporting to CSV file

with open('hnews.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for index, item in hnfeed.items():
        writer.writerow([item[index]['link']])
