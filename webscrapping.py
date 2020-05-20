from bs4 import BeautifulSoup
import requests
import csv

""" Open a csv file to save our results"""

csv_file = open('webscrap.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

"""Get source HTML url from where we need to
    Scarp the data """

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e :
        yt_link = None

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()
