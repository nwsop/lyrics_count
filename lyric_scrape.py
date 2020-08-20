import bs4, requests, re, pprint
page_data = requests.get("https://genius.com/Billie-eilish-my-future-lyrics")
soup = bs4.BeautifulSoup(page_data.text, 'html.parser')
# Finds div tag with class lyric
lyric_list = soup.find(class_='lyrics')

#Pulls lyrics from P tags
lyrics = lyric_list.find_all('p')
lyric_list.text

s = re.sub(r'\[(.*?)\]', '', lyric_list.get_text())
s = s.replace("(","")
s = s.replace(")","")
s = s.replace(",","")

s = s.lower()

lyric_split = s.split()

d = {}

for split in lyric_split:
    if split not in d:
        d[split] = 1
    else:
        d[split] += 1

d = sorted(d.items(), key=lambda x: x[1], reverse=True)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(d)


