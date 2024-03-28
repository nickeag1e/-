html_page = ''
n = 0
while True:
    string = input()
    if string == '</html>':
        break
    else:
        html_page += string + '\n'
html_page = ' '.join(html_page.split('\n'))
res = []
while '<p>' in html_page and '</p>' in html_page:
    res.append(html_page[html_page.find('<p>') + 3:html_page.find('</p>')])
    html_page = html_page.replace(html_page[html_page.find('<p>'):html_page.find('</p>') + 3], '')
print(*reversed(res), sep='\n')
