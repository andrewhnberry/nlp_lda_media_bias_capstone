Hi there, if you stumbled upon this repository....congratulations. There is much to learn from my code! So hope you enjoy!

### What is this project?
This is an updated version of my original and first Data Science project on GitHub. Which you can find [here!](https://github.com/andrewhnberry/-Original--nlp_lda_media_bias_capstone) I was very curious about NLP work, and I was curious if I could use NLP methodologies as well as unsupervised learning, I would be able gather insights to answer this question. Do different media outlets treat the same topic differently?

I thought it was a very compelling problem to take on, and I was curious to see if I could work towards that. Since there are tonnes of different media outlets there with different agendas, especially in these more polarizing times as described by the various media I personally consume.

#### How to navigate?
In the Code file, you'll be able to find a few python notebooks/scripts.

|  Jupyter Notebook or Python Script |  Description |
|---|---|
| **aticle_scraper_MT_v1.py**  |  is a short script that scrapes certain articles online. It's robust! |
| **Updated - Part 1 - Data Cleaning & EDA**  |  goes over a little bit of my data cleaning methodologies and EDA from the data I scrapped online. |
| **Updated - Part 2 - NLP preprocessing & LDA Gensim**  |  where I go over some NLP preprocessing, as well as Gensim's version of NLP. I also perform some hyper-parameter tuning, and attempt to explain topic modeling in that notebook. |
|**Updated - Part 3 - NLP preprocessing & LDA Modeling SKLearn**|is similar to the notebook above, but this time I explored SkLearn's version, I tuned different types of parameters and used a tfidf vectorizer instead.|
|**Updated - Part 4 - Model Anlaysis**|where I compared my Gensim models and Sklearn models, I also performed a sentiment analysis.|


You can find the data i used in the **data folder**. In addition I also pickled all my models and saved my plyDavis visualization in the **lda_models folder**.

#### Is it perfect?
Not at all, there is much I could do to improve on this and will do in the future. List of things I need to have a more meaningful project.
- Larger Dataset
- Diverse Dataset
- Study my dataset a bit closer to create more unique data cleaning rules.


Any feedback and suggestions for improvement would be greatly appreciated. :)
