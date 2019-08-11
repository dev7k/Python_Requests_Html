from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    # use chromium (downloading at first run)
    html.render()

match = html.find('#footer', first=True)
print(match.html)
