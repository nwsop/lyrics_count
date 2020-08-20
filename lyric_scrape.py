import bs4, requests, re
page_data = requests.get("https://genius.com/Billie-eilish-my-future-lyrics")
soup = bs4.BeautifulSoup(page_data.text, 'html.parser')
# Finds div tag with class lyric
lyric_list = soup.find(class_='lyrics')

#Pulls lyrics from P tags
lyrics = lyric_list.find_all('p')
lyric_list.text

s = re.sub(r'\[(.*?)\]', '', lyric_list.get_text())

print(s)

