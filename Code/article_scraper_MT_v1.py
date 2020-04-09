# Scraping Articles using newspaper3k package: Multi-Threading Edition
# Documentation could be found here: https://newspaper.readthedocs.io/en/latest/

# Import Newspaper API that I will be using
import newspaper
from newspaper import Article
from newspaper import Source
from newspaper import news_pool

# Other important Plugins
import pandas as pd

#List of online sources we want to scrape
cnn = newspaper.build("https://edition.cnn.com/", memoize_articles=False)
bbc = newspaper.build("https://www.bbc.com/news",memoize_articles=False)
slate = newspaper.build('https://slate.com', memoize_articles=False)
breitbart = newspaper.build("https://www.breitbart.com/politics/", memoize_articles=False)
politico = newspaper.build("https://www.politico.com/", memoize_articles=False)
thehill = newspaper.build("https://thehill.com/", memoize_articles=False)
cbc = newspaper.build('https://www.cbc.ca/news', memoize_articles=False)
washingtonpost = newspaper.build("https://www.washingtonpost.com/", memoize_articles=False)
globeandmail = newspaper.build("https://www.theglobeandmail.com/", memoize_articles=False)
tc = newspaper.build('https://techcrunch.com/', memoize_articles=False)
gamespot = newspaper.build('https://www.gamespot.com/news/', memoize_articles=False)
globalnewsca = newspaper.build('https://globalnews.ca/', memoize_articles=False)
thestar = newspaper.build('https://www.thestar.com/', memoize_articles=False)
cna = newspaper.build('https://www.channelnewsasia.com/news/international', memoize_articles=False)

#Combine all the sources
list_of_sources = [cnn,bbc,slate,breitbart,politico,
                   thehill,cbc,washingtonpost,globeandmail,
                   tc,gamespot,globalnewsca,thestar,cna]

#Intaitate Muli-Threading Downloads
#WARNING: keep the threads_per_source at a reasonable number
news_pool.set(list_of_sources, threads_per_source = 4) #2 threads per each source
news_pool.join()

#Create our final dataframe
df_articles = pd.DataFrame()

#Create a download limit per sources
limit = 100

for source in list_of_sources:
    #tempoary lists to store each element we want to extract
    list_title = []
    list_text = []
    list_source =[]

    count = 0

    for article_extract in source.articles:

        article_extract.parse()

        #if count > limit:
            #break

        #appending the elements we want to extract
        list_title.append(article_extract.title)
        list_text.append(article_extract.text)
        list_source.append(article_extract.source_url)

        #Update count
        count +=1
        print("article extracted")

    df_temp = pd.DataFrame({'Title': list_title, 'Text': list_text, 'Source': list_source})
    #Append to the final DataFrame
    df_articles = df_articles.append(df_temp, ignore_index = True)
    print('source extracted')

#save to csv
df_articles.to_csv('data/scraped_articles_v2.csv')
