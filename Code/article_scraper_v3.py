# Scraping Articles using newspaper3k package
# Site could be found here: https://newspaper.readthedocs.io/en/latest/

# Disclaimer:
# This script is very buggy, and produces a lot of duplicates.
# It does take a while to scrape so be patient!

# Import Newspaper API that I will be using
from newspaper import Article
import newspaper

# Importing Required Plugins
import pandas as pd

# List of sources, I added a variety to see if we can garner some interesting topics.
sources = ["https://edition.cnn.com/", "https://www.breitbart.com/politics/",
           'https://slate.com',
           "https://thehill.com/",
           "https://www.politico.com/","https://www.washingtonpost.com/", "https://www.bbc.com/news",
           'https://www.theguardian.com/international','https://www.latimes.com/',
           'https://www.cbc.ca/news', "https://www.theglobeandmail.com/", "https://thepostmillennial.com/politics",
           'https://www.ign.com/news', 'https://www.gamespot.com/news/', 'https://techcrunch.com/']

df_articles = pd.DataFrame()

#create loop to sources and start extracting
count = 0

# Loop to extract data
for source in sources:
    news_data = newspaper.build(source, memoize_articles=False)

    for article_extract in news_data.articles:
        count += 1
        print(f'Article Count: {count}')
        #article_extract = news_data.articles[i]

        try:
            article_extract.download()
            print('Initiating Download')
            article_extract.parse()
            print('Initiating Parse')
        except Exception as e:
            print(e)
            print("continuing...")
            continue


        #article_extract.download()
        #print('Initiating Download')
        #article_extract.parse()
        #print('Initiating Parse')
        # Only if you want NLP work from newspaper3k
        #article_extract.nlp()
        #print('Initiating nlp')
        print(article_extract.title)

        #temp_df = pd.DataFrame(columns = ['Title', 'Authors',
                                #      'Text','Summary','Keywords',
                                #      'published_date','Source'])
        # simpler extract
        temp_df = pd.DataFrame(columns = ['Title','Text','Source'])




        temp_df['Title'] = article_extract.title
        temp_df['Text'] = article_extract.text
        temp_df['Source'] = article_extract.source_url

        df_articles = df_articles.append(temp_df, ignore_index = True)


# To change the path of the output add below
df_articles.to_csv('data/scraped_articles.csv')
