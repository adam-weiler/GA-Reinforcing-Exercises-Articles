import random
from articles import articles

# Add a key-value pair to each article.
for article in articles['response']['results']:
    article['view'] = 0
    # print(article)

def read_article():  # Randomly selects an article and increases the articles "views" by one each time it's selected.
    num_of_articles = len(articles['response']['results']) # 10
    random_num = random.randint(1,num_of_articles-1)
    # print(random_num)
    # print(articles['response']['results'][random_num])
    articles['response']['results'][random_num]['view'] += 1
    # print(articles['response']['results'][random_num]['view'])


def display_views():  # Iterates through the articles and displays their titles and view counts.
    for article in articles['response']['results']:
        print(article['webTitle'])
        print(f"This article has been read {article['view']} times.\n")


read_article()
read_article()
read_article()
read_article()
read_article()

display_views()

