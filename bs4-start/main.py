from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
news_ycomb_page = response.text
# print(news_ycomb_page)

soup = BeautifulSoup(news_ycomb_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
# print(articles)

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])


# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)