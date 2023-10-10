from bs4 import BeautifulSoup

filename = 'dogdrip-1.html'

page = open(filename,mode='rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())

# titles = soup.findAll('span', attrs={'class': 'ed title-link'})
urls = soup.findAll('a', attrs={'class':'ed link-reset'})
# for t, u in zip(titles,urls):
#     print(t.text, u.href)


with open(filename + 'urls.txt','w') as f:
    for u in urls[1:]:
        f.write(u.attrs['href'] + '\n')
