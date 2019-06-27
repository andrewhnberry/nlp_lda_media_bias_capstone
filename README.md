# nlp_lda_media_bias_capstone
Brainstation Capstone - Determining Media Bias in Articles Using NLP

This was my capstone Data Science project that I ended up presenting at the end of my Data Science bootcamp at BrainStation in Toronto. I was in the spring cohort of 2019. 

Originally, I was curious about NLP work and wanted to further deepen my understanding on this space of Data Science since we briefly convered it in class. The hypothesis I had comming into the project was if I could possibly determine some sort of media bias or differences in the writing for different topics over different news outlets. 

Thus, the main two methodologies were NLP and LDA Topic Modeling. 

Key Technologies Used:
• Spacy (NLP library for Python)
• NLTK (NLP library for Python)
• Gensim (NLP library for Python, used this mainly for LDA topic Modeling)
• TextBlob (NLP library for Python)
• plyDavis (Python Visualization library)
• Tableau (Visualization Software)

Workﬂow Pipeline:
1. Deployed a web-scraper to gather articles from various news outlets.
2. Text Pre-Processing
    1. Tokenization (Spacy)
      1. Data Cleaning achieved during tokenization
    2. Removing Stopwords (NLTK)
    3. Lemmatization (NLTK - WordNetLemmatizer)
    4. Bigram Identiﬁer (Gensim)
    3. LDA Topic Modeling (Gensim)
4. Sentiment Analysis (TextBlob)
5. Tableau for Visualizations

## Future Work

1.) Improving on communicating my results
2.) Improve on clarity of my work
3.) Learn and integrate some form of entity sentimental anlaysis 


Any feedback and suggestions for imporvement would be greatly appreciated. :) 
