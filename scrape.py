from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# print(article.prettify())

csv_file = open('tester_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video ID'])

for article in soup.find_all('article'):
	headline = article.a.text
	print(headline)

	summary = article.find('div', class_ = 'entry-content').p.text
	print(summary)



	try:
		vid_src = article.find('iframe', class_ = 'youtube-player')['src']
		# print(vid_src)

		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
	except Exception as e:
		vid_id = None

	print(vid_id)
	print()

	csv_writer.writerow([headline, summary, vid_id])

csv_file.close()

