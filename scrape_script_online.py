import csv
from requests_html import HTML, HTMLSession


session = HTMLSession()
r = session.get('https://coreyms.com/')

articles = r.html.find('article')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)

    summary = article.find('.entry-content', first=True).text
    print(summary)

    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
