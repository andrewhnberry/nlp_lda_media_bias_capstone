# Scraping Articles
# This script is very buggy, and produces a lot of duplicates.


# Import Newspaper API that I will be using
from newspaper import Article
import newspaper

# Ofcourse Import Pandas
import pandas as pd

# List of sources
sources = ["https://edition.cnn.com/", "https://www.breitbart.com/politics/",
           'https://slate.com',
           "https://thehill.com/",
           "https://www.politico.com/","https://www.washingtonpost.com/", "https://www.bbc.com/news",
           'https://www.theguardian.com/international','https://www.latimes.com/',
           'https://www.cbc.ca/news']

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


        # Found a bug where if you put authors after the Title, the article title, doesn't get
        # recorded
        # if multiple authors, they repeat the copy
        # temp_df['Authors'] = article_extract.authors
        temp_df['Title'] = article_extract.title
        temp_df['Text'] = article_extract.text
        #temp_df['Summary'] = article_extract.summary
        #temp_df['Keywords'] = str(article_extract.keywords)
        #temp_df['published_date'] = article_extract.publish_date
        temp_df['Source'] = article_extract.source_url

        df_articles = df_articles.append(temp_df, ignore_index = True)


# To change the path of the output add below
# df_articles.to_csv('data/articles_data.csv') - Already produced version 1
df_articles.to_csv('data/articles_data2.csv')
