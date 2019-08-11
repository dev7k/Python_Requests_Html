from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# print(html.html)
# print(html.text)

# find method use css selector
match_title = html.find('title', first=True)
match_footer = html.find('#footer', first=True)
# print(match_title.html)
# print(match_title.text)
# print(match_footer.html)
# print(match_footer.text)

article = html.find('div.article', first=True)
headline = article.find('h2', first=True)
summary = article.find('p', first=True)
headline_text = article.find('h2', first=True).text
summary_text = article.find('p', first=True).text
# print(article.text)
# print(headline.text)
# print(summary.text)

articles = html.find('div.article')

for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(headline)
    print(summary)
    print()
